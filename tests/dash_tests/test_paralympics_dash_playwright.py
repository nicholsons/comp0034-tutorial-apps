""" Minimal example of a test using Python playwright instead of Selenium webdriver

Install the playwright and pytest-playwright packages with pip:
pip install pytest-playwright playwright

"""
import pytest
from dash.testing.application_runners import import_app
from playwright.sync_api import expect, sync_playwright


@pytest.fixture(autouse=True)
def start_app(dash_duo):
    """ Pytest fixture to start the app in a threaded server.
    This is a function-scoped fixture.
    Automatically used by all tests in this module.
    """
    app_file_loc = "dash_single.para_single"
    app = import_app(app_file_loc)
    yield dash_duo.start_server(app)


@pytest.fixture()
def app_url(start_app, dash_duo):
    """ Pytest fixture for the URL of the running Dash app. """
    yield dash_duo.server_url


def test_h1_text_equals(app_url):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading with an id of 'title' should have the text "Paralympics Dashboard"
    """

    with sync_playwright() as p:
        # Use the Chrome browser, see https://playwright.dev/python/docs/browsers#google-chrome--microsoft-edge
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page()

        # Go to the home page of the app
        page.goto(app_url)

        # Check that the h1 heading which has the id="title" has the expected text
        expected_text = "Paralympics Dashboard"
        title = page.locator("#title")
        expect(title).to_have_text(expected_text)

        browser.close()
