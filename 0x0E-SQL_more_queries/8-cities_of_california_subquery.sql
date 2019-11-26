-- Cities of California
--
SELECT cities.id, cities.name FROM cities 
WHERE state_id =(
SELECT state_id FROM states WHERE name = "California")
ORDER by id ASC;
