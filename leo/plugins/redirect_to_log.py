#@+leo-ver=5-thin
#@+node:edream.110203113231.924: * @thin redirect_to_log.py
"""Send all output to the log pane"""

#@@language python
#@@tabwidth -4

import leo.core.leoGlobals as g

__version__ = "1.3"

def init():
    ok = not g.app.unitTesting # Not for unit tests.
    if ok: # Register the handlers...
        g.registerHandler("start2", onStart)
        g.plugin_signon(__name__)
    return ok

def onStart (tag,keywords):
    g.redirectStdout() # Redirect stdout
    g.redirectStderr() # Redirect stderr
#@-leo
