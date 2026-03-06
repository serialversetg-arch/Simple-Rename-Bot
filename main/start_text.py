import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- CONFIGURATION (Images & Texts) ---

START_IMAGES = [
    "https://i.ibb.co/9Hnpgttg/x.jpg",
    "https://i.ibb.co/G3Q974K3/x.jpg",
    "https://i.ibb.co/fzZTRQh8/x.jpg",
    "https://i.ibb.co/S7609P4B/x.jpg",
    "https://i.ibb.co/pBZbL7V9/x.jpg"
]

START_TEXT = """
✨ **Aᴅᴠᴀɴᴄᴇᴅ Rᴇɴᴀᴍᴇ Bᴏᴛ V4** ✨

👋 **Hᴇʟʟᴏ** {mention},

I ᴀᴍ ᴀ Pᴏᴡᴇʀғᴜʟ **Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ** ᴡɪᴛʜ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ & Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ.

🚀 **Hᴏᴡ Tᴏ Usᴇ?**
1️⃣ Sᴇɴᴅ ᴍᴇ ᴀɴʏ **Fɪʟᴇ** ᴏʀ **Vɪᴅᴇᴏ**.
2️⃣ Sᴇɴᴅ ᴀ **Pʜᴏᴛᴏ** ᴛᴏ sᴇᴛ ɪᴛ ᴀs Tʜᴜᴍʙɴᴀɪʟ.
3️⃣ Usᴇ `/set_caption` ᴛᴏ sᴇᴛ ʏᴏᴜʀ Cᴀᴘᴛɪᴏɴ.

🛡 **Sᴜᴘᴘᴏʀᴛ:** [SᴇʀɪᴀʟVᴇʀsᴇ Sᴜᴘᴘᴏʀᴛ](https://t.me/SerialVerse_support)
"""

# --- BUTTONS SETUP ---

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💝 Jᴏɪɴ Tᴇʟᴇɢʀᴀᴍ Cʜᴀɴɴᴇʟ", url="https://t.me/Hindi_Tv_Verse")
        ],
        [
            InlineKeyboardButton("🧙‍♀️ Jᴏɪɴ Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ", url="https://t.me/AJ_TVSERIAL")
        ],
        [
            InlineKeyboardButton("👨‍💻 Oᴡɴᴇʀ", url="https://t.me/SerialVerse_support"),
            InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about")
        ]
    ]
)

# --- START COMMAND HANDLER ---

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    # Har baar /start par ek random photo select hogi
    random_photo = random.choice(START_IMAGES)
    
    try:
        await message.reply_photo(
            photo=random_photo,
            caption=START_TEXT.format(mention=message.from_user.mention),
            reply_markup=START_BUTTONS
        )
    except Exception as e:
        # Agar image load nahi hui toh text message bhej dega
        await message.reply_text(
            text=START_TEXT.format(mention=message.from_user.mention),
            reply_markup=START_BUTTONS
        )

# --- ABOUT CALLBACK (Optional) ---

@Client.on_callback_query(filters.regex("about"))
async def about(bot, update):
    ABOUT_TEXT = """
📜 **Bᴏᴛ Dᴇᴛᴀɪʟs** 📜

✨ **Nᴀᴍᴇ:** Rᴇɴᴀᴍᴇʀ V4
🚀 **Sᴘᴇᴇᴅ:** 100 Mbps+
💻 **Lᴀɴɢᴜᴀɢᴇ:** Pʏᴛʜᴏɴ 3
🛰 **Sᴇʀᴠᴇʀ:** V.P.S (Hɪɢʜ Sᴘᴇᴇᴅ)

🛡 **Oᴡɴᴇʀ:** [SᴇʀɪᴀʟVᴇʀsᴇ Sᴜᴘᴘᴏʀᴛ](https://t.me/SerialVerse_support)
⚡ **Pᴏᴡᴇʀᴇᴅ Bʏ:** [Hɪɴᴅɪ Tᴠ Vᴇʀsᴇ](https://t.me/Hindi_Tv_Verse)
"""
    await update.message.edit_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 Bᴀᴄᴋ", callback_data="back")]])
    )

@Client.on_callback_query(filters.regex("back"))
async def back(bot, update):
    await update.message.edit_caption(
        caption=START_TEXT.format(mention=update.from_user.mention),
        reply_markup=START_BUTTONS
    )
