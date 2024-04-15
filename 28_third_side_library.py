# https://pypi.org/

from faker import Faker
import requests

fake = Faker()

print(fake.name())
print(fake.address())
