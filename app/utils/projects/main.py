```python
import os
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я эхо бот. Отправь мне любое сообщение, и я повторю его.")

@router.message()
async def echo(message: Message):
    await message.answer(message.text)

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```