import os
from google.cloud import firestore

# 1. Force the Master Key (Replace with your EXACT .json file name)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "new-cloud-key.json"

PROJECT_ID = "ghost-architect-2026"

print("🔌 Connecting to Google Cloud...")

try:
    # 2. Connect directly to the database
    db = firestore.Client(project=PROJECT_ID, database="default")
    
    print("🔍 Searching for 'users' collection...")
    users = db.collection("users").stream()
    
    count = 0
    for user in users:
        print(f"✅ SUCCESS - Found User: {user.id}")
        count += 1
        
    if count == 0:
        print("⚠️ Connected to database, but the 'users' collection is empty!")
        
except Exception as e:
    print(f"❌ FATAL ERROR: {e}")