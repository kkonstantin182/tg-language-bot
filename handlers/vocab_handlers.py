from aiogram import Router, types
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command, CommandStart
from database.database import Database
from database.sql_commands import ADD_WORDS, GET_10_RAND_WORDS, GET_LEADERBOARD
import pandas as pd
from lexicon.lexicon import LEXICON

router = Router()
database = Database()


def _get_table(database_output, *args):

    dataframe = pd.DataFrame(database_output, columns=list(args))
    dataframe.index += 1
    table = f"```{dataframe.to_markdown()}```"
    return table


@router.message(Command(commands="add_words"))
async def add_words(message: Message) -> None:
    
    user_id  = message.from_user.id

    try:

        _, word_orig, word_trans = message.text.lower().split()
        args = user_id, word_orig, word_trans

        await database.execute(ADD_WORDS, *args, execute=True)
        await message.answer(text=f"You added {word_orig}: {word_trans}")

    except ValueError:
        await message.answer(text=f"Example: /add_words hello ciao")


@router.message(Command(commands="get_words"))
async def get_words(message: Message) -> None:

    user_id  = message.from_user.id
    words_result = await database.execute(GET_10_RAND_WORDS, user_id, fetch=True)

    if words_result:
        output = _get_table(words_result, 'word_orig', 'word_trans')
    else:
        output = "No words found for the user."

    await message.reply(output, parse_mode=ParseMode.MARKDOWN)

@router.message(Command(commands="get_leaderboard"))
async def get_leaderboard(message: Message) -> None:

    user_id  = message.from_user.id
    statistics = await  database.execute(GET_LEADERBOARD, user_id, fetch=True)

    if statistics:
        output = _get_table(statistics, 'user_name', 'n_words')
    else:
        output = "No words found for the user."

    await message.reply(output, parse_mode=ParseMode.MARKDOWN)

    