from aiogram import Router

from tg_bot.filters.admin import AdminFilter
from tg_bot.handlers.admin import admin

admin_router = Router()
admin_router.message.filter(AdminFilter())

admin_router.include_routers(*[
    admin.router,
])
