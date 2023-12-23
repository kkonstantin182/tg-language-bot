"""
For more information, please visit: https://www.wordsapi.com/
"""


import aiohttp
from configuration.config import load_config

config = load_config()

async def get_word_example(word):
    url = f'https://wordsapiv1.p.rapidapi.com/words/{word}/examples'
    headers = {
        'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com',
        'X-RapidAPI-Key': config.word_api.token,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                sentences = data.get('examples', [])
                return sentences[0] if sentences else 'None'
            else:
                return 'None'

