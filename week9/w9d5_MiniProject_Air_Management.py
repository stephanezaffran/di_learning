# Air Management System
# Your goal is to build an airplanes traffic management system.
#
# Your program should rely on four classes: Company, Airplane, Flight and Airport.
#
# Consider every plane can fly only once per day.
#
# Here is a description of those classes:
#
# 0) Company
# Attributes:
#
# id (str) A two letters code
# name (str)
# planes (List of Plane) Every plane that belong to this airlines
from typing import List


class Company:
	def __init__(self, id, name, planes: List = []):
		self.id = id
		self.name = name
		self.planes = planes


# 1) Airplane
# Attributes:
#
# id (int)
# current_location (Airport)
# company (Company) The airlines
# next_flights (List of Flight) Every future flight of the airplane, this list should always be sorted by datetime.
# Methods:


class Airplane:
	def __init__(self, id,  current_location, company, next_flights: List = []):
		self.id = id
		self.current_location = current_location
		self.company = company
		self.next_flights = next_flights

# fly(self, destination)
	def fly(self, destination):
		pass

# location_on_date(self, date) Returns where the plane will be on this date
	def location_on_date(self, date):
		pass

# available_on_date(self, date, location) Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).
	def available_on_date(self, date, location):
		pass


# 2) Flight
# Attributes:
#
# date (datetime.Date)
# destination (Airport) The destination airport.
# origine (Airport) The origine airport.
# plane (Plane)
# id (str) The ID is an encoded string composed of the destination, the airlines code and the date.


class Flight:
	def __init__(self, id, date, destination, origine, plane: Airplane,  ):
		self.id = id
		self.name = name
		self.planes = planes

# Methods (Those methods are here only to update the rest of the system, for example, to change the location of the plane when he arrives):
#
# take_off(self)
	def take_off(self):
		pass


# land(self)
	def land(self):
		pass


# 3) Airport
# Attributes:
#
# city (str) The code of the city where the airport is
# planes (List of Airplane) A list of every plane that is currently in this airport
# scheduled_departures (List of Flight) Every future flight from this airport, sorted by date
# scheduled_arrivals (List of Flight) Every future arrival to this airport, sorted by date

class Airport:
	def __init__(self, city, planes: List[Airplane], scheduled_departures: List = [Flight], scheduled_arrivals: List = [Flight]):
		self.id = id
		self.planes = planes
		self.scheduled_departures = scheduled_departures
		self.scheduled_arrivals = scheduled_arrivals


# schedule_flight(self, destination, datetime) This method finds when an available airplane from an airline that serve the origine and the destination and schedule a flight for it.
	def schedule_flight(self, destination, datetime):
		pass
# info(self, start_date, end_date) Display every scheduled flight from start_date to end_date.
	def  info(self, start_date, end_date):
		pass

# You are free to add any class/method/attribute to
	# code, be sure to document everything you write.



# Write a small code to test your program.