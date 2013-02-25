#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
rst2inao.

:copyright: Copyright 2012 by Takayuki SHIMIZUKAWA.
:license: Apache License 2.0.
"""

__docformat__ = 'reStructuredText'

if __name__ == '__main__':
    import sys
    # for debug
    sys.path.insert(0, '.')
    #import pdb
    #pdb.set_trace()
    from docutils_inao.main import main
    sys.exit(main())
