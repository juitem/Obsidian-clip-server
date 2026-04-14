#!/bin/bash
cd "$(dirname "$0")"

PID_FILE="server.pid"

if [ -f "$PID_FILE" ] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    echo "Server already running (PID $(cat "$PID_FILE"))"
    exit 1
fi

source venv/bin/activate
nohup python app.py > server.log 2>&1 &
echo $! > "$PID_FILE"
echo "Server started (PID $(cat "$PID_FILE")) on port 7676"
