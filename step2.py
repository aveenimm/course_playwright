# Откроет страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
# Заполнит поле "Email" значением "user.name@gmail.com"
# Заполнит поле "Username" значением "username"
# Заполнит поле "Password" значением "password"
# Нажмет на кнопку "Registration". После нажатия кнопки "Registration" произойдет редирект на страницу "Dashboard"
# Проверит, что на странице "Dashboard" отображается заголовок "Dashboard"

from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    user_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    user_name_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title).to_be_visible()
    expect(title).to_have_text('Dashboard')
    
    page.wait_for_timeout(7000)