-- Optional SQL to populate FIR_Criminal relationships for full demo
-- Run this in MySQL if your FIR_Criminal table is empty:
-- USE crimemanagementsystem;

INSERT IGNORE INTO FIR_Criminal (FIR_ID, Criminal_ID, Role, Accused_Status) VALUES
(1, 1, 'Prime Accused', 'Convicted'), -- The Joker linked to FIR-2026-001 (Theft)
(2, 4, 'Prime Accused', 'Under Investigation'), -- Walter White linked to FIR-2026-002 (Cyber Fraud)
(3, 7, 'Prime Accused', 'Chargesheeted'), -- Hans Gruber linked to FIR-2026-003 (Robbery)
(4, 5, 'Prime Accused', 'Under Investigation'), -- Loki linked to FIR-2026-004 (Assault)
(5, 6, 'Suspect', 'Chargesheeted'), -- Gru linked to FIR-2026-005 (Vehicle Theft)
(6, 2, 'Prime Accused', 'Chargesheeted'), -- Professor Moriarty linked to FIR-2026-006 (Burglary)
(7, 8, 'Prime Accused', 'Under Investigation'), -- Light Yagami linked to FIR-2026-007 (Identity Fraud)
(9, 10, 'Prime Accused', 'Chargesheeted'), -- Cruella De Vil linked to FIR-2026-009 (Forgery)
(10, 9, 'Prime Accused', 'Under Investigation'); -- Tommy Shelby linked to FIR-2026-010 (Corporate Fraud)
