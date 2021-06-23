from django.shortcuts import *
from django.http import *
import pandas as pd
import os
from forms import *
import random
import json
def homePage(request):
    return render(request,'homepage.html')

def sasbForm(request):
    print(request.GET)
    data=request.GET.items()
    if len(dict(request.GET.items())) > 0:
        print('I am entered')
        if(os.path.isfile('sasb_data.csv')):
            df = pd.DataFrame(data).T.iloc[1:]
            df.to_csv('sasb_data.csv',mode='a',index = False, header=False)
        else:
            df = pd.DataFrame(data).T
            df.to_csv('sasb_data.csv',index = False, header=False)
    return render(request,'sasb.html')

def griForm(request):
    print(request.GET)
    data=request.GET.items()
    if len(dict(request.GET.items())) > 0:
        print('I am entered')
        if(os.path.isfile('gri_data.csv')):
            df = pd.DataFrame(data).T.iloc[1:]
            df.to_csv('gri_data.csv',mode='a',index = False, header=False)
        else:
            df = pd.DataFrame(data).T
            df.to_csv('gri_data.csv',index = False, header=False)
    return render(request,'gri.html')


def renderingGraph(request):
    df = pd.read_csv('D:/ESG_Prototype/datasets/ESGData.csv')
    df['total_land']=df[(df['Indicator Name']=='Agricultural land (% of land area)')].sum(axis=1)
    barPlot=df[['Country Code','total_land']][(df['Indicator Name']=='Agricultural land (% of land area)')]
    countryCode=barPlot['Country Code'].tolist()
    values=barPlot['total_land'].tolist()
    context={'countryCode':countryCode,'values':values}
    return render(request,'graph.html',context)

def query_view(request):
    if request.method == 'POST':
        form = GriForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('QueryOptions')
            print(query)
            df = pd.read_csv('gri_data.csv')
            countryCode=list(df['year'].values)
            a=[]
            for i in query:
                t=dict()
                t['label']=i
                t['data']=list(df[i].values)
                t['backgroundColor']="rgb({},{},{})".format(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                a.append(t)
            # values=list(df[[query]].values)
            context={'countryCode':countryCode,'form': form,'dataSetRj':a}
    else:
        form = GriForm
        df = pd.read_csv('gri_data.csv')
        countryCode=list(df['year'].values)
        a=[]
        for i in list(df.columns[:-1]):
            t=dict()
            t['label']=i
            t['data']=list(df[i].values)
            t['backgroundColor']="rgb({},{},{})".format(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            a.append(t)
        context={'countryCode':countryCode,'form': form,'dataSetRj':a}

    return render(request,'render_country.html',context)
                             