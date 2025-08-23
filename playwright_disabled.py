from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    pege = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    dis_button_login = page.get_by_test_id('login-page-login-button')
    expect(dis_button_login).to_be_disabled()
    


