import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.employee1 = Employee("John", "Smith", 1000)


    def test_email(self):
        self.assertEqual(self.employee1.email, "John.Smith@email.com")


    def test_fullname(self):
        self.assertEqual(self.employee1.fullname, "John Smith")


    def test_apply_raise(self):
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.pay, 1000)


    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get_response):
        mock_get_response.return_value.ok = True
        self.assertEqual(self.employee1.monthly_schedule("March"), mock_get_response().text)



if __name__ == "__main__":
    unittest.main()