#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataBase 
@File    ：update_courses.py
@IDE     ：PyCharm 
@Author  ：ZCTong
@Date    ：2025/6/3 20:26 
"""

import pandas as pd

# 读取CSV文件
df = pd.read_csv('all_table/modified_courses.csv', encoding='utf-8-sig')

# 删除重复的课程号，只保留第一次出现的记录
df_unique = df.drop_duplicates(subset=['课程号'], keep='first')

# 将结果保存到新的CSV文件
df_unique.to_csv('final_courses.csv', index=False, encoding='utf-8-sig')

print(f"去重后剩余 {len(df_unique)} 条记录，已保存到 final_courses.csv")