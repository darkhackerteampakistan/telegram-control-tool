import os
from telethon.sync import TelegramClient

SESSION_DIR = "sessions"

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)


# =========================
# LOGIN SYSTEM
# =========================
api_id = input("Enter API ID: ")
api_hash = input("Enter API HASH: ")
phone = input("Enter Phone Number: ")

# session name input (multi-account support)
session_name = input("Session Name (example: account1): ")

session_path = os.path.join(SESSION_DIR, session_name)

client = TelegramClient(session_path, api_id, api_hash)

print("\n🔄 Checking session...")

# =========================
# START LOGIN
# =========================
client.start(phone=phone)

print("✅ Login Successful!")
print(f"📁 Session saved: sessions/{session_name}.session")


# =========================
# MENU SYSTEM
# =========================
while True:
    print("\n===== TELEGRAM CONTROL PANEL =====")
    print("[1] Promote Admin")
    print("[2] Demote Admin")
    print("[3] Ban User")
    print("[4] Unban User")
    print("[5] My Info")
    print("[0] Exit")
    print("==================================")

    choice = input("Select option: ")

    # -------------------------
    # PROMOTE ADMIN
    # -------------------------
    if choice == "1":
        try:
            group = input("Group username/ID: ")
            user = input("User ID/Username: ")

            client.edit_admin(group, user, is_admin=True)
            print("✅ Admin promoted!")

        except Exception as e:
            print("❌ Error:", e)

    # -------------------------
    # DEMOTE ADMIN
    # -------------------------
    elif choice == "2":
        try:
            group = input("Group: ")
            user = input("User: ")

            client.edit_admin(group, user, is_admin=False)
            print("✅ Admin removed!")

        except Exception as e:
            print("❌ Error:", e)

    # -------------------------
    # BAN USER
    # -------------------------
    elif choice == "3":
        try:
            group = input("Group: ")
            user = input("User: ")

            client.kick_participant(group, user)
            print("🚫 User banned!")

        except Exception as e:
            print("❌ Error:", e)

    # -------------------------
    # UNBAN USER
    # -------------------------
    elif choice == "4":
        try:
            group = input("Group: ")
            user = input("User: ")

            client.edit_permissions(group, user, view_messages=True)
            print("✅ User unbanned!")

        except Exception as e:
            print("❌ Error:", e)

    # -------------------------
    # INFO
    # -------------------------
    elif choice == "5":
        me = client.get_me()
        print("\n👤 ACCOUNT INFO")
        print("Name:", me.first_name)
        print("Username:", me.username)
        print("ID:", me.id)

    # -------------------------
    # EXIT
    # -------------------------
    elif choice == "0":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice")

    elif choice == "2":
        group = input("Group: ")
        user = input("User: ")

        client.edit_admin(group, user, is_admin=False)
        print("Admin removed!")

    elif choice == "3":
        group = input("Group: ")
        user = input("User: ")

        client.kick_participant(group, user)
        print("User banned!")

    elif choice == "4":
        group = input("Group: ")
        user = input("User: ")

        client.edit_permissions(group, user, view_messages=True)
        print("User unbanned!")

    elif choice == "5":
        me = client.get_me()
        print(f"\nName: {me.first_name}")
        print(f"Username: {me.username}")
        print(f"ID: {me.id}")

    elif choice == "0":
        break

    else:
        print("Invalid choice")
