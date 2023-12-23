from aiogram.fsm.state import State, StatesGroup

# FSM to 'open'/'close' a vocabulary
class FSMVocabulary(StatesGroup):
    open_vocabulary = State() 
    add_words = State()
    
