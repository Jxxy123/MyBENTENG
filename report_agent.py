# report_agent.py
import os
from dotenv import load_dotenv  # 👈 Add this line
import google.generativeai as genai

load_dotenv()  # 👈 This line "opens" your .env vault
api_key = os.getenv("GOOGLE_API_KEY")  # 👈 This line "grabs" the key safely

# 🟢 THIS IS THE SAFE WAY:
genai.configure(api_key=api_key)

def generate_executive_report(chat_history: str) -> str:
    """Uses Google AI Studio to generate reports for $0.00."""
    
    # 👇 UPDATED PROMPT: MyBENTENG Branding & English Rules 👇
    prompt = f"""
    Act as the Lead Reporting Agent for the Prime Minister's Office using the MyBENTENG (Digital Floodwall) GovTech system. 
    Review the following raw chat history from a MyBENTENG geospatial audit.
    Generate a formal, structured Executive Report based strictly on the provided audit history.
    
    CRITICAL RULE 1: You MUST write the entire report strictly in ENGLISH. Do not use Bahasa Melayu.
    CRITICAL RULE 2: Do NOT generate a 'To/From/Date/Subject' header. Start your response directly at Section 1.
    
    You MUST format the output exactly using the following structure:
    
    ### 1. EXECUTIVE SUMMARY
    (Provide a brief, 2-3 sentence overview of the audit's purpose and the final safety verdict in English. Mention that the MyBENTENG AI processed this evaluation.)
    
    ### 2. AUDIT FINDINGS & TELEMETRY DATA
    (Use bullet points to list specific financial figures, RM losses, locations, and data extracted during the audit. Be highly specific. English only.)
    
    ### 3. RISK ASSESSMENT & DIRECTIVES
    (Clearly state if the permit or project was marked 'RED ZONE / FAILED' or 'APPROVED'. List the immediate policy actions required to protect citizens. English only.)

    Keep the tone highly professional, bureaucratic, and objective. Do not use conversational AI language.
    
    RAW CHAT HISTORY:
    {chat_history}
    """
    
    # 🟢 CHANGED: Initializing the AI Studio free tier model
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    try:
        # 👇 THIS GENERATION LOGIC STAYS EXACTLY THE SAME
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # 👇 THIS ERROR HANDLING STAYS EXACTLY THE SAME
        return f"🚨 MODEL ROUTING ERROR: {str(e)}\n\n(Tip: If this persists, try 'gemini-2.5-pro' instead.)"