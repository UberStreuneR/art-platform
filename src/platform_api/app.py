from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_swagger_ui_html
)


def create_app() -> FastAPI:

    app = FastAPI(docs_url=None)

    @app.get("/health")
    def health_check():
        return "Health Check"

    # specifying different CDN
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui-bundle.js",
            swagger_css_url="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.14.0/swagger-ui.css",
        )

    from platform_api.routers.auth import auth
    app.include_router(auth)

    return app
