#!/usr/bin/python

from itertools import cycle
import operator
import re
import signal
import sys

class InitiativeOrder:
  def __init__(self, combatants):
    self.initialize_initiative_cycle(combatants)

  def initialize_initiative_cycle(self, combatants):
    self.sorted_initiatives = sorted(combatants.items(), key = operator.itemgetter(1), reverse = True)
    self.initiative_cycle = cycle(range(len(self.sorted_initiatives)))

  def next_combatant(self):
    return self.sorted_initiatives[self.initiative_cycle.next()][0]

class InputReader:
  def read_input(self):
    print "Add combatants. Use an empty value when you're done.\n\n"
    combatants = {}
    while True:
      combatant_input = raw_input("Enter combatant (name [qty] initiative): ")
      if combatant_input:
        combatants.update(self._parse_combatant_input(combatant_input))
      else:
        break
    return combatants

  def _parse_combatant_input(self, combatant_input):
    regex_matcher = re.match(r'^(.+) (\d+) ([0-9]+\.?[0-9]*)$', combatant_input)
    if regex_matcher:
      combatants = {}
      for i in range(int(regex_matcher.group(2))):
        combatants["%s %s" % (regex_matcher.group(1), str(i + 1))] = float(regex_matcher.group(3))
      return combatants
    else:
      regex_matcher = re.match(r'^(.+) ([0-9]+\.?[0-9]*)$', combatant_input)
      return {regex_matcher.group(1): float(regex_matcher.group(2))}

def sigint_handler(signal, frame):
  quit()

def quit():
  print "\n\nBye :)\n"
  sys.exit(0)

if __name__ == '__main__':
  signal.signal(signal.SIGINT, sigint_handler)
  combatants = InputReader().read_input()
  initiative_order = InitiativeOrder(combatants) if combatants else quit()
  
  while True:
    print "\nNow it's %s's turn\n" % initiative_order.next_combatant()
    raw_input("press Enter for next combatant or hit Ctrl+c to leave")

