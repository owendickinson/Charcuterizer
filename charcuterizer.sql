CREATE DATABASE charcuterizer;

USE charcuterizer;


CREATE TABLE max_temp (id int PRIMARY KEY auto_increment,
                                          value DOUBLE NOT NULL);


CREATE TABLE min_temp (id int PRIMARY KEY auto_increment,
                                          value DOUBLE NOT NULL);


CREATE TABLE max_humidity (id int PRIMARY KEY auto_increment,
                                              value DOUBLE NOT NULL);


CREATE TABLE min_humidity (id int PRIMARY KEY auto_increment,
                                              value DOUBLE NOT NULL);


CREATE TABLE duration (id int PRIMARY KEY auto_increment,
                                          value DOUBLE NOT NULL);


CREATE TABLE temperatures_for_recipes (id int PRIMARY KEY auto_increment,
                                                          recipe_id int NOT NULL,
                                                                        min_temp_id int NOT NULL,
                                                                                        max_temp_id int NOT NULL,
                                                                                                        stage_in_recipe int NOT NULL);


CREATE TABLE humidities_for_recipes (id int PRIMARY KEY auto_increment,
                                                        recipe_id int NOT NULL,
                                                                      min_humidity_id int NOT NULL,
                                                                                          max_humidity_id int NOT NULL,
                                                                                                              stage_in_recipe int NOT NULL);


CREATE TABLE durations_for_recipes (id int PRIMARY KEY auto_increment,
                                                       recipe_id int NOT NULL,
                                                                     duration_id int NOT NULL,
                                                                                     stage_in_recipe int NOT NULL);


CREATE TABLE suppliers (id int PRIMARY KEY auto_increment,
                                           name varchar(100) NOT NULL,
                                                             is_organic bool NOT NULL DEFAULT 0,
                                                                                              address TEXT, telephone VARCHAR(15),
                                                                                                                      email VARCHAR(255),
                                                                                                                            website TEXT);


CREATE TABLE ingredients (id int PRIMARY KEY auto_increment,
                                             name varchar(50) NOT NULL,
                                                              stock int NOT NULL DEFAULT 0,
                                                                                         supplier_id int NOT NULL);


CREATE TABLE ingredients_for_recipes (id int PRIMARY KEY auto_increment,
                                                         recipe_id int NOT NULL,
                                                                       ingredient_id int NOT NULL);


CREATE TABLE recipes (id int PRIMARY KEY auto_increment,
                                         name varchar(255) NOT NULL,
                                                           VERSION int NOT NULL DEFAULT 0,
                                                                                        creation_date DATETIME NOT NULL,
                                                                                                               special_instructions TEXT, literature_id int(11),
                                                                                                                                                        literature_extra_info text);


CREATE TABLE batches (id int PRIMARY KEY auto_increment,
                                         recipe_id int NOT NULL,
                                                       start_date DATETIME NOT NULL,
                                                                           score int NOT NULL DEFAULT 11,
                                                                                                      comments TEXT);


CREATE TABLE logs_for_batches (id int PRIMARY KEY auto_increment,
                                                  batch_id int NOT NULL,
                                                               last_stage_completed int, time_last_stage_completed DATETIME,
                                                                                         time_last_alive DATETIME,
                                                                                         error_count int NOT NULL DEFAULT 0);


CREATE TABLE literature ( id int PRIMARY KEY auto_increment,
                                             source_type enum('website', 'book', 'magazine', 'self', 'advice'),
                                                         title text NOT NULL,
                                                                    author text, website_url text);

-- Example for inserting a new recipe. Note some entries are omitted to be left
-- as their default values or NULL

INSERT INTO recipes (name, creation_date)
VALUES ("Guanciale",
        NOW());


INSERT INTO literature (source_type, title, author, website_url)
VALUES ('book',
        'In the Charcuterie',
        'Taylor Boetticher',
        'www.fattedcalf.com');


INSERT INTO suppliers (name, is_organic, address, telephone, email, website)
VALUES ('Hugh Grierson',
        1,
        'New Miln Farm, Tibbermore, Perth, PH1 1QN',
        '01738730201',
        'orders@hughgrierson.co.uk',
        'hughgrierson.co.uk');


INSERT INTO ingredients (name, supplier_id)
VALUES ('Pork Cheek',
        1);


INSERT INTO max_temp (value)
VALUES (4.0);


INSERT INTO min_temp (value)
VALUES (2.0);


INSERT INTO max_humidity (value)
VALUES (55.0);


INSERT INTO min_humidity (value)
VALUES (50.0);


INSERT INTO duration (value)
VALUES (14.0);


