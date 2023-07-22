
<div align="center">
  
  [![License](https://img.shields.io/badge/License-MIT-blue)](#license "Go to license section")
  [![Made with Python](https://img.shields.io/badge/Python->=3.7-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
</div>

<div align="center">
  
  [![PANZERMAG - Automatic_Unpopular_Post_Removal_Tool](https://img.shields.io/static/v1?label=PANZERMAG&message=Validation_creditcard.git&color=blue&logo=github)](https://github.com/PANZERMAG/Validation_creditcard)
  [![stars - badge-generator](https://img.shields.io/github/stars/PANZERMAG/Validation_creditcard?style=social)](https://github.com/PANZERMAG/Validation_creditcard)
  [![forks - badge-generator](https://img.shields.io/github/forks/PANZERMAG/Validation_creditcard?style=social)](https://github.com/PANZERMAG/Validation_creditcard)
</div>

# Credit card validator 
In the life cycle of each of the businesses will be a moment when we need to validate credit cards for paying. And at this moment this simple project solves this problem. 
This script validates the card via a request to a third-party website that checks the card which you provide.

**THIS SCRIPT DOESN'T MAKE A PAYING TO THIRD-PARTY RESOURCES**



## For whom is this app?
For small businesses or small web resources which apply a credit card for a personal profile. And don't make a payment immediately or just use a card for verification user.
## Installation

Install this project with git

```bash
  git clone https://github.com/PANZERMAG/Validation_creditcard.git
```
    
## Deployment

Firstly, you need to create a virtual environment

```bash
  python -m venv venv
```

After that, you need to activate the virtual environment.

**For Windows:**
```bash
  venv/Scripst/activate.bat
```
**For Linux:**
```bash
  source venv/Scripts/activate
```

And install the requirement library.

```bash
  pip install -r requirements.txt
```

## Usage
You can just import *ValidateCard* class in your execute file and provide parametrs to him.

Example of use
```python
    from ValidationCard import ValidateCard

    ValidateCard('1111222233334444', '03', '24')
```
