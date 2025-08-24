# Откроет страницу регистрации.
# Проверит, что кнопка "Registration" находится в состоянии disabled.
# Заполнит форму регистрации.
# Убедится, что кнопка "Registration" стала доступной для взаимодействия (enabled).

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto(
        ' https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    email_input = page.get_by_test_id(
        'registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id(
        'registration-form-email-input').locator('input')
    email_input.fill('username')

    pass_input = page.get_by_test_id(
        'registration-form-password-input').locator('input')
    pass_input.fill('password')

    expect(reg_button).to_be_enabled()

    page.wait_for_timeout(5000)
