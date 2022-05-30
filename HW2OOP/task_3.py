'''3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
'''
class DictMixin:
    def to_dict(self):
        return list(self.__dict__.values())


class Profile(DictMixin):
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

p = Profile('Andrew','Kobzar', '+380994567890', 'Kyiv', 'akobzar@ukr.net', '02.12.2001', 21, 'male')
print(p.to_dict())