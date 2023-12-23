# Telegram language bot

This is a simple Telegram bot designed to help users learn new English words. It is written using Aiogram 3 and utilizes Postgres as a database. In addition, for every saved word, it provides an example of usage, leveraging the WordsAPI.

## Getting Started

The project was written in Python 3.10. To run it, you need to install [PostgreSQL](https://www.postgresql.org/). Alternatively, you can use [Docker](https://www.docker.com/) to lift a container with the database.

Additionally, you need to obtain the tokens:
- [Telegram](https://core.telegram.org/bots/tutorial) 
- [WordsAPI](https://www.wordsapi.com/)

### Installing

1. Clone this reprository.
```
git clone https://github.com/kkonstantin182/tg-language-bot.git
```

2. Create <i>.env</i> file and specify the tokens and credentials for the database (see the <i>.env.example</i>):
- BOT_TOKEN: Telegram bot authentication token.
- WORDS_API_TOKEN: API key for the WordsAPI service.
- DB_HOST: Hostname or IP address of the PostgreSQL server.
- DB_USER: Username for PostgreSQL database authentication
- DB_PASSWORD: Password for PostgreSQL database authentication.
- DATABASE: Name of the PostgreSQL database.

3. If you are using Docker, lift the container with the database in the project folder (or start the Postgres):

```
docker compose up
```

4. Create a virtual environment and install dependencies from <i>requirements.txt</i>.

5. Run the bot:

```
python app.py
```
## Built With

* [Aiogram 3](https://docs.aiogram.dev/en/latest/) - Asynchronous framework for Telegram Bot API.
* [Asyncpg](https://magicstack.github.io/asyncpg/current/) - Database interface library for PostgreSQL for use with Python’s asyncio framework.

## Status

More features may be added :)

