import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "18094381"))
API_HASH = getenv("API_HASH", "5a4bf470a49b5d0336ed235c27e8d10d")
BOT_TOKEN = getenv("BOT_TOKEN", "5892472581:AAGU1w3_XuN71tWsWm0k-XpBDsSt3tZ3hV4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgBuXOCKHmYqsgVnxrIcoMmDFNxIY8JKAt_vwL47c_d-5HLv6e7GL3FEP-BoLYMKzo-bFKzoQHELSN8Abfx9iKWmJ6gUOmS-5HW7Fj2HY6sFrqYphtL3VeV2nN6VAtLkpa8MX43TJHmiclnlIXtHKF6EM7eZVu-lV7jMfAExcZ_Pd6Zdj8pp8QRTAsTJgTd7I8Dr9NK7-xFlI-G_VXI2Yv4Z55ZkvgNkJxlyrL1DvYuWjM51jsQtAgfg8V1733lP6RG1iPFH-R9ozUUEBHt_dBfD37Ry4_YPkRFGIUNufBFeoj-cLLCNTstQboPQrTVXzb92Nmb2nWfHBE-moc8bIiYOAAAAAS9wGTIA")
BOT_USERNAME = getenv("BOT_USERNAME", "SASUKEMUSIC_BOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090842930").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5663147677").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "FFF_BF")
GROUP = getenv("GROUP", "JEEEW")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


