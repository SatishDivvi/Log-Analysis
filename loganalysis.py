# "Database code" for the Log Analysis Report.

import psycopg2

"""Return all posts from the 'database', most recent first."""
DBNAME = "news"
conn = psycopg2.connect(database=DBNAME)
cur = conn.cursor()
print('1. What are the most popular three articles of all time?')
# query1 is for the most popular three articles.
query1 = "Select * from Top_Viewed_Articles limit 3;"
cur.execute(query1)
result = cur.fetchall()
for article, count in result:
  print('"{}" article viewed count is {}.'.format(article,int(count)))
print('=' * 10)
print('Who are the most popular article authors of all time?')
# query2 is for the top authors based on article views from the logs.
query2 = "Select * from Top_Authors;"
cur.execute(query2)
result = cur.fetchall()
for author, count in result:
  print('"{}" article viewed count is {}.'.format(author,int(count)))
print('=' * 10)
print('On which days did more than 1% of requests lead to errors?')
# query3 is for the days which have errors i.e. not 200 OK status greater than 1%.
query3 = "select to_char(day, 'Mon DD YYYY') as day, totalerrorpercentage from errors_report where totalerrorpercentage > '1.0';"
cur.execute(query3)
result = cur.fetchall()
for day, percentage in result:
  print('"{}" day\'s error count is {}.'.format(day,percentage))
print('=' * 10)
conn.close()









