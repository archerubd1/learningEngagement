<?php
session_start();
$learner_id = $_SESSION['learner_id'] ?? 1;

exec("python3 /home/username/python/engagement_engine.py $learner_id");
?>
