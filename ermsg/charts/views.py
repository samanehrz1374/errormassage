from multiprocessing import context
from django.shortcuts import render
from .models import mychart,VolDatabase
import pandas as pd
from datetime import datetime
import time
import sqlite3


# Create your views here.
def charts(request):
    chart=mychart.objects.all().values()
    df=pd.DataFrame(chart)
    df1=df.name.tolist()
    df=df['rank'].tolist()

    # df1=['blue','pink']
    # df=[10,30]

    mydict={
        'df':df,
        'df1':df1
    }

    return render(request,'charts/charts.html',context=mydict)

def db(request):
    charts=VolDatabase.objects.all().values()
    # df=time.time()
    # df1=datetime.fromtimestamp(df)
    # Df=VolumeTable.objects.get('created_at').values()
    # times=datetime.fromtimestamp(df)

    context={
        'results':charts,
        # 'df':df,
        # 'df1':df1
    }
    return render(request,'charts/db.html',context)
    



# def db(request):
#     conn = sqlite3.connect("vol_database.db")
#     try:
#         cur = conn.cursor()
#         # cur.execute("delete from volume_table where date = ''; ")
#         cur.execute("select * from volume_table;")
#         results = cur.fetchall()
#     finally:
#         conn.close()
#     context={
#         "results": results
#     }
#     return render(request,'charts/db.html',context)
#     # return render(request,'charts/db.html',{})

