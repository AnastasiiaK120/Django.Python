from django.test import TestCase

class SmokeTest(TestCase):
    '''toxicity test'''

    def test_bad_maths(self):
        '''test: incorrect mathematical calculations'''
        self.assertEqual(1 + 1, 3)