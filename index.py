#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
import os, sys, codecs

import ephem
import datetime

import os, sys, codecs

from jinja2 import FileSystemLoader, Environment

env = Environment(extensions=['jinja2.ext.loopcontrols'],
                  loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/')))

# ideally this would be a config option
years = 3

now = datetime.datetime.now()

planets = list(("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"))
symbols = list(('☿', '♀', '♂', '♃', '♄', '♅', '♆'))

chart_list = list(("Mercury", "Venus", "Mars"))
chart_data = []

# convert names to objects
for (index, name) in enumerate(planets):
    planets[index] = getattr(ephem, name)(now)
for (index, name) in enumerate(chart_list):
    chart_list[index] = getattr(ephem, name)(now)


# build a useful constant
lm = (ephem.meters_per_au/ephem.c)/60 # conversion factor from AU to lightminutes

# get the current distance list
by_distance = list()
for (index, planet) in enumerate(planets):
  by_distance.append({'planet': planet, 
                      'distance': planet.earth_distance*lm, 
                      'km': int(planet.earth_distance*ephem.meters_per_au/1000),
                      'symbol': symbols[index]})

by_distance = sorted(by_distance)

# the chart loop
i = -60
while (i<365*years):
  next = now+datetime.timedelta(days=i)

  row = []
  row.append(next.strftime("%Y-%m-%d"))
  
  # add to chart data
  for (index, planet) in enumerate(chart_list):
    planet.compute(next)
    row.append(planet.earth_distance*lm)

  chart_data.append(row)

  i += 2

# previous order
order = list()
changes = list()

# the change loop
i = 0
while (len(changes) < 3):
  next = now+datetime.timedelta(days=i)

  # find distances
  [planet.compute(next) for planet in planets]
  distances = sorted([(planet.earth_distance*lm, planet) for planet in planets])

  new_order = [d[1] for d in distances]
  if (order and order != new_order):
    changes.append({'date': next.strftime("%Y-%m-%d"), 'planets': distances[:3], })
      
  order = new_order
  i += 1

template_values={ 'chart_data': chart_data, 
                  'chart_list': chart_list, 
                  'by_distance': by_distance, 
                  'changes': changes,
                }

template = env.get_template('index.html')
print template.render(template_values).encode('utf8')

