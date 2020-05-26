from unittest import TestCase
import unittest
from derrive_logic import replace_function, preprocess_replace_list, data_frame_replace_list, revert_replace_function
import pandas as pd
from pandas.util.testing import assert_frame_equal

class Test(TestCase):
    def test_replace_function(self):
        # Array
        test_case_statement = ["sample space ' ' demo", "this is another double space demo '  '"]
        test_case_statement_expected = ["sample space '<space_replace>' demo", "this is another double space demo '  '"]

        result = replace_function(preprocess_replace_list, test_case_statement)
        self.assertEqual(test_case_statement_expected, result, "error processing preprocess_replace_list")

        test_case_statement_expected = ["sample<space_replace>space<space_replace>'<space_replace>'<space_replace>demo",
                                        "this<space_replace>is<space_replace>another<space_replace>double<space_replace>"
                                        "space<space_replace>demo<space_replace>'<space_replace>'"]
        result = replace_function(data_frame_replace_list, test_case_statement)
        self.assertEqual(test_case_statement_expected, result, "error in processing data_frame_replace_list")

        # Dictionary
        test_case_statement = {"test_data": ["sample space ' ' demo"], "test_2": ["nothing change"]}
        test_case_statement_expected = {"test_data" : ["sample space '<space_replace>' demo"], "test_2" : ["nothing change"]}
        result = replace_function(preprocess_replace_list, test_case_statement,"test_data")
        self.assertEqual(test_case_statement_expected, result, "error in dictionary")

        # Dataframe
        test_case_statement = pd.DataFrame({"test": ["sample space ' ' demo", "this is another double space demo '  '"]})
        test_case_statement_expected = pd.DataFrame({"test": ["sample<space_replace>space<space_replace>'<space_replace>'<space_replace>demo",
                                        "this<space_replace>is<space_replace>another<space_replace>double<space_replace>"
                                        "space<space_replace>demo<space_replace>'<space_replace>'"]})
        result = replace_function(data_frame_replace_list, test_case_statement)
        assert_frame_equal(test_case_statement_expected, result,check_exact=True)


    def test_revert_replace_function(self):
        test_case_statement_expected = ["sample space ' ' demo"]
        test_case_statement = ["sample space '<space_replace>' demo"]
        result = revert_replace_function(preprocess_replace_list, test_case_statement)
        self.assertEqual(test_case_statement_expected,result, "error in preprocess_replace_list")

if __name__ == '__main__':
    unittest.main()