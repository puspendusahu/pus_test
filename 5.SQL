
-- SQL QuesƟons (20 minutes)
-- 5. Database Schema and Query (10 minutes)
-- Task:
-- Design a database schema for a Blog System from scratch.
-- Tables:
--  Users: user_id, name, email.
--  Posts: post_id, user_id, Ɵtle, content, created_at.
--  Comments: comment_id, post_id, user_id, comment_text, created_at. 

-- Write SQL queries to:
-- 1. Fetch the top 5 most recent posts along with the number of comments for each post.
-- 2. Find all users who haven’t wriƩen any posts.

-- create tables for user
CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- create tables for post
CREATE TABLE post (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(255),
    content TEXT NOT NULL,
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);


-- create tables for comment
CREATE TABLE comment (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at DATETIME,
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- 1. Fetch the top 5 most recent posts along with the number of comments for each post.
SELECT p.post_id, p.title, p.content, p.created_at, COUNT(c.comment_id) AS comment_count
FROM post p
LEFT JOIN comment c ON p.post_id = c.post_id
GROUP BY p.post_id
ORDER BY p.created_at DESC
LIMIT 5;

-- 2. Find all users who haven’t wriƩen any posts.
SELECT u.user_id, u.name, u.email
FROM user u
LEFT JOIN post p ON u.user_id = p.user_id
WHERE p.post_id IS NULL;
