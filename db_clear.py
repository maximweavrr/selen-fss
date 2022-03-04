import psycopg2

conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "fss_dev",
    user = "empi",
    password = "empi123",
    port = "5454"
)

cur = conn.cursor()

delete_script = '''delete from imagescorelistdetail i where exists (select 1 from imagescorelist i2 where notes='VIS2021Q3-SQA' and i2.id = i.id)'''

cur.execute(delete_script)
conn.commit()

cur.close()
conn.close()