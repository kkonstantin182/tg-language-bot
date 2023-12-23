LEXICON: dict[str, str] = {
    "/start": "This a bot to study new words!\n"
              "To see the commnands use <b>/help</b>.",
              
    "/help": "Available commands:\n\n"
             "<b>/open_vocabulary</b>: Open vocabulary to add words.\n"
             "<b>/close_vocabulary</b>: Close vocabulary\n"
             "<b>/get_words</b>: Get 10 random words.\n"
             "<b>/get_leaderboard</b>: Get top 10 learners.\n\n"
             "How to add words?\n"
             "your_message: /open_vocabulary\n" 
             "your_message: cat gatta\n"
             "your_message: dog cane\n"
             "...\n"
             "your_message:/close_vocabulary",
    
    "/open_vocabulary": "You opened the vocabulary!\n"
                        "Now you can add a word pair in each message.\n"
                        "Don't forget to use a SPACE between the words.",

    "/close_vocabulary": "You close the vocabulary.",

    "/get_words":       "10 random words you've added:",
    
    "/get_leaderboard": "Top learners are:"

}


MENU_COMMANDS: dict[str, str] = {
    "/start": "Let's begin!",
    "/help": "Get help.",
    "/open_vocabulary": "Open vocabulary, then: <i>word_orig</i> <i>word_trans</i>.",
    "/close_vocabulary": "Close vocabulary.",
    "/get_words": "Get 10 random words from the vocabulary. ",
    "/get_leaderboard": "Get top 10 learners.",    
}