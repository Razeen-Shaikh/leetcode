WITH UserRatingCount AS (
    SELECT
        u.name,
        COUNT(*) AS rating_count
    FROM MovieRating mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY u.name
),
TopUser AS (
    SELECT
        name
    FROM UserRatingCount
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
),
FebRatings AS (
    SELECT
        mr.movie_id,
        m.title,
        AVG(mr.rating) AS avg_rating
    FROM MovieRating mr
    JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY mr.movie_id, m.title
),
TopMovie AS (
    SELECT
        title
    FROM FebRatings
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
)

SELECT name AS results FROM TopUser
UNION ALL
SELECT title AS results FROM TopMovie;
