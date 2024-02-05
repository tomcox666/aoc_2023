import unittest

class CalibrationTestCase(unittest.TestCase):
    def test_words_to_numbers(self):
        self.assertEqual(words_to_numbers("one"), "o1e")
        self.assertEqual(words_to_numbers("two"), "t2o")
        self.assertEqual(words_to_numbers("eightwothree"), "e8t2o3e")
        self.assertEqual(words_to_numbers("one1two"), "o1et2o")
        self.assertEqual(words_to_numbers("one2eight"), "o1e2e8t")

    def test_sum_of_first_and_last_digits(self):
        self.assertEqual(sum_of_first_and_last_digits("1abc2"), 3)
        self.assertEqual(sum_of_first_and_last_digits("pqr3stu8vwx"), 11)
        self.assertEqual(sum_of_first_and_last_digits("two1nine"), 11)
        self.assertEqual(sum_of_first_and_last_digits("e8t2o3e"), 13)

    def test_main(self):
        with open("calibration_input.txt", "r") as file:
            expected_output = (
                "Solution to problem 1: 142\n"
                "Solution to problem 2: 281\n"
            )
            # Temporarily redirect stdout to capture printed output
            # ... (code to capture output) ...
            main("calibration_input.txt")
            captured_output = ... (get captured output) ...
            self.assertEqual(captured_output, expected_output)

if __name__ == "__main__":
    unittest.main()