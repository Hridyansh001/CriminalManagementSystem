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
(Name, Badge_Number, Police_Rank, Email, Phone, Station_ID)
VALUES
('Frank Castle', 'raven001', 'scout sniper', 'punisher@police.gov', '9000000001', 1),
('Hank Schrader', 'HS002', 'Inspector', 'hank@police.gov', '9000000002', 1),
('Jim Gordon', 'JG003', 'Commissioner', 'gordon@police.gov', '9000000003', 2),
('L Lawliet', 'LL004', 'Detective', 'l@police.gov', '9000000004', 3),
('Sherlock Holmes', 'SH005', 'Inspector', 'sherlock@police.gov', '9000000005', 4),
('John McClane', 'JM006', 'Sergeant', 'mcclane@police.gov', '9000000006', 1),
('Jessica Jones', 'JJ007', 'Detective', 'jessica@police.gov', '9000000007', 2),
('Daredevil', 'DD008', 'Inspector', 'daredevil@police.gov', '9000000008', 5);

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