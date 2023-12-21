from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from asyncpg import UniqueViolationError
from database.database import Database
from database.sql_commands import ADD_USER
from lexicon.lexicon import LEXICON
from aiogram.enums.parse_mode import ParseMode

parse_mode=ParseMode.MARKDOWN

router = Router()
database = Database()

@router.message(CommandStart())
async def show_hello_message(message: Message) -> None:
    
    
    user_id  = message.from_user.id
    username = message.from_user.first_name
    full_name = message.from_user.full_name
    args = user_id, username, full_name
    
    try:
        await database.execute(ADD_USER, *args, execute=True)
        await message.answer(text=f"Hello, {username}!\n{LEXICON[message.text]}", parse_mode=ParseMode.HTML)
    except UniqueViolationError:
        await message.answer(text=f"Hello again, {username}!\n{LEXICON[message.text]}", parse_mode=ParseMode.HTML)
        

@router.message(Command(commands="help"))
async def show_help(message: Message) -> None:
    await message.answer(text=f"{LEXICON[message.text]}", parse_mode=ParseMode.HTML)

