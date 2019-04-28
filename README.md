# Project Logs Analysis - Full Stack Nanodegree Program

### Introduction:

In this project we create queries to answer below questions in order to understand the behavior of the users on the news website.
   1. What are the most popular three articles of all time?
   2. Who are the most popular article authors of all time?
   3. On which days did more than 1% of requests lead to errors?

### Installation

Enter news database by typing `psql news`

 - You can either run below queries to create views in news **newsdata.sql** database or run the command `psql -d news -f create_views.sql`

##### View 1 (Top_Viewed_Articles):
#
```sql
CREATE VIEW Top_Viewed_Articles AS select articles.title, count(log.path) AS articlesView 
FROM articles, log 
WHERE log.path = '/article/' || articles.slug 
AND status = '200 OK' 
GROUP BY articles.title 
ORDER BY articlesView desc;
```

##### View 2 (Top_Authors):
#
```sql
CREATE VIEW Top_Authors AS Select authors.name, count(log.path) AS articleViews 
FROM authors, articles, log 
WHERE authors.id = articles.author 
AND log.path = '/article/' || articles.slug 
AND status = '200 OK' 
GROUP BY authors.name 
ORDER BY articleViews DESC;
```

##### View 3 (total_requests):
#
```sql
CREATE VIEW total_requests AS select date(time) AS day, count(status) AS requests 
FROM log 
GROUP BY 1 
ORDER BY 1 DESC;
```

##### View 4 (total_errors):
#
```sql
CREATE VIEW total_errors AS select date(time) AS day, count(status) AS errors 
FROM log 
WHERE status != '200 OK' 
GROUP BY 1 
ORDER BY 1 DESC;
```

##### View 5 (errors_report):
#
```sql
CREATE VIEW errors_report AS 
SELECT total_errors.day, ROUND((100.0 * total_errors.errors / total_requests.requests),2) 
|| '%' AS totalErrorPercentage 
FROM total_errors, total_requests 
WHERE total_errors.day = total_requests.day 
ORDER BY totalErrorPercentage DESC;
```

Exit the database by typing `ctrl+D`.

### Project Execution:

Python file **loganalysis** answers all the three questions as stated in section **_Introduction_**.

- Move the file `loganalysis.py` in /vagrant folder if not done.
- Run command `python loganalysis.py`

### Results Screenshot:

Below results should be displayed after running `python loganalysis.py` and you can also verify your results with the results in **results.txt** file provided:

```
1. What are the most popular three articles of all time?
"Candidate is jerk, alleges rival" article viewed count is 338647.
"Bears love berries, alleges bear" article viewed count is 253801.
"Bad things gone, say good people" article viewed count is 170098.
==========
Who are the most popular article authors of all time?
"Ursula La Multa" article viewed count is 507594.
"Rudolf von Treppenwitz" article viewed count is 423457.
"Anonymous Contributor" article viewed count is 170098.
"Markoff Chaney" article viewed count is 84557.
==========
On which days did more than 1% of requests lead to errors?
"Jul 17 2016" day's error count is 2.26%.
==========
```