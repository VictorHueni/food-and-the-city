UPDATE
    fc_locations
SET
    loc_geography = ST_SetSRID(ST_MakePoint(loc_longitude, loc_latitude), 4326) :: geography
WHERE
    loc_latitude IS NOT NULL
    AND loc_longitude IS NOT NULL;

SELECT
    r. *,
    l. *,
    ST_Distance(
        l.loc_geography,
        ST_MakePoint(-73.98014, 40.575552) :: geography
    ) AS distance
FROM
    fc_restaurants r
    JOIN fc_locations l ON r.res_location_id = l.loc_id
WHERE
    l.loc_geography IS NOT NULL
ORDER BY
    distance ASC
LIMIT
    5;