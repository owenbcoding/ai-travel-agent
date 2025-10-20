#!/usr/bin/env python
import streamlit as st
import warnings
from datetime import datetime
from ai_travel_agent.crew import AiTravelAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Set page config
st.set_page_config(
    page_title="AI Travel Agent",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">🌍 AI Travel Agent 🌍</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your intelligent travel planning assistant</p>', unsafe_allow_html=True)
    
    # Sidebar with instructions
    with st.sidebar:
        st.image("https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=400", use_container_width=True)
        st.markdown("### 📋 How it works")
        st.markdown("""
        1. **Fill in your travel details** in the form
        2. **Click 'Create My Travel Plan'** to start
        3. **Wait for the AI agents** to research and create your personalized itinerary
        4. **Download or view** your custom travel report
        """)
        st.markdown("---")
        st.markdown("### 🤖 AI Agents")
        st.markdown("""
        - **Research Agent**: Finds the best information about your destination
        - **Reporting Analyst**: Creates a detailed travel report
        """)
    
    # Main form
    with st.form("travel_form"):
        st.markdown("### ✈️ Tell us about your trip")
        
        col1, col2 = st.columns(2)
        
        with col1:
            origin = st.text_input(
                "📍 Where are you traveling from?",
                placeholder="e.g., New York, USA",
                help="Enter your departure city and country"
            )
            
            destination = st.text_input(
                "🎯 Where do you want to go?",
                placeholder="e.g., Tokyo, Japan",
                help="Enter your destination city and country"
            )
            
            date_range = st.text_input(
                "📅 When do you want to travel?",
                placeholder="e.g., March 2026",
                help="Enter your preferred travel dates or time period"
            )
            
            duration = st.text_input(
                "⏱️ How long is your trip?",
                placeholder="e.g., 10 days",
                help="Enter the duration of your trip"
            )
        
        with col2:
            interests = st.text_input(
                "🎭 What are your interests?",
                placeholder="e.g., culture, food, history, adventure",
                help="Enter your travel interests separated by commas"
            )
            
            budget = st.text_input(
                "💰 What's your budget range?",
                placeholder="e.g., $3000-5000 or moderate",
                help="Enter your budget range or category"
            )
            
            travelers = st.text_input(
                "👥 Number of travelers",
                placeholder="e.g., 2",
                help="Enter the number of people traveling"
            )
        
        st.markdown("")  # Spacing
        submitted = st.form_submit_button("✨ Create My Travel Plan")
    
    # Process form submission
    if submitted:
        # Validate inputs
        if not all([origin, destination, date_range, duration, interests, budget, travelers]):
            st.error("⚠️ Please fill in all fields before submitting!")
            return
        
        # Show loading state
        with st.spinner("🔍 Our AI agents are working on your personalized travel plan..."):
            try:
                # Prepare inputs
                inputs = {
                    'origin': origin,
                    'destination': destination,
                    'date_range': date_range,
                    'duration': duration,
                    'interests': interests,
                    'budget': budget,
                    'travelers': travelers,
                    'current_year': str(datetime.now().year),
                    'topic': f"travel from {origin} to {destination}"
                }
                
                # Create a placeholder for the output
                output_container = st.container()
                
                # Run the crew
                with output_container:
                    st.success("✅ AI Agents are researching your destination...")
                    result = AiTravelAgent().crew().kickoff(inputs=inputs)
                
                # Display success message
                st.balloons()
                st.success("🎉 Your travel plan is ready!")
                
                # Display the result
                st.markdown("---")
                st.markdown("### 📄 Your Personalized Travel Report")
                
                # Try to read the generated report
                try:
                    with open('report.md', 'r') as f:
                        report_content = f.read()
                    
                    st.markdown(report_content)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Report",
                        data=report_content,
                        file_name=f"travel_plan_{destination.replace(' ', '_').replace(',', '')}_{datetime.now().strftime('%Y%m%d')}.md",
                        mime="text/markdown"
                    )
                except FileNotFoundError:
                    st.warning("Report file not found, but here's the raw output:")
                    st.write(result)
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.exception(e)

if __name__ == "__main__":
    main()

