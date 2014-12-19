#!/usr/bin/python

from itertools import cycle
import operator
import re

class InitiativeOrder:

  def __init__(self, raw_combatant_list):
    self.initialize_initiative_cycle(raw_combatant_list)

  def initialize_initiative_cycle(self, raw_combatant_list):
    initiatives = {}
    for combatant_entry in map(InitiativeOrder._map_combatant_entry, raw_combatant_list):
      initiatives.update(combatant_entry)
    self.sorted_initiatives = sorted(initiatives.items(), key = operator.itemgetter(1), reverse = True)
    self.initiative_cycle = cycle(range(len(self.sorted_initiatives)))

  def print_next_combatant(self):
    print "\nNow it's %s's turn\n" % self.sorted_initiatives[self.initiative_cycle.next()][0]

  @staticmethod
  def _map_combatant_entry(raw_combatant):
    combatant_entry = {}
    re_matcher = re.match(r'^(.+) (\d+) (\d+)$', raw_combatant)
    if re_matcher:
      for i in range(int(re_matcher.group(2))):
        combatant_entry[re_matcher.group(1) + str(i + 1)] = int(re_matcher.group(3))
    else:
      re_matcher = re.match(r'^(.+) (\d+)$', raw_combatant)
      combatant_entry[re_matcher.group(1)] = int(re_matcher.group(2))
    return combatant_entry

def read_input():
  combatants = []
  while True:
    combatant = raw_input("Enter combatant (name [qty] initiative): ")
    if (combatant):
      combatants.append(combatant)
    else:
      break
  return combatants

initiative_order = InitiativeOrder(read_input())

while True:
  initiative_order.print_next_combatant()
  raw_input("press Enter for next")
