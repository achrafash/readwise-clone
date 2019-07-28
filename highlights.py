from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from book import Book

def open_amazon():
    browser = webdriver.Chrome()
    browser.get("https://read.amazon.com/notebook")
    return browser

def sign_in(browser, account_email, account_password):
    signin = ActionChains(browser)
    signin.click(browser.find_element_by_css_selector("#ap_email"))
    signin.send_keys(account_email)
    signin.click(browser.find_element_by_css_selector("#ap_password"))
    signin.send_keys(account_password)
    signin.click(browser.find_element_by_css_selector("#a-autoid-0 > span"))
    signin.perform()

def get_library():    
    account_email = # enter your email account
    account_password = # enter your password

    browser = open_amazon()
    sign_in(browser, account_email, account_password)

    book_shelve = browser.find_element_by_xpath(
        '//*[@id="kp-notebook-library"]')
    books = book_shelve.find_elements_by_xpath(
        './/div[@class="a-row kp-notebook-library-each-book a-color-base-background"]')
    books += book_shelve.find_elements_by_xpath(
        './/div[@class="a-row kp-notebook-library-each-book"]')

    library = []
    for book in books:
        title = book.find_element_by_xpath('.//h2').text.encode('utf-8')
        author = book.find_element_by_xpath('.//p').text.encode('utf-8')

        actions = ActionChains(browser)
        actions.click(book).perform()

        timeout = 5
        try:
            element_present = EC.presence_of_element_located(
                (By.ID, 'kp-notebook-highlights-count'))
            WebDriverWait(browser, timeout).until(element_present)
            highlights_count = int(browser.find_element_by_id(
                'kp-notebook-highlights-count').text)
        except TimeoutException:
            print("Timed out waiting for page to load")
        book_highlights = []
        if highlights_count > 0:
            highlights = browser.find_elements_by_id("highlight")
            for highlight in highlights:
                book_highlights.append(highlight.text.encode('utf-8'))

        library.append(Book(title, author, book_highlights))
    browser.quit()
    return library
