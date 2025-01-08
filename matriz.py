from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.headless = False

browser = Chromium(co)
tab = browser.latest_tab
tab.set.window.max()
tab.get('https://freebitco.in/')
tab.ele('#signup_form_email').input('teste@gmail.com')
tab.ele('#signup_form_password').input('123456')
input('Press Enter to close the browser...')
browser.quit()

