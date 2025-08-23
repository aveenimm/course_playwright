# Необходимо написать скрипт, который откроет страницу
# Заполнит поле "Email" значением user.name@gmail.com
# Заполнит поле "Password" значением password
# Нажмет на кнопку "Login"
# Проверит наличие алерта с текстом "Wrong email or password"


from playwright.sync_api import sync_playwright, expect
with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.locator(
        '//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill('user.name@gmail.com')

    password_input = page.get_by_test_id(
        'login-form-password-input').locator('input')
    password_input.fill('password')

    login_button = page.get_by_test_id("login-page-login-button")
    login_button.click()

    wrong_email_or_password_allert = page.locator(
        '//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_allert).to_be_visible()
    expect(wrong_email_or_password_allert).to_have_text(
        'Wrong email or password')

    page.wait_for_timeout(5000)
