# report_agent.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY")

# 🟢 THIS IS THE SAFE WAY:
genai.configure(api_key=api_key)

def generate_executive_report(chat_history: str, language: str) -> str:
    """Uses Google AI Studio to generate reports in the user's selected language."""
    
    # 👇 UPDATED PROMPT: Supports English & Bahasa Melayu dynamically 👇
    prompt = f"""
    Act as the Lead Reporting Agent for the Prime Minister's Office using the MyBENTENG (Digital Floodwall) GovTech system. 
    Review the following raw chat history from a MyBENTENG geospatial audit.
    Generate a formal, structured Executive Report based strictly on the provided audit history.
    
    CRITICAL RULE 1: You MUST write the entire report strictly in {language}. 
    If {language} is 'Bahasa Melayu', use formal, professional government terminology (Bahasa Istana/Baku).
    
    CRITICAL RULE 2: Do NOT generate a 'To/From/Date/Subject' header. Start your response directly at Section 1.
    
    You MUST format the output exactly using the following structure (Translate these headers into {language}):
    
    ### 1. EXECUTIVE SUMMARY
    (Provide a brief, 2-3 sentence overview of the audit's purpose and the final safety verdict. Mention that the MyBENTENG AI processed this evaluation.)
    
    ### 2. AUDIT FINDINGS & TELEMETRY DATA
    (Use bullet points to list specific financial figures, RM losses, locations, and data extracted during the audit. Be highly specific.)
    
    ### 3. RISK ASSESSMENT & DIRECTIVES
    (Clearly state if the permit or project was marked 'RED ZONE / FAILED' or 'APPROVED'. List the immediate policy actions required to protect citizens.)

    Keep the tone highly professional, bureaucratic, and objective. Do not use conversational AI language.
    
    RAW CHAT HISTORY:
    {chat_history}
    """
    
    # 🟢 Initializing the AI Studio free tier model
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"🚨 MODEL ROUTING ERROR: {str(e)}\n\n(Tip: If this persists, try 'gemini-2.5-pro' instead.)"