import pymysql

from SpareFoodShare.settings import DATABASES
import pandas as pd


def read_data_from_sql():
    # db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='pdP2PEoOZSeiDrm6T280RE6k', db='Food4Share')
    # cursor = db.cursor()
    # cursor.execute('''select * from food''')
    # data = cursor.fetchall()
    # data = pd.DataFrame(list(data))

    con = pymysql.connect(host=DATABASES.get("default").get("HOST"), port=DATABASES.get("default").get("PORT"), user=DATABASES.get("default").get("USER"), passwd=DATABASES.get("default").get("PASSWORD"), db=DATABASES.get("default").get("NAME"),)
    data = pd.read_sql("select * from food", con)

    return data


def cataCount(data):
    cata_cont = data['categories'].value_counts().rename_axis('categories').reset_index(name='count')
    cata = cata_cont["categories"].tolist()
    cont = cata_cont["count"].tolist()
    return cata, cont


def date_OrderCount(data):
    date_cont = data['releaseDate'].value_counts().rename_axis('releaseDate').reset_index(name='count')
    date_cont['releaseDate'] = pd.to_datetime(date_cont['releaseDate'])
    date_cont = date_cont.sort_values(by='releaseDate')
    date_cont.reset_index(inplace=True)
    date = date_cont['releaseDate'].tolist()
    cont = date_cont["count"].tolist()
    return date, cont


def location_infor(data):
    locgrp = data.groupby('location', as_index=False).agg({'price': 'sum', 'quantity': 'sum'})
    loc = locgrp['location'].tolist()
    avgPrice = locgrp['price'].tolist()
    avgQuan = locgrp['quantity'].tolist()
    return loc, avgPrice, avgQuan


def q_infor(data):
    weekdaygrp = data.groupby('releaseDate', as_index=True).agg({'price': 'mean', 'quantity': 'sum'})
    weekdaygrp.index = pd.to_datetime(weekdaygrp.index)
    q = weekdaygrp.resample('q').mean().to_period('q')
    q = q.reset_index()
    Quarterly = q['releaseDate'].tolist()
    avgprice = q['price'].tolist()
    avgquan = q['quantity'].tolist()
    return Quarterly, avgprice, avgquan


def food_interested():
    con = pymysql.connect(host=DATABASES.get("default").get("HOST"), port=DATABASES.get("default").get("PORT"), user=DATABASES.get("default").get("USER"), passwd=DATABASES.get("default").get("PASSWORD"), db=DATABASES.get("default").get("NAME"),)
    totalfoodid = pd.read_sql("select foodID from food", con)['foodID'].tolist()
    interesfoodid = pd.read_sql("select foodID from interests", con)['foodID'].tolist()
    inOrnot = []
    for food in totalfoodid:
        if food in interesfoodid:
            inOrnot.append(1)
        else:
            inOrnot.append(0)
    return [sum(inOrnot) / len(totalfoodid)]


def getTable():
    con = pymysql.connect(host=DATABASES.get("default").get("HOST"), port=DATABASES.get("default").get("PORT"), user=DATABASES.get("default").get("USER"), passwd=DATABASES.get("default").get("PASSWORD"), db=DATABASES.get("default").get("NAME"),)
    data = pd.read_sql("select * from user", con).head(100)
    data.drop(labels={'ID'}, axis=1, inplace=True)
    data.drop(labels={'PassWord'}, axis=1, inplace=True)
    tableName = data.columns.tolist()
    table = data.values
    return tableName, table
