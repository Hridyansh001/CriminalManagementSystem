INSERT INTO User(
    Name,Email,Phone,DOB,Gender,Residential_Address,Password)
values
('burt bargain', 'burt@gmail.com','9811221145','1912-02-29','other','gurgaon','noob@123'),
('Walter White', 'walter@gmail.com', '9811221146', '1958-09-07', 'Male', 'Albuquerque', 'heisenberg@123'),
('Saul Goodman', 'saul@gmail.com', '9811221147', '1960-11-12', 'Male', 'Albuquerque', 'bettercall@123'),
('Tony Stark', 'tony@gmail.com', '9811221148', '1970-05-29', 'Male', 'New York', 'ironman@123'),
('Bruce Wayne', 'bruce@gmail.com', '9811221149', '1972-02-19', 'Male', 'Gotham', 'batman@123'),
('Peter Parker', 'peter@gmail.com', '9811221150', '2001-08-10', 'Male', 'Queens', 'spidey@123'),
('Sherlock Holmes', 'sherlock@gmail.com', '9811221151', '1854-01-06', 'Male', 'London', 'elementary@123'),
('Wednesday Addams', 'wednesday@gmail.com', '9811221152', '2006-10-13', 'Female', 'Nevermore', 'thing@123'),
('Jack Sparrow', 'jack@gmail.com', '9811221153', '1963-06-09', 'Male', 'Port Royal', 'rum@123'),
('Gordon Ramsay', 'gordon@gmail.com', '9811221154', '1966-11-08', 'Male', 'London', 'idiot_sandwich@123');


INSERT INTO Criminal
(Name, National_ID, Status, Level_of_Crime, Aliases, Living_Status)
VALUES
('The Joker', 'NID001', 'Accused', 'High', 'Joker', 'Alive'),
('Professor Moriarty', 'NID002', 'Accused', 'High', 'Napoleon of Crime', 'Alive'),
('Tom Marvolo Riddle', 'NID003', 'Convicted', 'High', 'Lord Voldemort', 'Deceased'),
('Walter White', 'NID004', 'Convicted', 'High', 'Heisenberg', 'Deceased'),
('Loki Laufeyson', 'NID005', 'Accused', 'High', 'Loki', 'Alive'),
('Gru', 'NID006', 'Under Investigation', 'Medium', 'Felonious Gru', 'Alive'),
('Hans Gruber', 'NID007', 'Convicted', 'High', 'Hans', 'Deceased'),
('Light Yagami', 'NID008', 'Under Investigation', 'High', 'Kira', 'Deceased'),
('Tommy Shelby', 'NID009', 'Accused', 'High', 'Thomas Shelby', 'Alive'),
('Cruella De Vil', 'NID010', 'Accused', 'Medium', 'Cruella', 'Alive');

INSERT INTO PoliceStation
(Station_Name, Address, City, Jurisdiction, Phone)
VALUES
('Central City Police Station', 'Downtown Avenue', 'Central City', 'Downtown', '01123450001'),
('Gotham Central Police Station', 'Gotham Central', 'Gotham', 'Central Gotham', '01123450002'),
('Baker Street Police Station', '221B Baker Street', 'London', 'West London', '01123450003'),
('Albuquerque Police Station', 'Central Avenue', 'Albuquerque', 'Central Albuquerque', '01123450004'),
('Queens Police Station', 'Queens Boulevard', 'New York', 'Queens', '01123450005');

INSERT INTO Police
(Name, Badge_Number, Police_Rank, Email, Phone, Station_ID, Password)
VALUES
('Frank Castle', 'raven001', 'scout sniper', 'punisher@police.gov', '9000000001', 1, 'punisher@101'),
('Hank Schrader', 'HS002', 'Inspector', 'hank@police.gov', '9000000002', 1, 'mineral@212'),
('Jim Gordon', 'JG003', 'Commissioner', 'gordon@police.gov', '9000000003', 2, 'gotham@303'),
('L Lawliet', 'LL004', 'Detective', 'l@police.gov', '9000000004', 3, 'kira@404'),
('Sherlock Holmes', 'SH005', 'Inspector', 'sherlock@police.gov', '9000000005', 4, 'elementary@505'),
('John McClane', 'JM006', 'Sergeant', 'mcclane@police.gov', '9000000006', 1, 'yippee@606'),
('Jessica Jones', 'JJ007', 'Detective', 'jessica@police.gov', '9000000007', 2, 'alias@707'),
('Daredevil', 'DD008', 'Inspector', 'daredevil@police.gov', '9000000008', 5, 'hellskitchen@808');

