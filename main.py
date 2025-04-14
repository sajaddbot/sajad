
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID", "0"))

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message) -> None:
    if message.chat.id == TARGET_CHAT_ID or message.chat.type == "private":
        if str(message.from_user.id) == str(ADMIN_ID):
            await message.reply("✅ البوت يعمل")
        else:
            await message.reply("❌ ليس لديك صلاحية التحكم بهذا البوت.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
