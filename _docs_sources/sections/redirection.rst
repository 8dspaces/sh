.. _redirection:

Redirection
-----------

sh can redirect the standard and error output streams of a process to a file
or file-like object.  This is done with the special ``_out`` and ``_err``
:ref:`special keyword argument <special_arguments>`. You can pass a filename
or a file object as the argument value.
When the name of an already existing file is passed, the contents of the file
will be overwritten::

	ls(_out="files.list")
	ls("nonexistent", _err="error.txt")
	
You can also redirect to a function.  See :ref:`callbacks`.
