CREATE TABLE engagement_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    learner_id INT,
    journey_area VARCHAR(50),
    event_type VARCHAR(50),
    event_weight FLOAT,
    created_on DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE engagement_scores (
    learner_id INT PRIMARY KEY,
    presence_score FLOAT,
    continuity_score FLOAT,
    interaction_score FLOAT,
    participation_score FLOAT,
    reflection_score FLOAT,
    overall_engagement FLOAT,
    calculated_on DATETIME
);

CREATE TABLE engagement_weekly_trends (
    learner_id INT,
    week_start DATE,
    presence_score FLOAT,
    interaction_score FLOAT,
    participation_score FLOAT,
    reflection_score FLOAT,
    overall_engagement FLOAT,
    recorded_on DATETIME
);

CREATE TABLE engagement_area_summary (
    learner_id INT,
    journey_area VARCHAR(50),
    engagement_score FLOAT,
    calculated_on DATETIME
);
CREATE TABLE learners (
  learner_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);


CREATE TABLE engagement_engine_log (
  learner_id INT,
  execution_type VARCHAR(50),
  executed_on DATETIME,
  status VARCHAR(50)
);





CREATE TABLE engagement_settings (
  scoring_window_days INT DEFAULT 14,
  heatmap_window_days INT DEFAULT 30,
  last_updated DATETIME
);

