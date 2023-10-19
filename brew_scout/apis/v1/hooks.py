from fastapi import APIRouter, Depends, status

from ...libs.dependencies.common import on_async_session_factory
from ...libs.dependencies.handlers import telegram_hook_handler_factory
from ...libs.serializers.telegram import TelegramHookIn
from ...libs.handlers.handle_telegram_hook import TelegramHookHandler


router = APIRouter(tags=["Hooks"])


@router.post("/hook/telegram", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(on_async_session_factory)])
async def handle_hook(
    hook_in: TelegramHookIn, use_case: TelegramHookHandler = Depends(telegram_hook_handler_factory)
) -> None:
    await use_case.process_hook(hook_in)
