#!/usr/bin/env python
# coding: utf-8

# ### A Company decided to give bonus to all its employee's on diwali. A 5% bonus on salary is given to the male workers and 10% bonus on salary to the female worker's. Write a program to enter the salary of the employee and gender of the employee. If the salary of the employee is less than Rs.10000 then the employee gets an extra 2% bonus on salary. Calculate the bonus that has to be given to the employee and display the salary that the employee will get.
# 

# In[ ]:


gender=input("enter the gennder 'M 0r F': ").upper()
salary=int(input("enter the amount :"))
if salary>10000:
    if gender=='M':
        bonus=0.05*salary
        total_salary=salary+bonus
    else:
        bonus=0.1*salary
        total_salary=salary+bonus
else:
    if gender=='M':
        extra_bonus=0.07*salary
        total_salary=salary+extra_bonus
    else:
        extra_bonus=0.12*salary
        total_salary=salary+extra_bonus
print("Gender=",gender)
print("salary=",salary)
print("total salary=",total_salary)


# In[ ]:




