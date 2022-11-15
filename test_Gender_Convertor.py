from unittest import TestCase

from Gender_Convertor import convert_gender


class Test(TestCase):
    def test_convert_gender_when_male(self):
        actual = convert_gender("M")
        expected = "Male"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_female(self):
        actual = convert_gender("F")
        expected = "Female"
        self.assertEqual(actual, expected)

    def test_convert_gender_when_transgender(self):
        actual = convert_gender("T")
        expected = "Transgender"
        self.assertEqual(actual, expected)
