import signal
import sys

TIMEOUT_SECS = 60  # adjust as needed

def _timeout_handler(signum, frame):
    print("\nNo activity detected. Program closed due to timeout.")
    sys.exit(0)

# setup once at program start
signal.signal(signal.SIGALRM, _timeout_handler)

def reset_timeout():
    """Reset the inactivity timer."""
    signal.alarm(TIMEOUT_SECS)

def cancel_timeout():
    """Cancel the inactivity timer (use before clean exit)."""
    signal.alarm(0)
