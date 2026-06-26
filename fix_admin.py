from supabase import create_client
import bcrypt

# These are your EXACT new database credentials
URL = "https://enagkhfoyqxlwamvauqu.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVuYWdnaGZveXF4bHdhbXZhdXF1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODI0NjY2NDgsImV4cCI6MjA5ODA0MjY0OH0.Mwpnc6Wo-LzDDOjcrX7q4LrAdrCO4d1Owj3YKN-FK5o"

db = create_client(URL, KEY)

# 1. Delete any existing admin to start fresh
db.table('admins').delete().neq('id', 0).execute()
print("Cleared old admins.")

# 2. Create new admin with Python's bcrypt (guaranteed to match)
password_hash = bcrypt.hashpw("Admin@2026#".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

result = db.table('admins').insert({
    'username': 'admin',
    'email': 'admin@gmail.com',
    'password_hash': password_hash,
    'email_verified': 1
}).execute()

print("SUCCESS! Admin created in the NEW database.")