INSERT INTO FIR
(FIR_Number, User_ID, Date_Filed, Crime_Type, Description,
 Location, Jurisdiction, Status, Last_Updated)
VALUES
('FIR-2026-001', 1, '2026-01-10', 'Theft',
 'A rare collection of watches was reported stolen.',
 'Gotham', 'Central Gotham', 'Case Closed', '2026-04-20'),

('FIR-2026-002', 2, '2026-02-15', 'Cyber Fraud',
 'Large cryptocurrency transactions were made without authorization.',
 'Albuquerque', 'Central Albuquerque', 'Under Investigation', '2026-08-15'),

('FIR-2026-003', 3, '2026-03-01', 'Robbery',
 'A jewellery store was robbed during closing hours.',
 'Central City', 'Downtown', 'Case In Court', '2026-07-25'),

('FIR-2026-004', 4, '2026-07-05', 'Assault',
 'Physical assault reported following an argument.',
 'New York', 'Queens', 'Under Investigation', '2026-08-12'),

('FIR-2026-005', 5, '2026-06-10', 'Vehicle Theft',
 'A motorcycle was stolen from a private parking area.',
 'Gotham', 'Central Gotham', 'Investigation Completed', '2026-07-10'),

('FIR-2026-006', 6, '2026-04-14', 'Burglary',
 'A residence was broken into during the night.',
 'London', 'West London', 'Case In Court', '2026-07-30'),

('FIR-2026-007', 7, '2026-07-31', 'Identity Fraud',
 'Personal identity information was allegedly misused.',
 'Nevermore', 'Central City', 'Under Investigation', '2026-08-14'),

('FIR-2026-008', 8, '2026-08-16', 'Piracy',
 'A complaint was filed regarding unauthorized cargo and vessel activity.',
 'Port Royal', 'Downtown', 'FIR Registered', '2026-08-16'),

('FIR-2026-009', 9, '2026-05-19', 'Forgery',
 'Historic documents were allegedly replaced with forged copies.',
 'London', 'West London', 'Case In Court', '2026-07-20'),

('FIR-2026-010', 10, '2026-08-17', 'Corporate Fraud',
 'Company financial records showed suspicious transactions.',
 'New York', 'Queens', 'Under Investigation', '2026-08-17'),

('FIR-2026-011', 4, '2026-08-17', 'Property Dispute',
 'A dispute was reported over ownership of a large estate.',
 'Gotham', 'Central Gotham', 'FIR Registered', '2026-08-17'),

('FIR-2026-012', 6, '2026-08-16', 'Missing Person',
 'A person was reported missing after failing to return home.',
 'Central City', 'Downtown', 'Under Investigation', '2026-08-16');

INSERT INTO Investigation
(FIR_ID, Police_ID, Start_Date, End_Date, Status,
 Findings, Chargesheet_Date, Remarks)
VALUES
(1, 1, '2026-01-11', '2026-03-15', 'Completed',
 'CCTV footage and recovered fingerprints linked the accused to the scene.',
 '2026-03-20',
 'Investigation completed successfully.'),

(2, 2, '2026-02-16', NULL, 'Ongoing',
 'Digital transaction records and cryptocurrency wallets are being investigated.',
 NULL,
 'Cyber forensic analysis in progress.'),

(3, 5, '2026-03-02', '2026-05-15', 'Completed',
 'Security footage and witness statements identified the accused.',
 '2026-05-20',
 'Chargesheet submitted.'),

(4, 8, '2026-07-05', NULL, 'Ongoing',
 'Witness statements have been recorded and medical evidence collected.',
 NULL,
 'Further investigation required.'),

(5, 1, '2026-06-12', '2026-07-05', 'Completed',
 'Vehicle recovered and fingerprints collected from the motorcycle.',
 '2026-07-10',
 'Chargesheet filed.'),

(6, 4, '2026-04-15', '2026-06-20', 'Completed',
 'Forensic evidence connected the accused with the point of entry.',
 '2026-06-25',
 'Case forwarded to court.'),

(7, 3, '2026-08-01', NULL, 'Ongoing',
 'Digital identity records and account activity are being examined.',
 NULL,
 'Cyber investigation continuing.'),

