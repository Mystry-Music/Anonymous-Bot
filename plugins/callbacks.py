from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.setting import caption_False, caption_True

from .start import REPLY_MARKUP, START


@Client.on_callback_query(filters.regex("^captz$"))
async def capa(_, query):
    await query.edit_message_text(
        text=f"""💠If you want to get your files back with the caption select "<b>Forward with caption ✅<b>"

💠If you want to get your files back without the caption select "<b>Forward without caption ❌<b>"

If you want to edit the caption afterwards send the text you want to set as the caption <b>as a reply to the file you forwarded to me.</b>

<i>press /help and see instructons if you do not understand!</i>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Forward with caption✅", callback_data="ca_yes"),
                    InlineKeyboardButton(text="Forward without caption ❌", callback_data="ca_no"),
                ],
                [InlineKeyboardButton(text="Back", callback_data="bbb")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("^ca_yes$"))
async def captyes(_, query):
    caption_True(query.from_user.id)
    await query.edit_message_text(
        "Now all of your files will be forwarded back with the caption. You can change this later if you want!",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data="bbb")]]
        ),
    )


@Client.on_callback_query(filters.regex("^ca_no$"))
async def captno(_, query):
    caption_False(query.from_user.id)
    await query.edit_message_text(
        "Now all of your files will be forwarded back without the caption. You can change this later if you want!",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Back", callback_data="bbb")]]
        ),
    )


@Client.on_callback_query(filters.regex("^bbb$"))
async def backbtt(_, query):
    await query.edit_message_text(
        START, reply_markup=REPLY_MARKUP, disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("^(yes|no)-"))
async def cbb(client, call):
    k = call.data
    msgid = int(k.split("-")[1])
    chat = call.message.chat.id
    if k.startswith("yes"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid)
    if k.startswith("no"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid, caption="")
