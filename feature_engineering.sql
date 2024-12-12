-- feature_engineering.sql
set SQL_SAFE_UPDATES = 0;
-- Calculate the total bytes exchanged in a connection
ALTER TABLE network_traffic ADD COLUMN total_bytes VARCHAR(255);  -- Using VARCHAR to accommodate potential hex values
UPDATE network_traffic SET total_bytes = CAST(H AS DECIMAL) + CAST(I AS DECIMAL);  -- H and I represent 'sbytes' and 'dbytes'

-- Calculate the ratio of bytes sent to bytes received
ALTER TABLE network_traffic ADD COLUMN byte_ratio FLOAT;
UPDATE network_traffic 
SET byte_ratio = CAST(H AS DECIMAL) / CAST(I AS DECIMAL) 
WHERE CAST(I AS DECIMAL) != 0 
AND A = 'some_value';  -- Replace 'some_value' with an appropriate value

-- Create a categorical feature based on connection duration
ALTER TABLE network_traffic ADD COLUMN duration_category VARCHAR(10);
UPDATE network_traffic SET duration_category = 
  CASE 
    WHEN G < 1 THEN 'short'  -- G represents 'dur'
    WHEN G >= 1 AND G < 10 THEN 'medium'
    ELSE 'long'
  END;