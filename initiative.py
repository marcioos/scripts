#!/usr/bin/python

from itertools import cycle
import operator
import re

def map_combatant_entry(combatant):
  combatant_entry = {}
  re_matcher = re.match(r'^(.+) (\d+) (\d+)$', combatant)
  if re_matcher:
    for i in range(int(re_matcher.group(2))):
      combatant_entry[re_matcher.group(1) + str(i + 1)] = int(re_matcher.group(3))
  else:
    re_matcher = re.match(r'^(.+) (\d+)$', combatant)
    combatant_entry[re_matcher.group(1)] = int(re_matcher.group(2))
  return combatant_entry


combatants = []
while True:
  combatant = raw_input("Enter combatant (name [qty] initiative): ")
  if (combatant):
    combatants.append(combatant)
  else:
    break

initiatives = {}
for combatant_entry in map(map_combatant_entry, combatants):
  initiatives.update(combatant_entry)

sorted_initiatives = sorted(initiatives.items(), key = operator.itemgetter(1), reverse = True)

initiative_cycle = cycle(range(len(sorted_initiatives)))
while True:
  print "\nNow it's %s's turn\n" % sorted_initiatives[initiative_cycle.next()][0]
  raw_input("press Enter for next")
