import unittest
from flask_testing import TestCase
from app import app

class KalkulatorBMITest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kalkulator BMI', response.data)
        self.assertEqual()

if __name__ == '__main__':
    unittest.main()