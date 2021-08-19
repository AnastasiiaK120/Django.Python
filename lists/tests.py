from django.test import TestCase

class HomePageTest(TestCase):
    '''homepage test'''

    def test_uses_home_template(self):
        '''test: home page returns correct html'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')