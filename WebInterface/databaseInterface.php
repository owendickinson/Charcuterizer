<?php

class RecipeSummary {

  private $dbConnection = null;
  private $recipeId = null;
  private $stageResult = null;

  function __construct($dbConnection, $recipeId){
    $this->dbConnection = $dbConnection;
    $this->recipeId = $recipeId;
  }

  function getStageDetails(){
    $stageQuery = "select
    recipes.name,
    min_temp.value,
    max_temp.value,
    min_humidity.value,
    max_humidity.value,
    temperatures_for_recipes.stage_in_recipe
    from recipes left join (temperatures_for_recipes,
    humdidities_for_recipes,
    durations_for_recipes,
    min_temp, max_temp,
    min_humidity, max_humidity,
    duration,
    ingredients)
    on (recipes.id = temperatures_for_recipes.recipe_id and
    temperatures_for_recipes.min_temp_id = min_temp.id and
    temperatures_for_recipes.max_temp_id = max_temp.id and
    humdidities_for_recipes.min_humidity_id = min_humidity.id and
    humdidities_for_recipes.max_humidity_id = max_humidity.id and
    durations_for_recipes.duration_id = duration.id) where
    (recipes.id = ".$this->recipeId."
    and temperatures_for_recipes.stage_in_recipe = humdidities_for_recipes.stage_in_recipe
    and temperatures_for_recipes.stage_in_recipe = durations_for_recipes.stage_in_recipe)";

    if(!$this->stageResult = $this->dbConnection->query($stageQuery)){
      print('There was an error running the recipe stage details query [' . $this->dbConnection->error . ']');
      return;
    }

    $stageRows = array();
    while($row = mysqli_fetch_assoc($this->stageResult)) {
      $stageRows[] = $row;
    }
    print json_encode($stageRows);
  }
}

// INITIAL DATABASE CONNECTION
$database = new mysqli($_SERVER['CHARC_MYSQL_HOST'], $_SERVER['CHARC_MYSQL_USER'], $_SERVER['CHARC_MYSQL_PASS'], $_SERVER['CHARC_MYSQL_DB']);

if($database->connect_errno > 0){
  die('Unable to connect to database [' . $database->connect_error . ']');
}

$recipeSummary = new RecipeSummary($database, 1);
$recipeSummary->getStageDetails();

function echoFormData($postData){

  $inputNames = ['durationDays', 'minTempC', 'maxTempC', 'minHumPc', 'maxHumPc'];
  $inputDescriptions = [ 'Stage', 'Duration (days)',	'Min. Temp. (C)',	'Max. Temp. (C)',	'Min. Hum. (%)',	'Max. Hum. (%)' ];
  //$databaseQuery  = $postData;
  $returnString = '<h1>RECIPE SUMMARY:</h1>'.
  '<h3>NAME: '.$postData['recipeName'].'</h3>'.
  '<h3>STAGES: '.count($postData['durationDays']).'</h3><table><tr>';
  for ($iInput = 0; $iInput < count($inputDescriptions); $iInput++){
    $returnString .= '<td>'.$inputDescriptions[$iInput].'<td>';
  }
  $returnString .= '</tr>';
  for ($iStage = 0; $iStage < count($postData['durationDays']); $iStage++){
    $returnString .= '<tr><td>'.($iStage+1).'</td>';
    for ($iInput = 0; $iInput < count($inputNames); $iInput++){
      $returnString .= '<td>'.$postData[$inputNames[$iInput]][$iStage].'<td>';
    }
    $returnString .= '</tr>';
  }

  echo $returnString."</table><input type='button' name='dismiss' value='Dismiss' onclick='dismissModal()' class='ui-button'>";
}
?>
