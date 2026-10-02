#!/usr/bin/env python3
"""Record execution timestamps for cron job timing analysis."""

import json
import time
from datetime import datetime
from pathlib import Path

# Log file location - using a path relative to the repository root
LOG_FILE = Path(__file__).parent.parent.parent / "logs" / "execution_log.json"

def append_timestamp():
    """Record the current timestamp to the execution log."""
    # Create logs directory if it doesn't exist
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Create or load existing log
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            log_data = json.load(f)
    else:
        log_data = {"executions": []}
    
    # Append new timestamp
    execution_record = {
        "unix_timestamp": time.time(),
        "iso_timestamp": datetime.utcnow().isoformat() + "Z",
        "description": "Cron execution recorded"
    }
    log_data["executions"].append(execution_record)
    
    # Write updated log
    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)
    
    print(f"Timestamp recorded: {execution_record['iso_timestamp']}")

if __name__ == "__main__":
    append_timestamp()
