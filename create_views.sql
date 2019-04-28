-- View 1 (Top_Viewed_Articles)

CREATE VIEW Top_Viewed_Articles AS select articles.title, count(log.path) AS articlesView 
FROM articles, log 
WHERE log.path = '/article/' || articles.slug 
AND status = '200 OK' 
GROUP BY articles.title 
ORDER BY articlesView desc;

-- View 2 (Top_Authors):

CREATE VIEW Top_Authors AS Select authors.name, count(log.path) AS articleViews 
FROM authors, articles, log 
WHERE authors.id = articles.author 
AND log.path = '/article/' || articles.slug 
AND status = '200 OK' 
GROUP BY authors.name 
ORDER BY articleViews DESC;

-- View 3 (total_requests):

CREATE VIEW total_requests AS select date(time) AS day, count(status) AS requests 
FROM log 
GROUP BY 1 
ORDER BY 1 DESC;

-- View 4 (total_errors):

CREATE VIEW total_errors AS select date(time) AS day, count(status) AS errors 
FROM log 
WHERE status != '200 OK' 
GROUP BY 1 
ORDER BY 1 DESC;

-- View 5 (errors_report):

CREATE VIEW errors_report AS 
SELECT total_errors.day, ROUND((100.0 * total_errors.errors / total_requests.requests),2) 
|| '%' AS totalErrorPercentage 
FROM total_errors, total_requests 
WHERE total_errors.day = total_requests.day 
ORDER BY totalErrorPercentage DESC;

