#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7466292166:AAGDfvvC7RTeCYRnXjGwn2iv5sFL6JoOy-8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27526328"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "db231e73712db0b6397f624a75a760f8")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001901878734"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7102263732"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Animeverse07:shubh07@cluster0.i7z8kjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002088432628"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001767529410"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002106084128"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋 ʜɪ ᴅᴜᴅᴇ! 😎 {first}\n\nI'am file store bot of @Ariesaep! 📁✨\nʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ❗️")
try:
    ADMINS=[7102263732]
    for x in (os.environ.get("ADMINS", "1582227872 6095034047").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ꜱᴏʀʀʏ ᴅᴜᴅᴇ! ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ʏᴇᴛ.\n\nᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴀʟʟ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰɪʀꜱᴛ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜰɪʟᴇꜱ! 📂✨")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Kindly avoid messaging me directly I'm only able to assist through admin..!"

ADMINS.append(OWNER_ID)
ADMINS.append(7102263732)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
