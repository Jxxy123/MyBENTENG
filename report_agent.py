# ==============================================================================
# MODULE: MyBENTENG Executive Reporting Engine (Agent-to-Agent Architecture)
# PURPOSE: Transforms raw geospatial audit data into formal government memoranda.
# COMPLIANCE: Supports Multilingual Output (English & Bahasa Melayu Baku).
# ==============================================================================

import os
from dotenv import load_dotenv
import google.generativeai as genai

# --- SECTION 1: SYSTEM CONFIGURATION ---
# This agent utilizes the Google AI Studio (Generative AI) SDK for high-speed
# text synthesis and professional document formatting

load_dotenv() 
api_key = os.getenv("GOOGLE_API_KEY")

# Secure API configuration for the secondary reporting agent

genai.configure(api_key=api_key)

# --- SECTION 2: THE EXECUTIVE REPORTING ENGINE ---
# This function is triggered by the Main Terminal (Fatima's Dashboard) to
# Summarize an entire audit trail into a PMO-ready format

def generate_executive_report(chat_history: str, language: str) -> str:
    """Uses Google AI Studio to generate reports in the user's selected language."""
    
    # --- SECTION 3: PROMPT ENGINEERING & AGENT PERSONA ---
    # We define a "Lead Reporting Agent" persona to ensure the output 
    # Maintains a professional, objective, and bureaucratic tone

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
    
    # --- SECTION 4: MODEL EXECUTION & ERROR HANDLING ---
    # Initializing the model with 2.5-Flash for low-latency response generation

    model = genai.GenerativeModel("gemini-2.5-flash")
    
    try:
        # Agent processes the data through the system instructions defined above
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Fail-safe reporting for satellite connectivity/API issues
        return f"🚨 MODEL ROUTING ERROR: {str(e)}\n\n(Tip: If this persists, try 'gemini-2.5-pro' instead.)"

# ==============================================================================
#                         END OF REPORTING MODULE
# ==============================================================================