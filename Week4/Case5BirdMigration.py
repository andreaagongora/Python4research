#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 04:58:06 2020

@author: andrea32
"""
cd Python4Research/Week4

## Introduction to GPS Tracking of Birds

import pandas as pd
birddata = pd.read_csv("bird_tracking.csv")
birddata.info()
birddata.head()

## Simple Data Visualizations

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric"
x , y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize=(10,10))
plt.plot(x,y,".")

bird_names = pd.unique(birddata.bird_name)
bird_names


bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(17,17))
for bird_name in bird_names:  
    ix = birddata.bird_name == bird_name
    x , y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,".", label=bird_name)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")


## Examining Flight Speed

import matplotlib.pyplot as plt
import numpy as np

ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig("hist.pdf")


plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20), normed=True)
plt.xlabel("2D speed (m/s)")
plt.ylabel("Frequency")


birddata.speed_2d.plot(kind='hist', range=[0 , 30])
plt.xlabel("2D speed");
plt.savefig("pd_hist.pdf")

## Using Datetime

birddata.columns
birddata.date_time[0:3]

import datetime
datetime.datetime.today()
time_1 = datetime.datetime.today()
time_2 = datetime.datetime.today()

time_2 - time_1

date_str = birddata.date_time[0]
type(date_str)
date_str

date_str[:-3]

datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

birddata.head()

birddata.timestamp[4] - birddata.timestamp[3]

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]

elapsed_time[0]
elapsed_time[1000]

elapsed_time[1000] / datetime.timedelta(days=1)
elapsed_time[1000] / datetime.timedelta(hours=1)

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed time (days")
plt.savefig("timeplot.pdf")

## Calculating Daily Mean Speed

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)


next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in  enumerate(elapsed_days):
    if t < next_day:
           inds.append(i)
    else:
        # compute mean speed
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)"); 
plt.savefig("dms.pdf")


## Task

data = birddata[birddata.bird_name == "Sanne"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

## Using the Cartopy Library

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')


for name in bird_names:
    ix = birddata['bird_name'] == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name)

plt.legend(loc="upper left")
plt.savefig("map2.pdf")


birddata.head()
grouped_birds = birddata.groupby(['bird_name']).mean()

mean_speeds = grouped_birds.speed_2d
mean_altitudes = grouped_birds.altitude

mean_speeds['Sanne']

b = birddata.date_time
birddata.date_time = pd.DataFrame(b)

birddata_date_time = pd.DataFrame(b)

################## Exercise 2

date = []
for i in range(len(birddata)):
    s = birddata.date_time[i]
    d =s[0:10] 
    date.append(d)

birddata["date"] = date
grouped_bydates = birddata.groupby(['date'])
mean_altitudes_perday =  birddata.groupby(['date']).mean()
mean_altitudes_perday.altitude['2013-09-12']

################## Exercise 3

grouped_birdday2 = birddata.groupby(['date','bird_name']).mean()

mean_altitudes_perday2 = grouped_birdday2.altitude
mean_altitudes_perday2['2013-08-18']

################## Exercise 4

import matplotlib.pyplot as plt

mean_altitudes_perday3 = birddata.groupby(['date']).mean()
mean_altitudes_perday3.columns 
birddata.columns

#tray = grouped_birdday2.groupby(['date'], level='bird_name').mean()
daily_speed = grouped_birdday2.speed_2d
daily_speed['2014-04-04']

#Obtener 
mean_altitudes_perday3.altitude[i]


eric_daily_speed  = # Enter your code here.
sanne_daily_speed = # Enter your code here.
nico_daily_speed  = # Enter your code here.

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()

date[1]

df = pd.DataFrame(date, columns=['date'])
li = pd.unique(df.date)

nico_daily= []
for i in range(len(li)):
    x = li[i]
    nic = daily_speed[x]['Nico']
    nico_daily.append(nic)



data_daily_per_bird = pd.DataFrame(li, columns=['date'])
data_daily_per_bird.set_index("date", inplace=True)
data_daily_per_bird['nico_daily']= nico_daily

data_daily_per_bird.loc['2013-08-15']


