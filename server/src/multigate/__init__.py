from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from litestar import Litestar, get
from litestar.config.cors import CORSConfig
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.response import Response, Template
from litestar.template import TemplateConfig
from litestar_granian import GranianPlugin
from litestar_vite import ViteConfig, VitePlugin

ROOT = Path(__file__).resolve().parent
FE_ROOT = ROOT / "../../../frontend"


@get("/")
async def index() -> Template:
    return Template("index.html.j2")


@get("/ping")
async def ping() -> Response:
    return Response({"status": "OK"})


# jinja_env = Environment(loader=FileSystemLoader(ROOT / "templates"))
# template_conf = TemplateConfig(JinjaTemplateEngine.from_environment(jinja_env))

vite_conf = ViteConfig(
    hot_reload=True,
    use_server_lifespan=True,
    dev_mode=True,
    resource_dir=FE_ROOT / "src",
    template_dir=ROOT / "templates",
    port=5300,
)

app = Litestar(
    route_handlers=[index, ping],
    plugins=[GranianPlugin(), VitePlugin(vite_conf)],
    cors_config=CORSConfig(allow_origins=["*"]),
    # template_config=template_conf,
)
