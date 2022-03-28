#Developer: Hiruwa

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer", url="https://t.me/r5pro")],
        [InlineKeyboardButton(
            "Report Bugs 😪", url="https://t.me/r5pro")]
    ])
    welcomed = f" <b>{message.from_user.first_name}</b>\ /help 🖕🖕🖕.\n\nHey <b>{message.from_user.first_name}</b>\n/help for More info..🤭"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