(8, 6, '2026-08-16', NULL, 'Initial Investigation',
 'Cargo records and vessel logs are being verified.',
 NULL,
 'Initial investigation started.'),

(9, 4, '2026-05-20', '2026-06-30', 'Completed',
 'Document analysis identified multiple forged signatures.',
 '2026-07-05',
 'Case forwarded to court.'),

(10, 8, '2026-08-17', NULL, 'Ongoing',
 'Company financial records are being audited.',
 NULL,
 'Financial investigation in progress.'),

(11, 1, '2026-08-17', NULL, 'Initial Investigation',
 'Property ownership documents are being reviewed.',
 NULL,
 'Initial investigation started.'),

(12, 5, '2026-08-16', NULL, 'Ongoing',
 'Last known location and communication records are being examined.',
 NULL,
 'Search operation underway.');



 INSERT INTO Evidence
(FIR_ID, Evidence_Type, Description, Collected_Date,
 Storage_Location, Status, Collected_By)
VALUES
(1, 'CCTV Footage',
 'Security camera footage showing the suspect near the residence.',
 '2026-01-11', 'Locker A-101', 'Verified', 1),

(1, 'Fingerprint',
 'Fingerprint recovered from the display cabinet.',
 '2026-01-12', 'Locker A-102', 'Verified', 1),

(2, 'Bank Statement',
 'Transaction records showing suspicious transfers.',
 '2026-02-17', 'Digital Evidence Server', 'Under Review', 2),

(2, 'Digital Wallet Records',
 'Cryptocurrency wallet transaction history.',
 '2026-02-18', 'Digital Evidence Server', 'Under Review', 2),

(3, 'CCTV Footage',
 'Security footage from the jewellery store.',
 '2026-03-03', 'Locker B-201', 'Verified', 5),

(3, 'Witness Statement',
 'Statement from a store employee.',
 '2026-03-04', 'Evidence Archive', 'Verified', 5),

(4, 'Medical Report',
 'Medical examination report of the complainant.',
 '2026-07-06', 'Evidence Archive', 'Verified', 8),

(5, 'Vehicle Registration Record',
 'Vehicle ownership and recovery documentation.',
 '2026-06-13', 'Locker C-101', 'Verified', 1),

(5, 'Fingerprint',
 'Fingerprint recovered from the motorcycle.',
 '2026-06-14', 'Locker C-102', 'Verified', 1),

(6, 'Forensic Report',
 'Forensic analysis of the burglary entry point.',
 '2026-04-18', 'Evidence Archive', 'Verified', 4),

(6, 'Footprint Analysis',
 'Footprint comparison from the crime scene.',
 '2026-04-19', 'Evidence Archive', 'Verified', 4),

(7, 'Digital Records',
 'Records related to suspected identity misuse.',
 '2026-08-02', 'Digital Evidence Server', 'Under Review', 3),

(8, 'Cargo Manifest',
 'Manifest of cargo associated with the vessel.',
 '2026-08-16', 'Locker D-101', 'Under Review', 6),

(9, 'Document Sample',
 'Original document compared against suspected forgery.',
 '2026-05-22', 'Locker D-201', 'Verified', 4),

(10, 'Financial Records',
 'Company financial statements showing suspicious transfers.',
 '2026-08-17', 'Digital Evidence Server', 'Under Review', 8),

(11, 'Property Deed',
 'Original property ownership document.',
 '2026-08-17', 'Locker E-101', 'Under Examination', 1),

(12, 'Phone Records',
 'Last known communication records of missing person.',
 '2026-08-16', 'Digital Evidence Server', 'Under Review', 5);


 INSERT INTO FIR_Status_History
(FIR_ID, Status, Updated_Date, Updated_By, Remarks)
VALUES

-- FIR 1
(1, 'FIR Registered', '2026-01-10', 'System',
 'FIR successfully registered.'),
(1, 'Investigation Started', '2026-01-11', 'Jim Gordon',
 'Officer assigned and investigation started.'),
(1, 'Evidence Collected', '2026-01-20', 'Jim Gordon',
 'CCTV footage and fingerprints collected.'),
(1, 'Chargesheet Filed', '2026-03-20', 'Jim Gordon',
 'Chargesheet submitted.'),
(1, 'Case In Court', '2026-03-25', 'System',
 'Case transferred to court.'),
(1, 'Case Closed', '2026-04-20', 'Court',
 'Final judgment delivered.'),

-- FIR 2
(2, 'FIR Registered', '2026-02-15', 'System',
 'FIR successfully registered.'),
