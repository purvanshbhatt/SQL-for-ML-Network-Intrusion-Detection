-- data_cleaning.sql

-- No specific cleaning needed for this dataset as it's relatively clean.
-- However, you can add checks for missing values or inconsistencies if required.

-- Example: Check for missing values in the 'service' column
SELECT COUNT(*) FROM network_traffic WHERE N IS NULL;  -- N represents the 'service' column

-- If there are missing values, you can replace them with 'unknown'
UPDATE network_traffic SET N = 'unknown' WHERE N IS NULL;