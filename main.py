import os
from telethon import TelegramClient, events

# =========================
# SESSION FOLDER
# =========================
SESSION_DIR = "sessions"

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

# =========================
# USER INPUT (NO HARDCODE)
# =========================
api_id = input("Enter API ID: ")
api_hash = input("Enter API HASH: ")
bot_token = input("Enter BOT TOKEN: ")

session_name = input("Session name (example: bot1): ")
session_path = os.path.join(SESSION_DIR, session_name)

# =========================
# CLIENT START (SESSION BASED)
# =========================
bot = TelegramClient(session_path, api_id, api_hash).start(bot_token=bot_token)

print("\n✅ Bot started successfully!")
print("📁 Session saved in sessions folder")


# =========================
# COMMAND SYSTEM
# =========================
@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("🤖 Bot is running!")

@bot.on(events.NewMessage(pattern="/promote"))
async def promote(event):
    try:
        if not event.is_group:
            await event.reply("❌ Use this in group")
            return

        if not event.reply_to_msg_id:
            await event.reply("❌ Reply to a user message")
            return

        user = await event.get_reply_message()

        await bot.edit_admin(
            event.chat_id,
            user.sender_id,
            is_admin=True
        )

        await event.reply("✅ User promoted to admin")

    except Exception as e:
        await event.reply(f"❌ Error: {e}")


@bot.on(events.NewMessage(pattern="/demote"))
async def demote(event):
    try:
        user = await event.get_reply_message()

        await bot.edit_admin(
            event.chat_id,
            user.sender_id,
            is_admin=False
        )

        await event.reply("✅ Admin removed")

    except Exception as e:
        await event.reply(f"❌ Error: {e}")


print("Bot is running...")
bot.run_until_disconnected()
