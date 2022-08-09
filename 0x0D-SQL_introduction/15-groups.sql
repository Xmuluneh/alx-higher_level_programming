-- A script lists the number with the same recorde
SELECT score,COUNT(*) AS number FROM second_table GROUP By score ORDER BY number DESC