#!/bin/bash

# Hugo Server Launcher Script
# This script starts the Hugo development server with optimal settings

echo "🚀 Starting Hugo Development Server..."
echo "======================================"

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "❌ Error: Hugo is not installed or not in PATH"
    echo "Please install Hugo first: https://gohugo.io/installation/"
    exit 1
fi

# Display Hugo version
echo "📦 Hugo version:"
hugo version
echo ""

# Check if we're in the correct directory
if [ ! -f "config.yml" ] && [ ! -f "config.toml" ]; then
    echo "❌ Error: Not in a Hugo project directory"
    echo "Please run this script from your Hugo project root (where config.yml is located)"
    exit 1
fi

# Check if the site builds successfully
echo "🔨 Building site to check for errors..."
if hugo --quiet; then
    echo "✅ Site builds successfully"
else
    echo "❌ Site has build errors. Please fix them before starting the server."
    exit 1
fi

echo ""
echo "🌐 Starting Hugo server with the following options:"
echo "   • Live reload enabled"
echo "   • Draft content included"
echo "   • Accessible from other devices on network"
echo "   • Fast render mode enabled"
echo ""

# Start Hugo server with optimal settings
echo "🎯 Server will be available at:"
echo "   • Local: http://localhost:1313"
echo "   • Network: http://0.0.0.0:1313"
echo ""
echo "📝 Press Ctrl+C to stop the server"
echo "======================================"

# Start Hugo server with all the options we discussed
hugo server \
    --bind 0.0.0.0 \
    --port 1313 \
    --buildDrafts \
    --buildFuture \
    --disableFastRender=false \
    --liveReloadPort 0 \
    --navigateToChanged \
    --renderToDisk=false \
    --templateMetrics \
    --templateMetricsHints \
    --verboseLog \
    --log \
    --verbose 