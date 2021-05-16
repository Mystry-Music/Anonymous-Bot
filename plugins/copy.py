from pyrogram import Client, filters

from database.blacklist import check_blacklist
from database.userchats import add_chat


@Client.on_message(filters.private & ~filters.caption & ~filters.command("start") & ~filters.command("help") & ~filters.command("captionsettings"))
async def copy(client, message):
    fuser = str(message.from_user.id)
    if check_blacklist(fuser):
        return
    add_chat(fuser)
    chat = message.chat.id
    await message.copy(chat)
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
