create database charcuterizer;

use charcuterizer;

create table max_temp (
id int primary key auto_increment,
value DOUBLE NOT NULL);

create table min_temp (
id int primary key auto_increment,
value DOUBLE NOT NULL);

create table max_humidity (
id int primary key auto_increment,
value DOUBLE NOT NULL);

create table min_humidity (
id int primary key auto_increment,
value DOUBLE NOT NULL);

create table duration (
id int primary key auto_increment,
value DOUBLE NOT NULL);

create table temperatures_for_recipes (
id int primary key auto_increment,
recipe_id int NOT NULL,
min_temp_id int NOT NULL,
max_temp_id int NOT NULL,
stage_in_recipe int NOT NULL);

create table humidities_for_recipes (
id int primary key auto_increment,
recipe_id int NOT NULL,
min_humidity_id int NOT NULL,
max_humidity_id int NOT NULL,
stage_in_recipe int NOT NULL);

create table durations_for_recipes (
id int primary key auto_increment,
recipe_id int NOT NULL,
duration_id int NOT NULL,
stage_in_recipe int NOT NULL);

create table suppliers (
id int primary key auto_increment,
name varchar(100) NOT NULL,
is_organic bool NOT NULL DEFAULT 0,
address TEXT,
telephone VARCHAR(15),
email VARCHAR(255),
website TEXT);

create table ingredients (
id int primary key auto_increment,
name varchar(50) NOT NULL,
stock int NOT NULL DEFAULT 0,
supplier_id int NOT NULL);

create table ingredients_for_recipes (
id int primary key auto_increment,
recipe_id int NOT NULL,
ingredient_id int NOT NULL);

create table recipes (
id int primary key auto_increment,
name varchar(255) NOT NULL,
version int NOT NULL DEFAULT 0,
creation_date DATETIME NOT NULL,
special_instructions TEXT,
literature_id int(11),
literature_extra_info text);

create table batches (
id int primary key auto_increment,
recipe_id int not null,
start_date DATETIME NOT NULL,
score int NOT NULL DEFAULT 11,
comments TEXT);

create table logs_for_batches (
id int primary key auto_increment,
batch_id int not null,
last_stage_completed int,
time_last_stage_completed DATETIME,
time_last_alive DATETIME,
error_count int NOT NULL DEFAULT 0
);

create table literature (
  id int primary key auto_increment,
  source_type enum('website', 'book', 'magazine', 'self', 'advice'),
  title text not null,
  author text,
  website_url text
);

-- Example for inserting a new recipe. Note some entries are omitted to be left
-- as their default values or NULL

insert into recipes (name, creation_date) values ("Guanciale", NOW());

insert into literature (source_type, title, author, website_url) values ('book', 'In the Charcuterie', 'Taylor Boetticher', 'www.fattedcalf.com');

insert into suppliers (name, is_organic, address, telephone, email, website) values ('Hugh Grierson', 1, 'New Miln Farm, Tibbermore, Perth, PH1 1QN', '01738730201', 'orders@hughgrierson.co.uk','hughgrierson.co.uk');

insert into ingredients (name, supplier_id) values ('Pork Cheek', 1);

insert into max_temp (value) values ( 4.0);
insert into min_temp (value) values ( 2.0);
insert into max_humidity ( value) values ( 55.0);
insert into min_humidity ( value) values ( 50.0);
insert into duration (value) values ( 14.0);
insert into temperatures_for_recipes (
recipe_id,
min_temp_id,
max_temp_id,
stage_in_recipe
)
values (
  (select max(id) from recipes),
  (select max(id) from min_temp),
  (select max(id) from max_temp),
  0
);

insert into humidities_for_recipes (
recipe_id,
min_humidity_id,
max_humidity_id,
stage_in_recipe
)
values (
  (select max(id) from recipes),
  (select max(id) from min_humidity),
  (select max(id) from max_humidity),
  0
);

insert into durations_for_recipes (
recipe_id,
duration_id,
stage_in_recipe
)
values (
  (select max(id) from recipes),
  (select max(id) from duration),
  0
);


insert into max_temp ( value) values ( 11.0);
insert into min_temp (value) values ( 9.0);
insert into max_humidity ( value) values ( 55.0);
insert into min_humidity (value) values ( 50.0);
insert into duration (value) values ( 21.0);
  insert into temperatures_for_recipes (
  recipe_id,
  min_temp_id,
  max_temp_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from min_temp),
    (select max(id) from max_temp),
    1
  );

  insert into humidities_for_recipes (
  recipe_id,
  min_humidity_id,
  max_humidity_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from min_humidity),
    (select max(id) from max_humidity),
    1
  );

  insert into durations_for_recipes (
  recipe_id,
  duration_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from duration),
    1
  );

insert into max_temp (value) values ( 4.0);
insert into min_temp (value) values ( -4.0);
insert into max_humidity ( value) values ( 65.0);
insert into min_humidity (value) values ( 60.0);
insert into duration (value) values (42.0);
  insert into temperatures_for_recipes (
  recipe_id,
  min_temp_id,
  max_temp_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from min_temp),
    (select max(id) from max_temp),
    2
  );

  insert into humidities_for_recipes (
  recipe_id,
  min_humidity_id,
  max_humidity_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from min_humidity),
    (select max(id) from max_humidity),
    2
  );

  insert into durations_for_recipes (
  recipe_id,
  duration_id,
  stage_in_recipe
  )
  values (
    (select max(id) from recipes),
    (select max(id) from duration),
    2
  );

-- Example for adding a new batch

insert into batches (
recipe_id,
start_date,
score,
comments
)
values
(
  1, NOW(), 5, 'Test 1'
);

insert into batches (
recipe_id,
start_date,
score,
comments
)
values
(
  1, NOW(), 7, 'Test 2'
);

insert into logs_for_batches (
batch_id,
last_stage_completed,
time_last_stage_completed,
time_last_alive,
error_count
)
values
(1, 1, DATE_SUB(NOW(), INTERVAL 2 DAY), NOW(), 1);

insert into logs_for_batches (
batch_id,
last_stage_completed,
time_last_stage_completed,
time_last_alive,
error_count
)
values
(2, 0, DATE_SUB(NOW(), INTERVAL 1.5 DAY), NOW() - INTERVAL 5 MINUTE, 1);

select
recipes.name,
min_temp.value,
max_temp.value,
min_humidity.value,
max_humidity.value,
temperatures_for_recipes.stage_in_recipe
 from recipes left join (temperatures_for_recipes,
humidities_for_recipes,
durations_for_recipes,
min_temp, max_temp,
min_humidity, max_humidity,
duration,
ingredients)
on (recipes.id = temperatures_for_recipes.recipe_id and
temperatures_for_recipes.min_temp_id = min_temp.id and
temperatures_for_recipes.max_temp_id = max_temp.id and
humidities_for_recipes.min_humidity_id = min_humidity.id and
humidities_for_recipes.max_humidity_id = max_humidity.id and
durations_for_recipes.duration_id = duration.id) where
(temperatures_for_recipes.stage_in_recipe = humidities_for_recipes.stage_in_recipe
and temperatures_for_recipes.stage_in_recipe = durations_for_recipes.stage_in_recipe);

select * from recipes left join (ingredients_for_recipes, ingredients, suppliers)
on
(recipes.id = ingredients_for_recipes.id and
ingredients.id = ingredients_for_recipes.ingredient_id and
suppliers.id = ingredients.supplier_id);

select * from recipes left join literature on literature_id = literature.id;

select * from recipes left join (batches, logs_for_batches)
on
(recipes.id = batches.recipe_id and
logs_for_batches.batch_id = batches.id);
