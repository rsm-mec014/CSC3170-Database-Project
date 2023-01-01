[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9434978&assignment_repo_type=AssignmentRepo)
# CSC3170 Course Project

## Project Overall Description

This is our implementation for the course project of CSC3170, 2022 Fall, CUHK(SZ). For details of the project, you can refer to [project-description.md](project-description.md). In this project, we will utilize what we learned in the lectures and tutorials in the course, and implement either one of the following major jobs:

<!-- Please fill in "x" to replace the blank space between "[]" to tick the todo item; it's ticked on the first one by default. -->

- [x] **Application with Database System(s)**
- [ ] **Implementation of a Database System**

## Team Members

Our team consists of the following members, listed in the table below (the team leader is shown in the first row, and is marked with 🚩 behind his/her name):

<!-- change the info below to be the real case -->

| Student ID | Student Name | GitHub Account (in Email) | GitHub User Name |
| ---------- | ------------ | ------------------------- | ---------------- |
| 119010351  | 谢昊轩 Haoxuan Xie 🚩      | 119010351@link.cuhk.edu.cn        |@[ForwardStar](https://github.com/ForwardStar) |
| 119010020  | 陈梦洁 Mengjie Chen        | 119010020@link.cuhk.edu.cn        |@[wuli-mA](https://github.com/wuli-mA) |
| 121090434  | 潘婕 Jie Pan          | 121090434@link.cuhk.edu.cn        | @[121090434](https://github.com/121090434)|
| 120090302  | 苏梦琦 Mengqi Su        | 120090302@link.cuhk.edu.cn        | @[Su-823](http://github.com/Su-823) |
| 120090005  | 钟文柯 Wenke Zhong        | 120090005@link.cuhk.edu.cn        | @[120090005](https://github.com/120090005)|
| 120090527  | 林锦睿 Jinrui Lin        | 120090527@link.cuhk.edu.cn        | @[RickLin616](https://github.com/RickLin616)|
| 119010224  | 罗杨知心 Yangzhixin Luo      | rep_laureline@hotmail.com        | @[lyzx2001](https://github.com/lyzx2001) |
| 119020226  | 蒋舒亭 Shuting Jiang        | 119020226@link.cuhk.edu.cn        | @[zxcg770](https://github.com/zxcg770)|
| 120090466  | 何兴杰 Xingjie He        | 120090466@link.cuhk.edu.cn        | @[JAck-Yolo](https://github.com/JAck-Yolo)|
| 120090454  | 仝研 Yan Tong          | yantong1775@gmail.com       | @[yantong1775](https://github.com/yantong1775) |

## Project Specification

<!-- You should remove the terms/sentence that is not necessary considering your option/branch/difficulty choice -->

After thorough discussion, our team made the choice and the specification information is listed below:

- Our option choice is: **Option 1**
- Our branch choice is: **Branch 1, 2**
- The difficulty level is: **Enhanced**

## Report
For the complete report, please refer to [``CSC3170_Project_Report.pdf``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/CSC3170_Project_Report.pdf).

## ER Diagram
![ER Diagram](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/ER_diagram.png)

## Web Application Link
We have deployed the app on the cloud, the url is attached as follows:

https://chipandas.streamlit.app

If you want to run the app locally, refer to the following section.

## How To Run the App
All the web codes are stored in the web directory. The app is written with streamlit, a Python-based frontend language.

To run the app locally, first go to the web directory:
```
cd web/
```
To set up the environment:
```
pip install -r requirements.txt
```
To execute the code:
```
streamlit run main.py
```

## Video Link
Clipchamp:

[Presentation_Video_in_Clipchamp](https://clipchamp.com/watch/9wZpLeW58tA)

Bilibili:

If the video is vague, please see our Bilibili backup [CSC3170_Final_Pre](https://www.bilibili.com/video/BV1pP4y1q7AW/?spm_id_from=333.337.search-card.all.click&vd_source=910ecdca8e556f0b929ec8687e2cfccb)

Please notice that our report [``CSC3170_Project_Report.pdf``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/CSC3170_Project_Report.pdf) contains a more thorough explanation and covers more main functions of our project in detail.

## Project Abstract
Our project aims at developing a web platform based on a consumer database for the **Chipanda Semiconductor Manufacturing Company**. This platform allows customers to place orders, as well as enables staff to manage those orders. The platform is designed with  in mind, allowing it to easily accommodate future growth and changes in customer needs. In addition, the system has been designed with usability in mind so that customers can quickly and easily place their orders without any confusion or frustration. Finally, the system provides detailed reporting capabilities for both staff and consumers, which will allow them greater insight into order trends over time.

The target users of our platform are chip-manufacture corporations that need a secure, efficient, and easy-to-use system to manage customer orders. Our platform provides several advantages over traditional methods, such as:
- Increased concurrency measures to guarantee the successful payment during transmission and storage, providing scalability to accommodate future growth in demand;

- Detailed reporting capability provides greater insight into order trends;

- The system is designed with availability and transaction costs in mind, so plant managers can place orders in the most convenient and cost-effective manner.

By providing these features and benefits, we believe our platform will offer the best possible experience to both staff and customers alike.

## Database Creation and Data Generation
To create database schemas, run the sql file [``source/db_table.sql``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/source/db_table.sql).

To insert data into database schemas, run the sql file [``source/db_insert.sql``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/source/db_insert.sql).

To drop all the database schemas, run the sql file [``source/db_clean.sql``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/source/db_clean.sql).

To generate random data in ``.csv`` format, run the ``.ipynb`` codes in [``source/data_generation``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/tree/main/source/data_generation).

The detailed information of database schemas is included in [``database_intro.md``](https://github.com/CSC3170-2022Fall/project-whiskey-drunkards/blob/main/database_intro.md).

## Remarks
Note that the Huawei cloud database RDS for MySQL that we rendered for our back end was paid to be available before Jan 10, 2023, thus after this date our web application may have some database-related functions that do not work as expected. If you encounter issues related to it, please contact rep_laureline@hotmail.com, and we will extend the service lifespan of our Huawei cloud database RDS.

There is a similar issue with the cloud of streamlit, where we deploy our app. If the app has not been visited for several weeks, it might sleep temporarily. Contact 120090527@link.cuhk.edu.cn if the app is sleeping.
