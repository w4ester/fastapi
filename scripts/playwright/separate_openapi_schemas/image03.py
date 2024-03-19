import subprocess

from playwright.sync_api import Playwright, sync_playwright
from security import safe_command


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 960, "height": 1080})
    page = context.new_page()
    page.goto("http://localhost:8000/docs")
    page.get_by_text("GET/items/Read Items").click()
    page.get_by_role("tab", name="Schema").click()
    page.get_by_label("Schema").get_by_role("button", name="Expand all").click()
    page.screenshot(
        path="docs/en/docs/img/tutorial/separate-openapi-schemas/image03.png"
    )

    # ---------------------
    context.close()
    browser.close()


process = safe_command.run(subprocess.Popen, ["uvicorn", "docs_src.separate_openapi_schemas.tutorial001:app"]
)
try:
    with sync_playwright() as playwright:
        run(playwright)
finally:
    process.terminate()
