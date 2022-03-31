import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

TOKEN = "1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM"
id =  972299703

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)
async def send_to_admin(dp):
    await bot.send_message(chat_id=id, text="Salem, Kezdeseyik")

@dp.message_handler()
async def echo(message:Message):
    text = f"Salem, senin basyn istei ma: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)

if __name__ == "__name__":
    executor.start_polling(dp, on_startup=send_to_admin)


