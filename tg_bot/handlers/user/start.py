from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.models import User
from infrastructure.database.requests import RequestsRepo
from settings.app_settings import AppSettings

router = Router()


@router.message(CommandStart())
async def user_start(
        message: Message,
        user: User,
        state: FSMContext,
        command: CommandObject,
        repo: RequestsRepo,
        settings: AppSettings
):
    await state.clear()
    await message.answer("Hello, I'm not finished yet!")
