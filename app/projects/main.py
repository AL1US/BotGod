import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()
dp.include_router(router)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я эхо бот. Напиши мне что-нибудь, и я повторю.")

@router.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
