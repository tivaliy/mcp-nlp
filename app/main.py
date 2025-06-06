from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from app.core.middlewares import ApiKeyAuthMiddleware
from app.core.settings import get_app_settings
from app.resources.version import VersionResource
from app.tools.text_distance import textdistance_mcp


def create_application() -> tuple[FastMCP, Starlette]:
    """Create a FastMCP app"""
    settings = get_app_settings()

    # Configure logging
    settings.configure_logging()

    # Configure middlewares
    custom_middlewares = [
        Middleware(
            CORSMiddleware,
            allow_origins=settings.allowed_hosts,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    if settings.api_key_enabled:
        custom_middlewares.append(
            Middleware(
                ApiKeyAuthMiddleware,
                api_key=settings.api_key,
                api_key_name=settings.api_key_name,
            )
        )

    mcp_app: FastMCP = FastMCP(**settings.fastmcp_kwargs)
    # Extract the Starlette application for use with ASGI servers, like uvicorn
    starlette_app = mcp_app.http_app(
        middleware=custom_middlewares,
        transport=settings.transport,
    )

    # Tools
    mcp_app.mount("textdistance", textdistance_mcp)
    # Resources
    mcp_app.add_resource(VersionResource(settings.app_version))

    return mcp_app, starlette_app


# Create the application instance
app, http_app = create_application()
