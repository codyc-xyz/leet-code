Table: Movies

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
 

Table: Users

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
 

Table: MovieRating

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user''s review date. 
 

Write a solution to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

# Write your MySQL query statement below

WITH MostRatings AS (
    SELECT MovieRating.user_id, name, COUNT(MovieRating.user_id) as num_ratings
    FROM MovieRating
    RIGHT JOIN Users ON Users.user_id = MovieRating.user_id
    GROUP BY MovieRating.user_id
    ORDER BY num_ratings DESC, name ASC
    LIMIT 1
),

HighestRating AS (
    SELECT MovieRating.movie_id, title, created_at, AVG(rating) AS avg_rating
    FROM MovieRating
    RIGHT JOIN Movies ON Movies.movie_id = MovieRating.movie_id
    WHERE SUBSTR(created_at, 1, 7) = "2020-02"
    GROUP BY MovieRating.movie_id
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
)

SELECT name AS results FROM MostRatings
UNION ALL
SELECT title FROM HighestRating;