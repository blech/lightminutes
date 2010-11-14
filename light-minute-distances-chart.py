#!/usr/bin/python2.5

import ephem
import datetime

import os, sys, codecs

from jinja2 import FileSystemLoader, Environment

env = Environment(extensions=['jinja2.ext.loopcontrols'],
                  loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/')))

# ideally this would be a config option
years = 5

now = datetime.datetime.now()

planets = list(("Sun", "Mercury", "Venus", "Mars")) #, "Jupiter", "Saturn", "Uranus", "Neptune"))
chart_data = [];

# convert name to object
for (index, name) in enumerate(planets):
    planets[index] = getattr(ephem, name)(now)

# build a useful constant
lm = (ephem.meters_per_au/ephem.c)/60 # conversion factor from AU to lightminutes

# the main loop
i = -60;
while (i<365*years):
  next = now+datetime.timedelta(days=i)

  row = []
  row.append(next.strftime("%Y-%m-%d"));
  
  # add to chart data
  for (index, planet) in enumerate(planets):
    planet.compute(next)
    row.append(planet.earth_distance*lm)

  chart_data.append(row)

  i += 2

template_values={ 'chart_data': chart_data, }
# template_values={ 'planets': planets, 'lm': lm, }

template = env.get_template('distance-time.html')
print template.render(template_values).encode('utf8')

