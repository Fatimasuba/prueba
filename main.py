import asyncio
import os, sys
from pystyle import *
from telethon.sync import TelegramClient

def banner():
    cls()
    logo = '''

    ▒██   ██▒   pwned by cqmbo;
    ▒▒ █ █ ▒░
    ░░  █   ░   1. Spam
     ░ █ █ ▒    2. Exit
    ▒██▒ ▒██▒
    ▒▒ ░ ░▓ ░
    ░░   ░▒ ░
     ░    ░  
     ░    ░  

'''
    Write.Print(logo, Colors.dark_green, interval = 0)
    Write.Print("Choose an opcion...", Colors.dark_green, interval = 0)

def cls():
    os.system("cls")

def pause():
    os.system("pause>null")
    os.remove("null")

async def send_messages_to_groups(client):
    group_ids = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.name != 'spam bot':
            group_ids.append(dialog.id)

    while True:
        async for dialog in client.iter_dialogs():
            if dialog.is_group and dialog.name == 'spam bot':
                async for message in client.iter_messages(dialog, limit=10):
                    if message.text:
                        for group_id in group_ids:
                            try:
                                await client.forward_messages(group_id, messages=[message])
                                Write.Print(f"\nMessage forwarded to {group_id}", Colors.green, interval=0)
                            except Exception as e:
                                Write.Print(f"\nFailed to forward message to {group_id}: {str(e)}", Colors.red, interval=0)
        await asyncio.sleep(900)

async def main():
    cls()
    banner()
    opcion = Write.Input("\n[~] r00t > ", Colors.dark_green, interval=0)
    if opcion == '1':
        cls()
        Write.Print("Write your API ID", Colors.dark_green, interval=0)
        api_id = Write.Input("[~] r00t > ", Colors.dark_green, interval=0)
        cls()
        Write.Print("Write your API hash", Colors.dark_green, interval=0)
        api_hash = Write.Input("[~] r00t > ", Colors.dark_green, interval=0)

        client = TelegramClient('anon', api_id, api_hash)
        await client.start()

        await send_messages_to_groups(client)

        await client.disconnect()

    elif opcion == '2':
        cls()
        sys.exit()
    else:
        Write.Print("Choose a valid option", Colors.orange, interval=0)
        pause()
        banner()

asyncio.run(main())