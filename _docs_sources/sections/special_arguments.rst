.. _special_arguments:

.. |def| replace:: Default value:

Special keyword arguments
#########################

These arguments alter the way a command is launched or run.  You can use them on
any command that you run, but some may not be used together.  ``sh`` will tell
you if there are conflicts.

To set default special keyword arguments on *every* command run, you may use
:ref:`default_kwargs`.

Controlling Output
==================

_out
----
What to redirect STDOUT to.  If this is a string, it will be treated as a file
name.  You may also pass a file object (or file-like object), as well as a
StringIO object.  See :ref:`redirection`.

Example::

    import sh
    sh.ls(_out="/tmp/output")

.. seealso::
    :ref:`redirection`
		
_err
----
What to redirect STDERR to.  See ``_out`` above.
    
_err_to_out
-----------
If True, this redirects the STDERR stream to the STDOUT stream, so that any
returned data from a command will be both from STDOUT and STDERR.

_encoding
---------
The character encoding of the process's STDOUT.  By default, this is "utf8".
			
_decode_errors
--------------
.. versionadded:: 1.07.0

This is how Python should handle decoding errors of the process's output.
By default, this is "strict", but you can use any value that's valid
to a string's ``.decode()`` method, such as "ignore".
		
_tee
----
.. versionadded:: 1.07.0

As of 1.07.0, any time redirection is used, either for stdout or stderr, the
respective internal buffers are not filled.  For example, if you're downloading
a file and using a callback on stdout, the internal stdout buffer, nor the pipe
buffer be filled with data from stdout.  This option forces those buffers to be
filled anyways, in effect "tee-ing" the output into two places (the
callback/redirect handler, and the internal buffers).


Execution
=========

.. _fg:

_fg
---
.. versionadded:: 1.12.0

|def| ``False``

_bg
---
|def| ``False``

Runs a command in the background.  The command will return immediately, and you
will have to run ``.wait()`` on it to allow it to finish.  See
:ref:`background`.

_env
----
A dictionary defining the only environment variables that will be made
accessible to the process.  If not specified, the calling process's environment
variables are used.  See :ref:`environments`.

.. _timeout:

_timeout
--------
How much time, in seconds, we should give the process to complete.  If the
process does not finish within the timeout, it will be sent the signal defined
by :ref:`timeout_signal`.

.. _timeout_signal:

_timeout_signal
---------------
|def| ``signal.SIGKILL``

The signal to be sent to the process if :ref:`timeout` is not ``None``.

_cwd
----
|def| ``None``

A string that sets the current working directory of the process.

_ok_code
--------
|def| ``0``

Either an integer, a list, or a tuple containing the exit code(s) that are
considered "ok", or in other words: do not raise an exception.  Some misbehaved
programs use exit codes other than 0 to indicate success.  See
:ref:`exit_codes`.

_new_session
------------
|def| ``True``

Determines if our forked process will be executed in its own session via
`os.setsid() <https://docs.python.org/3.5/library/os.html#os.setsid>`_.

.. note::

    If ``_new_session`` is ``False``, the forked process will be put into its
    own group via ``os.setpgrp()``.  This way, the forked process, and all of
    it's children, are always alone in their own group that may be signalled
    directly, regardless of the value of ``_new_session``.

_uid
----
.. versionadded:: 1.12.0

|def| ``None``

_preexec_fn
-----------
.. versionadded:: 1.12.0

|def| ``None``

		

Communication
=============

_in
---
Specifies an argument for the process to use as its standard input.  This
may be a string, a `Queue <http://docs.python.org/library/queue.html#queue-objects>`_,
a file object, or any iterable.  See :ref:`stdin`.
		
_piped
------
May be ``True``, ``"out"``, or ``"err"``.  Signals a command that it is being
used as the input to another command, so it should return its output
incrementally as it receives it, instead of aggregating it all at once.  See
:ref:`advanced_piping`.
		
_iter
-----
May be ``True``, ``"out"``, or ``"err"``.  Puts a command in iterable mode.  In
this mode, you can use a ``for`` or ``while`` loop to iterate over a command's
output in real-time.  See :ref:`iterable`.
		
_iter_noblock
-------------
Same as ``_iter``, except the loop will not block if there is no output to
iterate over.  Instead, the output from the command will be
``errno.EWOULDBLOCK``.  See :ref:`iterable`.

