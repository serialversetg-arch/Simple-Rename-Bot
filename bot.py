import os
import asyncio
from aiohttp import web
from pyrogram import Client, idle
from config import *

async def health_check(request):
    return web.Response(text="Bot is Alive!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", 8000).start()

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Stylish-Renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "main"}
        )

    async def start(self):
        await super().start()
        asyncio.create_task(start_server())
        me = await self.get_me()
        print(f"✅ {me.first_name} STARTED on Port 8000")

    async def stop(self, *args):
        await super().stop()

if __name__ == "__main__":
    Bot().run()
