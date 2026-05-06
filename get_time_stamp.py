from datetime import datetime, timezone

def get_time_stamp():
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    return timestamp