-- Rank country origin of band by number of funs
-- select origin of band and fun
SELECT origin, SUM(fans) AS nb_fans
       FROM metal_bands
       GROUP BY origin
       ORDER BY SUM(fans) DESC;
