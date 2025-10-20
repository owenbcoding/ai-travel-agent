# Quick Deployment Reference Card 🚀

Choose your deployment method and follow the commands!

---

## 🟢 Option 1: Streamlit Cloud (Easiest - Free)

**Best for:** Public apps, no maintenance, instant deployment

```bash
# 1. Push to GitHub
git add . && git commit -m "Deploy" && git push

# 2. Visit https://share.streamlit.io
# 3. Login with GitHub
# 4. Click "New app"
# 5. Repository: your-username/ai_travel_agent
# 6. Main file: src/ai_travel_agent/app.py
# 7. Add secret: OPENAI_API_KEY = "your-key"
# 8. Click Deploy!
```

**Result:** `https://your-app.streamlit.app` ✅

---

## 🟡 Option 2: ngrok (Quick Testing)

**Best for:** Temporary sharing, testing, demos

```bash
# Terminal 1: Start the app
streamlit run src/ai_travel_agent/app.py

# Terminal 2: Create public tunnel
ngrok http 8501

# Or use our script:
bash run_ngrok.sh
```

**Result:** `https://abc123.ngrok.io` (temporary) ✅

---

## 🔵 Option 3: Docker (Portable)

**Best for:** Any server, reproducible deployments

```bash
# Build and run with docker-compose
docker-compose up -d

# Or manually:
docker build -t ai-travel-agent .
docker run -p 8501:8501 -e OPENAI_API_KEY=your-key ai-travel-agent
```

**Result:** `http://your-server:8501` ✅

---

## 🟣 Option 4: Railway (Cloud Platform)

**Best for:** Automated deployments, scalability

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway variables set OPENAI_API_KEY=your-key
railway up

# Get your URL
railway domain
```

**Result:** `https://your-app.railway.app` ✅

---

## 🟠 Option 5: Custom Server (VPS)

**Best for:** Full control, custom domain

```bash
# On your server (Ubuntu/Debian):
git clone https://github.com/your-username/ai_travel_agent.git
cd ai_travel_agent
pip install -r requirements.txt
echo "OPENAI_API_KEY=your-key" > .env

# Run with screen (stays running):
screen -S ai-travel
streamlit run src/ai_travel_agent/app.py
# Press Ctrl+A, then D to detach

# Or set up as system service (see DEPLOYMENT.md)
```

**Result:** `http://your-server-ip:8501` ✅

---

## 🔐 Don't Forget!

### For ALL deployments:
- ✅ Set `OPENAI_API_KEY` environment variable
- ✅ Never commit API keys to Git
- ✅ Test locally first: `streamlit run src/ai_travel_agent/app.py`
- ✅ Monitor your OpenAI usage/costs

### For production:
- ✅ Set up HTTPS/SSL
- ✅ Configure custom domain
- ✅ Add rate limiting if needed
- ✅ Monitor logs and errors

---

## 📊 Comparison

| Method | Cost | Speed | Difficulty | Best For |
|--------|------|-------|------------|----------|
| Streamlit Cloud | Free | ⚡⚡⚡ | ⭐ Easy | Public apps |
| ngrok | Free* | ⚡⚡⚡ | ⭐ Easy | Testing |
| Docker | $5+/mo | ⚡⚡ | ⭐⭐ Medium | Flexibility |
| Railway | $5+/mo | ⚡⚡ | ⭐⭐ Medium | Auto-deploy |
| VPS | $5+/mo | ⚡ | ⭐⭐⭐ Hard | Full control |

*ngrok free has limitations (1 connection, dynamic URL)

---

## 🆘 Quick Troubleshooting

**App won't start:**
```bash
# Check Python version
python --version  # Should be 3.10-3.13

# Reinstall dependencies
pip install -r requirements.txt
```

**API key not found:**
```bash
# For local:
echo "OPENAI_API_KEY=sk-..." > .env

# For cloud: Add in platform's secrets/environment variables
```

**Port already in use:**
```bash
# Use different port
streamlit run src/ai_travel_agent/app.py --server.port 8502
```

---

## 📚 Full Documentation

- Detailed deployment guide: [DEPLOYMENT.md](DEPLOYMENT.md)
- Quick start guide: [QUICKSTART.md](QUICKSTART.md)
- Main README: [README.md](README.md)

---

**Need help?** See full documentation or contact support!

Happy deploying! 🌍✈️

