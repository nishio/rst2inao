# -*- coding: utf8 -*-
"""
docutils inao builder.

:copyright: Copyright 2012 by Takayuki SHIMIZUKAWA.
:license: Apache Software License
"""

__docformat__ = 'reStructuredText'

import os

from docutils import nodes
try:
    from sphinx.builders.text import TextBuilder
    from sphinx.util.osutil import relative_uri, ensuredir, copyfile
    from sphinx.util.console import brown
except ImportError:
    raise ImportError("sphinx: you NEED Sphinx installation if you want to use `docutils_inao.builder`.")

from docutils_inao.writer import InaoWriter, InaoTranslator


class SphinxInaoTranslator(InaoTranslator):

    def __init__(self, document, builder):
        InaoTranslator.__init__(self, document)
        self.builder = builder

    def unknown_visit(self, node):
        msg = ('%s visiting unknown node type: %s'
               % (self.__class__, node.__class__.__name__))
        self.builder.warn(msg, (self.builder.current_docname, node.line))
        InaoTranslator.unknown_visit(self, node)


class SphinxInaoWriter(InaoWriter):
    def __init__(self, builder):
        InaoWriter.__init__(self)
        self.builder = builder

    def translate(self):
        visitor = SphinxInaoTranslator(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.body


class SphinxInaoBuilder(TextBuilder):
    name = 'inao'
    format = 'text'
    out_suffix = '.txt'

    def prepare_writing(self, docnames):
        self.writer = SphinxInaoWriter(self)

    def write_doc(self, docname, doctree):
        self.imgpath = relative_uri(self.get_target_uri(docname), '_images')
        self.post_process_images(doctree)
        self.current_docname = docname
        return TextBuilder.write_doc(self, docname, doctree)

    def post_process_images(self, doctree):
        for node in doctree.traverse(nodes.image):
            candidate = node['uri']
            if candidate.startswith(self.outdir):
                candidate = candidate[len(self.outdir):]
            candidate = candidate.replace('\\', '/').lstrip('/')
            node['uri'] = candidate
            if candidate not in self.env.images:
                # non-existing URI; let it alone
                continue
            self.images[candidate] = self.env.images[candidate][1]

    def finish(self):
        self.copy_image_files()
        return TextBuilder.finish(self)

    def copy_image_files(self):
        # copy image files
        if self.images:
            ensuredir(os.path.join(self.outdir, '_images'))
            for src in self.status_iterator(self.images, 'copying images... ',
                                            brown, len(self.images)):
                dest = self.images[src]
                try:
                    copyfile(os.path.join(self.srcdir, src),
                             os.path.join(self.outdir, '_images', dest))
                except Exception, err:
                    self.warn('cannot copy image file %r: %s' %
                              (os.path.join(self.srcdir, src), err))
