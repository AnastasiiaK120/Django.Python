from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        '''installing'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''dismantling'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: you can start the list and get it later'''
        # Edith heard about a cool new to-do list online app.
        # She decides to rate its homepage .
        self.browser.get('http://localhost:8000')

        # She sees that the title and heading of the page are talking about
        # lists urgent matters
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is immediately prompted to enter a list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types in the text box "Buy peacock feathers" (her hobby is
        # knitting fishing flies)
        inputbox.send_keys('Buy peacock feathers')

        # When she press enter, the page is refreshed and the page is now
        # contains "1: Buy peacock feathers" as a list item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New list item did not appear in the table"
        )

        # The text box still prompts her to add another item.
        # She introduces "Make a Peacock Feather Fly"
        # (Edith is very methodical)

        self.fail('Finish test!')

        # The page refreshes again, and now shows both elements of its list

        # Edith wonders if the site will remember her list. Then she sees that
        # the site generated a unique URL for it - about this
        # displays a short text with explanations.

        # She visits that URL - her list is still there.

        # Satisfied, she goes to bed again

if __name__ == '__main__':
    unittest.main(warnings='ignore')