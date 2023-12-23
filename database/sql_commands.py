
from configuration.config import load_config, Config

config: Config = load_config()


CREATE_USER_TABLE = """

CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY,
    user_name TEXT UNIQUE NOT NULL,
    user_full_name TEXT NOT NULL
);
"""

CREATE_VOCAB_TABLE = """

CREATE TABLE IF NOT EXISTS vocab (
    user_id BIGINT NOT NULL,
    word_orig TEXT NOT NULL,
    word_trans TEXT NOT NULL,
    example TEXT NOT NULL,
    UNIQUE (user_id, word_orig)
);
"""

ADD_USER = """

INSERT INTO users(user_id, user_name,  user_full_name)
  VALUES ($1, $2, $3)
"""

ADD_WORDS = """

INSERT INTO vocab(user_id, word_orig,  word_trans, example)
  VALUES ($1, $2, $3, $4)
"""

GET_10_RAND_WORDS = """

SELECT word_orig,
       word_trans,
       example
FROM vocab
WHERE user_id = $1
ORDER BY RANDOM()
"""

GET_LEADERBOARD = """

SELECT u.user_name AS user_name,
       COUNT(v.word_orig) AS n_words
       
FROM users AS u
LEFT JOIN vocab AS v
  ON u.user_id = v.user_id

WHERE u.user_id = $1

GROUP BY u.user_id
ORDER BY n_words DESC
LIMIT 10;
"""



