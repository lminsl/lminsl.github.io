#!/bin/bash

# Simple Hugo Server Launcher
# Quick start for development

echo "🚀 Starting Hugo Server (Simple Mode)..."

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "❌ Hugo not found. Please install Hugo first."
    exit 1
fi

# Check if we're in a Hugo project
if [ ! -f "config.yml" ] && [ ! -f "config.toml" ]; then
    echo "❌ Not in a Hugo project directory"
    exit 1
fi

echo "✅ Starting server at http://localhost:1313"
echo "📝 Press Ctrl+C to stop"

# Simple Hugo server start
hugo server -D --bind 0.0.0.0 