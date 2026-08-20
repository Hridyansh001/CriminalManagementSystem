-- -- UPDATE FIR
-- -- SET Status = 'Investigation Completed',
-- --     Last_Updated = CURDATE()
-- -- WHERE FIR_ID = 2;

-- SELECT *
-- FROM FIR
-- WHERE FIR_ID = 2;


-- UPDATE FIR
-- SET Status = ' Investigation complete',
--     Last_Updated = CURDATE()
-- WHERE FIR_Number = 'FIR-2026-013';

-- SELECT
--     FIR_Number,
--     Crime_Type,
--     Status,
--     Last_Updated
-- FROM FIR
-- WHERE FIR_Number = 'FIR-2026-013';

-- UPDATE FIR
-- SET Crime_Type = 'robbery',
--       Last_Updated=CURDATE()
--     WHERE FIR_Number='FIR-2026-004';

-- SELECT FIR_Number,Crime_Type,Status, Last_Updated
-- FROM FIR WHERE FIR_Number='FIR-2026-004';

-- INSERT INTO FIR_Status_History
-- (FIR_ID,Status,Updated_Date,Updated_By,Remarks )
-- SELECT
--     FIR_ID,
--     'under investigation',
--     CURDATE(),
--     'system',
--     'investigation started for new fir'
-- FROM FIR
-- WHERE FIR_Number='FIR-2026-004';

-- SELECT *
-- FROM FIR_Status_History
-- WHERE FIR_ID = (
--     SELECT FIR_ID
--     FROM FIR
--     WHERE FIR_Number = 'FIR-2026-004'
-- );


-- INSERT INTO FIR_Status_History
-- (FIR_ID,Status,Updated_Date,Updated_By,Remarks)
-- SELECT
--     FIR_ID,
--     'investigation complete',
--     CURDATE(),
--     'police manager',
--     'investigation ended for the fir'
-- FROM FIR
-- WHERE FIR_Number = 'FIR-2026-009';

-- SELECT * from FIR_Status_History WHERE FIR_ID=(select FIR_ID from fir where FIR_Number ='FIR-2026-009' );


-- INSERT INTO FIR_Criminal
-- (FIR_ID, Criminal_ID, Role, Accused_Status)
-- SELECT
--  f.FIR_ID,
--  c.Criminal_ID,
--  'accused',
--  'convicted'

-- from FIR f
-- JOIN Criminal c
--     on c.Name='The Joker'
-- where FIR_Number='FIR-2026-001'

SELECT *
FROM FIR_Criminal
WHERE FIR_ID = (
    SELECT FIR_ID
    FROM FIR
    WHERE FIR_Number = 'FIR-2026-001'
);