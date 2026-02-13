<?php
include("../config/db.php");
$learner_id = 1;

$data = $conn->query("
SELECT * FROM engagement_scores WHERE learner_id=$learner_id
")->fetch_assoc();
?>

<h2>Your Engagement Snapshot</h2>
<p>This reflects how you've been interacting with learning activities recently.</p>

<ul>
<li>Presence: <?php echo $data['presence_score']; ?></li>
<li>Continuity: <?php echo $data['continuity_score']; ?></li>
<li>Interaction: <?php echo $data['interaction_score']; ?></li>
<li>Participation: <?php echo $data['participation_score']; ?></li>
<li>Reflection: <?php echo $data['reflection_score']; ?></li>
<li>Overall: <?php echo $data['overall_engagement']; ?></li>
</ul>
