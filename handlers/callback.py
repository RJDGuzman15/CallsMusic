from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import sira
import tgcalls


@Client.on_callback_query(filters.regex("close"))
async def close(client: Client, query: CallbackQuery):
    await query.message.delete()
