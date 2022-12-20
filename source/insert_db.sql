-- Active: 1668517554814@@127.0.0.1@3306@project
SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT;
SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS;
SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION;
SET NAMES utf8;
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';
SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0;
LOAD DATA LOCAL
-- INFILE 'E:/Couse Materials/CSC 3170/Final proj/Codes/project-wiskey-drunkards/source/data_generation/dataset/user.csv'
INFILE 'source/data_generation/dataset/user.csv'
INTO TABLE user 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/package.csv'
INTO TABLE package 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/state.csv'
INTO TABLE state 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine_type.csv'
INTO TABLE machine_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/plant.csv'
INTO TABLE plant 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine.csv'
INTO TABLE machine 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip_type.csv'
INTO TABLE chip_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SET FOREIGN_KEY_CHECKS = 0;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip.csv'
INTO TABLE chip 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/operation_type.csv'
INTO TABLE operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/operation.csv'
INTO TABLE operation 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/plant_with_package.csv'
INTO TABLE plant_with_package 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/chip_type_with_operation_type.csv'
INTO TABLE chip_type_with_operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
LOAD DATA LOCAL
INFILE 'source/data_generation/dataset/machine_type_with_operation_type.csv'
INTO TABLE machine_type_with_operation_type 
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
SET FOREIGN_KEY_CHECKS = 1;
-- DELETE FROM `machine_type`;
-- DELETE FROM `chip`;
-- DELETE FROM `chip_type`;
SELECT * FROM `chip_type`;
SELECT * FROM `machine`;
SELECT * FROM operation;
