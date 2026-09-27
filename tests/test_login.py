from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page, base_url):
    page.goto(base_url)
    return page

def test_login_exitoso(login_page: Page, base_url):
    login = LoginPage(login_page)

    login.login("standard_user", "secret_sauce")

    expect(login_page).to_have_url(base_url + "inventory.html")
    expect(login_page.get_by_text("Products")).to_be_visible()


@pytest.mark.parametrize(
    "username,password",
    [("standard_user", "incorrect_password"), ("usuario_inexistente", "secret_sauce"),])
def test_login_credenciales_invalidas(login_page: Page, username, password, base_url):

    login = LoginPage(login_page)

    login.login(username, password)

    expect(login_page).to_have_url(base_url)
    expect(login.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")


def test_login_username_obligatorio(login_page: Page, base_url):

    login = LoginPage(login_page)

    login.login("", "incorrect_password")

    expect(login_page).to_have_url(base_url)
    expect(login.error_message).to_have_text("Epic sadface: Username is required"
)