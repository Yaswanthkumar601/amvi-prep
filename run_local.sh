#!/bin/bash
# ==============================================================================
# APPSC AMVI Portal - Local Server Launcher
# ==============================================================================

PORT=8080
echo "========================================================================"
echo "🚗 Launching APPSC AMVI Examination & Preparation Portal"
echo "   A.P. Transport Subordinate Service (Paper-I & Paper-II)"
echo "========================================================================"

# Check if Python 3 is available
if command -v python3 &>/dev/null; then
    echo "⚡ Starting local server via Python 3 on port $PORT..."
    echo "👉 Open your browser at: http://localhost:$PORT"
    echo "Press [Ctrl+C] to stop."
    python3 -m http.server $PORT
elif command -v npx &>/dev/null; then
    echo "⚡ Starting local server via npx serve on port $PORT..."
    echo "👉 Open your browser at: http://localhost:$PORT"
    npx serve -l $PORT .
else
    echo "❌ Error: Neither Python 3 nor Node/npx found. Please install Python 3 or Node.js to run the local server."
    exit 1
fi

