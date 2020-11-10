-- SQLite

-- TO list all tables
-- SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';
-- To select all from blog_blog table
-- SELECT * FROM 'blog_blog' LIMIT 0,30;

SELECT * from portfolio_project WHERE id=2;
-- UPDATE portfolio_project SET url='https://www.facebook.com' WHERE id=2;