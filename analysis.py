#! /usr/bin/env python
"PROJECT:-Log analysis"
import psycopg2
import time
database = "news"
portno = 5432
username = "vagrant"
pwd = "vagrant"


def connect():
    return psycopg2.connect(dbname=database, password=pwd,
                            user=username, port=portno)

q121 = ''' select title, loganalysisviews from
udacityloganalysis_articles inner join articles on
articles.slug = udacityloganalysis_articles.loganalysisslug
order by loganalysisviews desc limit 3; '''


def pop_article_3(q121):
    db1 = connect()
    c21 = db1.cursor()
    c21.execute(q121)
    rlt1 = c21.fetchall()
    for i in range(len(rlt1)):
        title = rlt1[i][0]
        views = rlt1[i][1]
        print("%s****%d" % (title, views))
    db1.close()
q211 = '''
    SELECT udacityloganalysis_authors.loganalysisname as at,
    sum(udacityloganalysis_articles.loganalysisviews) as
    loganalysisviews from udacityloganalysis_articles inner join
    udacityloganalysis_authors on udacityloganalysis_authors.
    loganalysisslug=udacityloganalysis_articles.loganalysisslug
    group by udacityloganalysis_authors.loganalysisname order by
    loganalysisviews desc limit 4;
    '''


def pop_authors_4(q211):
    db1 = connect()
    c11 = db1.cursor()
    c11.execute(q211)
    rts21 = c11.fetchall()
    for i in range(len(rts21)):
        name = rts21[i][0]
        views = rts21[i][1]
        print("%s****%d" % (name, views))
    db1.close()


q311 = '''
    select udacityloganalysis_totalfilled.date ,
    (udacityloganalysis_totalfilled.count*100.00*1*1.00 /
    udacityloganalysis_totalerrors.count) as
    per from udacityloganalysis_totalfilled inner join
    udacityloganalysis_totalerrors
    on udacityloganalysis_totalfilled.date =
    udacityloganalysis_totalerrors.date
    and  1<(udacityloganalysis_totalfilled.count*100.00*1*1.00 /
    udacityloganalysis_totalerrors.count)
    order by (udacityloganalysis_totalfilled.count*100.00*1*1.00 /
    udacityloganalysis_totalerrors.count) asc limit 1;
    '''


def error1_1(q311):
    db1 = connect()
    c = db1.cursor()
    c.execute(q311)
    rts22 = c.fetchall()
    for i in range(len(rts22)):
        date = rts22[i][0]
        err_prc = rts22[i][1]
        print("%s****%.1f %%" % (date,  err_prc))

if __name__ == "__main__":
    print("The List of the Most Popular Article:")
    print("-------------------------------------")
    pop_article_3(q121)
    print("\n")
    print("The List of the Popular Authors :")
    print("---------------------------------")
    pop_authors_4(q211)
    print("\n")
    print(" Error :")
    print("------------")
    error1_1(q311)
