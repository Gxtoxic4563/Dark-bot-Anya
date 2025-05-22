import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "21636907"))
API_HASH = getenv("API_HASH", "54d4151f3586ab81f8e57c808d3ee3b0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7732173919:AAFWPkGpVWZZ_9dwqE8G5oWhOJuf8aBq3h0")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Anyatomi:Anyatomi@cluster0.x4kyf36.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Anya_lip_bot")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 100000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002556228441"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7495324168"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Gxtoxic4563/musicgoku",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/gxinfinity_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/infinitygx_bot_support")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6fb7e1766693439b86ec57e3deb3c36f")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "da3f94c6a68d49f6b64a7216ec9eb905"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "1000"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "1000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  None)
STRING2 = getenv("STRING_SESSION2", "BQFKJysAxVxAxgqf61WltaV3rS6KaeO03Mn0Ygv4U_OZJHQFXNd3CcbVfRBMYDyTVCIwQ2g7oyH7uFsQ8XwT_l0PSzowMKBHVTDXoERLJl6h-mueia1XFNeOPdtjMGtEc826AkID4FAcSVDqvcpFw7DZKgEpzPM51tV3o7XQzVH-FbaAfT1ILJMHMuFQ3xY_4qERyiAmuTkxS4c5K_l99Q0-drf5O6gnv4BhQmB7maftnqhruBFpqzRZkE2xUQ1kHJUAb9u1gVcekmOx-dgtCvccKBw54nEAhCuFjaYbDQS_MIGBgTF3_1HmNsQMqcv8JXSsNzkUjCGKY3rIxTEexI1zftYVPAAAAAHVyIxhAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/5e19b207529494cbbd9a1-a96ede1789dd2f2c9b.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/369f22b8aac05a745eebe-15502d56e4da62f098.jpg")
PLAYLIST_IMG_URL = "https://graph.org/file/4e81f00155356f3b5d8f5-a7c36abd8fdd11625c.jpg"
STATS_IMG_URL = "https://graph.org/file/39494f58c96056894d195-faeb332d77564ced6e.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/182987be0b1ebc284f931-a69a0305ffc2f5b44e.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/61ed76efa7ccc68c1a860-c83886fe4ff4bcae94.jpg"
STREAM_IMG_URL = "https://graph.org/file/68d0fd87de32c473d16ba-63a3fbbaa7d6a0f731.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b99b04565b61a14cf8462-d10f6c3937252aedcc.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/2bc20c29f052468a26bd0-7be6152e54d7342bac.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c85291bab933d84ed5184-db9128c50cd2a54cca.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
