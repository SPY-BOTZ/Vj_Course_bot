# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

api_id = int(os.environ.get("API_ID", "23621595"))
api_hash = os.environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
bot_token = os.environ.get("BOT_TOKEN", "8653062194:AAHFvoh5A9zO5OYk5ruroH1-EYe56dk1smg")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "1249672673").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
