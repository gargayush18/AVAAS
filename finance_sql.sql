-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema try1
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema try1
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `try1` DEFAULT CHARACTER SET utf8 ;
USE `try1` ;

-- -----------------------------------------------------
-- Table `try1`.`Financial Instituitons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `try1`.`Financial Instituitons` (
  `idFinancial Instituitons` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Location` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFinancial Instituitons`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `try1`.`FinancialCustomers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `try1`.`FinancialCustomers` (
  `idFinancialCustomers` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `category` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFinancialCustomers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `try1`.`TransactionData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `try1`.`TransactionData` (
  `idTransactionData` INT NOT NULL,
  `Date` VARCHAR(45) NOT NULL,
  `Sender` VARCHAR(45) NOT NULL,
  `Reciever` VARCHAR(45) NOT NULL,
  `TransactionDatacol` VARCHAR(45) NULL,
  `Amount` DOUBLE NULL,
  `FinancialCustomers_idFinancialCustomers` INT NOT NULL,
  `Financial Instituitons_idFinancial Instituitons` INT NOT NULL,
  PRIMARY KEY (`idTransactionData`, `FinancialCustomers_idFinancialCustomers`, `Financial Instituitons_idFinancial Instituitons`),
  INDEX `fk_TransactionData_FinancialCustomers1_idx` (`FinancialCustomers_idFinancialCustomers` ASC) VISIBLE,
  INDEX `fk_TransactionData_Financial Instituitons1_idx` (`Financial Instituitons_idFinancial Instituitons` ASC) VISIBLE,
  CONSTRAINT `fk_TransactionData_FinancialCustomers1`
    FOREIGN KEY (`FinancialCustomers_idFinancialCustomers`)
    REFERENCES `try1`.`FinancialCustomers` (`idFinancialCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TransactionData_Financial Instituitons1`
    FOREIGN KEY (`Financial Instituitons_idFinancial Instituitons`)
    REFERENCES `try1`.`Financial Instituitons` (`idFinancial Instituitons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `try1`.`Financial Instituitons_has_FinancialCustomers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `try1`.`Financial Instituitons_has_FinancialCustomers` (
  `Financial Instituitons_idFinancial Instituitons` INT NOT NULL,
  `FinancialCustomers_idFinancialCustomers` INT NOT NULL,
  PRIMARY KEY (`Financial Instituitons_idFinancial Instituitons`, `FinancialCustomers_idFinancialCustomers`),
  INDEX `fk_Financial Instituitons_has_FinancialCustomers_FinancialC_idx` (`FinancialCustomers_idFinancialCustomers` ASC) VISIBLE,
  INDEX `fk_Financial Instituitons_has_FinancialCustomers_Financial _idx` (`Financial Instituitons_idFinancial Instituitons` ASC) VISIBLE,
  CONSTRAINT `fk_Financial Instituitons_has_FinancialCustomers_Financial In`
    FOREIGN KEY (`Financial Instituitons_idFinancial Instituitons`)
    REFERENCES `try1`.`Financial Instituitons` (`idFinancial Instituitons`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Financial Instituitons_has_FinancialCustomers_FinancialCus1`
    FOREIGN KEY (`FinancialCustomers_idFinancialCustomers`)
    REFERENCES `try1`.`FinancialCustomers` (`idFinancialCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
