#Developer : Hiruwa

from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"ඔබට ලබා ගත හැක්කේ යූ ටියුබ් වීඩියෝස් සහ ඕඩියෝ පමනයි කරුනාකර ප්ලේලිස්ට් ලින්ක් ලබා නොදෙන්න..\nCurrently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_text(helptxt)
