from .middleware import CheckUserMiddleware
from .start import router as start_router
from .assistant import router as assistant_router
from .search_videos import router as search_videos_router


def register_handlers(dp):
    for router in (assistant_router, search_videos_router, start_router):
        dp.include_router(router)

    dp.message.middleware(CheckUserMiddleware())


__all__ = (register_handlers,)
