import psycopg2

conn = psycopg2.connect(
    host = "127.0.0.1",
    database = "fss_dev",
    user = "empi",
    password = "empi123",
    port = "5454"
)

cur = conn.cursor()

delete_script = '''
UPDATE dropimages 
SET isbanished = FALSE 
WHERE id IN ( 
    SELECT d.id
    FROM dropimages d
    WHERE EXISTS (
        SELECT 1
        FROM (SELECT * FROM imagescorelist i2 WHERE i2.dataset = 'VIS2021Q3-SQA') i
        WHERE d.id::bigint = ALL(i.ref_dropimages_id)
    ) AND d.isbanished is TRUE
)'''

cur.execute(delete_script)
conn.commit()

cur.close()
conn.close()