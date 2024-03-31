-- A script that lists all cities contained in the database hbtn_0d_usa

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states.name
ON cities.id = states.id
BY ORDER cities.id ASC;