INSERT INTO temperatures_for_recipes (recipe_id, min_temp_id, max_temp_id, stage_in_recipe)
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_temp),
            (SELECT max(id)
             FROM max_temp), 0);


INSERT INTO humidities_for_recipes (recipe_id, min_humidity_id, max_humidity_id, stage_in_recipe)
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_humidity),
            (SELECT max(id)
             FROM max_humidity), 0);


INSERT INTO durations_for_recipes (recipe_id, duration_id, stage_in_recipe)
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM duration), 0);


INSERT INTO max_temp (value)
VALUES (11.0);


INSERT INTO min_temp (value)
VALUES (9.0);


INSERT INTO max_humidity (value)
VALUES (55.0);


INSERT INTO min_humidity (value)
VALUES (50.0);


INSERT INTO duration (value)
VALUES (21.0);


INSERT INTO temperatures_for_recipes ( recipe_id, min_temp_id, max_temp_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_temp),
            (SELECT max(id)
             FROM max_temp), 1 );


INSERT INTO humidities_for_recipes ( recipe_id, min_humidity_id, max_humidity_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_humidity),
            (SELECT max(id)
             FROM max_humidity), 1 );


INSERT INTO durations_for_recipes ( recipe_id, duration_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM duration), 1 );


INSERT INTO max_temp (value)
VALUES (4.0);


INSERT INTO min_temp (value)
VALUES (-4.0);


INSERT INTO max_humidity (value)
VALUES (65.0);


INSERT INTO min_humidity (value)
VALUES (60.0);


INSERT INTO duration (value)
VALUES (42.0);


INSERT INTO temperatures_for_recipes ( recipe_id, min_temp_id, max_temp_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_temp),
            (SELECT max(id)
             FROM max_temp), 2 );


INSERT INTO humidities_for_recipes ( recipe_id, min_humidity_id, max_humidity_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM min_humidity),
            (SELECT max(id)
             FROM max_humidity), 2 );


INSERT INTO durations_for_recipes ( recipe_id, duration_id, stage_in_recipe )
VALUES (
            (SELECT max(id)
             FROM recipes),
            (SELECT max(id)
             FROM duration), 2 );

-- Example for adding a new batch

INSERT INTO batches (recipe_id, start_date, score, comments)
VALUES ( 1,
         NOW(),
         5,
         'Test 1');


INSERT INTO batches (recipe_id, start_date, score, comments)
VALUES ( 1,
         NOW(),
         7,
         'Test 2');


INSERT INTO logs_for_batches (batch_id, last_stage_completed, time_last_stage_completed, time_last_alive, error_count)
VALUES (1,
        1,
        DATE_SUB(NOW(), INTERVAL 2 DAY),
        NOW(),
        1);


INSERT INTO logs_for_batches (batch_id, last_stage_completed, time_last_stage_completed, time_last_alive, error_count)
VALUES (2,
        0,
        DATE_SUB(NOW(), INTERVAL 1.5 DAY),
        NOW() - INTERVAL 5 MINUTE,
                           1);


SELECT recipes.name,
       min_temp.value,
       max_temp.value,
       min_humidity.value,
       max_humidity.value,
       temperatures_for_recipes.stage_in_recipe
FROM recipes
LEFT JOIN (temperatures_for_recipes,
           humidities_for_recipes,
           durations_for_recipes,
           min_temp,
           max_temp,
           min_humidity,
           max_humidity,
           duration,
           ingredients) ON (recipes.id = temperatures_for_recipes.recipe_id
                            AND temperatures_for_recipes.min_temp_id = min_temp.id
                            AND temperatures_for_recipes.max_temp_id = max_temp.id
                            AND humidities_for_recipes.min_humidity_id = min_humidity.id
                            AND humidities_for_recipes.max_humidity_id = max_humidity.id
                            AND durations_for_recipes.duration_id = duration.id)
WHERE (temperatures_for_recipes.stage_in_recipe = humidities_for_recipes.stage_in_recipe
       AND temperatures_for_recipes.stage_in_recipe = durations_for_recipes.stage_in_recipe);


SELECT *
FROM recipes
LEFT JOIN (ingredients_for_recipes,
           ingredients,
           suppliers) ON (recipes.id = ingredients_for_recipes.id
                          AND ingredients.id = ingredients_for_recipes.ingredient_id
                          AND suppliers.id = ingredients.supplier_id);


SELECT *
FROM recipes
LEFT JOIN literature ON literature_id = literature.id;


SELECT *
FROM recipes
LEFT JOIN (batches,
           logs_for_batches) ON (recipes.id = batches.recipe_id
                                 AND logs_for_batches.batch_id = batches.id);

