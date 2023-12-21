import asyncio
import logging
from aiogram import Bot, Dispatcher

from configuration.config import load_config, Config
from handlers import basic_handlers, vocab_handlers
from database.database import Database
from database.sql_commands import CREATE_USER_TABLE, CREATE_VOCAB_TABLE
from keyboards.main_menu import set_main_menu

# Initialize logger
logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
           '[%(asctime)s] - %(name)s - %(message)s')
    
    logger.info('Starting bot')

    # Load configuration file
    config: Config = load_config()
    
    # Start a database
    database = Database()
    await database.create_pool()
    await database.execute(command=CREATE_USER_TABLE, execute=True)
    await database.execute(command=CREATE_VOCAB_TABLE, execute=True)

    # Bot and dispatcher initialization
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()
    
    # Set a main menu
    await set_main_menu(bot) 

    # Register routers
    dp.include_router(basic_handlers.router)
    dp.include_router(vocab_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




