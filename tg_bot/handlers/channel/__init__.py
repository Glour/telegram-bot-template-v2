from aiogram import Router, F

from tg_bot.handlers.channel.new_channel_member import router
from settings import settings

channel_router = Router()
channel_router.chat_member.filter(F.chat.id == settings.bot.channel_link)

channel_router.include_routers(*[
    router,
])
