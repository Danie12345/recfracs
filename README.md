[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Recursive Fractions
> Like the project? Leave a star, it helps! ;)

**Release 0.4.0**

## Description
recfracs is an app that expands any rational (decimal) number into fraction form. It does not use the conventional method of division by powers of 10. It uses an entirely different and intuitive mathematical algorithm.

A few years ago, when I came up with this algorithm, I did not know much about programming nor github. This is now my attempt at making it known.


## Installation
### Get the app!
- Currently there is only the src/ folder with the basic script. You would need to setup or build the project in-order-to use it.


## Explanation
### How it works
- Found a paper that explains it [here](https://begriffs.com/pdf/dec2frac.pdf). But I have my own explanation :) (it's very similar though)


## Contribute
### Requirements
- Have Python 3.9.1+ installed in your system
- Have pip3 installed

### Setup
- Clone repository
- Navigate to root dir, then run commands
  - `python -m venv *path_to_repository*\recfracs\venv`
  - `python -m pip install -r requirements.txt`

### Introduce new packages used
- Navigate to root dir, then run command
  - `pip freeze > requirements.txt`

### Build
- Navigate to root dir, then run command
  - `pyinstaller -F -w src/main.py`


### Run
- Navigate to `main.py` and run the file normally

### Open a pull request
- Once you've finished adding changes, add yourself as a contributor below
- Open your pull request, and @ [me](https://github.com/Danie12345)


## Contributors
- [Your name](https://github.com)


## License
Licensed under the [GNU GPL v3 license](LICENSE).