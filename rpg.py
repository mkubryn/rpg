import sys,random

who = sys.stdin.readline().split()

print 'Wygrywa: %s' % random.choice(who)
