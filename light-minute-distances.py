#!/usr/bin/python

import ephem
import datetime

# ideally this would be a config option
years = 5

now = datetime.datetime.now()

planets = list(("Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"))

# convert name to object
for (index, name) in enumerate(planets):
    planets[index] = getattr(ephem, name)(now)

# build a useful constant
lm = ephem.meters_per_au/ephem.c/60 # conversion factor from AU to lightminutes

for planet in planets:
    print "%s: %.2f" % (planet.name, planet.earth_distance*lm)

# previous order
order = list()

# the main loop
i = 0
while (i<365*years):
  next = now+datetime.timedelta(days=i)

  # find distances
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
