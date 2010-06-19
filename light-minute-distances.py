#!/usr/bin/python

import ephem
import datetime

now = datetime.datetime.now()

planets = list(("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"))

# convert name to object
for (index, name) in enumerate(planets):
    planets[index] = getattr(ephem, name)()
    
lm = ephem.meters_per_au/ephem.c/60 # conversion factor from AU to lightminutes

order = list()

years = 5

i = 0
while (i<365*years):
  next = now+datetime.timedelta(days=i)

  [planet.compute(next) for planet in planets]
  distances = sorted([(planet.earth_distance*lm, planet) for planet in planets])

  new_order = [d[1] for d in distances]
  if order != new_order:
      print "%02i-%02i-%02i" % (next.year, next.month, next.day)
      
      for (distance, planet) in distances[:3]:
          print "%s - %.2f" % (planet.name, distance)

      print ""

  order = new_order

  i += 1
