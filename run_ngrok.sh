#!/bin/bash

# Script to run the app with ngrok for public access
# Prerequisites: ngrok must be installed and configured

echo "🌍 Starting AI Travel Agent with ngrok..."
echo ""
echo "This will make your app publicly accessible on the internet!"
echo ""

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok is not installed!"
    echo ""
    echo "Please install ngrok first:"
    echo "  - Visit: https://ngrok.com/download"
    echo "  - Or use: snap install ngrok (Linux)"
    echo "  - Or use: brew install ngrok (Mac)"
    echo ""
    exit 1
fi

# Check if Streamlit is running
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "✅ Streamlit appears to be running on port 8501"
    echo ""
else
    echo "⚠️  Streamlit doesn't seem to be running yet."
    echo ""
    echo "Starting Streamlit in the background..."
    nohup streamlit run src/ai_travel_agent/app.py > /dev/null 2>&1 &
    sleep 5
    echo "✅ Streamlit started!"
    echo ""
fi

echo "🔗 Creating public tunnel with ngrok..."
echo ""
echo "Your app will be accessible at the URL shown below:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start ngrok
ngrok http 8501

