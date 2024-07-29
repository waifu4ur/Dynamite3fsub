from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    """
    Handles callback queries for the bot.

    Args:
        client (Bot): The Pyrogram bot instance.
        query (CallbackQuery): The callback query object.

    Returns:
        None
    """
    data = query.data

    # Handle "about" callback data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ○ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ : <a href='tg://user?id=7102263732'>Waifu</a>\n× ○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/+ZsTyVaKlWL9lNjdl'>ʜᴇɴᴛᴀɪ ꜰʟɪx :)</a>\n× ○ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/blackhawks_unit'>Haniflix network</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data="close")
                    ]
                ]
            )
        )

    # Handle "close" callback data
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
