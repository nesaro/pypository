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

class TestQuery(unittest.TestCase):
    """Test search query functions"""
    def teststrToQuery(self):
        from pypository.search.Query import str_to_memoryquery
        str_to_memoryquery("id")
        str_to_memoryquery("identifier=id")
        str_to_memoryquery("identifier=id&&description=desc")
        str_to_memoryquery("identifier=id&&!description=desc")
        
    def testdicttoQuery(self):
        from pypository.search.Query import dict_to_query
        dict_to_query({"identifier":"id"})
        dict_to_query({"identifier":"id","description":"desc"})
        dict_to_query({"identifier":"id","description":{"$not":"desc"}})
        myquery = dict_to_query({"roledict":{"$part":{"subject":"human"}}})
