#!/usr/bin/python
# -*- coding: utf-8 -*-
#This file is part of pypository.
#
#pypository is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#pypository is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with pypository.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2013, Nestor Arocha"
__email__ = "nesaro@gmail.com"

import unittest


class Text(object):
    def summary(self):
        return {"iclass":"Text"}


class TestMemory(unittest.TestCase):
    """Tests Local Memory"""
    def setUp(self):
        from pypository.Memory import LocalMemory
        self.mem = LocalMemory()
        
    def testSaveLoadAndDelete(self):
        texto1 = Text()
        texto2 = Text()
        self.mem.save(texto1,"id1")
        self.mem.save(texto2, "id2")
        newdg = self.mem["id1"]
        self.assertTrue(newdg == texto1)
        del self.mem["id1"]
        del self.mem["id2"]

    def testSimpleSearch(self):
        return True

class TestLoader(unittest.TestCase):
    """Test loaders"""
    def setUp(self):
        from pypository.Memory.Directory import DirStorage
        self.glibrary = DirStorage("/usr/share/pypository/lib_contrib/grammar")

    @unittest.skip
    def test_grammars(self):
        grammarlist = self.glibrary.all_names()
        from pypository.Memory.Loader import load
        for grammar in grammarlist:
            load(grammar)
