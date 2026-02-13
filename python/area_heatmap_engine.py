import sys
import mysql.connector

learner_id = int(sys.argv[1])

db = mysql.connector.connect(
    host="localhost",
    user="db_user",
    password="db_password",
    database="astraal_lxp"
)

cursor = db.cursor(dictionary=True)

cursor.execute("""
SELECT journey_area, SUM(event_weight) as score
FROM engagement_events
WHERE learner_id=%s
AND created_on >= NOW() - INTERVAL 30 DAY
GROUP BY journey_area
""", (learner_id,))

rows = cursor.fetchall()

cursor.execute("DELETE FROM engagement_area_summary WHERE learner_id=%s", (learner_id,))

for row in rows:
    cursor.execute("""
    INSERT INTO engagement_area_summary
    VALUES (%s,%s,%s,NOW())
    """, (learner_id, row['journey_area'], row['score']))

db.commit()
db.close()
