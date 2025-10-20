#!/bin/bash

# Run the AI Travel Agent Web Application
echo "🌍 Starting AI Travel Agent Web Application..."
echo "📝 The app will open in your browser automatically"
echo ""

streamlit run src/ai_travel_agent/app.py --server.port 8501 --server.address localhost

