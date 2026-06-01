import streamlit as st
import requests

# 1. Page Configuration & UI Styling
st.set_page_config(page_title="HookGen AI", page_icon="🎥", layout="centered")
st.title("🎥 HookGen AI — Viral Video Script Generator")
st.write("Generate high-retention hooks and 30-second video scripts instantly.")

# 2. Access Protection (Simulating a Free/Premium Wall without Lemon Squeezy)
# You can give this simple password to friends or early users for access.
ACCESS_CODE = "KarachiAI2026" 
user_code = st.sidebar.text_input("Enter Access Code to Unlock", type="password")

if user_code != ACCESS_CODE:
    st.warning("⚠️ Please enter a valid Access Code in the sidebar to use this tool for free.")
else:
    st.success("🔓 Access Granted! Generate your scripts below.")

    # 3. User Input Form
    with st.form("script_form"):
        topic = st.text_input("What is your video topic?", placeholder="e.g., How to learn Python fast")
        audience = st.text_input("Who is your target audience?", placeholder="e.g., College students in Pakistan")
        tone = st.selectbox("Select Script Tone", ["High Energy", "Funny", "Professional", "Storytelling"])
        submitted = st.form_submit_button("Generate Viral Script 🚀")

    # 4. Processing the API Request with Agnes AI
    if submitted:
        if not topic or not audience:
            st.error("Please fill in both the topic and audience fields.")
        else:
            with st.spinner("Agnes AI is analyzing viral trends and writing your script..."):
                
                # Constructing the exact prompt payload
                system_prompt = f"You are an expert viral video strategist. Write 5 different high-retention opening hooks and a 30-second high-energy script for the topic: '{topic}', specifically targeted at {audience}. Use a {tone} tone. Make it engaging and viral-worthy."
                
                # Agnes AI API Configuration
                AGNES_API_KEY = "sk-jgAtOKDypV6DaWJT8Gc4Dg74OGQvKuvilwiusbLaltdCmdCq"
                url = "https://apihub.agnes-ai.com/v1/chat/completions"
                
                headers = {
                    "Authorization": f"Bearer {AGNES_API_KEY}",
                    "Content-Type": "application/json"
                }
                
                payload = {
                    "model": "agnes-2.0-flash",
                    "messages": [
                        {"role": "system", "content": "You are an expert viral video strategist."},
                        {"role": "user", "content": system_prompt}
                    ]
                }
                
                try:
                    # Making the live HTTP call
                    response = requests.post(url, json=payload, headers=headers)
                    
                    if response.status_code == 200:
                        result = response.json()
                        # Extract the text answer returned by Agnes AI
                        ai_script = result["choices"][0]["message"]["content"]
                        
                        # 5. Displaying Output to the User
                        st.subheader("✨ Generated Content")
                        st.text_area("Copy your script here:", value=ai_script, height=400)
                        st.balloons()
                    else:
                        st.error(f"API Error from Agnes AI: {response.status_code} - {response.text}")
                        
                except Exception as e:
                    st.error(f"Failed to connect to the server: {str(e)}")
