# DataBase
## Part I
### 一、Student表数据生成
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Chinese_name.csv* 文件表根据 Dongbo Shi 和 Sherry Tong 于 2025 年 1 月 8 日发布的论文（ 详见 SSRN 网站：https://ssrn.com/abstract=5087045 ）中附带的数据集进行下载得到。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 通过代码 *expand_Student.py* 进行对 Student 表的数据扩充过程，随机从附带的数据集中选择足够的姓名数进行扩充的过程。

### 二、Class表数据生成
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class 表数据通过从 ehall 教务处官网全校课表查询模块进行数据爬取，利用 *make_Class.py* 代码进行数据的爬取过程，并将爬取得到的结果保存在文件 *all_courses.csv* 里。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 对于爬取得到的 4800+ 的课程数据，首先通过 *update_courses.py* 代码将其中课程号重复的课程全部删除；接下来将课程号按照所给的样例格式通过代码 *final_courses* 进行修改得到最终的 Class 表数据 *final_courses.csv* 。

### 三、SC表数据生成
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 通过从 *expand_student_data.csv* 的 S# 和 *final_courses.csv* 的 C# 进行随机的选择，联合作为主键确保不重复，利用 *SC_.py* 代码进行成绩的随机生成完成扩充。

## Part II 