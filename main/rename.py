import time, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from utills import progress_for_pyrogram, humanbytes
from database import db

@Client.on_message(filters.private & filters.command("set_caption"))
async def set_cap(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ **Usage:** `/set_caption Your Stylish Caption`")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text(f"✅ **Cᴀᴘᴛɪᴏɴ Sᴀᴠᴇᴅ!**\n\n`{caption}`")

@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def rename_handler(bot, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    
    await message.reply_text(
        text=f"📝 **Fɪʟᴇ Nᴀᴍᴇ:** `{filename}`\n\nSᴇɴᴅ Mᴇ Nᴇᴡ Nᴀᴍᴇ Wɪᴛʜ Extension.",
        reply_markup=ForceReply(True),
        quote=True
    )

@Client.on_message(filters.private & filters.reply)
async def do_rename(bot, message):
    if message.reply_to_message.reply_markup and isinstance(message.reply_to_message.reply_markup, ForceReply):
        new_name = message.text
        media = message.reply_to_message
        file = getattr(media, media.media.value)
        
        ms = await message.reply_text("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ғɪʟᴇ...**")
        path = await bot.download_media(
            message=media,
            file_name=new_name,
            progress=progress_for_pyrogram,
            progress_args=("📥 **Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ...**", ms, time.time())
        )
        
        await ms.edit("📤 **Uᴘʟᴏᴀᴅɪɴɢ ғɪʟᴇ...**")
        
        # Database se Thumb aur Caption uthana
        user_id = message.from_user.id
        thumb_id = await db.get_thumbnail(user_id)
        caption = await db.get_caption(user_id)
        
        try:
            await bot.send_document(
                chat_id=message.chat.id,
                document=path,
                thumb=thumb_id,
                caption=caption if caption else f"**{new_name}**",
                progress=progress_for_pyrogram,
                progress_args=("📤 **Uᴘʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ...**", ms, time.time())
            )
        except Exception as e:
            await ms.edit(f"❌ **Error:** `{e}`")
        
        await ms.delete()
        os.remove(path)
