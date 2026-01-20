import pytest
from selene import browser, have, be, query, command
from selenium.webdriver import Keys
from selenium.webdriver.common import by
# from selenium.webdriver.support.wait import WebDriverWait

input_element = browser.element(".new-todo")
todo_list_elements = browser.all(".todo-list>li")


def test_complete_todo():
    browser.open("/")
    input_element.should(be.blank)
    input_element.type("a").press_enter()
    input_element.type("b").press_enter()
    input_element.type("c").press_enter()
    todo_list_elements.with_(timeout=browser.config.timeout * 1.5).should(
        have.size(3)
    )  # added custom wait

    browser.all(".todo-list>li").should((have.size(3)))
    browser.all(".todo-list>li").wait.for_((have.size(3)))
    browser.all(".todo-list>li").first.should(have.exact_text('a'))
    browser.all(".todo-list>li").second.should(have.exact_text('b'))
    browser.all(".todo-list>li")[2].should(have.exact_text('c'))

    browser.all(".todo-list>li").should(have.exact_texts('a', 'b', 'c'))

    # browser.all(".todo-list>li").second.element('.toggle').click()
    # browser.element('//*[@id="todo-list"]/li[normalize-space(.)="b"]//*[contains(concat(" ", @class, " "), " toggle "').click()
    browser.all(".todo-list>li").element_by(have.exact_text('b')).element('.toggle').click()

    browser.all(".todo-list>li").by(have.css_class('completed')).should(have.exact_texts('b'))
    browser.all(".todo-list>li").by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))


    '''
    assert len(browser.driver.find_elements(*by.css(".todo-list>li")))
    WebDriverWait(driver=browser.driver, timeout=3.0).until(lambda driver: driver.find_elements(*by.css(".todo-list>li")))
    '''

def test_todos_storage_is_not_shared_between_browsers(with_new_browser):
    browser.open("/")
    input_element.type("a").press_enter()
    input_element.type("b").press_enter()
    input_element.type("c").press_enter()
    todo_list_elements.should(have.exact_texts('a', 'b', 'c'))

    browser2 = with_new_browser('firefox')
    browser2.open("/")
    browser2.element(".new-todo").type("p").press_enter()
    browser2.all(".todo-list>li").should(have.exact_texts('p'))
    browser.all(".todo-list>li").should(have.exact_texts('a', 'b', 'c'))

    browser3 = with_new_browser('chrome')
    browser3.open("/")
    browser3.element(".new-todo").type("q").press_enter()
    browser3.all(".todo-list>li").should(have.exact_texts("q"))
    browser.all(".todo-list>li").should(have.exact_texts("a", "b", "c"))

    # def test_add_todos_and_complete_one():
    #     browser.open("/")
    #     if browser.wait_until( have.title_containing('TodoMVCC')):
    #         print('Yahoo!!! The title is correct')
    #     else:
    #         print('The title is WRONG')
    #     input_element.type("a").press_enter()
    #     input_element.type("b").press_enter()
    #     input_element.type("c").press_enter()
    #     input_element.type("d").press_enter()
    #     todo_list_elements.should(have.exact_texts('a', 'b', 'c', 'd'))

    # def test_test_complete_todo(driver, browser):
    #     driver.get("https://todomvc.com/examples/emberjs/todomvc/dist")
    #     browser.element("#new-todo").should(have.attribute("value").value(""))
    #     browser.element("#new-todo").perform(command.select_all)
    #     browser.element("#new-todo").perform(command.drag_and_drop_by_offset(3, 4))
    #     browser.element("#new-todo").perform(command.js.click)
    #     browser.element("#new-todo").perform(command.js.type("123"))
    #     browser.element("#new-todo").with_(click_by_js=True).click()
    #     initial_value = browser.element('#new-todo').get(query.attribute('value')) == ''
    #     initial_value2 = browser.element('#new-todo').locate().get_attribute('value') == ''
    #     browser.element('#new-todo').send_keys('a' + Keys.ENTER)
    #     driver.find_elements(*by.css('#new-todo')).send_keys('b' + Keys.ENTER)
    #     driver.find_elements(*by.css('#new-todo')).send_keys('c' + Keys.ENTER)
    #
    #     assert initial_value == browser.element('#new-todo').get(query.attribute('value')) == ''
    #
    """
# Other Examples
    # to make all clicks be performed via JavaScript
    # * for cases when normal clicks does not work
    browser.config.click_by_js = True
    # ... but probably you don't want to «work around» all clicks.
    # to work-around just for specific elements you can do
    browser.element('#send').perform(command.js.click)
    # or if you need to repeat click via js a more than one time on same element:
    send = browser.element('#send').with_(click_by_js=True)
    send.click()
    ...
    send.click()
    # .with_(...) - is a special command that can be called on any Selene Entity
    # where Selene Entity is either:
    # * browser,
    # * element, like browser.element(selector), browser.all(selector).first, etc.
    # * or collection, like browser.all(selector), browser.all(selector).by(condition), etc.
    # so you can call .with_ on any entity
    # to customize any browser.config.* option
    # for specific entity only, for example:
    # * browser.config.timeout = 10.0 will set global timeout to 10.0
    # but
    # * browser.all('.slow-list-item').with_(timeout=10.0)
    #   will set such big timeout only for the specialized collection of slow list items

    # to make all type command calls to be performed via JavaScript
    # ... for cases when normal clicks does not work
    # ... or to speed up test execution (by faster typing)
    browser.config.type_by_js = True

    # setting driver instance manually for extra browser customization:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    chrome_options = Options()
    chrome_options.headless = True  # ... like headless mode
    browser.config.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )
    """
