#Developer: Hiruwa

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer", url="https://t.me/trexbots")],
        [InlineKeyboardButton(
            "Report Bugs 😪", url="https://t.me/hiruwa")]
    ])
    welcomed = f"හායි <b>{message.from_user.first_name}</b>\nවැඩි විස්තර සදහා /help ලබා දෙන්න.🤭\n\nHey <b>{message.from_user.first_name}</b>\n/help for More info..🤭"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
