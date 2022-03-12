# Forgery-of-identity
We have heard a lot about counterfeiting software values. For example, forging a MAC address, forging an IP, etc. We have nothing to do with these cases. Today we want to discuss the forgery of individual identity. In this post, we will get acquainted with a library in Python called Faker, which can produce fake identity information (even fake Iranian identity) for us.

First we need to install the Faker library. To install this library, we use the pip tool.

Install Faker on Linux :

    GHOSTEPROG@GHOST:~$ sudo pip3 install faker
    
Install Faker on Windows :

    C:\GHOSTEPROG> pip install faker
    
    
Now we can write our script. The work of this script that we are writing today is such that every time the script is executed, different fake identity information such as: name and surname, job, address, etc. are produced. It is interesting to know that this script produces fake Iranian identity information.

# Source script :
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
      print("Full Name : {}\n".format(fullname))
      print("Username : {}\n".format(username))
      print("Password : {}\n".format(password))
      print("Email : {}\n".format(email))
      print("Job : {}\n".format(job))
      print("address : {}\n".format(address.replace("\n" , " - ")))
      print("Favrite Color : {}\n".format(favorite_color))
      print("Web Site : {}\n".format(website))
      
# Description of source code :

We first imported the Faker class from the faker library. Then in the next line we created a faker object and put it inside the faker variable. If you notice in the input of this object we entered the string fa_IR. This field means that we want to produce Iranian identity information.

Below the GENERATE fake variables comment, we generated fake information. For example, in its first variable, we generated a fake name using the faker.name method and put it inside the fullname variable. In the same way, we defined all the required fake information.

Below the SHOW Fake Variables comment, we printed all the fake information we defined above and showed it to the user by the print command.

# Well, let me run the script for the first time. You can see the result in the image below :

![1](https://user-images.githubusercontent.com/96992358/158034113-a86811f6-4720-47a3-b65c-3c60e2c3b296.png)


As you can see, it has produced fake Iranian information.

The point is that the Faker library can generate a lot of other information such as fake IP address, fake MAC address, fake location, etc., each of which has its own function. Below is the link to the faker training resource that you can read :
            
            https://faker.readthedocs.io/en/master/
            
As you can see in the images below, different fake information is generated each time the script is executed.

![3](https://user-images.githubusercontent.com/96992358/158034167-87de7a5b-1354-41e0-aa3b-c9f7e9deaa36.png)



![4](https://user-images.githubusercontent.com/96992358/158034169-4be17b82-7619-4a83-beaa-e0944a8495e7.png)



![5](https://user-images.githubusercontent.com/96992358/158034171-95394ce3-c690-42b6-a448-2e575b2422ff.png)



![1](https://user-images.githubusercontent.com/96992358/158034173-5a87def4-c94c-4e60-a23b-f73e7635849f.png)

