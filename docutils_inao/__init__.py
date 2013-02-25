"""
docutils inao.

:copyright: Copyright 2012 by Takayuki SHIMIZUKAWA.
:license: Apache Software License
"""

__docformat__ = 'reStructuredText'

from docutils_inao.writer import InaoWriter as Writer  #for docutils rule.
    #if docutils receive 'foo' as writer name, execute `import foo.Writer`.


# setup hook for sphinx
def setup(app):
    from docutils_inao.builder import SphinxInaoBuilder
    app.add_builder(SphinxInaoBuilder)  #sphinx builder registration
