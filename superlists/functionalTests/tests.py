from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.startup.homepage', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url', 'about:blank')
        profile.set_preference('startup.homepage_welcome_url.additional', 'about:blank')
        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(3) 

    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_listTable(self, rowText):
        table = self.browser.find_element_by_id('listTable')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(rowText, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):

        # 彤彤聽說有一款很酷的待辦事項應用程式，她前往它的首頁
        self.browser.get(self.live_server_url)

        # 她注意到首頁的標題提到了待辦事項清單
        # assert '待辦事項' in browser.title
        self.assertIn('待辦事項', self.browser.title)
        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('待辦事項清單', headerText)

        # 網站邀請她輸入一個待辦事項
        inputBox = self.browser.find_element_by_id('newItem')
        self.assertEqual(
            inputBox.get_attribute('placeholder'),
            '輸入一個待辦事項'
        )

        # 她在文字框裡輸入了「買孔雀羽毛」(她的嗜好是做路亞假餌Fly-fishing lure)
        inputBox.send_keys('買孔雀羽毛')
        # 當她按下「送出」按鈕，頁面資訊更新，待辦事項清單裡多了一個項目：「買孔雀羽毛」
        inputBox.send_keys(Keys.ENTER)
        
        self.check_for_row_in_listTable('買孔雀羽毛')
        # 頁面另外還有一個文字框，邀請她再加入其他項目，她輸入了「利用孔雀羽毛來做一個路亞」
        # (彤彤做事很講究章法的)
        inputBox = self.browser.find_element_by_id('newItem')
        inputBox.send_keys('利用孔雀羽毛來做一個路亞')
        inputBox.send_keys(Keys.ENTER)
        # 頁面再次更新，現在待辦事項清單裡有兩個項目了
        self.check_for_row_in_listTable('買孔雀羽毛')
        self.check_for_row_in_listTable('利用孔雀羽毛來做一個路亞')
        # 彤彤懷疑這個網站是否會記住她，她看到網站有為她產生專屬的URL，URL裡
        # 有一些說明文字
        self.fail('Finish the test！')
        # 她前往該URL，待辦清單依舊存在
        
        # 她很滿意，就上床睡覺了
