--create your database 
CREATE DATABASE mydata;

SHOW DATABASES;

USE mydata;

--create table in database which is in use
CREATE TABLE `mydata`.`mydata` (
  `Nameoftablets` VARCHAR(45) NOT NULL,
  `Reference_No` VARCHAR(45) not NULL,
  `dose` VARCHAR(45) NULL,
  `Numbersoftablets` VARCHAR(45)  NULL,
  `lot` VARCHAR(45)  NULL,
  `issuedate` VARCHAR(45) NULL,
  `expdate` VARCHAR(45)  NULL,
  `dailydose` VARCHAR(45) NULL,
  `storage` VARCHAR(45) NULL,
  `nhsnumber` VARCHAR(45) NULL,
  `patientname` VARCHAR(45) NULL,
  `DOB` VARCHAR(45) NULL,
  `patientaddress` VARCHAR(45) NULL,
  PRIMARY KEY (`Reference_No`));


--to view table

SELECT * FROM mydata;

