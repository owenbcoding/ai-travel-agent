# Quick Start Guide 🚀

Get your AI Travel Agent up and running in minutes!

## Step 1: Install Dependencies

```bash
# Install the package and all dependencies
pip install -e .
```

## Step 2: Set Up Your API Key

Create a `.env` file in the project root:

```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual OpenAI API key.

## Step 3: Launch the Web Interface

```bash
streamlit run src/ai_travel_agent/app.py
```

Or use the convenience script:

```bash
bash run_webapp.sh
```

## Step 4: Plan Your Trip! ✈️

1. The web interface will open in your browser at `http://localhost:8501`
2. Fill in the travel form with your details:
   - Where you're coming from
   - Your destination
   - Travel dates and duration
   - Your interests
   - Budget
   - Number of travelers
3. Click "Create My Travel Plan"
4. Watch the AI agents work their magic! 🤖
5. Download your personalized travel report

## Alternative: Command Line

If you prefer the terminal:

```bash
crewai run
```

Then follow the prompts to enter your travel information.

## What You'll Get 📝

- A detailed research report about your destination
- Personalized recommendations based on your interests
- Budget-friendly suggestions
- Activities and attractions tailored to your preferences
- A downloadable Markdown file with your complete travel plan

## Troubleshooting 🔧

### Issue: "Module not found" error
**Solution**: Make sure you've installed the dependencies:
```bash
pip install -e .
```

### Issue: "API Key not found"
**Solution**: Ensure your `.env` file is in the project root with a valid OpenAI API key:
```bash
OPENAI_API_KEY=sk-...
```

### Issue: Streamlit won't start
**Solution**: Check if the port is already in use:
```bash
streamlit run src/ai_travel_agent/app.py --server.port 8502
```

## Need Help?

- Check the main [README.md](README.md)
- Visit [CrewAI Documentation](https://docs.crewai.com)
- Review the configuration files in `src/ai_travel_agent/config/`

Happy travels! 🌍✨

