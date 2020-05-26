from unittest import TestCase
import unittest
from derrive_logic import replace_function, preprocess_replace_list, data_frame_replace_list

class Test(TestCase):
    def test_replace_function(self):
        test_case_statement  = ["sample space ' ' demo", "this is another double space demo '  '"]
        test_case_statement_result = ["sample space '<space_replace>' demo", "this is another double space demo '  '"]

        result = replace_function(preprocess_replace_list, test_case_statement)
        self.assertEqual(test_case_statement_result, result, "error processing preprocess_replace_list")

        test_case_statement_expected = ["sample<space_replace>space<space_replace>'<space_replace>'<space_replace>demo",
                                        "this<space_replace>is<space_replace>another<space_replace>double<space_replace>"
                                        "space<space_replace>demo<space_replace>'<space_replace>'"]
        result = replace_function(data_frame_replace_list, test_case_statement)
        self.assertEqual(test_case_statement_expected, result, "error in processing data_frame_replace_list")

if __name__ == '__main__':
    unittest.main()