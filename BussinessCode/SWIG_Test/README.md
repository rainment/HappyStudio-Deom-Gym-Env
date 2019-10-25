To build a Python module, run SWIG using the -python option:

$ swig -python example.i
If building a C++ extension, add the -c++ option:

$ swig -c++ -python example.i
This creates two different files; a C/C++ source file example_wrap.c or example_wrap.cxx and a Python source file example.py. The generated C source file contains the low-level wrappers that need to be compiled and linked with the rest of your C/C++ application to create an extension module. The Python source file contains high-level support code. This is the file that you will import to use the module.


The preferred approach to building an extension module for python is to compile it with distutils, which comes with all recent versions of python (Distutils Docs).

Distutils takes care of making sure that your extension is built with all the correct flags, headers, etc. for the version of Python it is run with. Distutils will compile your extension into a shared object file or DLL (.so on Linux, .pyd on Windows, etc). In addition, distutils can handle installing your package into site-packages, if that is desired. A configuration file (conventionally called: setup.py) describes the extension (and related python modules). The distutils will then generate all the right compiler directives to build it for you.

Here is a sample setup.py file for the above example:

#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_example',
                           sources=['example_wrap.c', 'example.c'],
                           )
G
setup (name = 'example',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
In this example, the line: example_module = Extension(....) creates an Extension module object, defining the name as _example, and using the source code files: example_wrap.c, generated by swig, and example.c, your original c source. The swig (and other python extension modules) tradition is for the compiled extension to have the name of the python portion, prefixed by an underscore. If the name of your python module is "example.py", then the name of the corresponding object file will be"_example.so"

The setup call then sets up distutils to build your package, defining some meta data, and passing in your extension module object. Once this is saved as setup.py, you can build your extension with these commands:

$ swig -python example.i
$ python setup.py build_ext --inplace
And a .so, or .pyd or... will be created for you. It will build a version that matches the python that you run the command with. Taking apart the command line:

python -- the version of python you want to build for
setup.py -- the name of your setup script (it can be called anything, but setup.py is the tradition)
build_ext -- telling distutils to build extensions
--inplace -- this tells distutils to put the extension lib in the current dir. Otherwise, it will put it inside a build hierarchy, and you'd have to move it to use it.
The distutils have many other features, consult the python distutils docs for details.

This same approach works on all platforms if the appropriate compiler is installed. (it can even build extensions to the standard Windows Python using MingGW)





if error happened, try this(add to xxxx_wrap.c):
#pragma clang diagnostic ignored "-Wstrict-prototypes"