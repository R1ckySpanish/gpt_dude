import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from handlers import ask_gpt

config = dotenv_values('.env')


async def main():
    bot = Bot(token=config['TG_TOKEN'])
    dp = Dispatcher()
    # add handlers routers to dispatcher
    dp.include_router(ask_gpt.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    asyncio.run(main())
