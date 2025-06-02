#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataBase 
@File    ：make_Class.py
@IDE     ：PyCharm 
@Author  ：ZCTong
@Date    ：2025/6/2 21:44 
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# 设置 Selenium WebDriver
# options.add_argument('--headless')  # 无头模式
driver = webdriver.ChromiumEdge()

try:
    # 访问目标页面
    url = "https://ehall.xjtu.edu.cn"  # 请替换为实际 URL
    driver.get(url)
    print("访问页面成功")
    time.sleep(1)

    # 点击指定按钮
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ampHasNoLogin"]'))
        )
        button.click()
        print("按钮点击成功")
    except Exception as e:
        print(f"按钮点击失败: {e}")
        driver.quit()
        exit()
    time.sleep(2)

    # 在指定输入框输入账号
    try:
        account_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/input[1]'))
        )
        account_input.send_keys("2226114070")
        print("账号输入成功")
    except Exception as e:
        print(f"账号输入失败: {e}")
        driver.quit()
        exit()

    # 在指定输入框输入密码并按回车键
    try:
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div[1]/form/input[2]"))
        )
        password_input.send_keys("tzc20040913")  # 输入指定密码
        password_input.send_keys(Keys.RETURN)  # 按回车键
        print("密码输入成功并按下回车键")
    except Exception as e:
        print(f"密码输入或回车失败: {e}")
        driver.quit()
        exit()

    # 等待登录成功（假设跳转到课程页面）
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table"))  # 等待表格加载
        )
        print("登录成功，进入课程页面")
    except Exception as e:
        print(f"登录后页面加载失败: {e}")
        driver.quit()
        exit()

    # 点击“全校课表查询”按钮并切换到新页面
    try:
        query_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/article[5]/section/div[2]/div[1]/div[2]/pc-card-html-4786696181714491-01/amp-w-frame/div/div[2]/div/div[1]/widget-app-item[3]/div/div/div[2]/div[1]"))
        )
        # 记录当前窗口句柄
        original_window = driver.current_window_handle
        query_button.click()
        print("全校课表查询按钮点击成功")
        # 等待新窗口出现
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        # 切换到新窗口
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        # 等待新页面URL加载
        WebDriverWait(driver, 10).until(
            EC.url_contains("select_role.html")
        )
        print("成功切换到新页面: https://ehall.xjtu.edu.cn/portal/html/select_role.html")
    except Exception as e:
        print(f"全校课表查询按钮点击或新页面切换失败: {e}")
        driver.quit()
        exit()
    time.sleep(1)

    # 点击“学生”按钮
    try:
        stu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="20241125142542723"]'))
        )
        stu_button.click()
        print("学生按钮点击成功")
    except Exception as e:
        print(f"学生按钮点击失败: {e}")
        driver.quit()
        exit()
    time.sleep(1)

    # 初始化数据列表
    data = []

    # 总页数
    total_pages = 430

    # 遍历所有页面
    for page in range(1, total_pages + 1):
        print(f"爬取第 {page} 页")
        # 动态生成每页的行XPath
        row_xpaths = [
            f"/html/body/main/article/section/div/div[2]/div[1]/div/div[3]/div[2]/div/div[4]/div[2]/div/table[2]/tbody/tr[{i}]"
            for i in range(1, 11)  # 每页10行，从tr[1]到tr[10]
        ]

        # 读取每行数据
        for row_xpath in row_xpaths:
            try:
                row_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, row_xpath))
                )
                # 提取每列数据（假设每行有至少8列）
                cols = row_element.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 8:
                    course_id = cols[1].text.strip()  # 课程号
                    course_name = cols[2].text.strip()  # 课程名
                    class_id = cols[3].text.strip()  # 课序号
                    hours = cols[5].text.strip()  # 学时
                    credits = cols[6].text.strip()  # 学分
                    teacher = cols[7].text.strip()  # 老师
                    data.append([course_id, course_name, class_id, hours, credits, teacher])
                    print(f"成功读取行: {course_id}, {course_name}")
            except Exception as e:
                print(f"读取行 {row_xpath} 失败: {e}")
                continue

        # 如果不是最后一页，点击翻页按钮
        if page < total_pages:
            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/section/div/div[2]/div[1]/div/div[3]/div[2]/div/div[10]/div/div/div[1]/a[3]"))
                )
                next_button.click()
                print(f"成功翻到第 {page + 1} 页")
                time.sleep(3)  # 等待页面加载
            except Exception as e:
                print(f"翻页失败: {e}")
                break

    # 将数据保存为 CSV
    if data:
        df = pd.DataFrame(data, columns=['课程号', '课程名', '课序号', '学时', '学分', '老师'])
        df.to_csv('all_courses.csv', index=False, encoding='utf-8-sig')
        print(f"总共爬取 {len(data)} 条记录，数据已保存到 all_courses.csv")
    else:
        print("未读取到任何数据")

finally:
    # 确保浏览器关闭
    driver.quit()