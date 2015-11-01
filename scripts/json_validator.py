import glob
import json
import unittest


class TestJsonValidator(unittest.TestCase):

    TEMPLATES = 'templates/*.template'

    def test_load(self):
        templates = glob.glob(self.TEMPLATES)
        for template in templates:
            with open(template, 'r') as data_file:
                data = json.load(data_file)
                self.assertEqual(data['AWSTemplateFormatVersion'], '2010-09-09')
                self.assertItemsEqual(data['Outputs'].keys(), ['PublicIp', 'PublicDns'])

if __name__ == '__main__':
    unittest.main()
