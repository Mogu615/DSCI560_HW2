# DSCI560_HW2

## Q1 Create empty environment named dsci560H4.
### Step 1: clone hw2 from Github
``` 
git clone https://github.com/Mogu615/DSCI560_HW2.git
```
### Step 2: create a blank virtual environment and name it dsci560H4
```
pip install virtualenv
```
```
python -m venv dsci560H4
```
## Q2 Activate the environment and install ONLY the dependencies you need to execute the random number generator script of Homework 2.
```
source dsci560H4/bin/activate
```
```
python3 Random_Numbers.py
```
## Q3 Take a screenshot of your terminal with the activated environment after running the script for the number generator.
![image](https://github.com/Mogu615/DSCI560_HW2/blob/main/picture1.png)

## Q4 Extract the the dependencies of your virtual environment
check the exsisting dependency of empty environment, it should be empty:
```
pip freeze > requirements.txt
```
install numpy and matplotlib packages:
```
pip install numpy
```
```
pip install matplotlib
```
check the dependency after adding packagesa:
```
pip freeze > requirements.txt
```
![image](https://github.com/Mogu615/DSCI560_HW2/blob/main/picture2.png)
we can see the after we intsall packages, the pip freeze environement files show more dependecies.

Q6 Binder Badge
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mogu615/DSCI560_HW2/main?filepath=HW2-Q5.ipynb)
