# Deployment Guide 🚀

This guide will help you deploy your AI Travel Agent to the web so anyone can access it!

## Option 1: Streamlit Cloud (Recommended - Free!) ☁️

Streamlit Cloud is the easiest and free way to deploy your app.

### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository
- OpenAI API key

### Step-by-Step Instructions

#### 1. Push Your Code to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - AI Travel Agent"

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/ai_travel_agent.git

# Push to GitHub
git push -u origin main
```

#### 2. Sign Up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Authorize Streamlit to access your repositories

#### 3. Deploy Your App

1. Click "New app" in Streamlit Cloud
2. Select your repository: `YOUR_USERNAME/ai_travel_agent`
3. Set the main file path: `src/ai_travel_agent/app.py`
4. Click "Advanced settings"
5. Set Python version: `3.11`
6. Add your secrets:
   ```toml
   OPENAI_API_KEY = "your-actual-api-key-here"
   ```
7. Click "Deploy"

#### 4. Wait for Deployment

- Your app will build and deploy (takes 2-5 minutes)
- You'll get a public URL like: `https://your-app-name.streamlit.app`
- Share this URL with anyone! 🎉

### Managing Your Deployed App

- **Update Secrets**: Go to App Settings → Secrets
- **View Logs**: Click on "Manage app" → "Logs"
- **Reboot**: If the app crashes, use "Reboot app"
- **Update Code**: Just push to GitHub - auto-deploys!

---

## Option 2: Quick Testing with ngrok (Temporary) 🔗

For quick testing or temporary sharing, use ngrok:

### 1. Install ngrok

```bash
# Download from https://ngrok.com/download
# Or via snap on Linux:
snap install ngrok

# Or via brew on Mac:
brew install ngrok
```

### 2. Sign Up and Get Auth Token

1. Sign up at [ngrok.com](https://ngrok.com)
2. Get your auth token from the dashboard
3. Configure ngrok:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

### 3. Run Your App Locally

```bash
# In one terminal, start your Streamlit app
streamlit run src/ai_travel_agent/app.py
```

### 4. Create a Public Tunnel

```bash
# In another terminal, create the tunnel
ngrok http 8501
```

### 5. Share the URL

- ngrok will give you a public URL like: `https://abc123.ngrok.io`
- Share this URL - it's accessible from anywhere!
- **Note**: This URL is temporary and changes each time you restart ngrok

---

## Option 3: Railway (Alternative Cloud Platform) 🚂

Railway is another great option with a free tier.

### 1. Install Railway CLI

```bash
npm install -g @railway/cli
```

### 2. Login to Railway

```bash
railway login
```

### 3. Initialize and Deploy

```bash
# Initialize Railway project
railway init

# Add your OpenAI API key as environment variable
railway variables set OPENAI_API_KEY=your-key-here

# Deploy
railway up
```

### 4. Get Your URL

```bash
railway domain
```

---

## Option 4: Custom Server Deployment 🖥️

For more control, deploy to your own server.

### Using Docker (Recommended)

#### 1. Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "src/ai_travel_agent/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### 2. Build and Run

```bash
# Build Docker image
docker build -t ai-travel-agent .

# Run container
docker run -p 8501:8501 -e OPENAI_API_KEY=your-key ai-travel-agent
```

### Using a VPS (DigitalOcean, AWS, etc.)

#### 1. Set up server and install dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3.11 python3-pip -y

# Clone your repository
git clone https://github.com/YOUR_USERNAME/ai_travel_agent.git
cd ai_travel_agent

# Install dependencies
pip install -r requirements.txt
```

#### 2. Set up environment variables

```bash
# Create .env file
echo "OPENAI_API_KEY=your-key-here" > .env
```

#### 3. Run with systemd (persistent service)

Create `/etc/systemd/system/ai-travel-agent.service`:

```ini
[Unit]
Description=AI Travel Agent
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/home/your-username/ai_travel_agent
ExecStart=/usr/bin/streamlit run src/ai_travel_agent/app.py --server.port=8501
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable ai-travel-agent
sudo systemctl start ai-travel-agent
```

#### 4. Set up reverse proxy (nginx)

Install nginx:
```bash
sudo apt install nginx -y
```

Configure nginx (`/etc/nginx/sites-available/ai-travel-agent`):

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

Enable and restart:
```bash
sudo ln -s /etc/nginx/sites-available/ai-travel-agent /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## Environment Variables 🔐

Make sure to set these environment variables in your deployment:

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

---

## Troubleshooting 🔧

### App Won't Start
- Check logs for errors
- Verify all dependencies are installed
- Ensure Python version is 3.10-3.13

### API Key Issues
- Verify the environment variable is set correctly
- Check for typos in the key
- Ensure the key has sufficient credits

### Performance Issues
- Consider upgrading to a paid tier
- Optimize your agents and tasks
- Add caching for common requests

---

## Cost Considerations 💰

### Free Tiers
- **Streamlit Cloud**: Free for public apps
- **Railway**: $5 free credit monthly
- **ngrok**: Free with limitations (1 connection, dynamic URL)

### Paid Options
- **Streamlit Cloud**: $20/month for private apps
- **Railway**: Pay-as-you-go after free tier
- **VPS**: Starting from $5/month (DigitalOcean, Linode)

### OpenAI API Costs
- Monitor your usage in OpenAI dashboard
- Set spending limits
- Consider using GPT-3.5 for cost savings

---

## Security Best Practices 🔒

1. **Never commit API keys** to version control
2. **Use environment variables** or secrets management
3. **Enable HTTPS** for production deployments
4. **Add rate limiting** if needed
5. **Monitor API usage** regularly
6. **Keep dependencies updated** for security patches

---

## Next Steps 🎯

After deployment:

1. ✅ Test your live app thoroughly
2. ✅ Share the URL with users
3. ✅ Monitor logs and performance
4. ✅ Collect user feedback
5. ✅ Iterate and improve

Need help? Check out:
- [Streamlit Documentation](https://docs.streamlit.io)
- [CrewAI Documentation](https://docs.crewai.com)
- [Railway Documentation](https://docs.railway.app)

Happy deploying! 🚀

