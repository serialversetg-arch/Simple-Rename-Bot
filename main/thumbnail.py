from pyrogram import Client, filters

@Client.on_message(filters.private & filters.photo)
async def save_thumb(bot, message):
    # Temporary logic (Permanent ke liye MongoDB chahiye hoga)
    await message.reply_text("✅ **Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Tᴇᴍᴘᴏʀᴀʀɪʟʏ!**\n(Note: Setup MongoDB for permanent storage)")

@Client.on_message(filters.command("del_thumb") & filters.private)
async def delete_thumb(bot, message):
    await message.reply_text("🗑️ **Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ!**")
