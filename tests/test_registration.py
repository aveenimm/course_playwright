import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
@pytest.mark.registration
def test_successfull_reg():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('username')

        pass_input = page.get_by_test_id('registration-form-password-input').locator('input')
        pass_input.fill('password')

        reg_button = page.get_by_test_id('registration-page-registration-button')
        reg_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
