import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from config import get_bot_token

async def main():
    bot = Bot(get_bot_token())
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        print("Бот включен")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")         
        