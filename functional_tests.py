from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''new visitor test'''

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
        self.fail('Finish the test! ')

        # She is immediately prompted to enter a list item

        # She types in the text box "Buy peacock feathers" (her hobby is
        # knitting fishing flies)

        # When she hits enter, the page is refreshed and the page is now
        # contains "1: Buy peacock feathers" as a list item

        # The text box still prompts her to add another item.
        # She introduces "Make a Peacock Feather Fly"
        # (Edith is very methodical)

        # The page refreshes again, and now shows both elements of its list

        # Edith wonders if the site will remember her list. Then she sees that
        # the site generated a unique URL for it - about this
        # displays a short text with explanations.

        # She visits that URL - her list is still there.

        # Satisfied, she goes to bed again

if __name__ == '__main__':
    unittest.main(warnings='ignore')