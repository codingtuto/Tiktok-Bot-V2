import requests
import traceback
import asyncio
from pyrogram import *
from pyrogram.types import *

api_id = 9
api_hash = ""
token = ""

tiktok = Client("tiktoker", api_id, api_hash, bot_token=token)


@tiktok.on_message(filters.private & filters.command("start"))
async def starts(_, message):
    await tiktok.send_message(message.chat.id, f"""
Salut, {message.from_user.mention}!
Ce bot vous permet de télécharger des vidéos de TikTok avec une vitesse extrême et sans filigrane.

Tout ce que vous avez à faire est de soumettre un lien TikTok ici.

Il est également possible d'ajouter ce bot en groupe, afin de télécharger automatiquement les TikToks envoyés.
 Rien de plus simple.


🐱 Par @A_liou
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➕ Ajouter moi dans une groupe", url=f"https://t.me/{(await tiktok.get_me()).username}?startgroup=start")]]))


@tiktok.on_message(filters.new_chat_members)
async def botaggiunto(_, message):
    for user in message.new_chat_members:
        if user.is_self:
            await tiktok.send_message(message.chat.id, f"message du bot ajouté")

        

@tiktok.on_message(filters.incoming)
async def tikdownload(_, message):
    try:
        r = requests.get(f"https://u9963.thedc.ru/Sardorxon/Api/tiktok.php?url={message.text}").text
        await tiktok.send_message(message.chat.id, "[⬇️] Téléchargement en cours...")
        await asyncio.sleep(1.0)
        await tiktok.send_video(message.chat.id, r, caption=f"🐱 @{(await tiktok.get_me()).username}")
    except:
        traceback.print_exc()
        await tiktok.send_message(message.chat.id, f"lien invalide!")


tiktok.run()

