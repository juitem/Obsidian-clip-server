#!/bin/bash
cd "$(dirname "$0")"

PID_FILE="server.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "PID file not found. Server may not be running."
    exit 1
fi

PID=$(cat "$PID_FILE")
if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
    rm -f "$PID_FILE"
    echo "Server stopped (PID $PID)"
else
    rm -f "$PID_FILE"
    echo "Process $PID not running. Cleaned up PID file."
fi
