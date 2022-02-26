import unittest
import warnings
import pandas as pd
from main import match_area_code
from main import read_data
from main import main_get_state


class GetStateTestCase(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter("ignore", ResourceWarning)

    def test_read_data(self):
        result1 = read_data("friends.txt")
        result2 = read_data("area_code.txt")

        # self.assertTrue(result1,msg="The test has passed")
        # self.assertTrue(result2,msg="The test has passed")

        self.assertIsNotNone(result1)
        self.assertIsNotNone(result2)


    def test_match_area_code(self):

        test_area_code = ["+857-1234678","6405556666","tel: 6729998520", "(979)-6665869"]

        expected_result = ["857", "640", "672", "979"]
        result = match_area_code(test_area_code)

        self.assertEqual(result, expected_result,msg="The test has passed")

    def test_joint_result(self):
        result_state = main_get_state()["state"].values.tolist()
        result_name = main_get_state()["name"].values.tolist()
        result_phone_num = main_get_state()["phone_num"].values.tolist()
        result_area_code_result = main_get_state()["area_code"].values.tolist()

        expect_state_result = ["Utah","New Jersey","Washington","New Jersey"]
        expect_name_result = ["Ana", "Ben", "Cory", "Danny"]
        expect_phone_num_result = ["801-456-789", "609 4567890", "(206)-345-2619", "6095648765"]
        expect_area_code_result = ["801", "609", "206", "609"]

        self.assertListEqual(result_state,expect_state_result)
        self.assertListEqual(result_name, expect_name_result)
        self.assertListEqual(result_phone_num, expect_phone_num_result)
        self.assertListEqual(result_area_code_result, expect_area_code_result)




if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)