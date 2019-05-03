# Project Logs Analysis - Full Stack Nanodegree Program

### Introduction:

This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:
   1. What are the most popular three articles of all time?
   2. Who are the most popular article authors of all time?
   3. On which days did more than 1% of requests lead to errors?

### Installation

1. Install Vagrant and VirtualBox:
    - Install [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
    - Please fork the repository [VM Configuration](https://github.com/SatishDivvi/fullstack-nanodegree-vm) or download **Vagrantfile** from the repository.
    - Open terminal in *Mac* or *Linux* or GitBash in *Windows*. 

    **Note (Windows User only):** _please install [GitBash](https://git-scm.com/downloads) if not installed._

2. Configure Vagrant:
    - Open *GitBash* and `cd` to the directory where you have installed Vagrant.
    - Run command `vagrant up`. **Note:** _This step will take some time if executed for the first time._
    - Run command `vagrant ssh`
    - `cd` to folder _vagrant_ with command `cd vagrant`.

3. How to create the news database:
   - if you are using the Vagrantfile from the repository you have just cloned or used then this step is automated by the Vagrantfile.
   - If virtual machine is not considered by the users then they will need to manually create the news database. They can do so from the psql console by typing `CREATE DATABASE news;`.

4. where to get the newsdata.sql file with the database schema and data.
   - Click the [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to download the zip and extract the **newsdata.sql** file.
   - Move **newsdata.sql** file to the /vagrant folder of your VM if VM is being used.
   - Run the command `psql -d news -f newsdata.sql`

5. You can create views by directly running the command `psql -d news -f create_views.sql`. _Please note that **create_views.sql** must be present in vagrant folder if you are using VM._
6. if you chose to exclude option-3 then enter news database by typing `psql news` and execute below queries:

 
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

