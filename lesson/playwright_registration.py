# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
# Заполнить все поля и нажать кнопку "Registration"
# После чего в local storage будут сохранены все нужные данные, необходимые для авторизации
# Далее с помощью Playwright мы сохраним состояние браузера, чтобы в будущем использовать его. Это позволит сильно оптимизировать автотесты и не регистрироваться в приложении в каждом автотесте
from playwright.sync_api import sync_playwright

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
