-- Active: 1668517554814@@127.0.0.1@3306@project

-- DELETE FROM package;
-- DELETE FROM user;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/user.csv'
INTO TABLE user 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/package.csv'
INTO TABLE package 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/state.csv'
INTO TABLE state 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
SELECT * from state; ----state name not filled
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine_type.csv'
INTO TABLE machine_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/plant.csv'
INTO TABLE plant 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine.csv'
INTO TABLE machine 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip_type.csv'
INTO TABLE chip_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- SET FOREIGN_KEY_CHECKS = 0;

-- DELETE FROM chip;
-- 6 warnings --
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip.csv'
INTO TABLE chip 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/operation_type.csv'
INTO TABLE operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/operation.csv'
INTO TABLE operation 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/operation_with_machine.csv'
INTO TABLE operation_with_machine 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
--- START_TIME ATTRIBUTE NOTE GENERATED
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/plant_with_package.csv'
INTO TABLE plant_with_package 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip_type_with_operation_type.csv'
INTO TABLE chip_type_with_operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine_type_with_operation_type.csv'
INTO TABLE machine_type_with_operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;
-- SET FOREIGN_KEY_CHECKS = 1;
-- DELETE FROM `machine_type`;
-- DELETE FROM `chip`;
-- DELETE FROM `chip_type`;
-- SELECT * FROM `chip_type`;
-- SELECT * FROM `machine`;
-- SELECT * FROM chip;
-- ALTER TABLE machine_type MODIFY COLUMN machine_version varchar(20);