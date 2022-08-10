-- A script that lists all cities contained in the database hbtn_0d_usa
SELECT C.id,C.name,S.name
FROM cities C
JOIN states S
USING(s.id)
ORDER BY C.id 