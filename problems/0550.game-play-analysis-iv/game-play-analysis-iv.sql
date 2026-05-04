WITH CTE AS (
    SELECT
        player_id, min(event_date) as event_start_date
    FROM
        Activity
    GROUP BY player_id
)

SELECT
    ROUND(
        (COUNT(DISTINCT c.player_id) / (SELECT COUNT(DISTINCT player_id) FROM activity)),2
    ) AS fraction
FROM
    CTE c
JOIN Activity a
ON c.player_id = a.player_id
AND DATEDIFF(c.event_start_date, a.event_date) = -1