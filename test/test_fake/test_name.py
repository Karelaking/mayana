import unittest
from parameterized import parameterized
import re
import random

# Sample data for different countries
names_data = {
    'USA': {
        'first_names': ['John', 'Michael', 'Jessica', 'Emily', 'Robert', 'Ashley', 'William', 'David', 'Sarah',
                        'Daniel'],
        'middle_names': ['William', 'Lee', 'Marie', 'Grace', 'James', 'Lynn', 'Thomas', 'Elizabeth', 'Ann', 'Rose'],
        'last_names': ['Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    },
    'India': {
        'first_names': ['Amit', 'Neha', 'Ravi', 'Sita', 'Arjun', 'Priya', 'Vijay', 'Anita', 'Rajesh', 'Pooja'],
        'middle_names': ['Kumar', 'Devi', 'Singh', 'Rani', 'Raj', 'Lakshmi', 'Chandra', 'Rao', 'Bala', 'Sundar'],
        'last_names': ['Patel', 'Sharma', 'Iyer', 'Gupta', 'Reddy', 'Nair', 'Singh', 'Kumar', 'Joshi', 'Verma']
    },
    'UK': {
        'first_names': ['Oliver', 'Harry', 'George', 'Emma', 'Olivia', 'Sophia', 'Jack', 'Charlie', 'Amelia',
                        'Isabella'],
        'middle_names': ['John', 'Anne', 'Charles', 'Jane', 'David', 'Mary', 'Alexander', 'Louise', 'Edward', 'Grace'],
        'last_names': ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Evans',
                       'Thomas']
    },
    'Canada': {
        'first_names': ['Liam', 'Noah', 'Lucas', 'Mia', 'Sophia', 'Emily', 'James', 'Benjamin', 'Chloe', 'Ella'],
        'middle_names': ['Michael', 'Elizabeth', 'James', 'Grace', 'Marie', 'Alexander', 'Rose', 'John', 'Ann', 'Lee'],
        'last_names': ['Smith', 'Brown', 'Tremblay', 'Martin', 'Roy', 'Wilson', 'MacDonald', 'Gagnon', 'White',
                       'Taylor']
    },
    'Australia': {
        'first_names': ['Oliver', 'William', 'Jack', 'Charlotte', 'Ava', 'Mia', 'Noah', 'Lucas', 'Henry', 'Amelia'],
        'middle_names': ['James', 'Marie', 'John', 'Rose', 'Lee', 'Elizabeth', 'Thomas', 'Ann', 'Grace', 'Alexander'],
        'last_names': ['Smith', 'Jones', 'Williams', 'Brown', 'Wilson', 'Taylor', 'Johnson', 'White', 'Martin',
                       'Anderson']
    },
    'France': {
        'first_names': ['Louis', 'Gabriel', 'Arthur', 'Emma', 'Louise', 'Alice', 'Jules', 'Hugo', 'Chloe', 'Lina'],
        'middle_names': ['Marie', 'Luc', 'Jean', 'Elise', 'Paul', 'Anne', 'Pierre', 'Lea', 'Charles', 'Rose'],
        'last_names': ['Martin', 'Bernard', 'Dubois', 'Thomas', 'Robert', 'Richard', 'Petit', 'Durand', 'Leroy',
                       'Moreau']
    },
    'Germany': {
        'first_names': ['Max', 'Paul', 'Jonas', 'Mia', 'Emma', 'Hannah', 'Leon', 'Felix', 'Sophie', 'Marie'],
        'middle_names': ['Karl', 'Friedrich', 'Anna', 'Maria', 'Johann', 'Elisabeth', 'Heinrich', 'Clara', 'Peter',
                         'Luise'],
        'last_names': ['Müller', 'Schmidt', 'Schneider', 'Fischer', 'Weber', 'Meyer', 'Wagner', 'Becker', 'Schulz',
                       'Hoffmann']
    },
    'Japan': {
        'first_names': ['Haru', 'Sora', 'Yuki', 'Aoi', 'Hana', 'Kaito', 'Riku', 'Sakura', 'Ren', 'Mio'],
        'middle_names': ['Kazuo', 'Akira', 'Hiroshi', 'Yumi', 'Takumi', 'Natsuki', 'Haruto', 'Yuna', 'Shin', 'Ayaka'],
        'last_names': ['Sato', 'Suzuki', 'Takahashi', 'Tanaka', 'Watanabe', 'Ito', 'Yamamoto', 'Nakamura', 'Kobayashi',
                       'Kato']
    },
    'Korea': {
        'first_names': ['Ji-ho', 'Seo-jun', 'Ha-joon', 'Ji-woo', 'Ji-yoon', 'Seo-yeon', 'Min-jun', 'Joo-won',
                        'Hyun-woo', 'Yu-jin'],
        'middle_names': ['Eun', 'Jin', 'Hyun', 'Joon', 'Yoon', 'Soo', 'Seok', 'Min', 'Kyung', 'Chul'],
        'last_names': ['Kim', 'Lee', 'Park', 'Choi', 'Jeong', 'Kang', 'Cho', 'Yoon', 'Jang', 'Lim']
    },
    'China': {
        'first_names': ['Wei', 'Fang', 'Lei', 'Mei', 'Jian', 'Lili', 'Yue', 'Ming', 'Hui', 'Chen'],
        'middle_names': ['Xiao', 'Ling', 'Hua', 'Bo', 'De', 'Min', 'Yan', 'Wei', 'Jia', 'Ping'],
        'last_names': ['Wang', 'Li', 'Zhang', 'Liu', 'Chen', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou']
    },
    'Pakistan': {
        'first_names': ['Ahmed', 'Ayesha', 'Ali', 'Fatima', 'Hassan', 'Noor', 'Usman', 'Zainab', 'Bilal', 'Sara'],
        'middle_names': ['Khan', 'Zafar', 'Ali', 'Bibi', 'Iqbal', 'Hussain', 'Raza', 'Nawaz', 'Javed', 'Akhtar'],
        'last_names': ['Ahmed', 'Malik', 'Sheikh', 'Butt', 'Bhatti', 'Chaudhry', 'Raja', 'Mirza', 'Shah', 'Jutt']
    },
    'Italy': {
        'first_names': ['Luca', 'Matteo', 'Giulia', 'Sofia', 'Marco', 'Francesca', 'Davide', 'Chiara', 'Riccardo',
                        'Martina'],
        'middle_names': ['Maria', 'Giovanni', 'Luigi', 'Angela', 'Antonio', 'Elena', 'Paolo', 'Silvia', 'Franco',
                         'Roberta'],
        'last_names': ['Rossi', 'Russo', 'Ferrari', 'Esposito', 'Bianchi', 'Romano', 'Colombo', 'Ricci', 'Marino',
                       'Greco']
    },
    'Thailand': {
        'first_names': ['Arthit', 'Chaiya', 'Malee', 'Ploy', 'Niran', 'Anong', 'Kanya', 'Somchai', 'Chan', 'Lamai'],
        'middle_names': ['Sawat', 'Anurak', 'Somsak', 'Pattana', 'Siri', 'Thida', 'Praphat', 'Jinda', 'Phan', 'Karn'],
        'last_names': ['Somsak', 'Saetang', 'Pongchai', 'Khamdee', 'Phasuk', 'Siriwat', 'Kanjan', 'Namsai',
                       'Chaiprasit', 'Saelim']
    },
    'Philippines': {
        'first_names': ['Jose', 'Maria', 'Juan', 'Rizal', 'Angel', 'David', 'Rose', 'Luis', 'Grace', 'Mark'],
        'middle_names': ['Santos', 'Reyes', 'Cruz', 'Dela', 'Garcia', 'Lopez', 'Martinez', 'Perez', 'Ramos',
                         'Gonzalez'],
        'last_names': ['Santos', 'Reyes', 'Cruz', 'Bautista', 'Garcia', 'Lopez', 'Martinez', 'Perez', 'Ramos',
                       'Gonzalez']
    }
    # Add more countries as needed
}


def generate_random_name(country, is_middle_name=False):
    first_names = names_data[country]['first_names']
    last_names = names_data[country]['last_names']

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    if is_middle_name:
        middle_name = random.choice(names_data[country]['middle_names'])
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"


class TestGenerateRandomName(unittest.TestCase):

    @parameterized.expand([
        ('USA', False),
        ('India', False),
        ('UK', False),
        ('Canada', False),
        ('Australia', False),
        ('France', False),
        ('Germany', False),
        ('Japan', False),
        ('Korea', False),
        ('China', False),
        ('Pakistan', False),
        ('Italy', False),
        ('Thailand', False),
        ('Philippines', False),
        ('USA', True),
        ('India', True),
        ('UK', True),
        ('Canada', True),
        ('Australia', True),
        ('France', True),
        ('Germany', True),
        ('Japan', True),
        ('Korea', True),
        ('China', True),
        ('Pakistan', True),
        ('Italy', True),
        ('Thailand', True),
        ('Philippines', True),
    ])
    def test_generate_random_name(self, country, is_middle_name):
        first_names = names_data[country]['first_names']
        last_names = names_data[country]['last_names']

        if is_middle_name:
            middle_name = names_data[country]['middle_names']

        generated_name = generate_random_name(country, is_middle_name)

        self.assertIsInstance(generated_name, str)

        # Check if generated name matches expected patterns (first name and last name)
        first_name_matched = any(first_name in generated_name for first_name in first_names)
        last_name_matched = any(last_name in generated_name for last_name in last_names)

        self.assertTrue(first_name_matched)
        self.assertTrue(last_name_matched)
        #
        # # Regex pattern to match the format of a name
        # name_pattern = re.compile(r'^[A-Za-z\'\-]+ [A-Za-z\'\-]+$')
        #
        # # Assert that the generated name matches the regex pattern
        # self.assertTrue(re.match(name_pattern, generated_name))


if __name__ == '__main__':
    unittest.main()
