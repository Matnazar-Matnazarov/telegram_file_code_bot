from aiogram import Bot, types, Dispatcher, executor
import requests
from config import API_KEY,BOT_TOKEN,ADMIN_ID
import logging
logging.basicConfig(level=logging.INFO)

bot=Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
        await message.reply(f"Xush kelibsiz {message.from_user.full_name}\nBu bot sizga video,photo,document larni fayl kodini olib beradi !")
        await bot.send_message(ADMIN_ID,f"{message.from_user.full_name or message.from_user.username} \nid={message.from_user.id}")
@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    try:
        await bot.send_photo(chat_id=message.chat.id, photo=message.text, caption=f"Mana  rasm")
    except:
        try:
            await bot.send_video(chat_id=message.chat.id,video=message.text,caption=f"Mana  video")
        except :
            try:
                await bot.send_document(chat_id=message.chat.id,document=message.text,caption=f"Mana  document")
            except :
                await message.reply("Siz faqat video photo document larni kodini tashlay olasiz va\n xato qilmasligingiz kerak")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo(message: types.Message):
    photo=message.photo[-1]
    file_id = photo.file_id
    await bot.send_photo(chat_id=message.chat.id, photo=file_id, caption=f"{message.caption or '!'}\nMana  rasm kodi :```\n{file_id}```",parse_mode=types.ParseMode.MARKDOWN)
    await bot.send_photo(chat_id=ADMIN_ID,photo=file_id,caption=f"Full name : {message.from_user.full_name} username or chat id : {message.from_user.username or message.chat.id}\n {message.caption  or 1}\nMana  rasm kodi :```\n{file_id}```",parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(content_types=types.ContentType.VIDEO)
async def video(message: types.Message):
    video=message.video
    file_id=video.file_id
    await bot.send_video(chat_id=message.chat.id,video=file_id, caption=f"{message.caption or video.file_name or '!'}\nMana  video kodi :```\n{file_id}```",parse_mode=types.ParseMode.MARKDOWN)
    await bot.send_video(chat_id=ADMIN_ID,video=file_id,caption=f"Full name : {message.from_user.full_name} username or chat id : {message.from_user.username or message.chat.id}\n {message.caption or video.file_name or '!'}\nMana  video kodi :```\n{file_id}```",parse_mode=types.ParseMode.MARKDOWN)

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def document(message: types.Message):
    document=message.document
    file_id=document.file_id
    file_name=document.file_name
    await bot.send_document(chat_id=message.chat.id,document=file_id, caption=f"{message.caption  or file_name or '!'}\nMana  document kodi :\n{file_id}")
    await bot.send_document(chat_id=ADMIN_ID,document=file_id,caption=f"Full name : {message.from_user.full_name} username or chat id : {message.from_user.username or message.chat.id}\n {message.caption or file_name or '!'}\nMana  video kodi :\n{file_id}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)