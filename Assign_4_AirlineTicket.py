""" 4. Create a class that captures airline tickets. Each ticket lists the departure
and arrival cities, a flight number, and a seat assignment.
A seat assignment has both a row and a letter for the seat within the row (such as 12F).
Make two examples of tickets."""

class AirlineTickets:
    i=0
    def __init__(self,departure_city,arrival_city,flight_no,seat_assign):
        AirlineTickets.i+=1
        self.Departure_city=departure_city
        self.Arrival_city=arrival_city
        self.Flight_no=flight_no
        self.Seat_assignment=seat_assign
    def show(self):
        print("Ticket",AirlineTickets.i)

        print("Deparure_city", self.Departure_city)
        print("Arrival_city", self.Arrival_city)
        print("Flight_no", self.Flight_no)
        print("Seat_assignment", self.Seat_assignment)
        print("**********************************".center(50, '*'))
print("Airline Ticket Details".center(50, '*'))
o1=AirlineTickets("Aurangabad","Mumbai",230,"12F")
o1.show()
o2=AirlineTickets("Banglore","Hydrabad",540,"15A")
o2.show()
