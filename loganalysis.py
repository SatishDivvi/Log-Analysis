#!/usr/bin/env python3

# "Database code" for the Log Analysis Report.

import psycopg2


def db_connect():
    """
    Create and return a database connection and cursor.

    The functions creates and returns a database connection and cursor to the
    database defined by DBNAME.
    Returns:
        conn, cur - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    DBNAME = "news"
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    return (conn, cur)


def execute_query(query):
    """
    execute_query returns the results of an SQL query.

    execute_query takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    conn, cursor = db_connect()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def print_top_articles():
    """Print out the top 3 articles of all time."""
    print('1. What are the most popular three articles of all time?')
    query = """Select * from Top_Viewed_Articles limit 3;"""
    results = execute_query(query)
    for article, count in results:
        print('"{}" article viewed count is {}.'.format(article, int(count)))
    print('=' * 10)


def print_top_authors():
    """Print a list of authors ranked by article views."""
    print('Who are the most popular article authors of all time?')
    query = """Select * from Top_Authors;"""
    results = execute_query(query)
    for author, count in results:
        print('"{}" author\'s articles viewed count is {}.'
              .format(author, int(count)))
    print('=' * 10)


def print_errors_over_one():
    """Print out the error report.

    This function prints out the days and that day's error percentage where
    more than 1% of logged access requests were errors.
    """
    print('On which days did more than 1% of requests lead to errors?')
    query = """select to_char(day, 'Mon DD YYYY') as day, totalerrorpercentage
    from errors_report where totalerrorpercentage > '1.0';"""
    results = execute_query(query)
    for day, percentage in results:
        print('"{}" day\'s error count is {}.'.format(day, percentage))
    print('=' * 10)


if __name__ == "__main__":
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
