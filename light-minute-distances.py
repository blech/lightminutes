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

for planet in (mercury, venus, mars, jupiter, saturn, uranus, neptune):
  print "%s: %.1f light-minutes distant" % (planet.name, planet.earth_distance*au/c/60)
