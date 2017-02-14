## Activity-4-Unit-Testing

### class User
#### attributes
username - string <br>
email - class Email <br>
SS# - class Social <br>
hash - class Hash <br>
#### methods
__init__(self, username, email, SS, pass) <br>
each of these four parameters are strings which will be passed to the corresponding classes as parameters
check_password(passwrd) <br>
   uses the hashes equal operator to validate the password<br>
__str__(self) <br>
   return the username, email, and social strings in a nice readable way
   
### class Email
#### attributes
email - string
#### methods
__init__(self, email) <br>
    -verifies email is a proper email address
    -if email is a proper email address then self.email = email <br>
__str__(self)
    returns self.email
 
### class SS
#### attributes
social - string
#### methods
__init__(self, SS) <br>
    - verifies that SS is a proper social security number
    - if SS is a proper social security number then self.social = SS <br>
__str__(self) <br>
   returns self.social

### class Hash * - see below for a definition of hashing
#### exceptions
InvalidPassword
#### attributes
hash - string
#### methods
__init__(self, passwrd) <br>
    - verifies that the password is of sufficient length, if it is not then init raises InvalidPassword.
    - if the password is of sufficient length then a hash is created for the password and stored in self.hash.
    - the hash should be long, complicated, and for any two passwords that are the same, the same hash should be generated. <br>
__eq__(self, pass) <br>
    - pass is a string. __eq__ will check that pass generates the same hash as self.hash, making the passwords equal.
    
## Unit Testing
You will be responsible for creating the User class. I will provide the  Email, SS, and Hash classes. You are responsible for the
unit testing of all of these classes. You will test all of the classes in one unit test. Make sure to test the email, SS, and 
Hash classes thoroughly. How you choose to test is going to be a large part of the grade for this assignment. I will guarantee 
that the first iteration of the classes that I send you will NOT work properly, your unit testing should show that.

## Submission
When you are ready, create a repository on github for this assignment with your code for the User class. Send me a link. I will fork the assignment, add my code, and
create a pull request. Then you can get my code, test it, and respond to my pull request with comments. After communicating by 
github for a while, we should have a full working version of the program.
       
* Hashing
One way of securely storing a password is to not actually store the password, but a one way representation of the password called a 
hash. The hash is generally computed from the password using a rather complicated mathematical formula. The formula is designed so
that
1. The resulting hash is long, ie not easily guessed.
2. Is not reversible. So if you know the hash there is no way to get back to the password. One side effect of this is that it is
possible for two different passwords to generate the same hash, but the odds are very slim. But, it is possible someone could use
an improper password to login to an account protected by a hash.
3. If someone discovers the hash it does them no good.

Let's look at an example. Suppose I have a password of Bob. When the password is set to the hash object it generates a hash of 
D#css!94a82dkgE2cMmv#5&. We save the users hash for the password, not the password.

Now suppose someone tries to login. If they type in Robert for the password the system then generates a hash for Robert based on 
the formula the system is using and compares it to the stored hash. Say the hash for Robert is 44Ft1Cbb%&mEdk9xY3. Then 44Ft1Cbb%&mEdk9xY3
is not equal to the stored hash D#css!94a82dkgE2cMmv#5& from above, and the login fails (as it should). Now suppose the user types
in the correct password, Bob. The hash for Bob is computed, D#css!94a82dkgE2cMmv#5&, compared with the stored hash, D#css!94a82dkgE2cMmv#5&
. Those are equal so the password is confirmed.

So why use hashing? Well suppose someone hacks the system and tries to get Bob's password. What they are going to get is the stored
hash D#css!94a82dkgE2cMmv#5&. If they try to use that as the password for Bob, the system is going to compute as hash of
D#css!94a82dkgE2cMmv#5&, which is going to be something completely different like ThIsIsNOTtheCoRrEcTHasH. It then compares this 
hash of hash ThIsIsNOTtheCoRrEcTHasH with the original hash D#css!94a82dkgE2cMmv#5& and says they are not the same. So, hashing is 
a safe way to store passwords. There is much more to hashing than what I have explained here, but there are the basics.




