#import custom_packages.our_custom_module
#import custom_packages.our_custom_module as ocm
from custom_packages.our_custom_module import add_two_numbers as add_two, User
#custom_packages.our_custom_module.add_two_numbers(4, 7)
add_two(4, 7)
print(User.username)

user = User(False)
print(user.is_admin)
