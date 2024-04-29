from litestar import Litestar, get
from litestar.response import Response
from litestar_granian import GranianPlugin


@get("/")
async def index() -> Response:
    return Response({"status": "OK"})


app = Litestar(route_handlers=[index], plugins=[GranianPlugin()])

