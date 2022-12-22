import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import plotly_express as px

db = mysql.connector.connect(
host="127.0.0.1",
port=3306,
user="root",
password="root",
database="project",
auth_plugin = "mysql_native_password")  


st.set_page_config(page_title="Sales Profile", page_icon=":bar_chart:", layout="wide")

def get_sidebar():
    cursor=db.cursor()
    sql = '''SELECT * FROM user natural join package'''
    cursor.execute(sql)
    # Get column names
    column=[col[0] for col in cursor.description]
    # Get data
    data = cursor.fetchall()

    # Get df
    df=pd.DataFrame(list(data),columns=column)

    st.sidebar.header("Filter here:")
    province = st.sidebar.multiselect(
        "Select province:",
        options=df['PROVINCE'].unique(),
        default=df['PROVINCE'].unique()
    )

    df_selection = df.query(
        "PROVINCE == @province"
    )

    st.title(":bar_chart: Sales Data Dashboard")
    st.markdown("##")

    # KPI Summation
    total_sales = int(df_selection["BUDGET"].sum())
    num_pkg = int(df_selection['USER_ID'].count())
    # star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["BUDGET"].mean(), 2)

    # 3-col layout
    left_column, middle_column, right_column = st.columns(3)

    # Sub-headers
    with left_column:
        st.markdown("Total Sales:")
        st.subheader(f"RMB {total_sales:,}")
    with middle_column:
        st.markdown("Number of Orders:")
        st.subheader(f"{num_pkg}")
    with right_column:
        st.markdown("Average Sales:")
        st.subheader(f"RMB {average_sale_by_transaction}")

    # Divider
    st.markdown("""---""")
    with st.container():
        st.write('test')
        st.area_chart(np.random.randn(50,3))

    cursor=db.cursor()
    cursor.execute('''select c.chip_name as ChipName,sum(p.budget) as revenue
            from user AS u, package AS p, chip AS c
            where u.user_id=p.user_id and province='Guangdong'
            group by c.chip_name
            order by sum(p.budget) desc
            limit 0,5
            ''')
    provincial_data=pd.DataFrame(cursor.fetchall(),columns=[col[0] for col in cursor.description])
    provincial_data = provincial_data.round({'revenue':2})
    st.write(provincial_data)
    # 各类商品销售情况(柱状图)
    # sales_by_product_line = (
    #     df_selection.groupby(by=["商品类型"]).sum()[["总价"]].sort_values(by="总价")
    # )
    # fig_product_sales = px.bar(
    #     sales_by_product_line,
    #     x="总价",
    #     y=sales_by_product_line.index,
    #     orientation="h",
    #     title="<b>每种商品销售总额</b>",
    #     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    #     template="plotly_white",
    # )
    # fig_product_sales.update_layout(
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     xaxis=(dict(showgrid=False))
    # )

    # # 每小时销售情况(柱状图)
    # sales_by_hour = df_selection.groupby(by=["小时"]).sum()[["总价"]]
    # print(sales_by_hour.index)
    # fig_hourly_sales = px.bar(
    #     sales_by_hour,
    #     x=sales_by_hour.index,
    #     y="总价",
    #     title="<b>每小时销售总额</b>",
    #     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    #     template="plotly_white",
    # )
    # fig_hourly_sales.update_layout(
    #     xaxis=dict(tickmode="linear"),
    #     plot_bgcolor="rgba(0,0,0,0)",
    #     yaxis=(dict(showgrid=False)),
    # )


    # left_column, right_column = st.columns(2)
    # left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
    # right_column.plotly_chart(fig_product_sales, use_container_width=True)

def visualize_region():
    sql= '''SELECT * FROM user'''
    cursor.execute(sql)
    column=[col[0] for col in cursor.description]
    data = cursor.fetchall()
    data_df=pd.DataFrame(list(data),columns=column)

if __name__=='__main__':
    get_sidebar()