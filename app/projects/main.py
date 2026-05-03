import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# Load environment variables
load_dotenv()

# Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables")

# Enable logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        "👋 Привет! Я эхо-бот.\n\n"
        "Отправь мне любое сообщение, и я повторю его. "
        "Используй /help для получения справки."
    )

@router.message(Command("help"))
async def help_command(message: Message) -> None:
    await message.answer(
        "📖 Справка по боту:\n\n"
        "Я просто повторяю все твои сообщения.\n"
        "Могу работать с текстом, фото, видео, стикерами и другими типами сообщений.\n\n"
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение"
    )

@router.message()
async def echo_message(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception as e:
        logger.error(f"Error while echoing message: {e}")
        await message.answer("⚠️ Не могу повторить это сообщение. Попробуйте что-то другое.")

async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())