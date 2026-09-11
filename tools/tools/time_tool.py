from datetime import datetime
from zoneinfo import ZoneInfo


def current_time():
    """Return the current local date and time."""
    return datetime.now(
        tz=ZoneInfo("Africa/Lagos")
    ).strftime("%Y-%m-%d %H:%M:%S")