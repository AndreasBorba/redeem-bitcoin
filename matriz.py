from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.headless = False

browser = Chromium(co)
tab = browser.latest_tab
tab.get('https://freebitco.in/')

input('Press Enter to close the browser...')
browser.quit()

