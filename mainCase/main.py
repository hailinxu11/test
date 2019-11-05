import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def setup_class1(request):
    browser_type = int(myConfig.getDriver())
    if browser_type == 1:
        try:
            cls.driver = webdriver.Chrome()
            # chrome_opt = webdriver.ChromeOptions()
            # chrome_opt.add_argument('--headless')
            # cls.driver = webdriver.Chrome(chrome_options=chrome_opt)
        except Exception as e:
            MyLog.logger().error('浏览器chrome driver有误 %s', e)
    elif browser_type == 2:
        try:
            firefox_opt = webdriver.ChromeOptions()
            firefox_opt.add_argument('--headless')
            cls.driver = webdriver.Chrome(firefox_options=firefox_opt)
        except Exception as e:
            MyLog.logger().error('浏览器Firefox driver有误 %s', e)
    elif browser_type == 3:
        try:
            ie_opt = webdriver.ChromeOptions()
            ie_opt.add_argument('--headless')
            cls.driver = webdriver.Chrome(ie_options=ie_opt)
        except Exception as e:
            MyLog.logger().error('浏览器IE driver有误 %s', e)
    yield driver

    driver.close()



class Test_one(object):
    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


    def test_1(self, setup_class1):

        print('====================')



    def test_2(self, setup_class1):
        print('++++++++++++++++++++++')
