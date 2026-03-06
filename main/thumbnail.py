from pyrogram import Client, filters
from database import db # Maan lijiye aapka DB setup hai

@Client.on_message(filters.private & filters.photo)
async def add_thumbs(bot, message):
    user_id = message.from_user.id
    await db.set_thumbnail(user_id, file_id=message.photo.file_id)
    await message.reply_text("✅ **Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\nNᴏᴡ I ᴡɪʟʟ ᴜsᴇ ᴛʜɪs ɪᴍᴀɢᴇ ɪɴ ʏᴏᴜʀ ʀᴇɴᴀᴍᴇᴅ ғɪʟᴇs.")

@Client.on_message(filters.private & filters.command("del_thumb"))
async def delete_thumbs(bot, message):
    user_id = message.from_user.id
    await db.set_thumbnail(user_id, file_id=None)
    await message.reply_text("🗑️ **Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ!**")

@Client.on_message(filters.private & filters.command("show_thumb"))
async def view_thumbs(bot, message):
    user_id = message.from_user.id
    thumb = await db.get_thumbnail(user_id)
    if thumb:
        await message.reply_photo(photo=thumb, caption="🖼️ **Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ**")
    else:
        await message.reply_text("❌ **Nᴏ Tʜᴜᴍʙɴᴀɪʟ Fᴏᴜɴᴅ!**")