(2, 'Investigation Started', '2026-02-16', 'Hank Schrader',
 'Cyber investigation initiated.'),
(2, 'Evidence Collected', '2026-02-18', 'Hank Schrader',
 'Digital evidence collected.'),
(2, 'Under Investigation', '2026-08-15', 'Hank Schrader',
 'Additional financial records requested.'),

-- FIR 3
(3, 'FIR Registered', '2026-03-01', 'System',
 'FIR successfully registered.'),
(3, 'Investigation Started', '2026-03-02', 'Frank Castle',
 'Investigation initiated.'),
(3, 'Evidence Collected', '2026-03-04', 'Frank Castle',
 'CCTV and witness evidence collected.'),
(3, 'Chargesheet Filed', '2026-05-20', 'Frank Castle',
 'Chargesheet submitted.'),
(3, 'Case In Court', '2026-06-01', 'System',
 'Case transferred to court.'),

-- FIR 4
(4, 'FIR Registered', '2026-07-05', 'System',
 'FIR successfully registered.'),
(4, 'Investigation Started', '2026-07-05', 'Daredevil',
 'Investigation initiated.'),
(4, 'Evidence Collected', '2026-07-06', 'Daredevil',
 'Medical evidence collected.'),
(4, 'Under Investigation', '2026-08-12', 'Daredevil',
 'Witness statements being reviewed.'),

-- FIR 5
(5, 'FIR Registered', '2026-06-10', 'System',
 'FIR successfully registered.'),
(5, 'Investigation Started', '2026-06-12', 'Jim Gordon',
 'Investigation initiated.'),
(5, 'Evidence Collected', '2026-06-14', 'Jim Gordon',
 'Vehicle and fingerprint evidence collected.'),
(5, 'Investigation Completed', '2026-07-05', 'Jim Gordon',
 'Investigation completed.'),

-- FIR 6
(6, 'FIR Registered', '2026-04-14', 'System',
 'FIR successfully registered.'),
(6, 'Investigation Started', '2026-04-15', 'Sherlock Holmes',
 'Investigation initiated.'),
(6, 'Evidence Collected', '2026-04-19', 'Sherlock Holmes',
 'Forensic evidence collected.'),
(6, 'Chargesheet Filed', '2026-06-25', 'Sherlock Holmes',
 'Chargesheet submitted.'),
(6, 'Case In Court', '2026-07-01', 'System',
 'Case transferred to court.'),

-- FIR 7
(7, 'FIR Registered', '2026-07-31', 'System',
 'FIR successfully registered.'),
(7, 'Investigation Started', '2026-08-01', 'L Lawliet',
 'Digital investigation initiated.'),
(7, 'Under Investigation', '2026-08-14', 'L Lawliet',
 'Digital records still being examined.'),

-- FIR 8
(8, 'FIR Registered', '2026-08-16', 'System',
 'FIR successfully registered.'),
(8, 'Investigation Started', '2026-08-16', 'John McClane',
 'Cargo investigation initiated.'),

-- FIR 9
(9, 'FIR Registered', '2026-05-19', 'System',
 'FIR successfully registered.'),
(9, 'Investigation Started', '2026-05-20', 'Sherlock Holmes',
 'Document investigation initiated.'),
(9, 'Chargesheet Filed', '2026-07-05', 'Sherlock Holmes',
 'Chargesheet submitted.'),
(9, 'Case In Court', '2026-07-20', 'System',
 'Case transferred to court.'),

-- FIR 10
(10, 'FIR Registered', '2026-08-17', 'System',
 'FIR successfully registered.'),
(10, 'Investigation Started', '2026-08-17', 'Daredevil',
 'Financial investigation initiated.'),

-- FIR 11
(11, 'FIR Registered', '2026-08-17', 'System',
 'FIR successfully registered.'),

-- FIR 12
(12, 'FIR Registered', '2026-08-16', 'System',
 'Missing person complaint registered.'),
(12, 'Investigation Started', '2026-08-16', 'Frank Castle',
 'Search operation initiated.'),
(12, 'Under Investigation', '2026-08-17', 'Frank Castle',
 'Search operation continuing.');


 INSERT INTO Court
