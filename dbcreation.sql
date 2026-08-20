

CREATE TABLE User (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Phone VARCHAR(15),
    DOB DATE,
    Gender VARCHAR(20),
    Residential_Address VARCHAR(255),
    Password VARCHAR(255) NOT NULL
);


CREATE TABLE PoliceStation (
    Station_ID INT AUTO_INCREMENT PRIMARY KEY,
    Station_Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(50),
    Jurisdiction VARCHAR(100),
    Phone VARCHAR(15)
);


CREATE TABLE Police (
    Police_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Badge_Number VARCHAR(30) NOT NULL UNIQUE,
    police_rank VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(15),
    Station_ID INT NOT NULL,

    FOREIGN KEY (Station_ID)
        REFERENCES PoliceStation(Station_ID)
);



CREATE TABLE FIR (
    FIR_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_Number VARCHAR(30) NOT NULL UNIQUE,
    User_ID INT NOT NULL,
    Date_Filed DATE NOT NULL,
    Crime_Type VARCHAR(100) NOT NULL,
    Description TEXT,
    Location VARCHAR(255),
    Jurisdiction VARCHAR(100),
    Status VARCHAR(50) NOT NULL,
    Last_Updated DATE,

    FOREIGN KEY (User_ID)
        REFERENCES User(User_ID)
);



CREATE TABLE Criminal (
    Criminal_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    National_ID VARCHAR(30) UNIQUE,
    Status VARCHAR(50),
    Level_of_Crime VARCHAR(50),
    Aliases VARCHAR(255),
    Living_Status VARCHAR(50)
);


CREATE TABLE FIR_Criminal (
    FIR_ID INT,
    Criminal_ID INT,
    Role VARCHAR(50),
    Accused_Status VARCHAR(50),

    PRIMARY KEY (FIR_ID, Criminal_ID),

    FOREIGN KEY (FIR_ID)
        REFERENCES FIR(FIR_ID),

    FOREIGN KEY (Criminal_ID)
        REFERENCES Criminal(Criminal_ID)
);



CREATE TABLE Investigation (
    Investigation_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_ID INT NOT NULL UNIQUE,
    Police_ID INT NOT NULL,
    Start_Date DATE,
    End_Date DATE,
    Status VARCHAR(50),
    Findings TEXT,
    Chargesheet_Date DATE,
    Remarks TEXT,

    FOREIGN KEY (FIR_ID)
        REFERENCES FIR(FIR_ID),

    FOREIGN KEY (Police_ID)
        REFERENCES Police(Police_ID)
);



CREATE TABLE Evidence (
    Evidence_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_ID INT NOT NULL,
    Evidence_Type VARCHAR(100),
    Description TEXT,
    Collected_Date DATE,
    Storage_Location VARCHAR(255),
    Status VARCHAR(50),
    Collected_By INT NOT NULL,

    FOREIGN KEY (FIR_ID)
        REFERENCES FIR(FIR_ID),

    FOREIGN KEY (Collected_By)
        REFERENCES Police(Police_ID)
);


CREATE TABLE FIR_Status_History (
    History_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_ID INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    Updated_Date DATE NOT NULL,
    Updated_By VARCHAR(100),
    Remarks TEXT,

    FOREIGN KEY (FIR_ID)
        REFERENCES FIR(FIR_ID)
);



CREATE TABLE Court (
    Court_ID INT AUTO_INCREMENT PRIMARY KEY,
    Court_Name VARCHAR(150) NOT NULL,
    Court_Type VARCHAR(50),
    Location VARCHAR(255),
    Judge_Name VARCHAR(100)
);



CREATE TABLE `Case` (
    Case_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIR_ID INT NOT NULL UNIQUE,
    Court_ID INT NOT NULL,
    Case_Number VARCHAR(50) NOT NULL UNIQUE,
    Case_Type VARCHAR(100),
    Filing_Date DATE,
    Status VARCHAR(50),

    FOREIGN KEY (FIR_ID)
        REFERENCES FIR(FIR_ID),

    FOREIGN KEY (Court_ID)
        REFERENCES Court(Court_ID)
);



CREATE TABLE Hearing (
    Hearing_ID INT AUTO_INCREMENT PRIMARY KEY,
    Case_ID INT NOT NULL,
    Hearing_Date DATE NOT NULL,
    Hearing_Time TIME,
    Hearing_Type VARCHAR(100),
    Status VARCHAR(50),
    Next_Hearing_Date DATE,
    Remarks TEXT,

    FOREIGN KEY (Case_ID)
        REFERENCES `Case`(Case_ID)
);

CREATE TABLE Judgment (
    Judgment_ID INT AUTO_INCREMENT PRIMARY KEY,
    Case_ID INT NOT NULL UNIQUE,
    Judgment_Date DATE,
    Decision VARCHAR(100),
    Basis TEXT,
    Sentence TEXT,
    Remarks TEXT,

    FOREIGN KEY (Case_ID)
        REFERENCES `Case`(Case_ID)
);

