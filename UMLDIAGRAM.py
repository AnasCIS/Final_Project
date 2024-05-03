class Employee:
    """Represents an Employee with attributes and a manager relationship if applicable."""

    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, managers=None):
        self.name = name  # Employee's full name
        self.employee_id = employee_id  # Unique identifier for the Employee
        self.department = department  # Department where the Employee works
        self.job_title = job_title  # Job title of the Employee
        self.basic_salary = basic_salary  # Basic salary of the Employee
        self.age = age  # Age of the Employee
        self.date_of_birth = date_of_birth  # Date of birth of the Employee
        self.manager = managers  # Manager of this Employee, another Employee object


class Client:
    """Represents a Client who organizes events."""

    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id  # Unique identifier for the Client
        self.name = name  # Client's full name
        self.address = address  # Address of the Client
        self.contact_details = contact_details  # Contact details of the Client
        self.budget = budget  # Budget the Client has for events


class Event:
    """Represents an Event organized for clients at a venue with various suppliers."""

    def __init__(self, event_id, event_type, date, time, duration, clients, venues):
        self.event_id = event_id  # Unique identifier for the Event
        self.event_type = event_type  # Type of the event (e.g., wedding, birthday)
        self.date = date  # Date of the event
        self.time = time  # Time the event starts
        self.duration = duration  # Duration of the event
        self.client = clients  # Association to a Client object
        self.venue = venues  # Association to a Venue object
        self.suppliers = []  # List of Supplier objects involved in the event
        self.guests = []  # List of Guest objects attending the event
        self.event_detail = None  # Detailed aspects of the event, owned exclusively by this Event


class Venue:
    """Venue where events are held."""

    def __init__(self, venue_id, name, address, contact, capacity):
        self.venue_id = venue_id  # Unique identifier for the Venue
        self.name = name  # Name of the venue
        self.address = address  # Address of the venue
        self.contact = contact  # Contact details for the venue
        self.capacity = capacity  # Maximum capacity of the venue


class Supplier:
    """Supplier providing services for events, differentiated by type."""

    def __init__(self, supplier_id, name, service_type, contact_details):
        self.supplier_id = supplier_id  # Unique identifier for the Supplier
        self.name = name  # Name of the supplier
        self.service_type = service_type  # Type of service provided (e.g., catering, cleaning)
        self.contact_details = contact_details  # Contact details of the supplier


class Guest:
    """Guest attending an event."""

    def __init__(self, guest_id, name, contact_details):
        self.guest_id = guest_id  # Unique identifier for the Guest
        self.name = name  # Full name of the guest
        self.contact_details = contact_details  # Contact details of the guest


class EventDetail:
    """Detailed aspects of an event, owned exclusively by an Event."""

    def __init__(self, detail_id, catering_details, decoration_details, furniture_details, entertainment_details):
        self.detail_id = detail_id  # Unique identifier for the Event Detail
        self.catering_details = catering_details  # Details about catering
        self.decoration_details = decoration_details  # Details about decoration
        self.furniture_details = furniture_details  # Details about furniture
        self.entertainment_details = entertainment_details  # Details about entertainment


# Example usage of the classes

# Create some employees
manager = Employee("John Doe", 101, "Sales", "Manager", 50000, 42, "1978-05-2")
salesperson = Employee("Jane Doe", 102, "Sales", "Salesperson", 30000, 35, "1985-10-16", manager)

# Create a client
client = Client("Client1", "Good Client", "1234 Business", "555-0199", 200000)

# Create a venue
venue = Venue("Venue1", "Grand Hall", "5678 Event", "555-0234", 300)

# Create an event
event = Event("Event1", "Wedding", "2021-09-15", "15:00", 8, client, venue)

# Add suppliers and guests
supplier = Supplier("Supplier1", "Top Catering", "Catering", "555-0111")
guest = Guest("Guest1", "Anas", "555-0222")
event.suppliers.append(supplier)
event.guests.append(guest)

# Add event details
event_details = EventDetail("Detail1", "Menu A, Vegetarian Options", "Floral Themes", "Chairs and Tables", "Live Band")
event.event_detail = event_details

# Print some details to showcase
print(f"Event {event.event_id} organized by {event.client.name} at {event.venue.name}")
print(f"Managed by employee {salesperson.manager.name}")
