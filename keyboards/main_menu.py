from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import MENU_COMMANDS

# Configure the "Menu" button

async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(
        command=command,
        description=description
    ) for command, description in MENU_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)