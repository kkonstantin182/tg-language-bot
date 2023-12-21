import asyncio
import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from typing import Union
from configuration.config import load_config, Config
from database import sql_commands

# Load configuration file
config: Config = load_config()

# A singleton to create an instance of the DataBase class only once.
class Singleton(object):

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
 

class Database(Singleton):

    def __init__(self):

        self.pool: Union[Pool, None] = None

    async def create_pool(self):
        
        self.pool = await asyncpg.create_pool(
            user=config.db.db_user,
            password=config.db.db_password,
            host=config.db.db_host,
            database=config.db.database
        )        

    async def execute(self, 
                      command: str, 
                      *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            
            if fetch:
                result = await connection.fetch(command, *args)
            elif fetchval:
                result = await connection.fetchval(command, *args)
            elif fetchrow:
                result = await connection.fetchrow(command, *args)
            elif execute:
                result = await connection.execute(command, *args)
        return result


    


        


