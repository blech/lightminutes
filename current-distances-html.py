#!/usr/bin/python2.5
# -*- coding: utf-8 -*-
import os, sys, codecs

import datetime

import ephem
from jinja2 import FileSystemLoader, Environment

env = Environment(extensions=['jinja2.ext.loopcontrols'],
                  loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/')))

reload(sys)
sys.setdefaultencoding('utf-8')

# ideally this would be a config option
years = 5

now = datetime.datetime.now()

planets = list(("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"))
symbols = list(('☿', '♀', '♂', '♃', '♄', '♅', '♆'))

# convert name to object
for (index, name) in enumerate(planets):
    planets[index] = getattr(ephem, name)(now)

# build a useful constant
lm = ephem.meters_per_au/ephem.c/60 # conversion factor from AU to lightminutes

output = list()
for (index, planet) in enumerate(planets):
  output.append({'planet': planet, 'distance': planet.earth_distance*lm, 'symbol': symbols[index]});

next = now+datetime.timedelta(days=1)
for hash in output:
  hash['planet'].compute(next)
  hash['tomorrow'] = hash['planet'].earth_distance*lm

  if hash['distance'] > hash['tomorrow']:
    hash['change_symbol'] = '↓'
    hash['change_text'] = 'nearer'
  else:
    if hash['distance'] < hash['tomorrow']:
      hash['change_symbol'] = '↑'
      hash['change_text'] = 'more distant'
    else:
      hash['change_symbol'] = '='
      hash['change_text'] = 'neither nearer nor more distant'

template_values={ 'planets': output, }
# template_values={ 'planets': planets, 'lm': lm, }

template = env.get_template('current_distance.html')
print template.render(template_values).encode('utf8')
