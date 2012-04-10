statprof - statistical profiling for Python
===========================================

This package provides a simple statistical profiler for Python.

Python's default profiler has been `lsprof` for several years. This is
an *instrumenting* profiler, which means that it saves data on every
action of interest.  In the case of lsprof, it runs at function entry
and exit.  This has problems: it can be expensive due to frequent
sampling, and it is blind to hot spots *within* a function.

In contrast, `statprof` samples the call stack periodically (by
default, 1000 times per second), and it correctly tracks line numbers
*inside* a function.  This means that if you have a 50-line function
that contains two hot loops, `statprof` is likely to report them both
accurately.

<b>Note</b>: This package does not yet work on Windows! See the
implementation and portability notes below for details.


Basic usage
-----------

It's easy to get started with `statprof`:

    import statprof

    statprof.start()
	try:
	    my_questionable_function()
    finally:
	    statprof.stop()
		statprof.display()

For more comprehensive help, run `pydoc statprof`.


Portability
-----------

Because `statprof` uses the Unix `itimer` signal facility, it does not
currently work on Windows. (Patches to improve portability would be
most welcome.)


Implementation notes
--------------------

The `statprof` profiler works by setting the Unix profiling signal
`ITIMER_PROF` to go off after the interval you define in the call to
`reset()`. When the signal fires, a sampling routine is run which
looks at the current procedure that's executing, and then crawls up
the stack, and for each frame encountered, increments that frame's
code object's sample count.  Note that if a procedure is encountered
multiple times on a given stack, it is only counted once. After the
sampling is complete, the profiler resets profiling timer to fire
again after the appropriate interval.

Meanwhile, the profiler keeps track, via `os.times()`, how much CPU
time (system and user -- which is also what `ITIMER_PROF` tracks), has
elapsed while code has been executing within a `start()`/`stop()`
block.

The profiler also tries (as much as possible) to avoid counting or
timing its own code.


History
-------

This package was originally
[written and released by Andy Wingo](http://wingolog.org/archives/2005/10/28/profiling).
It was ported to modern Python by Alex Frazer, and posted to github by
Jeff Muizelaar.  The current maintainer is Bryan O'Sullivan
<bos@serpentine.com>.


Reporting bugs, contributing patches
------------------------------------

The current maintainer of this package is Bryan O'Sullivan
<bos@serpentine.com>.

Please report bugs using the
[github issue tracker](https://github.com/bos/statprof.py/issues).

If you'd like to contribute patches, please do - the source is on
github, so please just issue a pull request.

    $ git clone git://github.com/bos/statprof.py