(Court_Name, Court_Type, Location, Judge_Name)
VALUES
('Gotham District Court', 'District Court', 'Gotham', 'Harvey Dent'),
('Central City District Court', 'District Court', 'Central City', 'Janet van Dyne'),
('Old Bailey', 'Criminal Court', 'London', 'Albus Dumbledore'),
('Albuquerque District Court', 'District Court', 'Albuquerque', 'Saul Goodman');


INSERT INTO `Case`
(FIR_ID, Court_ID, Case_Number, Case_Type, Filing_Date, Status)
VALUES
(1, 1, 'CASE-2026-001', 'Theft', '2026-03-25', 'Closed'),

(3, 2, 'CASE-2026-002', 'Robbery', '2026-06-01', 'Under Trial'),

(6, 3, 'CASE-2026-003', 'Burglary', '2026-07-01', 'Under Trial'),

(9, 3, 'CASE-2026-004', 'Forgery', '2026-07-20', 'Under Trial');


INSERT INTO Hearing
(Case_ID, Hearing_Date, Hearing_Time, Hearing_Type,
 Status, Next_Hearing_Date, Remarks)
VALUES

-- Case 1
(1, '2026-04-05', '10:30:00', 'Evidence Hearing',
 'Completed', '2026-04-20',
 'Evidence presented before the court.'),

(1, '2026-04-20', '11:00:00', 'Judgment Hearing',
 'Completed', NULL,
 'Final judgment delivered.'),

-- Case 2
(2, '2026-06-20', '10:00:00', 'Initial Hearing',
 'Completed', '2026-07-15',
 'Charges read before the accused.'),

(2, '2026-07-15', '10:30:00', 'Evidence Hearing',
 'Completed', '2026-09-10',
 'Witness evidence recorded.'),

(2, '2026-09-10', '10:00:00', 'Final Arguments',
 'Scheduled', NULL,
 'Final arguments scheduled.'),

-- Case 3
(3, '2026-07-20', '11:00:00', 'Initial Hearing',
 'Completed', '2026-08-25',
 'Initial proceedings completed.'),

(3, '2026-08-25', '10:30:00', 'Evidence Hearing',
 'Completed', '2026-09-20',
 'Forensic evidence presented.'),

(3, '2026-09-20', '11:00:00', 'Witness Hearing',
 'Scheduled', NULL,
 'Witness testimony scheduled.'),

-- Case 4
(4, '2026-08-05', '10:00:00', 'Initial Hearing',
 'Completed', '2026-09-05',
 'Initial hearing completed.'),

(4, '2026-09-05', '10:30:00', 'Evidence Hearing',
 'Scheduled', NULL,
 'Property documents to be examined.');



 INSERT INTO Judgment
(Case_ID, Judgment_Date, Decision, Basis, Sentence, Remarks)
VALUES
(1, '2026-04-20',
 'Guilty',
 'CCTV footage, fingerprint evidence and witness testimony established the involvement of the accused.',
 '2 years imprisonment and applicable fine.',
 'Case closed after final judgment.');

INSERT INTO PoliceStation
(Station_Name, Address, City, Jurisdiction, Phone)
VALUES
('Bandra Police Station', 'Hill Road', 'Mumbai', 'Bandra West', '02226400245'),

('Connaught Place Police Station', 'Parliament Street', 'New Delhi', 'Central Delhi', '01123411001'),

('Koramangala Police Station', '80 Feet Road', 'Bengaluru', 'Koramangala', '08025551234'),

('Anna Nagar Police Station', '2nd Avenue', 'Chennai', 'Anna Nagar', '04426152600'),

('Salt Lake Police Station', 'Sector V', 'Kolkata', 'Bidhannagar', '03323343000'),

('Gomti Nagar Police Station', 'Vibhuti Khand', 'Lucknow', 'Gomti Nagar', '05222390900'),

('Koregaon Park Police Station', 'North Main Road', 'Pune', 'Koregaon Park', '02026129777'),

('Sector 17 Police Station', 'Madhya Marg', 'Chandigarh', 'Sector 17', '01722700017');
INSERT INTO Police
(Name, Badge_Number, Police_Rank, Email, Phone, Station_ID, Password)
VALUES
('Arjun Mehta', 'AM009', 'Inspector',
 'arjun.mehta@police.gov', '9000000009', 6, 'arjun@901'),

('Vikram Rathore', 'VR010', 'Sub Inspector',
 'vikram.rathore@police.gov', '9000000010', 7, 'vikram@902'),

('Riya Sharma', 'RS011', 'Inspector',
 'riya.sharma@police.gov', '9000000011', 8, 'riya@903'),

