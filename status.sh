#!/bin/bash
cd "$(dirname "$0")"

PID_FILE="server.pid"

if [ ! -f "$PID_FILE" ]; then
    echo "Server is not running (no PID file)"
    exit 1
fi

PID=$(cat "$PID_FILE")
if kill -0 "$PID" 2>/dev/null; then
    echo "Server is running (PID $PID)"
    echo "Port: $(lsof -iTCP:7676 -sTCP:LISTEN -P -n 2>/dev/null | tail -1)"
else
    echo "Server is not running (stale PID file)"
    rm -f "$PID_FILE"
    exit 1
fi
