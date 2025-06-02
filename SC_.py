#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataBase 
@File    ：SC_.py
@IDE     ：PyCharm 
@Author  ：ZCTong
@Date    ：2025/6/3 21:54 
"""

import pandas as pd
import numpy as np
from itertools import product

# Read the CSV files
students = pd.read_csv('all_table/expanded_student_data.csv')['S#'].dropna().unique()
courses = pd.read_csv('all_table/final_courses.csv')['课程号'].dropna().unique()

# Generate all possible combinations
combinations = list(product(students, courses))
np.random.shuffle(combinations)

# Generate grades (0.0 to 4.0 with 1 decimal place)
grades = np.round(np.random.uniform(30, 100.0, len(combinations)), 1)

# Create DataFrame
data = pd.DataFrame(combinations, columns=['S#', '课程号'])
data['grade'] = grades

# Ensure no duplicate primary keys (S# + 课程号)
data = data.drop_duplicates(subset=['S#', '课程号'])

# If needed, generate more rows by repeating with new grades
while len(data) < 100000:
    additional_combinations = list(product(students, courses))
    np.random.shuffle(additional_combinations)
    additional_grades = np.round(np.random.uniform(0, 4.0, len(additional_combinations)), 1)
    additional_data = pd.DataFrame(additional_combinations, columns=['S#', '课程号'])
    additional_data['grade'] = additional_grades
    data = pd.concat([data, additional_data]).drop_duplicates(subset=['S#', '课程号'])

# Trim or pad to exactly 100000+ rows
data = data.head(100000)

# Save to CSV
data.to_csv('generated_dataset.csv', index=False)