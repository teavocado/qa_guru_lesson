import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def config_browser():
    browser.config.window_height = 600
    browser.config.window_width = 400


def test_find_selen_from_google(config_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('sdihlshgsldkgh').press_enter()
    browser.element('[id="res"]').should(have.text('По запросу sdihlshgsldkgh ничего не найдено.'))
