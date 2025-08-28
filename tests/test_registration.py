# import pytest
# from playwright.sync_api import sync_playwright, Page, expect

# @pytest.mark.regression
# @pytest.mark.registration
# def test_successfull_reg(chromium_page: Page):

#     chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

#     email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('user.name@gmail.com')

#     username_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('username')

#     pass_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
#     pass_input.fill('password')

#     reg_button = chromium_page.get_by_test_id('registration-page-registration-button')
#     reg_button.click()

#     dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
#     expect(dashboard_title).to_be_visible()

import pytest

from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()

    dashboard_page.check_visible_dashboard_title()