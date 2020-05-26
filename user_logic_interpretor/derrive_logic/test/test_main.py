from unittest import TestCase
from main import get_all_rules

class Test(TestCase):
    def test_get_all_rules(self):
        test_string = "If ( AESA.X != '' ) Then  AESA.X ;"
        expected_output = [{'if': {'condition': ['AESA.X', '!=', "''"], 'action': ["main_data_document_df['AESA.X']"]}}]
                          # [{'if': {'condition': ['AESA.X', '!=', "''"], 'action': [["main_data_document_df['AESA.X']"]]}}]
        result = get_all_rules(test_string)
        self.assertEqual(expected_output, result, "error in output format")

        test_string = "ElseIf ( AESA.X == '' ) Then SDIS.Y ;"
        expected_output  = [{'elseif': {'condition': ['AESA.X', '==', "''"], 'action': ["main_data_document_df['SDIS.Y']"]}}]
        result =get_all_rules(test_string)
        self.assertEqual(expected_output, result, "else if has issue in rule generation")
