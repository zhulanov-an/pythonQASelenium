from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def base_url(base_url):
    return f"{base_url}/index.php?route=product/category&path=20"


def test_browser_title_is_desktops(base_url, browser):
    """
     проверка заголовка страницы Desktops
    """
    browser.get(f"{base_url}")
    assert base_url == browser.current_url
    assert "Desktops" in browser.title


def test_text_of_header_is_desktops(base_url, browser):
    """
    проверка наличия заголовка Desktops в странице
    """
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h2"))
    )
    assert browser.find_element_by_xpath("//*[@id='content']/h2").text == "Desktops"


def test_left_menu_present(base_url, browser):
    """
    проверка отображения меню слева
    """
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "column-left"))
    )


def test_text_description_is_present(base_url, browser):
    """
    проверка отображения описания блока
    """
    description_xpath = "//*[@id='content']/div[1]/div[2]/p"
    browser.get(f"{base_url}")
    assert WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, description_xpath))
    )
    description = browser.find_element_by_xpath(description_xpath)
    assert description.text == "Example of category description text"


def test_count_elements_in_main_block_equals_twelve(base_url, browser):
    """
    проверка количества блоков в разделе Desktops
    """
    browser.get(f"{base_url}")
    items = browser.find_elements_by_xpath("//*[@id='content']/div[4]/div")
    assert len(items) == 12

    count_of_showing_elements = browser.find_element_by_xpath("//*[@id='content']/div[5]/div[2]")
    assert count_of_showing_elements.text == "Showing 1 to 12 of 12 (1 Pages)"