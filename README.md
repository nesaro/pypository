pypository
==========

Repository pattern using python files. Store your classes into files, search for them and load them back to python

Media options
=============

* Directory
* Local Memory
* List inside a python file

How to use DirStorage
---------------------

DirStorage constructor has two parameters:
* directory path
* formatlist

each dictionary in the format list must contain:
 * extension: File Extension
 * summary_from_file function that generates a summary from a file
 * load_from_file: function that creates an instance from a file

example:

     [ {"extension":".py",  "summary_from_file":summary_python_file, "load_from_file":load_python_file}, ... ]

