import mysql.connector
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="db_user",
    password="db_password",
    database="astraal_lxp"
)

cursor = db.cursor(dictionary=True)

cursor.execute("""
SELECT learner_id FROM engagement_scores
""")

learners = cursor.fetchall()

for learner in learners:

    learner_id = learner['learner_id']

    cursor.execute("""
    SELECT COUNT(*) as total_events,
           SUM(event_weight) as total_weight
    FROM engagement_events
    WHERE learner_id=%s
    AND created_on >= NOW() - INTERVAL 7 DAY
    """, (learner_id,))

    data = cursor.fetchone()

    presence = data['total_events'] or 0
    interaction = data['total_weight'] or 0
    participation = interaction * 0.3
    reflection = interaction * 0.2
    overall = round((presence + interaction) / 20, 2)

    week_start = datetime.now() - timedelta(days=7)

    cursor.execute("""
    INSERT INTO engagement_weekly_trends
    VALUES (%s,%s,%s,%s,%s,%s,%s,NOW())
    """, (
        learner_id,
        week_start.date(),
        presence,
        interaction,
        participation,
        reflection,
        overall
    ))

db.commit()
db.close()
