from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging

logging.basicConfig(level=logging.INFO)

def about_text():
    """Returns the about text"""
    return f"""
    <b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓
    × ○ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : <a href='tg://user?id=7102263732'>Akki♛</a>
    × ○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/+ZsTyVaKlWL9lNjdl'>Haniflix :)</a>
    × ○ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/blackhawks_unit'>Anivoid</a>
    ┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>
    """

def about_keyboard():
    """Returns the about keyboard"""
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data="close")
            ]
        ]
    )

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=about_text(),
            disable_web_page_preview=True,
            reply_markup=about_keyboard()
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except Exception as e:
            logging.error(f"Error deleting message: {e}")
