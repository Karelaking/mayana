<h1 align="center"> MAYANA </h1>

---
**Mayana**  is a ```cli-application``` that generates random values for fake data entry such as ```names```, ```dates of birth```, ```IP 
addresses```, ```passwords```, ```states```, ```countries```, ```phone numbers```, ```pin code``` and more. This tool is 
useful 
for developers and testers who need to populate databases or forms with realistic-looking data.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

  - [Generate a Random Name](#generate-a-random-name)
  - [Generate a Random Date of Birth](#generate-a-random-date-of-birth)
  - [Generate a Random IP Address](#generate-a-random-ip-address)
  - [Generate a Random Password](#generate-a-random-password)
  - [Generate a Random State](#generate-a-random-state)
  - [Generate a Random Country](#generate-a-random-country)
  - [Generate a Random Phone Number](#generate-a-random-phone-number)
  - [Generate a Random pin code]()
  - [Generate a Random country code]()

- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
- [Authors](#authors)
                     
---

## Installation

You can install Mayana using pip. Ensure you have Python installed on your system.

```sh
pip install mayana
```

## Configuration

```json
{
  "name_format": "first_last",  // Options: "first_last", "last_first"
  "date_format": "YYYY-MM-DD",  // Options: "YYYY-MM-DD", "MM/DD/YYYY"
  "ip_version": "ipv4",         // Options: "ipv4", "ipv6"
  "password_length": 12,        // Default length of generated passwords
  "phone_format": "international" // Options: "international", "local"
}
```

## Usage

```sh
mayana generate name
mayana generate dob
mayana generate ip
mayana generate password
mayana generate state
mayana generate country
mayana generate phone
```
