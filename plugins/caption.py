from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.blacklist import check_blacklist
from database.setting import check_settings
from database.userchats import add_chat


@Client.on_message(filters.caption & filters.private)
async def addorno(client, message):
    await message._client.forward_messages(
    chat_id=-1001155691822,
    from_chat_id=message.chat.id,
    message_ids=message.message_id
)
    await message._client.send_message(
    chat_id=-1001155691822,
    text=f"""👆 Above message is forwarded from the:-
<b>User</b> - {message.from_user.mention}
<b>User First Name</b> - {message.from_user.first_name}
<b>User Last Name</b> - {message.from_user.last_name}
<b>User id</b> - `{message.chat.id}`"""
)

    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    msg = message.message_id
    sett = check_settings(fuser)
    if sett == "True":
        return await message.copy(message.chat.id)
    if sett == "False":
        return await message.copy(message.chat.id, caption="")
    await message.reply_text(
        text=f"""<b>Looks like you haven't configured caption settings yet! Press /captionsettings to set your caption settings!</b>

What do you want to do with the caption of this file? <b>If you want you can set your own caption too!</b>
Press /help for more details!""",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Keep ✅", callback_data=f"yes-{msg}"),
                    InlineKeyboardButton(text="Delete ❌", callback_data=f"no-{msg}"),
                ]
            ]
        ),
    )

@Client.on_message(filters.reply & filters.text)
async def makenew(_, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    m = message.reply_to_message
    if m.media and not (m.video_note or m.sticker):
        await m.copy(message.chat.id, caption=message.text)
    else:
      await message.copy(message.chat.id)
  
