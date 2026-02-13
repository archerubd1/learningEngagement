import sys
import mysql.connector
from datetime import datetime

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
AND created_on >= NOW() - INTERVAL 14 DAY
GROUP BY journey_area
""", (learner_id,))

rows = cursor.fetchall()

presence = len(rows)
interaction = sum(r['score'] for r in rows)
participation = sum(r['score'] for r in rows if r['journey_area'] == 'Collaborative Learning')
reflection = sum(r['score'] for r in rows if r['journey_area'] in ('Reflection','Revisit'))
continuity = min(presence / 5, 1.0)

overall = round((presence + interaction + participation + reflection) / 20, 2)

cursor.execute("DELETE FROM engagement_scores WHERE learner_id=%s", (learner_id,))
cursor.execute("""
INSERT INTO engagement_scores
VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())
""", (
    learner_id,
    presence,
    continuity,
    interaction,
    participation,
    reflection,
    overall
))

db.commit()
db.close()
