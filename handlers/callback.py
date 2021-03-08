from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
import sira
import tgcalls


@Client.on_callback_query(filters.regex("close"))
async def close(client: Client, query: CallbackQuery):
    await query.message.delete()

@Client.on_callback_query(filters.regex("skipcall"))
async def skipthecall(client: Client, query: CallbackQuery):
	user = await client.get_chat_member(chat_id=query.message.chat.id, user_id=query.from_user.id)
	if not (user.status == "creator" or user.status == "administrator"):
		return
	else:
		chat_id = query.message.chat.id
	    sira.task_done(chat_id)
	    if sira.is_empty(chat_id):
	        tgcalls.pytgcalls.leave_group_call(chat_id)
	    else:
	        tgcalls.pytgcalls.change_stream(
	            chat_id, sira.get(chat_id)["file_path"]
	        )

	    await query.message.reply_text("⏩ Skipped the current song!")