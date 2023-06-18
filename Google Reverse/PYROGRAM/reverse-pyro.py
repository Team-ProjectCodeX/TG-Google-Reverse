# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# PROVIDED BY https://t.me/ProjectCodeX


#IMPORTS
import requests 
from pyrogram import *
from pyrogram.types import *
from pyrogram.enums import *

# (name = Your Bot's File Name)
from name import *

#REVERSE API
url = "https://karma-reverse-api2-0.vercel.app/reverse"

#REVERSE FUNCTION
COMMANDS = ["reverse", "pp", "grs"]
@app.on_message(filters.command(COMMANDS))
async def reverse(_, message):
    if not message.reply_to_message:
        await message.reply_text("Reply To A Photo Or A Sticker")
    elif message.reply_to_message.photo:
        msg =  await message.reply_text("Searching For The Image")
        photo_id = message.reply_to_message.photo.file_id
        get_path = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={photo_id}"
        ).json()
        file_path = get_path["result"]["file_path"]
        data = {
            "imageUrl": f"https://images.google.com/searchbyimage?safe=off&sbisrc=tg&image_url=https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        }

        response = requests.post(url, json=data)
        result = response.json()
        if response.ok:
            await msg.edit_text(
                f"[{result['data']['resultText']}]({result['data']['similarUrl']})",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await message.reply_text("Some Exception Occured")
    elif message.reply_to_message.sticker:
        msg = await message.reply_text("Searching Sticker")
        sticker_id = message.reply_to_message.sticker.id
        get_path = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={sticker_id}"
        ).json()
        file_path = get_path["result"]["file_path"]
        data = {
            "imageUrl": f"https://images.google.com/searchbyimage?safe=off&sbisrc=tg&image_url=https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        }

        response = requests.post(url, json=data)
        result = response.json()
        if response.ok:
            await msg.edit_text(
                f"[{result['data']['resultText']}]({result['data']['similarUrl']})",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await message.reply_text("Some Exception Occured")
    else:
        await message.reply_text("reply to a photo or sticker")