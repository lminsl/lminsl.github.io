# Hugo Server Scripts

This directory contains shell scripts to easily start your Hugo development server.

## 📁 Available Scripts

### 1. `start-hugo-server.sh` - Full Featured Server
**Complete Hugo server with all features and error checking**

```bash
./start-hugo-server.sh
```

**Features:**
- ✅ Checks if Hugo is installed
- ✅ Validates you're in a Hugo project directory
- ✅ Pre-builds the site to catch errors
- ✅ Shows Hugo version
- ✅ Detailed status messages
- ✅ All Hugo server options enabled
- ✅ Network accessible (0.0.0.0)
- ✅ Draft content included
- ✅ Live reload enabled

### 2. `start-hugo-simple.sh` - Quick Start
**Simple and fast Hugo server launch**

```bash
./start-hugo-simple.sh
```

**Features:**
- ✅ Basic error checking
- ✅ Quick startup
- ✅ Same functionality as manual `hugo server -D --bind 0.0.0.0`

## 🚀 How to Use

### First Time Setup
```bash
# Make scripts executable (if not already done)
chmod +x start-hugo-server.sh
chmod +x start-hugo-simple.sh
```

### Daily Usage
```bash
# Option 1: Full featured server (recommended)
./start-hugo-server.sh

# Option 2: Quick start
./start-hugo-simple.sh
```

## 🌐 Server Access

Once running, your site will be available at:
- **Local**: http://localhost:1313
- **Network**: http://0.0.0.0:1313 (accessible from other devices)

## 📝 What the Scripts Do

### Full Featured Script (`start-hugo-server.sh`)
```bash
hugo server \
    --bind 0.0.0.0 \          # Accessible from network
    --port 1313 \             # Standard Hugo port
    --buildDrafts \           # Include draft content
    --buildFuture \           # Include future posts
    --disableFastRender=false \ # Enable fast rendering
    --liveReloadPort 0 \      # Auto-assign live reload port
    --navigateToChanged \     # Auto-navigate to changed files
    --renderToDisk=false \    # Serve from memory
    --templateMetrics \       # Show template performance
    --templateMetricsHints \  # Performance hints
    --verboseLog \            # Detailed logging
    --log \                   # Enable logging
    --verbose                 # Verbose output
```

### Simple Script (`start-hugo-simple.sh`)
```bash
hugo server -D --bind 0.0.0.0
```

## 🔧 Troubleshooting

### Script Permission Issues
```bash
chmod +x *.sh
```

### Hugo Not Found
```bash
# Install Hugo (macOS with Homebrew)
brew install hugo

# Or download from https://gohugo.io/installation/
```

### Wrong Directory
Make sure you're in your Hugo project root (where `config.yml` is located).

### Port Already in Use
The scripts use port 1313. If it's busy, you can modify the script or kill the existing process:
```bash
# Find Hugo processes
ps aux | grep hugo

# Kill specific process
kill -9 <process_id>
```

## 📚 Related Files

- `PAPERMOD_FEATURES.md` - PaperMod theme documentation
- `content/olympiad/_index.md` - Your Olympiad problems page

## 🎯 Quick Commands

```bash
# Start full server
./start-hugo-server.sh

# Start simple server
./start-hugo-simple.sh

# Stop server
Ctrl+C

# Check Hugo version
hugo version

# Build site only
hugo --minify
```

---

*These scripts make Hugo development much easier! 🎉* 