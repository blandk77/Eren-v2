#(©) PythonBotz 




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7658357765:AAFNojY3QWjcLUvT17D5RYv1ZQFwhSQHCEA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26728872"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "96985c2aaea6c75408528909b7e18879")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002343892805"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1705634892"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DB_NAME = os.environ.get("DATABASE_NAME", "Not2Worry")

#Time in seconds for message Auto delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002169827133"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002347470858"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝑰 𝒘𝒐𝒏'𝒕 𝒍𝒆𝒕 𝒂𝒏𝒚𝒐𝒏𝒆 𝒕𝒂𝒌𝒆 𝒎𝒚 𝒇𝒓𝒆𝒆𝒅𝒐𝒎! 𝑨𝒏𝒅 <a href='https://t.me/Ongoing_AnimeGuy'>𝗢𝗻𝗴𝗼𝗶𝗻𝗴 𝗔𝗻𝗶𝗺𝗲 𝗚𝘂𝘆!!</a> 𝒘𝒊𝒍𝒍 𝒉𝒆𝒍𝒑 𝒚𝒐𝒖 𝒇𝒊𝒏𝒅 𝒕𝒉𝒆 𝒂𝒏𝒊𝒎𝒆 𝒚𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒃𝒓𝒆𝒂𝒌 𝒇𝒓𝒆𝒆 𝒇𝒓𝒐𝒎 𝒃𝒐𝒓𝒆𝒅𝒐𝒎! 𝑺𝒐 𝒘𝒉𝒚 𝒂𝒓𝒆 𝒚𝒐𝒖 𝒔𝒕𝒊𝒍𝒍 𝒘𝒂𝒊𝒕𝒊𝒏𝒈? 𝑱𝒐𝒊𝒏 𝒏𝒐𝒘!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1705634892 7465574522").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ!\n\nTᴏ ʜᴇʟᴘ ᴘʀᴇᴠᴇɴᴛ sᴘᴀᴍ ᴏɴ ᴏᴜʀ ʙᴏᴛs, ᴏɴʟʏ ᴜsᴇʀs ᴡʜᴏ ᴀʀᴇ ᴍᴇᴍʙᴇʀs ᴏғ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀʀᴇ ᴘᴇʀᴍɪᴛᴛᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ. Tᴏ ᴀᴄᴄᴇss ʏᴏᴜʀ ғɪʟᴇs, ᴘʟᴇᴀsᴇ ɪᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟs ʟɪsᴛᴇᴅ ʙᴇʟᴏᴡ ᴀɴᴅ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ!")

# Start & Fsub Pics ----------------------------------- #

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://files.catbox.moe/lllex3.jpg https://files.catbox.moe/2yztvd.jpg https://files.catbox.moe/uhv8s5.webp https://files.catbox.moe/2fbp1d.webp https://files.catbox.moe/pponhx.jpg https://files.catbox.moe/yzx835.jpg")).split() #Required

# Start & Fsub Pics ----------------------------------- #

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝑰 𝒅𝒐𝒏'𝒕 𝒘𝒐𝒓𝒌 𝒇𝒐𝒓 𝒚𝒐𝒖, 𝒃𝒖𝒅!!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

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
