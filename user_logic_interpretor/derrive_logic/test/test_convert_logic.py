from unittest import TestCase
from derrive_logic import convert_logic
from main import get_all_rules
import pandas as pd
from pandas.util.testing import assert_frame_equal

class Test(TestCase):
    def test_convert_logic(self):
        expected_output = pd.DataFrame({"AESA.X": ["something", "", "other"], "if_else_mark": [1.0, None, 1.0], "newcol": ["something", None, "other"]})
        main_data_document = {
            "AESA.X": ["something", '', 'other']
        }
        test_string = "If ( AESA.X != '' ) Then  AESA.X ;"
        rule = get_all_rules(test_string)

        # print(rule)

        data_frame = convert_logic(rule, main_data_document)
        assert_frame_equal(data_frame, expected_output, check_exact=True)
