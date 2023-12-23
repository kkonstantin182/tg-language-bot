from aiogram import Router, types
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command, CommandStart, StateFilter 
from aiogram.fsm.context import FSMContext 
from aiogram.fsm.state import default_state

from database.database import Database
from database.sql_commands import ADD_WORDS, GET_10_RAND_WORDS, GET_LEADERBOARD
import pandas as pd
from lexicon.lexicon import LEXICON
from states.states import FSMVocabulary 

router = Router()
database = Database()

# Output a table in the markdown format
def _get_table(database_output, *args):
    dataframe = pd.DataFrame(database_output, columns=list(args))
    dataframe.index += 1
    table = f"```{dataframe.to_markdown()}```"
    return table

# Open FSM, switch to the state add_words
@router.message(Command(commands="open_vocabulary"), StateFilter(default_state))
async def handle_open_vocabulary(message: Message, state: FSMContext):
    await message.answer(text=f"{LEXICON[message.text]}", parse_mode=ParseMode.HTML)
    await state.set_state(FSMVocabulary.add_words)
    
# Process a word pair if it has a correct format: "<word1> <word2>"
@router.message(StateFilter(FSMVocabulary.add_words), 
                (lambda s: len(s.text.split()) == 2 and all(word.isalpha() for word in s.text.split())))
async def process_words(message: Message, state: FSMContext):
    user_id  = message.from_user.id
    word_orig, word_trans = message.text.lower().split()
    args = user_id, word_orig, word_trans

    await database.execute(ADD_WORDS, *args, execute=True)
    await message.answer(text=f"You added {word_orig} : {word_trans}")

# Exit FSM (works only when a uses's inside FSM obv.)
@router.message(Command(commands="close_vocabulary"), ~StateFilter(default_state))
async def close_vocabulary(message: Message, state: FSMContext):
    await message.answer(text=f"{LEXICON[message.text]}", parse_mode=ParseMode.HTML) 
    await state.clear()

# Process a wrongly formatted word pair 
@router.message(StateFilter(FSMVocabulary.add_words))
async def handle_wrong_words(message: Message, state: FSMContext):
    await message.answer(text="Please, make sure to use correct notation.")

# Output a vocabulary 
@router.message(Command(commands="get_words"),  StateFilter(default_state))
async def get_words(message: Message):
    user_id  = message.from_user.id
    words_result = await database.execute(GET_10_RAND_WORDS, user_id, fetch=True)

    if words_result:
        output = f"{LEXICON[message.text]}\n"
        output += _get_table(words_result, 'word_orig', 'word_trans')
    else:
        output = "No words found for the user."

    await message.answer(output, parse_mode=ParseMode.MARKDOWN)

# Output top users by number of words added
@router.message(Command(commands="get_leaderboard"),  StateFilter(default_state)) 
async def get_leaderboard(message: Message):

    user_id  = message.from_user.id
    statistics = await  database.execute(GET_LEADERBOARD, user_id, fetch=True)

    if statistics:
        output = f"{LEXICON[message.text]}\n"
        output += _get_table(statistics, 'user_name', 'n_words')
    else:
        output = "No words found for the user."

    await message.answer(output, parse_mode=ParseMode.MARKDOWN)

    