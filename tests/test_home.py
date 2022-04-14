from page_objects.home_page import HomePage

class HomeTest(HomePage):
    def setUp(self):
        super().setUp()
        print("Set Up called before test")

        #login
        HomePage.login(self)

        #open home page
        HomePage.open_page(self)

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
        self.assert_element(HomePage.logo_icon)

        #click on get started button and assert url
        self.click(HomePage.get_started_btn)
        current_url = self.get_current_url()
        #self.assert_equal("https://practice.automationbro.com/#get-started",current_url,"uRRL is not correct ")
        self.assert_true("#get-started" in current_url)

        #get header text and assert the value
        self.assert_text("Think different. Make different.",HomePage.heading_text)

        #scroll to bottom and assert footer text
        self.scroll_to_bottom()
        self.assert_text("Copyright © 2020 Automation Bro",HomePage.copyright_text)


    def test_menu_links(self):
        expected_menu_links_texts = ["Home","About", "Shop", "Blog", "Contact", "My account"]

        #find menu elements
        actual_menu_links_elements = self.find_elements(HomePage.menu_links)

        #loop through menu links elements
        for idx,ele_text in enumerate(actual_menu_links_elements):
            print(idx,ele_text.text)
            self.assert_equal(expected_menu_links_texts[idx],ele_text.text)
