import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

db = mysql.connector.connect(
host="127.0.0.1",
port=3306,
user="root",
password="root",
database="project",
auth_plugin = "mysql_native_password")  


##### Sales time series #####
cursor=db.cursor()
cursor.execute('''select sum(p.budget) as revenue, DATE_FORMAT(p.create_time,'%Y-%m-%d') as create_time
                from user as u, package as p
                where u.province in ('Guangdong','Hubei')
                GROUP BY MONTH(p.create_time)
                ORDER BY p.create_time asc''')
column=[col[0] for col in cursor.description]
data = cursor.fetchall()
df=pd.DataFrame(list(data),columns=column)
df['create_time'] = pd.to_datetime(df['create_time'])
df = df.set_index('create_time')
df['revenue'] = df['revenue'].astype(float)
st.line_chart(df)


#### Completion rate area chart #####
cursor=db.cursor()
cursor.execute('''select Date, count(*) as finish_num
                from (select DATE(p.CREATE_TIME) as date, s.name as status
                from package as p natural join state as s) as joint
                where Status='Finished'
                GROUP BY MONTH(Date)
                ORDER BY Date asc''')
column=[col[0] for col in cursor.description]
data = cursor.fetchall()
finished=pd.DataFrame(list(data),columns=column)

cursor=db.cursor()
cursor.execute('''select Date, count(*) as all_num
                from (select DATE(p.CREATE_TIME) as date, s.name as status
                from package as p natural join state as s) as joint
                GROUP BY MONTH(Date)
                ORDER BY Date asc''')
column=[col[0] for col in cursor.description]
data = cursor.fetchall()
all=pd.DataFrame(list(data),columns=column)

all['Finished num'] = finished['finish_num'].values
all['date'] = pd.to_datetime(all['date'])
all = all.set_index('date')
st.area_chart(all)