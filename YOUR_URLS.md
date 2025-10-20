# 🌐 Your AI Travel Agent URLs

## Your GitHub Repository
```
https://github.com/owenbcoding/ai-travel-agent
```
✅ **This is already set up!**

---

## 🚀 Method 1: Streamlit Cloud (Recommended - Takes 5 min)

### Step 1: Push Your Latest Changes
```bash
git add .
git commit -m "Ready for deployment"
git push
```

### Step 2: Deploy on Streamlit Cloud

1. **Go to:** https://share.streamlit.io

2. **Sign in** with your GitHub account

3. **Click "New app"** button

4. **Fill in these EXACT values:**
   ```
   Repository:    owenbcoding/ai-travel-agent
   Branch:        main  (or master)
   Main file:     src/ai_travel_agent/app.py
   ```

5. **Click "Advanced settings"** → Add this in "Secrets":
   ```toml
   OPENAI_API_KEY = "your-actual-api-key-here"
   ```

6. **Click "Deploy"**

### Step 3: Your Live URL Will Be:
```
🌍 https://ai-travel-agent-owenbcoding.streamlit.app
```
Or something similar like:
```
🌍 https://owenbcoding-ai-travel-agent.streamlit.app
```

**This URL is:**
- ✅ Permanent
- ✅ Free
- ✅ Accessible from anywhere
- ✅ Share with anyone!

---

## ⚡ Method 2: Get Online RIGHT NOW with ngrok (2 minutes)

Want a URL immediately for testing? Do this:

### Terminal 1: Start Your App
```bash
streamlit run src/ai_travel_agent/app.py
```

### Terminal 2: Create Public URL
```bash
ngrok http 8501
```

### OR just run our script:
```bash
bash run_ngrok.sh
```

### Look for this in the output:
```
Forwarding    https://abc-123-def.ngrok-free.app -> http://localhost:8501
                      ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
                      THIS IS YOUR PUBLIC URL!
```

**Copy that HTTPS URL and share it!**

⚠️ **Note:** This URL is temporary - changes each time you restart ngrok

---

## 📋 Quick Comparison

| Method | URL Example | Duration | Setup Time |
|--------|------------|----------|-----------|
| **Streamlit Cloud** | `https://ai-travel-agent-owenbcoding.streamlit.app` | Permanent ♾️ | 5 minutes |
| **ngrok** | `https://abc-123.ngrok-free.app` | Temporary ⏰ | 2 minutes |

---

## 🎯 Which Should You Use?

### Use Streamlit Cloud if:
- ✅ You want a permanent URL
- ✅ You want to share with many people
- ✅ You want automatic updates from GitHub
- ✅ You want it to stay online 24/7

### Use ngrok if:
- ✅ You want to test RIGHT NOW
- ✅ You're showing someone quickly
- ✅ You don't want to push to GitHub yet
- ✅ It's just for temporary demo

---

## 🚀 Recommended: Do BOTH!

1. **First:** Use ngrok to test now (2 min)
   ```bash
   bash run_ngrok.sh
   ```

2. **Then:** Deploy to Streamlit Cloud for permanent URL (5 min)
   - Go to https://share.streamlit.io
   - Connect your repo: `owenbcoding/ai-travel-agent`
   - Deploy!

---

## 📱 After You Get Your URL

### Share It:
```
🌍 Hey! Check out my AI Travel Agent:
   https://your-app-url.streamlit.app
   
   Just enter your travel details and get a personalized plan!
```

### Test It:
1. Open the URL in your browser
2. Fill in travel details
3. Click "Create My Travel Plan"
4. Download your report!

### Monitor It:
- **Streamlit Cloud:** https://share.streamlit.io → View logs
- **OpenAI Usage:** https://platform.openai.com/usage
- **GitHub:** https://github.com/owenbcoding/ai-travel-agent

---

## 🆘 Need the URLs Again?

**Your GitHub Repo:**
```
https://github.com/owenbcoding/ai-travel-agent
```

**Streamlit Cloud Dashboard:**
```
https://share.streamlit.io
```

**After deploying, your app will be at:**
```
https://[app-name]-owenbcoding.streamlit.app
```
(Streamlit will show you the exact URL after deployment)

---

## ✅ Next Steps

1. Choose your method (Streamlit Cloud recommended!)
2. Follow the steps above
3. Copy your URL
4. Share with the world! 🌍✨

Good luck! 🚀

