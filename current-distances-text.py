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
