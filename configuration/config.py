from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:

    """
    Specifies database connection details.

    Parameters
    ----------
    database : str
        The name of the database to connect to.
    db_host : str
        The hostname or IP address of the database server.
    db_user : str
        The username for connecting to the database.
    db_password : str
        The password for connecting to the database.
    """

    database: str         
    db_host: str          
    db_user: str          
    db_password: str     


@dataclass
class BotConfig:

    """
    Specifies configuration parameters for the bot's API token.

    Parameters
    ----------
    token : str
        The bot's API token.
    """
    
    token: str   

@dataclass
class Config:
    bot: BotConfig
    db: DatabaseConfig
   
    
def load_config(path: str | None = None) -> Config:
    """
    Loads configuration settings from the provided environment file or the
    default environment variables.

    Parameters
    ----------
    path : str | None, optional
        (Optional) The path to an environment file to load configuration from.

    Returns
    -------
    Config
        A Config instance with loaded settings.
    """

    env = Env()
    env.read_env(path)

    config = Config(
        bot = BotConfig(
            token=env('BOT_TOKEN')
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )
    
    return config
