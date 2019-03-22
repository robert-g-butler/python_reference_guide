
'''
This script contains examples of functions that can be used from the sqlite3
module.
'''

import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('module_sqlite3.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS table_to_plot '
              '(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def enter_data():
    unix = time.time()
    datestamp = datetime.datetime.fromtimestamp(unix)
    datestamp = datestamp.strftime('%Y-%m-%d %H:%M:%S')
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute(
        ('INSERT INTO table_to_plot (unix, datestamp, keyword, value) '
         'VALUES (:unix, :datestamp, :keyword, :value)'),
        {
            'unix': unix, 'datestamp': datestamp,
            'keyword': keyword, 'value': value
        }
    )
    conn.commit()

def read_db(value=0):
    c.execute('SELECT * FROM table_to_plot WHERE value > :value',
              {'value': value})
    for row in c.fetchall():
        print(row[3])

def graph_db():
    c.execute('SELECT unix, value FROM table_to_plot')
    dates = []
    values = []
    for row in c.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    
    plt.plot_date(dates, values, '-')
    plt.show()

def update_db():
    c.execute('UPDATE table_to_plot SET value = 99 WHERE value = 8')
    conn.commit()

    c.execute('SELECT * FROM table_to_plot')
    [print(row) for row in c.fetchall()]

def delete_db_obs():
    c.execute('DELETE FROM table_to_plot WHERE value = 99')
    conn.commit()

    c.execute('SELECT * FROM table_to_plot')
    [print(row) for row in c.fetchall()]



create_table()

for i in range(10):
    enter_data()
    time.sleep(1)

read_db(value=3)

graph_db()

update_db()

delete_db_obs()

c.close()
conn.close()
