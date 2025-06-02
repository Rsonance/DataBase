#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataBase 
@File    ：expand_Student.py
@IDE     ：PyCharm 
@Author  ：ZCTong
@Date    ：2025/6/2 21:10 
"""

import pandas as pd
import random
from datetime import datetime, timedelta

# 读取 teenagers.csv 文件，指定制表符分隔
names_df = pd.read_csv('all_table/teenagers.csv', sep='\t', encoding='utf-8')
print("实际列名:", names_df.columns.tolist())

# 提取姓名和性别列
names = names_df['姓名'].tolist()  # 第一列：姓名
sexes = names_df['性别'].tolist()  # 第二列：性别

# 初始化数据列表
data = []

# 从现有数据开始，S# 从 01032010 到 01037009（5000 行）
for i in range(2010, 7010):
    s_number = f"0103{i:04d}"

    # 随机选择姓名和性别
    idx = random.randint(0, len(names) - 1)
    sname = names[idx]
    sex = sexes[idx]

    # 随机生成出生日期 (2002-2005)
    start_date = datetime(2002, 1, 1)
    days_range = (datetime(2005, 12, 31) - start_date).days
    bdate = start_date + timedelta(days=random.randint(0, days_range))

    # 随机生成身高 (1.58-1.90)
    height = round(random.uniform(1.58, 1.90), 2)

    # 随机生成宿舍号：东m舍n
    m = random.randint(1, 21)  # m 为 1-21
    n_first = random.randint(1, 9)  # 第一位为 1-9
    n_last_two = random.randint(1, 33)  # 第二三位为 01-33
    dorm = f"东{m}舍{n_first}{n_last_two:02d}"

    # 添加到数据列表
    data.append([s_number, sname, sex, bdate.strftime('%Y-%m-%d'), height, dorm])

# 创建 DataFrame
df = pd.DataFrame(data, columns=['S#', 'SNAME', 'SEX', 'BDATE', 'HEIGHT', 'DORM'])

# 保存为 CSV 文件
df.to_csv('expanded_student_data.csv', index=False, encoding='utf-8')
print("已生成 5000 行数据并保存到 expanded_student_data.csv")