#!/usr/bin/env python
# coding: utf-8

# Author: Kris Swartzbaugh
# CWID: 890939184 
# Project 1: Tukey Fences
# Project Description: 
#     Using Jupyter Notebook and standard python library (NO numpy or pandas)
#         1.) Use provided participants.csv data set
#         2.) Find the quartiles for week 1
#         3.) Use Tukey's method to find outliers for week 1 attendence (not attending enough class)
#         4.) Repeat steps 2-3 for weeks 2 and 3
#         5.) Consolidate steps 2-3 into a python function named tardy(), tardy students should be listed in the same order as the orinal file 
#         
# 
# Provided below:
#     Markdown cell 1: This cell, author info and project description
#     Code Cell 1: Import CSV and convert appropriate cells to type int
#     Code Cell 2: tardy() function 
#     Code Cell 3: call to tardy() function and print results
#     Markdown cell 2: Results when ran
# 

# In[50]:


from csv import reader
# read csv file as a list of lists
with open('participants.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    student_data = list(csv_reader)
    #remove header, convert times attended to type int 
    del student_data[0]
    for i in range(len(student_data)):
        student_data[i][1]=int(student_data[i][1])
        student_data[i][2]=int(student_data[i][2])    
        student_data[i][3]=int(student_data[i][3])




# In[51]:


def tardy(data):
    #tardy list to contain lists of names for each week
        #tardy[0] = list of students late week 1, tardy[1] students late week 1, tardy[3] students late week 2
    tardy = []
    for i in range(len(data)):
        data[i].append(i)
        #add student number for maintaing original order
    for i in range(3):
        tardy.append([])
    student_data_week1 = sorted(data, key=lambda x: x[1])
    #student_data_week1 = sorted(data, key = lambda, x:x[1])
    student_data_week2 = sorted(data, key=lambda x: x[2])
    #student_data_week1 = sorted(data, key = lambda, x:x[1])
    student_data_week3 = sorted(data, key=lambda x: x[3])
    #student_data_week1 = sorted(data, key = lambda, x:x[1])

    
    #Q1 = is the middle number between the minimum and the median 
    #Q3 is the middle number between the median and the maximum 
    # Q1, Q2 for week 1
    Q1_1 = student_data_week1[int(len(student_data)/4)][1]
    Q3_1 = student_data_week1[int(len(student_data)*(3/4))][1]
    # Q1, Q2 for week 2
    Q1_2 = student_data_week2[int(len(student_data)/4)][2]
    Q3_2 = student_data_week2[int(len(student_data)*(3/4))][2]
    # Q1, Q2 for week 2
    Q1_3 = student_data_week3[int(len(student_data)/4)][3]
    Q3_3 = student_data_week3[int(len(student_data)*(3/4))][3]


    # outliers are outside the range [Q1 - k(Q3-Q1),Q3+k(Q3-Q1)] per tukey's fences
    # k=1.5 per project guidelines
    k=1.5
    # we are only concerned with people lower than that range (did not attend enough class)
    lower_bound_1 = Q1_1 - k*(Q3_1-Q1_1)
    lower_bound_2 = Q1_2 - k*(Q3_2-Q1_2)
    lower_bound_3 = Q1_3 - k*(Q3_3-Q1_3)
    
    #add the tardy students and their classtime attended for that week to the respective week 
    for i in range(len(student_data)):
        if data[i][1] < lower_bound_1:
            tardy[0].append([data[i][0],data[i][1]])
        if data[i][2] < lower_bound_2:
            tardy[1].append([data[i][0],data[i][2]])
        if data[i][3] < lower_bound_3:
            tardy[2].append([data[i][0],data[i][3]])

        i=i+1    
    return tardy
        


# In[52]:


#call to tardy function using student data
late = []
late = tardy(student_data)
for j in range(len(late)):
    print("The students late for week ",j+1," are: ", late[j])


# Results When Ran:
# The students late for week  1  are:  [['Trey Khan', 110], ['Taya Curtis', 115], ['Wallace Rojas', 91]]
# The students late for week  2  are:  [['Trey Khan', 66], ['Taya Curtis', 74], ['Wallace Rojas', 35], ['Stephanie Hail', 143]]
# The students late for week  3  are:  [['Kaleb Cummings', 51], ['Ameerah Fulton', 24], ['Arman Mackie', 9]]
# 

# In[ ]:




