<h1 align="center"> MAYANA </h1>

---
**Mayana**  is a super useful ```package``` and ```cli-application``` that generates random values for fake data entry such as ```names```, ```dates of birth```, ```IP 
addresses```, ```passwords```, ```states```, ```countries```, ```phone numbers```, ```pin code``` and more. This tool is 
useful for developers and testers who need to populate databases or forms with realistic-looking data.

# Instantiation

[//]: # (```sh)

[//]: # (   pip install mayana)

[//]: # 

> available soon...

# Use as Package
you can use ```mayana``` as a ```package``` to generate random values for your ```models```, ```programs``` and 
```applications``` for example: 

```python

    # To generate a random value first you need to import the corresponding classes from the mayana package.
    
    from mayana import Name
    from mayana import Phone
    from mayana import Ip
    from mayana import Country
    from mayana import DOB
    from mayana import Password
```
after importing the class you can create a new instance of the class and use it to generate a random values.

# Examples

```python
    from mayana import Name

    # If you want to generate a random name for a 
    # specific country you can pass the name of the country and the number of names.
    
    name: Name = Name(count=10, country="India")
    
    # To generate a random value with your own configuration you can use the following syntax
    
    generated_name = name.name(name_format="f m l")
    
    # Name().name returns a generator so you can get the values from simply using the for loop.
    
    for name in generated_name:
        print(name)
        
    # Some extra attributes
    # All the attributes returns the generator
    name1 = name.get_name
    name2 = name.get_first_name
    name3 = name.get_last_name
    name4 = name.get_name_with_title
    name5 = name.get_name_with_prefix
    name6 = name.get_name_with_middel
    name7 = name.get_name_with_suffix

```

# TODO in future

we are constantly working on the mayana to improve there performance and features.

we are planning to create the mayana as a ``cli application``. this feature will be added in the future.

### Ongoing features

- Placeholder
- States
- Id
- Email
- Domain name
- Colors
- Language
- Gender
- Boolean
- Time
- Numbers
- Location (Latitude, and Longitude)
- Country code

# Contribute to mayana
``mayana`` is a completely open source project. so that you can also contribute to mayana. for contributing to 
mayana please follow the given instructions.

## setup the configuration locally

Before run this ``command`` make sure that you have installed git to your local system. if you have not installed 
git, check out  [git]("https://git-scm.com/download") 
```code
   git clone https://github.com/Karelaking/mayana.git
```
Go to mayana directory.

```bash
    cd mayana
```
Install all dependencies by running following command

```bash
    pip install -r requirements.txt
```
After installing all the dependencies create a new branch and start contribution.
