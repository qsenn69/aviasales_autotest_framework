from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class Header(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.base_locator = 'div[class*="s__n3XNjPDywfBvSKwc"]'

    def navigate_to_home(self):
        self.page.click('[data-test-id="logo"]')

    def navigate_to_settings(self):
        self.page.click('[data-test-id="profile-button"]')
        self.page.get_by_text("Настройки").click()
    
    def navigate_to_magazine(self):
        self.page.click('[data-test-id="header-blog-button"]')
    
    def navigate_to_support(self):
        self.page.click('[data-test-id="header-support-button"]')
    
    def navigate_to_hotels(self):
        self.page.get_by_role('link', name="Отели").click()

    def navigate_to_guides(self):
        self.page.get_by_role('link', name="Короче").click()

    def navigate_to_favorites(self):
        self.page.get_by_role('link', name="Избранное").click

    def navigate_to_b2b(self):
        self.page.get_by_role('link', name="Для бизнеса").click()

    def set_text_field_value_by_id(self, data_test_id: str, value: str):
        origin = self.page.locator(self.base_locator+'//[data-test-id="'+data_test_id+'"]")+""]')
        origin.click()
        origin.fill(value)

    def set_text_field_value_by_class(self, class_name: str, value: str):
        origin = self.page.locator('[contains(@class, "'+class_name+'")]')
        origin.click()
        origin.fill(value)

    def change_origin_destination(self):   
        button = self.page.locator(f'{self.base_locator} button[data-test-id="round-button"]')
        button.click()
    
    # def fill_origin(self, city: str):
    #     selector = '[data-test-id="origin-input"]'
    #     self.wait_for_element(selector)
    #     origin = self.page.locator(selector)
    #     origin.click()
    #     origin.fill(city)

    def fill_origin(self, city: str):
        self.page.locator('[data-test-id="origin-input"]').click()
        self.page.locator('[data-test-id="origin-input"]').fill(city)

    # def fill_destination(self, city: str):
    #     selector = '[data-test-id="destination-input"]'
    #     self.wait_for_element(selector)
    #     destination = self.page.locator(selector)
    #     destination.click()
    #     destination.fill(city)

    def fill_destination(self, city: str):
        self.page.locator('[data-test-id="destination-input"]').click()
        self.page.locator('[data-test-id="destination-input"]').fill(city)

    def select_start_date(self, start_date: str):
        self.page.locator('[data-test-id="start-date-field"]').click()
        self.page.locator(f'[data-test-id="date-{start_date}"]').click()

    def select_end_date(self, end_date: str):
        self.page.locator('[data-test-id="end-date-field"]').click()
        self.page.locator(f'[data-test-id="date-{end_date}"]').click()

    def click_button_search(self):
        self.page.locator('[data-test-id="form-submit"]').click()