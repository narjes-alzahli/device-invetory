#!/bin/bash
cd "$(dirname "$0")"

echo ""
echo "🔧 Setting up mhmd-world..."
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
  echo "❌ Python3 not found. Please install it from https://python.org"
  read -p "Press Enter to exit..."
  exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt -q

echo ""
echo "✅ Setup complete! Starting server..."
echo "   Open http://localhost:7788 in your browser."
echo ""

python3 server.py