('Aditya Nair', 'AN012', 'Sub Inspector',
 'aditya.nair@police.gov', '9000000012', 9, 'aditya@904'),

('Kavya Iyer', 'KI013', 'Inspector',
 'kavya.iyer@police.gov', '9000000013', 10, 'kavya@905'),

('Rohit Deshmukh', 'RD014', 'Sub Inspector',
 'rohit.deshmukh@police.gov', '9000000014', 11, 'rohit@906'),

('Neha Kapoor', 'NK015', 'Inspector',
 'neha.kapoor@police.gov', '9000000015', 12, 'neha@907'),

('Manish Verma', 'MV016', 'Sub Inspector',
 'manish.verma@police.gov', '9000000016', 13, 'manish@908');
 INSERT INTO Criminal
(Name, National_ID, Status, Level_of_Crime, Aliases, Living_Status)
VALUES
('Kabir Malhotra', 'NID011', 'Accused', 'High', 'Kabir', 'Alive'),

('Devendra Sethi', 'NID012', 'Under Investigation', 'Medium', 'Dev', 'Alive'),

('Aarav Khanna', 'NID013', 'Accused', 'High', 'AK', 'Alive'),

('Raghav Bansal', 'NID014', 'Convicted', 'High', 'Raghu', 'Alive'),

('Ishaan Mehra', 'NID015', 'Under Investigation', 'Medium', 'Ishaan', 'Alive'),

('Nikhil Arora', 'NID016', 'Accused', 'Medium', 'Nik', 'Alive'),

('Sameer Chawla', 'NID017', 'Accused', 'High', 'Sam', 'Alive'),

('Varun Bedi', 'NID018', 'Under Investigation', 'High', 'VB', 'Alive'),

('Manav Kapoor', 'NID019', 'Accused', 'Medium', 'Manav', 'Alive'),

('Yash Tandon', 'NID020', 'Convicted', 'High', 'YT', 'Alive');

INSERT INTO Court
(Court_Name, Court_Type, Location, Judge_Name)
VALUES
('Saket District Court', 'District Court', 'New Delhi', 'Ananya Rao'),

('Tis Hazari Courts', 'District Court', 'New Delhi', 'Rajiv Malhotra'),

('Bombay High Court', 'High Court', 'Mumbai', 'Meera Deshpande'),

('Karnataka High Court', 'High Court', 'Bengaluru', 'Sanjay Iyer'),

('Madras High Court', 'High Court', 'Chennai', 'Lakshmi Krishnan'),

('Calcutta High Court', 'High Court', 'Kolkata', 'Arindam Sen'),

('Allahabad High Court', 'High Court', 'Prayagraj', 'Vivek Tripathi'),

('Punjab and Haryana High Court', 'High Court', 'Chandigarh', 'Harpreet Kaur');

INSERT INTO FIR
(FIR_Number, User_ID, Date_Filed, Crime_Type, Description,
 Location, Jurisdiction, Status, Last_Updated)
VALUES

('FIR-2026-050', 1, '2026-08-18', 'Online Banking Fraud',
 'Unauthorized transactions were reported from the complainant bank account.',
 'Mumbai', 'Bandra West', 'Under Investigation', '2026-08-18'),

('FIR-2026-051', 2, '2026-08-18', 'Vehicle Theft',
 'A car was reported missing from a residential parking area.',
 'New Delhi', 'Central Delhi', 'Under Investigation', '2026-08-18'),

('FIR-2026-015', 3, '2026-08-19', 'Cyber Crime',
 'The complainant reported unauthorized access to an online account.',
 'Bengaluru', 'Koramangala', 'Under Investigation', '2026-08-19'),

('FIR-2026-016', 4, '2026-08-19', 'Chain Snatching',
 'A gold chain was reportedly snatched near a crowded marketplace.',
 'Chennai', 'Anna Nagar', 'FIR Registered', '2026-08-19'),

('FIR-2026-017', 5, '2026-08-20', 'Document Fraud',
 'Suspicious documents were submitted during a property transaction.',
 'Kolkata', 'Bidhannagar', 'Under Investigation', '2026-08-20'),

('FIR-2026-018', 6, '2026-08-20', 'Assault',
 'An altercation outside a commercial establishment resulted in injuries.',
 'Lucknow', 'Gomti Nagar', 'Under Investigation', '2026-08-20'),

