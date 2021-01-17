#!/usr/bin/env python
# coding=utf-8
"""
Copyright (C) 2010 Windell Oskay, drwho@evilmadscientist.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from lxml import etree

from plot_utils_import import from_dependency_import # plotink
inkex = from_dependency_import('ink_extensions.inkex')

class PresetHatch(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("--title")
        self.svgDefRead = None
        self.svg = None

    def effect(self):
        self.svgDefRead = False
        self.svg = self.document.getroot()
        self.recursiveDefDataScan(self.svg)

    def recursiveDefDataScan(self, aNodeList):
        for node in aNodeList:
            if node.tag in [inkex.addNS('defs', 'svg'), 'defs']:
                self.recursiveDefDataScan(node)
            elif node.tag == inkex.addNS('path-effect', 'inkscape'):
                if node.get('effect') == 'rough_hatches':
                    node.set('dist_rdm', '0;1')
                    node.set('growth', '0')
                    node.set('bottom_edge_variation', '0;1')
                    node.set('top_edge_variation', '0;1')
                    node.set('bottom_tgt_variation', '0;1')
                    node.set('top_tgt_variation', '0;1')
                    node.set('scale_bf', '2')
                    node.set('scale_bb', '2')
                    node.set('scale_tf', '2')
                    node.set('scale_tb', '2')
                    node.set('top_smth_variation', '0;1')
                    node.set('bottom_smth_variation', '0;1')
                    node.set('fat_output', 'false')


e = PresetHatch()
e.affect()
