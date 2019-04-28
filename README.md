# Project Logs Analysis - Full Stack Nanodegree Program

### Introduction:

In this project we create queries to answer below questions in order to understand the behavior of the users on the news website.
   1. What are the most popular three articles of all time?
   2. Who are the most popular article authors of all time?
   3. On which days did more than 1% of requests lead to errors?

### Installation

Enter news database by typing `psql news`

Please run below queries in order to create views in news **newsdata.sql** database:

##### View 1 (Top_Viewed_Articles):
#
```
CREATE VIEW Top_Viewed_Articles as  select articles.title, count(log.path) as articlesView from articles, log where log.path like '%' || articles.slug || '%' 
and status = '200 OK' group by articles.title order by articlesView desc;
```

##### View 2 (Top_Authors):
#
```
CREATE VIEW Top_Authors as Select authors.name, count(log.path) as articleViews from authors, articles, log where authors.id = articles.author and 
log.path like '%' || articles.slug || '%' and status = '200 OK' group by authors.name order by articleViews desc;
```

##### View 3 (total_requests):
#
```
CREATE VIEW total_requests as select date(time) as day, count(status) as requests from log group by 1 order by 1 desc;
```

##### View 4 (total_errors):
#
```
CREATE VIEW total_errors as select date(time) as day, count(status) as errors from log where status != '200 OK' group by 1 order by 1 desc;
```

##### View 5 (errors_report):
#
```
CREATE VIEW errors_report as Select total_errors.day, ROUND((100.0 * total_errors.errors / total_requests.requests),2) || '%' as totalErrorPercentage from total_errors, total_requests where 
total_errors.day = total_requests.day order by totalErrorPercentage desc;
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