('FIR-2026-019', 7, '2026-08-21', 'Burglary',
 'Electronic equipment was reported stolen from a residence.',
 'Pune', 'Koregaon Park', 'Investigation Completed', '2026-08-21'),

('FIR-2026-020', 8, '2026-08-21', 'Fraud',
 'A financial investment scheme was reported by multiple complainants.',
 'Chandigarh', 'Sector 17', 'Case In Court', '2026-08-21');

 INSERT INTO FIR_Criminal
(FIR_ID, Criminal_ID, Role, Accused_Status)
VALUES

(13, 11, 'Primary Accused', 'Under Investigation'),

(14, 12, 'Primary Accused', 'Under Investigation'),

(15, 13, 'Primary Accused', 'Under Investigation'),
(15, 15, 'Co-Accused', 'Under Investigation'),

(16, 14, 'Primary Accused', 'Under Investigation'),

(17, 16, 'Primary Accused', 'Under Investigation'),

(18, 17, 'Primary Accused', 'Under Investigation'),

(19, 18, 'Primary Accused', 'Chargesheet Filed'),

(20, 19, 'Primary Accused', 'Under Trial'),
(20, 20, 'Co-Accused', 'Under Trial');

INSERT INTO Investigation
(FIR_ID, Police_ID, Start_Date, End_Date, Status,
 Findings, Chargesheet_Date, Remarks)
VALUES

(13, 9, '2026-08-18', NULL, 'Ongoing',
 'Bank transaction records and account activity are being examined.',
 NULL,
 'Cyber financial investigation in progress.'),

(14, 10, '2026-08-18', NULL, 'Ongoing',
 'Vehicle registration and CCTV records are being verified.',
 NULL,
 'Vehicle recovery operation underway.'),

(15, 11, '2026-08-19', NULL, 'Ongoing',
 'Login records and device information are being analyzed.',
 NULL,
 'Digital forensic investigation in progress.'),

(16, 12, '2026-08-19', NULL, 'Ongoing',
 'Witness statements and nearby CCTV footage are being examined.',
 NULL,
 'Suspect identification underway.'),

(17, 13, '2026-08-20', NULL, 'Ongoing',
 'Property documents are being verified with available records.',
 NULL,
 'Document verification in progress.'),

(18, 14, '2026-08-20', NULL, 'Ongoing',
 'Witness statements and medical records have been collected.',
 NULL,
 'Further investigation required.'),

(19, 15, '2026-08-21', '2026-08-25', 'Completed',
 'CCTV footage and recovered property linked the accused to the incident.',
 '2026-08-26',
 'Investigation completed and chargesheet prepared.'),

(20, 16, '2026-08-21', NULL, 'Ongoing',
 'Financial transaction records and complainant statements are being examined.',
 NULL,
 'Investigation continuing.');

 INSERT INTO Evidence
(FIR_ID, Evidence_Type, Description, Collected_Date,
 Storage_Location, Status, Collected_By)
VALUES

(13, 'Bank Transaction Records',
 'Records showing unauthorized transfers from the complainant account.',
 '2026-08-18', 'Digital Evidence Server', 'Under Review', 9),

(13, 'Mobile Device',
 'Mobile device submitted for examination of banking activity.',
 '2026-08-18', 'Locker F-101', 'Under Examination', 9),

(14, 'CCTV Footage',
 'Parking area footage showing the vehicle before it was reported missing.',
 '2026-08-18', 'Evidence Archive', 'Under Review', 10),

(14, 'Vehicle Registration Record',
 'Vehicle ownership and registration documents.',
 '2026-08-19', 'Locker F-102', 'Verified', 10),

(15, 'Login Records',
 'Digital records showing unauthorized account access.',
 '2026-08-19', 'Digital Evidence Server', 'Under Review', 11),

(15, 'Computer Device',
 'Computer device submitted for forensic examination.',
 '2026-08-20', 'Locker F-103', 'Under Examination', 11),

(16, 'CCTV Footage',
 'Street footage recorded near the reported incident.',
 '2026-08-19', 'Locker F-104', 'Under Review', 12),

(17, 'Property Documents',
 'Documents submitted during the disputed property transaction.',
 '2026-08-20', 'Locker F-105', 'Under Examination', 13),

(18, 'Medical Report',
 'Medical examination report of the injured complainant.',
 '2026-08-20', 'Evidence Archive', 'Verified', 14),

(19, 'Fingerprint',
 'Fingerprint evidence recovered from the residence.',
 '2026-08-21', 'Locker F-106', 'Verified', 15),

