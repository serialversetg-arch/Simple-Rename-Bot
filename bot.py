from aiohttp import web
import asyncio
from pyrogram import Client
from config import *
import os


# --- Health Check Setup ---
async def health_check(request):
    # Jab platform Port 8000 pe request bhejega, ye "OK" return karega
    return web.Response(text="Bot is Alive and Running!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    # Port 8000 pe server start ho raha hai
    site = web.TCPSite(runner, "0.0.0.0", 8000)
    await site.start()
    print("✅ TCP Health Check Server started on Port 8000")

# --- Bot Start Logic ---
async def main():
    # Health check server ko background mein chalane ke liye
    await start_server()
    
    # Aapka bot start karne ka code yahan aayega
    # Example: await bot.start()
    # await idle()

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()      
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       
    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")


bot = Bot()
bot.run()
