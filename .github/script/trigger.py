#!/usr/bin/env python3
"""Record execution timestamps for cron job timing analysis."""

import json
import time
from datetime import datetime, timezone
from pathlib import Path

# Log file location - using a path relative to the repository root
LOG_FILE = Path(__file__).resolve().parents[2] / "logs" / "execution_log.json"


def append_timestamp():
    """Record the current timestamp to the execution log."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    if LOG_FILE.exists():
        with LOG_FILE.open("r", encoding="utf-8") as f:
            log_data = json.load(f)
    else:
        log_data = {"executions": []}

    execution_record = {
        "unix_timestamp": time.time(),
        "iso_timestamp": datetime.now(timezone.utc).isoformat(),
        "description": "Cron execution recorded",
    }
    log_data["executions"].append(execution_record)

    with LOG_FILE.open("w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)
        f.write("\n")

    print(f"Timestamp recorded: {execution_record['iso_timestamp']}")


if __name__ == "__main__":
    append_timestamp()
