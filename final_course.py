#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataBase 
@File    ：final_course.py
@IDE     ：PyCharm 
@Author  ：ZCTong
@Date    ：2025/6/3 20:45 
"""

import pandas as pd

# 读取CSV文件
df = pd.read_csv('all_table/unique_courses.csv', encoding='utf-8-sig')


# 定义函数来转换课程号
def transform_course_code(row):
    course_code = row['课程号']
    class_number = str(row['课序号'])  # 将课序号转换为字符串

    # 提取第一个字母（位置0）和第四个字母（位置3）
    first_letter = course_code[2]
    fourth_letter = course_code[3] if len(course_code) > 3 else 'X'  # 如果长度不足，补默认值

    # 提取课序号的后六位（不足六位则用原值），计算除以79的余数
    last_six = course_code[-6:]
    # print(last_six)
    remainder = int(last_six) % 97 if last_six.isdigit() else 0  # 确保是数字，否则默认0

    # 格式化余数为两位数字（不足两位补0）
    remainder_str = f"{remainder:02d}"

    # 组合成新格式：XY-MN
    new_code = f"{first_letter}{fourth_letter}-{remainder_str}"
    return new_code


# 应用转换函数到课程号列
df['课程号'] = df.apply(transform_course_code, axis=1)

# 删除课序号列
df = df.drop(columns=['课序号'])

# 将结果保存到新的CSV文件
df.to_csv('modified_courses.csv', index=False, encoding='utf-8-sig')

print(f"课程号已修改，课序号已删除并保存到 modified_courses.csv，共有 {len(df)} 条记录")