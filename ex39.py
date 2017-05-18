
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities

cities['OR'] = 'Portland'
cities['NY'] = 'New York'

# print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some state abbreviations
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then city dict

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation

print '-' * 10
for state, abbrev in states.items():
    print "State %s is abbreviated %s" % (state, abbrev)

# print every city in states

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at once

print '-' * 10
for state, abbrev in states.items():
    print "State %s has abbreviation %s, and has city %s" % (state, abbrev, cities[abbrev])

# safely print an abbreviation for a state that might not be there
print '-' * 10
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for state TX is: %s" % city
