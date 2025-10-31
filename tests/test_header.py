from playwright.sync_api import Page, expect
from utils.config import Config
from pages.header import Header
from datetime import date, timedelta
    
def test_search(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    today = date.today()
    start_date = today + timedelta(days=5)
    end_date = today + timedelta(days=12)
    start_str = start_date.strftime("%d.%m.%Y")
    end_str = end_date.strftime("%d.%m.%Y")
    start_for_url = start_date.strftime("%d%m")
    end_for_url = end_date.strftime("%d%m")
    header.fill_origin("Москва")
    header.fill_destination("Тайбей")
    header.select_start_date(start_str)
    header.select_end_date(end_str)
    header.click_button_search()
    header.assert_url(f"{Config.BASE_URL}?params=MOW{start_for_url}TPE{end_for_url}1&with_request=true")

def test_origin_valid_city(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.fill_origin("Москва")
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Москва")

def test_destination_valid_city(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.fill_destination("Тайбей")
    expect(page.locator('[data-test-id="destination-input"]')).to_have_value("Тайбей")

def test_change_origin_destination(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.click(('[data-test-id="origin-input"]'))
    header.fill_origin("Москва")
    header.fill_destination("Фукуок")
    page.wait_for_timeout(2000)
    page.locator('text=Фукуок').filter(has_not=page.locator('[data-test-id="destination-input"]')).first.click()
    header.change_origin_destination()
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Фукуок")
    expect(page.locator('[data-test-id="destination-input"]')).to_have_value("Москва")

def test_origin_invalid_city(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.fill_origin("Ксилоран")
    expect(page.locator('[data-test-id="origin-input"]')).to_have_value("Ксилоран")
    expect(page.locator('[data-test-id="status-message"]')).to_be_visible()

def test_check_calendar_open(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.page.locator('[data-test-id="start-date-field"]').click()
    expect(page.locator('div[class*="s__bksyKKQU44OvfaUA"]')).to_be_visible()

def test_open_settings(page: Page):
    header = Header(page)
    header.open(Config.BASE_URL)
    header.wait_page()
    header.navigate_to_settings()
    header.assert_url(f"{Config.BASE_URL}my/settings")

