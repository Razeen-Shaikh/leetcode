# Write your MySQL query statement below
SELECT Signups.user_id,
    IFNULL(
        ROUND(
            SUM(
                CASE
                    WHEN action = 'confirmed' THEN 1
                    ELSE 0
                END
            ) / COUNT(*),
            2
        ),
        0
    ) as confirmation_rate
FROM Signups
    LEFT JOIN Confirmations ON Signups.user_id = Confirmations.user_id
GROUP BY user_id;