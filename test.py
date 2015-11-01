import json
import unittest


class TestJsonParse(unittest.TestCase):

    def test_load(self):
        with open('templates/nginx.template') as data_file:
            data = json.load(data_file)
            self.assertEqual(data['AWSTemplateFormatVersion'], '2010-09-09')

if __name__ == '__main__':
    unittest.main()