(19, 'CCTV Footage',
 'Security footage showing movement near the residence.',
 '2026-08-21', 'Locker F-107', 'Verified', 15),

(20, 'Financial Records',
 'Records showing suspicious investment-related transactions.',
 '2026-08-21', 'Digital Evidence Server', 'Under Review', 16);

 INSERT INTO FIR_Status_History
(FIR_ID, Status, Updated_Date, Updated_By, Remarks)
VALUES

-- FIR 13
(13, 'FIR Registered', '2026-08-18', 'System',
 'FIR successfully registered.'),

(13, 'Investigation Started', '2026-08-18', 'Arjun Mehta',
 'Banking fraud investigation initiated.'),

(13, 'Evidence Collected', '2026-08-18', 'Arjun Mehta',
 'Bank records and mobile device collected.'),

-- FIR 14
(14, 'FIR Registered', '2026-08-18', 'System',
 'Vehicle theft FIR registered.'),

(14, 'Investigation Started', '2026-08-18', 'Vikram Rathore',
 'Vehicle theft investigation initiated.'),

(14, 'Evidence Collected', '2026-08-19', 'Vikram Rathore',
 'CCTV and vehicle records collected.'),

-- FIR 15
(15, 'FIR Registered', '2026-08-19', 'System',
 'Cyber crime FIR registered.'),

(15, 'Investigation Started', '2026-08-19', 'Riya Sharma',
 'Digital investigation initiated.'),

(15, 'Evidence Collected', '2026-08-20', 'Riya Sharma',
 'Digital devices and login records collected.'),

-- FIR 16
(16, 'FIR Registered', '2026-08-19', 'System',
 'Chain snatching complaint registered.'),

(16, 'Investigation Started', '2026-08-19', 'Aditya Nair',
 'Investigation initiated.'),

-- FIR 17
(17, 'FIR Registered', '2026-08-20', 'System',
 'Document fraud FIR registered.'),

(17, 'Investigation Started', '2026-08-20', 'Kavya Iyer',
 'Document verification initiated.'),

-- FIR 18
(18, 'FIR Registered', '2026-08-20', 'System',
 'Assault FIR registered.'),

(18, 'Investigation Started', '2026-08-20', 'Rohit Deshmukh',
 'Investigation initiated.'),

-- FIR 19
(19, 'FIR Registered', '2026-08-21', 'System',
 'Burglary FIR registered.'),

(19, 'Investigation Started', '2026-08-21', 'Neha Kapoor',
 'Burglary investigation initiated.'),

(19, 'Evidence Collected', '2026-08-21', 'Neha Kapoor',
 'Fingerprint and CCTV evidence collected.'),

(19, 'Investigation Completed', '2026-08-25', 'Neha Kapoor',
 'Investigation completed successfully.'),

(19, 'Chargesheet Filed', '2026-08-26', 'Neha Kapoor',
 'Chargesheet submitted to the appropriate authority.'),

-- FIR 20
(20, 'FIR Registered', '2026-08-21', 'System',
 'Financial fraud FIR registered.'),

(20, 'Investigation Started', '2026-08-21', 'Manish Verma',
 'Financial investigation initiated.');

 INSERT INTO `Case`
(FIR_ID, Court_ID, Case_Number, Case_Type, Filing_Date, Status)
VALUES

(19, 11, 'CASE-2026-005', 'Burglary',
 '2026-08-27', 'Under Trial'),

(20, 12, 'CASE-2026-006', 'Financial Fraud',
 '2026-08-28', 'Under Trial');

 INSERT INTO Hearing
(Case_ID, Hearing_Date, Hearing_Time, Hearing_Type,
 Status, Next_Hearing_Date, Remarks)
VALUES

(5, '2026-09-05', '10:30:00', 'Initial Hearing',
 'Scheduled', '2026-09-25',
 'Initial proceedings for burglary case.'),

(5, '2026-09-25', '11:00:00', 'Evidence Hearing',
 'Scheduled', NULL,
 'CCTV and fingerprint evidence to be presented.'),

(6, '2026-09-08', '10:00:00', 'Initial Hearing',
 'Scheduled', '2026-09-29',
 'Initial proceedings for financial fraud case.'),

(6, '2026-09-29', '10:30:00', 'Evidence Hearing',
 'Scheduled', NULL,
 'Financial records and transaction evidence to be examined.');