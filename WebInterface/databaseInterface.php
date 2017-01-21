<?php

$inputNames = ['durationDays', 'minTempC', 'maxTempC', 'minHumPc', 'maxHumPc'];
$inputDescriptions = [ 'Stage', 'Duration (days)',	'Min. Temp. (C)',	'Max. Temp. (C)',	'Min. Hum. (%)',	'Max. Hum. (%)' ];
$databaseQuery  = $_POST;
$returnString = '<h1>RECIPE SUMMARY:</h1>'.
'<h3>NAME: '.$_POST['recipeName'].'</h3>'.
'<h3>STAGES: '.count($_POST['durationDays']).'</h3><table><tr>';
for ($iInput = 0; $iInput < count($inputDescriptions); $iInput++){
  $returnString .= '<td>'.$inputDescriptions[$iInput].'<td>';
}
$returnString .= '</tr>';
for ($iStage = 0; $iStage < count($_POST['durationDays']); $iStage++){
  $returnString .= '<tr><td>'.$iStage.'</td>';
  for ($iInput = 0; $iInput < count($inputNames); $iInput++){
    $returnString .= '<td>'.$_POST[$inputNames[$iInput]][$iStage].'<td>';
  }
  $returnString .= '</tr>';
}

echo $returnString.'</table>';
?>
