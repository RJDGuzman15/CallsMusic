from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

import tgcalls
from converter import convert
from youtube import download
import sira
from config import DURATION_LIMIT
from helpers.wrappers import errors
from helpers.errors import DurationLimitError


@Client.on_message(filters.command("play") | filters.command("play@StreamMusicBot") | filters.regex(r"http"))
@errors
async def play(client: Client, message_: Message):
    audio = (message_.reply_to_message.audio or message_.reply_to_message.voice) if message_.reply_to_message else None
    linux_repo = -1001256038785
    chatID = message_.chat.id
    if message_.chat.type == "private":
        chatID = linux_repo
    res = None
    file_name = None
    file_path = None
    is_playing = None
    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {audio.duration / 60} minute(s)"
            )

        file_name = audio.file_id + audio.file_name.split(".")[-1]
        file_path = await convert(await message_.reply_to_message.download(file_name))
    else:
        messages = [message_]
        text = ""
        offset = None
        length = None

        if message_.reply_to_message:
            if not ("youtube" or "youtu.be") in message_.reply_to_message.text:
                return
            res = await message_.reply_text("🔄 Scaning ...", parse_mode="Markdown", disable_web_page_preview=True)
            messages.append(message_.reply_to_message)
        elif ("youtube" or "youtu.be") in message_.text:
            res = await message_.reply_text("🔄 Scaning ...", parse_mode="Markdown", disable_web_page_preview=True)
            messages.append(message_)
        else:
            # await res.delete()
            return
        for message in messages:
            if offset:
                break

            if message.entities:
                for entity in message.entities:
                    if entity.type == "url":
                        text = message.text or message.caption
                        offset, length = entity.offset, entity.length
                        break

        if offset == None:
            await res.edit_text("❕ You did not give me anything to play!")
            return

        url = text[offset:offset+length]

        file_path = await convert(download(url))
    try:
        is_playing = tgcalls.pytgcalls.is_playing(chatID)
    except:
        is_playing = False

    if is_playing:
        position = await sira.add(chatID, file_path)
        await res.edit_text(f"#️⃣  Queued at position {position} !!")
    else:
        await res.edit_text(f"A Song Requested By [{message_.from_user.first_name}](tg://user?id={message_.from_user.id})\n\n▶️ Playing `{file_name}` ...")
        tgcalls.pytgcalls.join_group_call(chatID, file_path, 48000)
