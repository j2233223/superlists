from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.startup.homepage', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url.additional', 'about:blank')
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(3) 

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # 彤彤聽說有一款很酷的待辦事項應用程式，她前往它的首頁
        self.browser.get('http://localhost:8000')

        # 她注意到首頁的標題提到了待辦事項清單
        # assert '待辦事項' in browser.title
        self.assertIn('待辦事項', self.browser.title)
        self.fail('Finish the test！') 

        # 網站邀請她輸入一個待辦事項

        ...

        # 她很滿意，就上床睡覺了


if __name__=='__main__':
    unittest.main(warnings='ignore')
