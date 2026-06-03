import os
from telethon.sync import TelegramClient

SESSION_DIR = "sessions"

if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

api_id = input("Enter API ID: ")
api_hash = input("Enter API HASH: ")
phone = input("Enter Phone Number (+880...): ")

session_name = os.path.join(SESSION_DIR, "session")

client = TelegramClient(session_name, api_id, api_hash)

print("\nLogging in...")
client.start(phone=phone)
print("Login Successful! Session saved.\n")

while True:
    print("\n===== TELEGRAM CONTROL TOOL =====")
    print("[1] Promote Admin")
    print("[2] Demote Admin")
    print("[3] Ban User")
    print("[4] Unban User")
    print("[5] My Info")
    print("[0] Exit")

    choice = input("Select: ")

    if choice == "1":
        group = input("Group username/ID: ")
        user = input("User ID/Username: ")

        client.edit_admin(group, user, is_admin=True)
        print("Admin promoted!")

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
