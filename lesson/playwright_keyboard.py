#введём текст user@gmail.com в поле Email на странице авторизации https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login, а затем выделим весь текст в поле Email с помощью комбинации клавиш Ctrl + A 

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # По символу имитируем нажатия клавиш для ввода текста
    for character in 'user@gmail.com':
        # Добавляем задержку 300 мс для имитации реального ввода
        page.keyboard.type(character, delay=300)
    
    page.keyboard.press("ControlOrMeta+A")
    
    # Ждём 5 секунд для наглядности результата
    page.wait_for_timeout(5000)


        