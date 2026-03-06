from pyrogram import Client, filters
from config import ADMIN

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN))
async def broadcast(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("✨ **Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ.**")
    
    ms = await message.reply_text("🚀 **Bʀᴏᴀᴅᴄᴀsᴛ Sᴛᴀʀᴛᴇᴅ...**")
    # Yahan loop lagega users ki list pe (Database required)
    await ms.edit("✅ **Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ!**")
