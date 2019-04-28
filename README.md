# Project Logs Analysis - Full Stack Nanodegree Program

### Introduction:

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
   1. What are the most popular three articles of all time?
   2. Who are the most popular article authors of all time?
   3. On which days did more than 1% of requests lead to errors?

### Installation


1. How to create the news database:
   - if you provide the Vagrantfile supplied by Udacity, this step is automated by the Vagrantfile. Be sure to instruct the user to install Vagrant and VirtualBox, and instruct them on how to start and log into the virtual machine.
   - if your instructions do not depend on the virtual machine, the user will need to manually create the news database. They can do so from the psql console by typing CREATE DATABASE news;.

2. where to get the newsdata.sql file with the database schema and data.
   - Click the [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to download the zip and extract the **newsdata.sql** file.
   - Move **newsdata.sql** file to the /vagrant folder of your VM if VM is being used.
   - Run the command `psql -d news -f newsdata.sql`

3. You can create views by directly running the command `psql -d news -f create_views.sql`. _Please note that **create_views.sql** must be present in vagrant folder if you are using VM_.
4. if you chose to exclude option-3 then enter news database by typing `psql news` and execute below queries:

 
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

### Author

Divvi Naga Venkata Satish - [Portfolio](https://satishdivvi.github.io)

