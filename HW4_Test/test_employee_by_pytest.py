from employee import Employee
import pytest
TestEmployee = Employee("John", "Smith", 1000)


def test_email():
    assert TestEmployee.email == "John.Smith@email.com"
    assert TestEmployee.email != "John@email.com"


def test_fullname():
    assert TestEmployee.fullname == "John Smith"
    assert TestEmployee.fullname != "JohnSmith"
    assert TestEmployee.fullname in "John John Smith Smith"


def test_apply_raise():
    assert TestEmployee.pay == 1000
    TestEmployee.apply_raise()
    assert TestEmployee.pay != 1050

@pytest.fixture()
def test_monthly_schedule(requests_mock):
    requests_mock.get(f"http://company.com/{TestEmployee.last}/january", text='data')
    assert TestEmployee.monthly_schedule('january') == 'data'