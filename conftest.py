import pytest
from playwright.sync_api import Page, Playwright


@pytest.fixture
def login_page(page: Page, base_url):
    page.goto(base_url)
    return page


@pytest.fixture
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    yield context

    context.dispose()