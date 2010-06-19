#!/usr/bin/python

import ephem
import datetime

now = datetime.datetime.now()

mercury = ephem.Mercury(now)
venus = ephem.Venus(now)
#earth = ephem.Earth(now)
mars = ephem.Mars(now)
jupiter = ephem.Jupiter(now)
saturn = ephem.Saturn(now)
uranus = ephem.Uranus(now)
neptune = ephem.Neptune(now)

planets = (mercury, venus, mars, jupiter, saturn, uranus, neptune)

c = ephem.c
au = ephem.meters_per_au

print "Planet distances, in light-minutes"

changes = list()
order = list()

i = 0
while (i<104):
  next = now+datetime.timedelta(days=i*7)

  [planet.compute(next) for planet in planets]
  distances = sorted([(planet.earth_distance, planet) for planet in planets])

  new_order = [d[1] for d in distances]
  if order != new_order:
      print "Ch ch ch changes!"
      print next.isoformat()
      print order

#   for (index, planet) in enumerate(planets):
#     print "%s %s: %.1f" % (index, planet.name, planet.earth_distance*au/c/60)

  order = new_order

  i += 1
