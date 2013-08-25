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

""" Directory storage """

from .Memory import Memory
from pypository.utils import ImmutableDict, getFileTuple
import logging
LOG = logging.getLogger(__name__)


class DirStorage(Memory):
    """A collection of elements stored inside a directory"""
    def __init__(self, dirpath):
        Memory.__init__(self)
        self.path = dirpath
        from pypository.search.Searcher import MemorySearcher
        self._searcher = MemorySearcher(self)

    def __iter__(self):
        self.index = 0
        self.cache = []
        for filename in self.all_files():
            try:
                self.cache.append(self.summary_from_filename(filename))
            except (AttributeError,ImportError, TypeError) as e:
                LOG.debug("Error while loading %s file summary %s" % (filename, e) )
        return self

    @property
    def allowed_extensions(self):
        raise NotImplementedError

    def next(self):
        try:
            result = self.cache[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result
        

    @staticmethod
    def summary_from_filename(filepath):
        raise NotImplementedError

    def all_files(self):
        import glob
        extensions = self.allowed_extensions or [""]
        for extension in extensions:
            searchstring = self.path + "*" + extension
            tmpresult = glob.glob(searchstring)
            for result in tmpresult:
                if result.endswith("__init__.py"):
                    continue
                yield result


    def all_names(self):
        """Generates all Static Ids"""
        for fullname in self.all_files():
            (_, _, fileBaseName, fileExtension) = getFileTuple(fullname)
            if self.allowed_extensions and fileExtension not in self.allowed_extensions:
                continue
            yield fileBaseName.split(".")[0]

    def load(self, name):
        raise NotImplementedError

    def __contains__(self, key):
        return key in self.all_names()

    def provided_iclasses(self):
        return set([x['iclass'] for x in self])

