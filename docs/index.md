# d6Dice

Python dice object: 
  - Uses dice notation '2d6', '3d6', '2d12', '3d8' etc
  - Default dice roller uses numpy
  - Dynamically change how dice are rolled

The d6dice project was created to be used with the d6Engine and OpenD6 games. 

## Quick Start

d6dice requires Python 3.5 or greater. It should run on any OS, but not verified.

1. Install python 3.7+ [Python Downloads](https://www.python.org/downloads/)
    - [Python3 Installation & Setup Guide](https://realpython.com/installing-python/)
    - DETAILS: [Using Python on Windows](https://docs.python.org/3/using/windows.html)
2. Install d6dice as user
    - `python3 -m pip install --user d6dice`


```bash
    > python3 -m pip install --user d6dice
    Looking in indexes: https://pypi.org/simple, https://uxtools.ohsu.edu:6868/simple
    Collecting d6dice
      Downloading https://files.pythonhosted.org/packages/42/72/b35a5a1277e330b86f32c02d840789f5724f36a54c6c6220216fece7e1e2/d6dice-0.2.2-py3-none-any.whl
    Requirement already satisfied: click<8.0,>=7.0 in ./Library/Python/3.7/lib/python/site-packages (from d6dice) (7.0)
    Collecting numpy<2.0,>=1.16 (from d6dice)
      Downloading https://files.pythonhosted.org/packages/43/6e/71a3af8680a159a141fab5b4d19988111a09c02ffbfdeb42175cca0fa341/numpy-1.16.3-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (13.9MB)
        100% |████████████████████████████████| 13.9MB 1.8MB/s
    Installing collected packages: numpy, d6dice
    Successfully installed d6dice-0.2.2 numpy-1.16.3
```
