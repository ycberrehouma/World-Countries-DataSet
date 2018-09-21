import csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

with open('countries of the world.csv', newline='') as File:

    reader = csv.DictReader(File)
    x=0
    asia_count =0
    eastern_europe_count=0
    western_europe_count = 0
    northern_africa_count = 0
    oceania_count=0
    sub_saharan_africa_count=0
    latin_count=0
    near_east_count=0
    northern_america_count=0
    baltics_count=0
    cw_count=0
    region_list =[]
    population=[]
    regions=[]
    total_population=0
    for row in reader:
        x=x+1

        #print(row['Country'])
        region= row['Region']
        population.append(row['Population'])
        regions.append(row['Region'])
        total_population= int(row['Population']) + total_population
        if region not in region_list:
            region_list.append(region)

    #print (population)
    print (regions)
    print (region_list)
    #print (total_population)
    asia='ASIA'
    eastern_europe='EASTERN'
    western_europe='WESTERN'
    northern_africa='NORTHERN AFRICA'
    oceania='OCEANIA'
    sub_saharan_africa='SUB-SAHARAN'
    latin='LATIN'
    near_east='NEAR EAST '
    cw='C.W.'
    baltics='BALTICS'
    northern_america='NORTHERN AMERICA'
    for i in range(0,len(regions)):
        if asia in regions[i]:
            asia_count+= 1
        if eastern_europe in regions[i]:
            eastern_europe_count+=1
        if western_europe in regions[i]:
            western_europe_count+=1
        if northern_africa in regions[i]:
            northern_africa_count+=1
        if oceania in regions[i]:
            oceania_count += 1
        if sub_saharan_africa in regions[i]:
           sub_saharan_africa_count+=1
        if latin in regions[i]:
           latin_count+=1
        if baltics in regions[i]:
           baltics_count+=1
        if cw in regions[i]:
           cw_count += 1
        if northern_america in regions[i]:
            northern_america_count += 1
        if near_east in regions[i]:
            near_east_count += 1

    print(asia_count)
    print(eastern_europe_count)
    print(western_europe_count)
    print(northern_africa_count)
    print(oceania_count)
    print(sub_saharan_africa_count)
    print(latin_count)
    print(near_east_count)
    print(northern_america_count)
    print(baltics_count)
    print(cw_count)
    #total_countries= asia_count+eastern_europe_count+western_europe_count+northern_africa_count+oceania_count+sub_saharan_africa_count+latin_count+near_east_count+northern_america_count+baltics_count+cw_count
    #print(total_countries)


    print(" Here is the result in percentile:")



'''df = pd.read_csv('countries of the world.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='sample-data-table')'''