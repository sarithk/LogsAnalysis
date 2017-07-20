#!/usr/bin/env python3
# Database code for the DB news.

import psycopg2

DBNAME = "news"


def get_article_data():
    """Prints the most popular three articles of all time"""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("""select articles.title as article, count(log.id) as views
                      from log, articles  where log.path = '/article/' ||
                      articles.slug group by articles.title order by views desc
                      limit 3;""")
    print("1. What are the most popular three articles of all time?")
    data = cursor.fetchall()
    for row in data:
            print("%s - %s Views" % (row[0], row[1]))
    print("")
    conn.close()


def get_author_data():
    """Prints the most popular article authors of all time"""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("""select  authors.name as Author, count(log.id) as Views
                      from authors, log, articles  where log.path = '/article/'
                      ||articles.slug and articles.author=authors.id
                      group by authors.name order by Views desc;""")
    print("2. Who are the most popular article authors of all time?")
    data = cursor.fetchall()
    for row in data:
            print("%s - %s Views" % (row[0], row[1]))
    print("")
    conn.close()


def get_error_data():
    """Prints On which days did more than 1% of requests lead to errors"""
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("""select time::date as date, (log.count*100.0) / total
                      .total_count  as error_percentage from log , (select
                      time::date as date, count(id) as total_count from log
                      group by time::date) as total where log.time::date=
                      total.date and log.status like '404%' group by time::date
                      ,total.total_count having (log.count*100.0)/total.
                      total_count > 1 ;""")
    print("3. On which days did more than 1% of requests lead to errors")
    data = cursor.fetchall()
    for row in data:
            print("{0:%B %d, %Y} - {1:.2f}% errors".format(row[0], row[1]))
    conn.close()


if __name__ == '__main__':
    get_article_data()
    get_author_data()
    get_error_data()
