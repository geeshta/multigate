from pathlib import Path

from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.response import Response
from litestar_granian import GranianPlugin
from litestar.static_files import create_static_files_router

ROOT = Path(__file__).resolve().parent
FE_ROOT = ROOT / "../../../frontend"


@get("/ping")
async def ping() -> Response:
    return Response({"status": "OK"})


static_router = create_static_files_router(
    "static", directories=[FE_ROOT / "dist" / "static"]
)

html_router = create_static_files_router(
    "/", directories=[FE_ROOT / "dist"], html_mode=True
)

app = Litestar(
    route_handlers=[ping, html_router, static_router],
    plugins=[GranianPlugin()],
    cors_config=CORSConfig(allow_origins=["*"]),
)
