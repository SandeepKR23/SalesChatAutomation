import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

driver = None
logged_in = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    global logged_in

    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/drivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Firefox":
        service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/geckodriver-win32/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "Edge":
        service_obj = Service("C:/Users/rajku-sa/Desktop/Selenium/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    else:
        print("No browser selected")

    driver.get("https://web-255-92.ect-telecoms.de/preview/16a1637704e147d99f639cae9888d998/#/Login/LoginPage")

    # driver.get("")
    # driver.refresh()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver  # assigning the local driver to class driver

    yield
    driver.close()


# Screenshots
# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            path = 'C:/Users/rajku-sa/PycharmProjects/SalesChatAutomation/Screenshots/'
            file_name = path + report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
