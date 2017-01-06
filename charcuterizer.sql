create databse charcuterizer;

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

create table humdidities_for_recipes (
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

create table incredients (
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
  1,
  (select max(id) from min_temp),
  (select max(id) from max_temp),
  0
);

insert into humdidities_for_recipes (
recipe_id,
min_humidity_id,
max_humidity_id,
stage_in_recipe
)
values (
  1,
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
  1,
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
    1,
    (select max(id) from min_temp),
    (select max(id) from max_temp),
    1
  );

  insert into humdidities_for_recipes (
  recipe_id,
  min_humidity_id,
  max_humidity_id,
  stage_in_recipe
  )
  values (
    1,
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
    1,
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
    1,
    (select max(id) from min_temp),
    (select max(id) from max_temp),
    2
  );

  insert into humdidities_for_recipes (
  recipe_id,
  min_humidity_id,
  max_humidity_id,
  stage_in_recipe
  )
  values (
    1,
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
    1,
    (select max(id) from duration),
    2
  );
