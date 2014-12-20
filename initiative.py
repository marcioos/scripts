#!/usr/bin/python

from itertools import cycle
import operator
import re
import signal
import sys

class InitiativeOrder:

  def __init__(self, raw_combatant_list):
    self.initialize_initiative_cycle(raw_combatant_list)

  def initialize_initiative_cycle(self, raw_combatant_list):
    initiatives = {}
    for combatant_entry in map(InitiativeOrder._map_combatant_entry, raw_combatant_list):
      initiatives.update(combatant_entry)
    self.sorted_initiatives = sorted(initiatives.items(), key = operator.itemgetter(1), reverse = True)
    self.initiative_cycle = cycle(range(len(self.sorted_initiatives)))

  def next_combatant(self):
    return self.sorted_initiatives[self.initiative_cycle.next()][0]

  @staticmethod
  def _map_combatant_entry(raw_combatant):
    combatant_entry = {}
    re_matcher = re.match(r'^(.+) (\d+) ([0-9]+\.?[0-9]*)$', raw_combatant)
    if re_matcher:
      for i in range(int(re_matcher.group(2))):
        combatant_entry["%s %s" % (re_matcher.group(1), str(i + 1))] = float(re_matcher.group(3))
    else:
      re_matcher = re.match(r'^(.+) ([0-9]+\.?[0-9]*)$', raw_combatant)
      combatant_entry[re_matcher.group(1)] = float(re_matcher.group(2))
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

def sigint_handler(signal, frame):
  print "\n\nBye :)\n"
  sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, sigint_handler)
  initiative_order = InitiativeOrder(read_input())
  while True:
    print "\nNow it's %s's turn\n" % initiative_order.next_combatant()
    raw_input("press Enter for next combatant")
