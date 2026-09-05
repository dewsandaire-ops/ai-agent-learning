from datetime import datetime


def current_time():
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")