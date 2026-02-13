<?php
include("../config/db.php");
session_start();

$learner_id = $_SESSION['learner_id'] ?? 1;
$journey_area = $_POST['journey_area'];
$event_type = $_POST['event_type'];

$weights = [
    "viewed" => 1,
    "attempted" => 2,
    "participated" => 3,
    "revisited" => 2
];

$weight = $weights[$event_type] ?? 1;

$stmt = $conn->prepare("
INSERT INTO engagement_events
(learner_id, journey_area, event_type, event_weight)
VALUES (?, ?, ?, ?)
");

$stmt->bind_param("issi", $learner_id, $journey_area, $event_type, $weight);
$stmt->execute();
?>
