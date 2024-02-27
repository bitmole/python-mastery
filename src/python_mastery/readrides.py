# readrides.py

import csv
from collections import namedtuple

class Ride(object):
    def __init__(self, route, date, daytype, rides):
        self._route = route
        self._date = date
        self._daytype = daytype
        self._rides = rides

class SlotRide(object):
    __slots__ = ['_route', '_date', '_daytype', '_rides']
    def __init__(self, route, date, daytype, rides):
        self._route = route
        self._date = date
        self._daytype = daytype
        self._rides = rides

TupRide = namedtuple('TupRide', ['route', 'date', 'daytype', 'rides'])
        

def read_rides_as_strings(filename):
    """
    Read the bus ride data as a list of strings
    """
    records = []
    with open(filename) as f:
        for row in f:
            records.append(row)
    return records

def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route, date, daytype, rides = row
            rides = int(rides)
            records.append((route, date, daytype, rides))
    return records

def read_rides_as_namedtuples(filename):
    """
    Read the bus ride data as a list of named tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route, date, daytype, rides = row
            rides = int(rides)
            records.append(TupRide(route, date, daytype, rides))
    return records

def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route, date, daytype, rides = row
            record = dict(
                    zip(
                        ('route', 'date', 'daytype', 'rides'), 
                        (route, date, daytype, int(rides))))
            records.append(record)
    return records

def read_rides_as_objects(filename):
    """
    Read the bus ride data as a list of objects
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route, date, daytype, rides = row
            records.append(Ride(route, date, daytype, int(rides)))
    return records

def read_rides_as_slobjects(filename):
    """
    Read the bus ride data as a list of objects with slots
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            route, date, daytype, rides = row
            records.append(SlotRide(route, date, daytype, int(rides)))
    return records

if __name__ == "__main__":
    import sys
    import tracemalloc
    if len(sys.argv) != 3:
        raise SystemExit('usage: readrides filename datastructure[strings, tuples, namedtupes, dicts, objects, slots]')

    callmap = {
            "strings": read_rides_as_strings,
            "tuples": read_rides_as_tuples,
            "namedtuples": read_rides_as_namedtuples,
            "dicts": read_rides_as_dicts,
            "obs": read_rides_as_objects,
            "slobs": read_rides_as_slobjects,
            }

    reader, filename = callmap[sys.argv[2]], sys.argv[1]
    tracemalloc.start()
    rows = reader(filename)
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
