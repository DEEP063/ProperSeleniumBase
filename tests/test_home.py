from seleniumbase import BaseCase
import time

class HomeTest(BaseCase):
    def setUp(self):
        super().setUp()
        print("Set Up called before test")

        #login
        self.open("https://practice.automationbro.com/my-account")
        self.add_text("#username","galgadot")
        self.add_text("#password","galgadot123")
        self.click("button[name=login]")
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

        #open home page
        self.open("https://practice.automationbro.com/")

    def tearDown(self):
        self.open("https://practice.automationbro.com/my-account")
        self.click(".woocommerce-MyAccount-content a[href*=logout]")
        self.assert_element_visible("button[name=login]")
        print("Tear Down called after test")
        super().tearDown()

    def test_home_page(self):

        #assert title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        #logo present
        self.assert_element(".custom-logo-link")

        #click on get started button and assert url
        self.click("#get-started")
        current_url = self.get_current_url()
        #self.assert_equal("https://practice.automationbro.com/#get-started",current_url,"uRRL is not correct ")
        self.assert_true("#get-started" in current_url)

        #get header text and assert the value
        self.assert_text("Think different. Make different.","h1")

        #scroll to bottom and assert footer text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",".tg-site-footer-section-1")


    def test_menu_links(self):
        expected_menu_links_texts = ["Home","About", "Shop", "Blog", "Contact", "My account"]

        #find menu elements
        actual_menu_links_elements = self.find_elements("//ul[@id='primary-menu']/*[starts-with(@id,'menu-item')]")

        #loop through menu links elements
        for idx,ele_text in enumerate(actual_menu_links_elements):
            print(idx,ele_text.text)
            self.assert_equal(expected_menu_links_texts[idx],ele_text.text)
