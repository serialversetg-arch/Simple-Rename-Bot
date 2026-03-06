from pyrogram import Client, filters
from pyrogram.types import ForceReply
from utils import progress_for_pyrogram
import time, os

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def rename_req(bot, message):
    await message.reply_text("📝 **Eɴᴛᴇʀ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ:**", reply_markup=ForceReply(True), quote=True)

@Client.on_message(filters.private & filters.reply)
async def rename_proc(bot, message):
    if message.reply_to_message.reply_markup and isinstance(message.reply_to_message.reply_markup, ForceReply):
        new_name = message.text
        media = message.reply_to_message
        ms = await message.reply_text("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
        
        path = await bot.download_media(media, file_name=new_name, progress=progress_for_pyrogram, progress_args=("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ...**", ms, time.time()))
        
        await ms.edit("📤 **Uᴘʟᴏᴀᴅɪɴɢ...**")
        await bot.send_document(message.chat.id, document=path, caption=f"**{new_name}**", progress=progress_for_pyrogram, progress_args=("📤 **Uᴘʟᴏᴀᴅɪɴɢ...**", ms, time.time()))
        
        await ms.delete()
        os.remove(path)
