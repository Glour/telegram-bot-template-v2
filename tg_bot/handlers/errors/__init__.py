from aiogram import Router

from tg_bot.handlers.errors import bot_api_errors

error_router = Router()
error_router.include_router(bot_api_errors.router)
