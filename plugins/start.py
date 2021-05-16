from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.userchats import add_chat
from vars import var

START_MSG = f"""
Hi {message.from_user.mention},

Just Forward me Some messages or media and I will **Anonymize** that !

If you forward me something I can reomove the forward tag and return it to you back.

𝗜 𝗰𝗮𝗻 𝗮𝗹𝘀𝗼 𝗲𝗱𝗶𝘁 𝘁𝗵𝗲 𝗰𝗮𝗽𝘁𝗶𝗼𝗻 𝗼𝗳 𝗮𝗻𝘆 𝗳𝗶𝗹𝗲 𝘆𝗼𝘂 𝘀𝗲𝗻𝗱 𝗺𝗲!🥳 

<b>First set your caption settings by pressing Caption Settings button!</b>
𝚙𝚛𝚎𝚜𝚜 /help 𝚝𝚘 𝚜𝚎𝚎 𝚖𝚘𝚛𝚎 𝚍𝚎𝚝𝚊𝚒𝚕𝚜!"""

HELP_TEXT = f"""
Forward Me A File,Video,Audio,Photo or Anything and I will Send You it Back!

First set your caption settings by pressing /captionsettings 

💠If you want to get your files back with the caption select "<b>Forward with caption ✅<b>"

💠If you want to get your files back without the caption select "<b>Forward without caption ❌<b>"

ᴡʜᴀᴛ ᴛᴏ ᴅᴏ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴛ ᴀ ɴᴇᴡ ᴄᴀᴘᴛɪᴏɴ?

Just write the caption you want to be on the file you sent me, <b>AS A REPLY TO THAT FILE</b> and the text you wrote will be attached to the file you sent!\n
See this image for example!👇
    Ex:- http://bit.ly/SEE-THlS"""

CAPTION_SETTINGS = f"""Configure your settings by pressing the below button👇"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Caption Settings", callback_data="captz")],
    ]
)


@Client.on_message(filters.command("start"))
async def start(client, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await message.reply_text(
        START, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )
    
@Client.on_message(filters.command("help"))    
async def help(client, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await message.reply_text(HELP_TEXT)
    
@Client.on_message(filters.command("captionsettings"))
async def captionsettings(client, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    await message.reply_text(
        CAPTION_SETTINGS, reply_markup=REPLY_MARKUP
    )
