# -*- coding: utf-8 -*-

import logging

from src.bot import Bot
from src.config.token import TOKEN as token

# Настраиваем логгирование.
logging.basicConfig(
    level=logging.INFO,
    format="[ # ] [ HidakiNuke ] - %(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

logging.getLogger("disnake").setLevel(logging.WARNING)

bot = Bot()

# Попытка запустить бота
try:
    bot.run(token)
    if not token:
        logger.error("Токен бота не найден. Впишите его в src/config/token.py.")
        exit(1)
except Exception:
    logger.exception(
        "Ошибка при запуске бота, вероятно нету токена, впишите его в src/config/token.py."
    )
    exit(1)
