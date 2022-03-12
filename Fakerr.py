from faker import Faker
faker = Faker("fa_IR")

#### GENERATE Fake Variables ###########
fullname = faker.name() # Random Full Name
username = faker.user_name() # Random Username
password = faker.password() # Random Password
email = faker.email() # random Email
job = faker.job() # Random JOB
address = faker.address() # Random Address
favorite_color = faker.color_name() # Random Favorite Color
website = faker.domain_name() # Random Website Domain

###### SHOW Fake Variables #########
print("Full Name :~$ {}\n".format(fullname))
print("Username :~$ {}\n".format(username))
print("Password :~$ {}\n".format(password))
print("Email :~$ {}\n".format(email))
print("Job :~$ {}\n".format(job))
print("address :~$ {}\n".format(address.replace("\n" , " - ")))
print("Favrite Color :~$ {}\n".format(favorite_color))
print("Web Site :~$ {}\n".format(website))