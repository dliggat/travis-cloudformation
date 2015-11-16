import glob
import json
import unittest


class TestJsonValidator(unittest.TestCase):

    TEMPLATES = 'templates/*.template'

    def setUp(self):
        """Load the template files."""
        self.templates = glob.glob(self.TEMPLATES)

    def test_load(self):
        """Test the JSON parse and the existence of particular keys."""
        for template in self.templates:
            with open(template, 'r') as data_file:

                # Parse the template => fails if invalid JSON.
                data = json.load(data_file)

                # Look for the top level keys.
                self.assertItemsEqual(data.keys(), ['AWSTemplateFormatVersion',
                                                    'Parameters',
                                                    'Description',
                                                    'Outputs',
                                                    'Resources',
                                                    'Mappings'])

                # Look for the 'AWSTemplateFormatVersion' key.
                self.assertEqual(data['AWSTemplateFormatVersion'], '2010-09-09')

                # Examine the CloudFormation 'Outputs' - expect these keys.
                self.assertItemsEqual(data['Outputs'].keys(),
                                      ['PublicIp', 'PublicDns'])


if __name__ == '__main__':
    unittest.main()
