-- list all bands with Glam rock as their main style, ranked by longevity
-- select where syle = "Glam rock"
SELECT band_name, IFNULL(split, YEAR(CURDATE())) - formed AS lifespan
       FROM metal_bands
       WHERE style LIKE '%Glam rock%'
       ORDER BY IFNULL(split, YEAR(CURDATE())) - formed DESC;
