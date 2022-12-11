import mysql.connector
cnx = mysql.connector.connect(
    host="123.60.157.95",
    port=3306,
    user="root",
    password="csc123456@",
    database="project")

# Get a cursor
cur = cnx.cursor()
# Execute a query
cur.execute("""
            SELECT *  
            FROM chip;
            """)

# Fetch one result
print(len(cur.fetchall()))