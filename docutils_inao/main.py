#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
docutils inao.

:copyright: Copyright 2012 by Takayuki SHIMIZUKAWA.
:license: Apache Software License
"""

__docformat__ = 'reStructuredText'

import docutils.core

description = """`rst2inao` is docutils inao writer convert reStructuredText(rst) to Inao format."""


def main():
    output = docutils.core.publish_cmdline(
            writer_name='docutils_inao',
            usage='usage',
            description=description,
            )
    return 0

if __name__ == '__main__':
    main()