_with
-----
Explicitly tells us that we're running a command in a ``with`` context.  This is
only necessary if you're using a command in a ``with`` context **and** passing
parameters to it.  See :ref:`with_contexts`.

_done
-----
.. versionadded:: 1.11.0

		
		
TTYs
====

_tty_in
-------

|def| ``False``, meaning a `pipe <http://docs.python.org/library/os.html#os.pipe>`_ will be used.

If ``True``, sh creates a `TTY <http://en.wikipedia.org/wiki/Pseudo_terminal>`_
for STDIN, essentially emulating a terminal, as if your command was entered from
the commandline.  This is necessary for commands that require STDIN to be a TTY.
    
_tty_out
--------

|def| ``True``

If ``True``, sh creates a `TTY <http://en.wikipedia.org/wiki/Pseudo_terminal#Applications>`_
for STDOUT, otherwise use a `pipe <http://docs.python.org/library/os.html#os.pipe>`_.
This is necessary for commands that require STDOUT to be a TTY.

_tty_size
---------

|def| ``(20, 80)``

The (rows, columns) of stdout's TTY.  Changing this may affect how much your
program prints per line, for example.

Performance & Optimization
==========================

_in_bufsize
-----------
The STDIN buffer size.  0 for unbuffered (the default), 1 for line
buffered, anything else for a buffer of that amount.  See :ref:`buffer_sizes`
		
_out_bufsize
------------
The STDOUT/ERR buffer size.  0 for unbuffered, 1 for line buffered (the
default), anything else for a buffer of that amount.  See :ref:`buffer_sizes`
		
_internal_bufsize
-----------------
How much of STDOUT/ERR your command will store internally.  This value
represents the *number of bufsize chunks* not the total number of bytes.  For
example, if this value is 100, and STDOUT is line buffered, you will be able to
retrieve 100 lines from STDOUT.  If STDOUT is unbuffered, you will be able to
retrieve only 100 characters.
		
_no_out
-------
.. versionadded:: 1.07.0

Disables STDOUT being internally stored.  This is useful for commands
that produce huge amounts of output that you don't need, that would
otherwise be hogging memory if stored internally by sh.
		
_no_err
-------
.. versionadded:: 1.07.0

Disables STDERR being internally stored.  This is useful for commands that
produce huge amounts of output that you don't need, that would otherwise be
hogging memory if stored internally by sh.
		
_no_pipe
--------
.. versionadded:: 1.07.0

Similar to ``_no_out``, this explicitly tells the sh command that it will never
be used for piping its output into another command, so it should not fill its
internal pipe buffer with the process's output.  This is also useful for
conserving memory.
		

Program Arguments
=================

These are options that affect how command options are fed into the program.

_long_sep
---------
.. versionadded:: 1.12.0

|def| ``"="``

This is the character(s) that separate a program's long argument's key from the
value, when using kwargs to specify your program's long arguments.  For example,
if your program expects a long argument in the form ``--name value``, the way to
achieve this would be to set ``_long_sep=" "``.

.. code-block:: python

    import sh
    sh.your_program(key=value, _long_sep=" ")

Would send the following list of arguments to your program:

.. code-block:: python

    ["--key value"]

If your program expects the long argument name to be separate from its value,
pass ``None`` into ``_long_sep`` instead:

.. code-block:: python

    import sh
    sh.your_program(key=value, _long_sep=None)

Would send the following list of arguments to your program:

.. code-block:: python

    ["--key", "value"]

_long_prefix
------------
.. versionadded:: 1.12.0

|def| ``"--"``

This is the character(s) that prefix a long argument for the program being run.
Some programs use single dashes, for example, and do not understand double
dashes.

_arg_preprocess
---------------
.. versionadded:: 1.12.0

|def| ``None``

This is an advanced option that allows you to rewrite a command's arguments on
the fly, based on other command arguments, or some other variable.  It is really
only useful in conjunction with :ref:`baking <baking>`, and only currently used when
constructing :ref:`contrib <contrib>` wrappers.

Example:

.. code-block:: python

    import sh

    def processor(args, kwargs):
        return args, kwargs

    my_ls = sh.bake.ls(_arg_preprocess=processor)

.. warning::

    The interface to the ``_arg_preprocess`` function may change without
    warning.  It is generally only for internal sh use, so don't use it unless
    you absolutely have to.

Misc
====

_log_msg
--------
.. versionadded:: 1.12.0
