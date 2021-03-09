from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command(["start", "start@StreamMusicBot"])
    & filters.private
    & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**Hi [{message.from_user.first_name}](tg://user?id={message.from_user.id})**

This is Music Stream Bot!
Send me your Fav Song's YouTube Link & Join Voice Chat in [Linux Repositories](https://t.me/linux_repo) Group,

Enjoy ...
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/linux_repo"
                    ),
                    InlineKeyboardButton(
                        "Bots Channel 🔈", url="https://t.me/Discovery_Updates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Developer", url="https://t.me/AbirHasan2005"
                    )
                ]
            ]
        ),
        parse_mode="Markdown"
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
