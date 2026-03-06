import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import START_IMAGES

START_TXT = """✨ **Aᴅᴠᴀɴᴄᴇᴅ Rᴇɴᴀᴍᴇ Bᴏᴛ V4** ✨

👋 **Hᴇʟʟᴏ** {mention},

I ᴀᴍ ᴀ Pᴏᴡᴇʀғᴜʟ **Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ** ᴡɪᴛʜ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ.

🛡 **Sᴜᴘᴘᴏʀᴛ:** [SᴇʀɪᴀʟVᴇʀsᴇ Sᴜᴘᴘᴏʀᴛ](https://t.me/SerialVerse_support)"""

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("💝 Jᴏɪɴ Cʜᴀɴɴᴇʟ", url="https://t.me/Hindi_Tv_Verse")],
        [InlineKeyboardButton("🧙‍♀️ Mᴀɪɴ Cʜᴀɴɴᴇʟ", url="https://t.me/AJ_TVSERIAL")],
        [InlineKeyboardButton("👨‍💻 Oᴡɴᴇʀ", url="https://t.me/SerialVerse_support")]
    ])
    await message.reply_photo(random.choice(START_IMAGES), caption=START_TXT.format(mention=message.from_user.mention), reply_markup=btn)
