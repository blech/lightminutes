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

c = ephem.c
au = ephem.meters_per_au

print "Planet distances, in light-minutes"

i = 0
while (i<104):
  next = now+datetime.timedelta(days=i*7)

  print "\nFor %s\n" % next.isoformat() 

  for planet in (mercury, venus, mars, jupiter, saturn, uranus, neptune):
    planet.compute(next)
    print "%s: %.1f" % (planet.name, planet.earth_distance*au/c/60)

  i += 1
