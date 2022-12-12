import streamlit as st
import mysql.connector

def log_in_page():
    cnx = mysql.connector.connect(
    host="123.60.157.95",
    port=3306,
    user="root",
    password="csc123456@",
    database="project")  

    first_name = st.text_input("First name",placeholder="Yangsheng")
    last_name = st.text_input("Last name",placeholder="Xu")
    password = st.text_input("Password",placeholder="1999GJ5")
    # Get a cursor
    cur = cnx.cursor()
    # Execute a query
    cur.execute("""
                SELECT *  
                FROM user_
                WHERE (FIRST_NAME = %s)
                AND (LAST_NAME = %s)
                AND (PASSWORD = %s);
                """, (first_name,last_name,password))

    # Fetch one result
    if st.button("Log In"):
        if len(cur.fetchall()) == 0:
            st.warning("INVALID INFORMATION! RECHECK YOUR INPUT!")
        else:
            st.balloons()

def sign_up_page():
    cnx = mysql.connector.connect(
    host="123.60.157.95",
    port=3306,
    user="root",
    password="csc123456@",
    database="project")
    cur  = cnx.cursor()

    #user_id = st.text_input("User ID")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    phone_number = st.text_input("Phone Number")

    # Create a selectbox for countries
    country_name = st.text_input("Input your country:")
    # Create a selectbox for provinces
    if country_name == "China":
        province_options =  ["Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei", "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Inner Mongolia", "Ningxia", "Qinghai", "Shaanxi", "Shandong", "Shanghai", 
                        "Shanxi", "Sichuan", "Tianjin", "Tibet", "Xinjiang", "Yunnan", "Zhejiang", 
                        "Taiwan", "Hong Kong", "Macau"]
        province = st.selectbox("Select a province:", province_options)
    else:
        province = st.selectbox("Select a province:", ["International",])
    # Print the selection

    role = st.selectbox("Role", ["consumer", "staff"])
    street_address = st.text_input("Street Address")
    password = st.text_input("Password")

    if st.button("Sign Up"):
        query = """
        INSERT INTO user_ (FIRST_NAME, LAST_NAME, PHONE_NUMBER, COUNTRY_NAME, PROVINCE, ROLE, STREET_ADDRESS, PASSWORD)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (first_name, last_name, phone_number, country_name, province, role, street_address, password))
        cnx.commit()