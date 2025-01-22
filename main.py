class Event:
    """Parent class for events."""
    def __init__(self, payload):
        self.payload = payload

class ApplicationSentEvent(Event):
    """Event triggered when an application is sent."""
    pass

class ApplicationAcceptedEvent(Event):
    """Event triggered when an application is accepted."""
    pass

class ApplicationRejectedEvent(Event):
    """Event triggered when an application is rejected."""
    pass

class CommunicationQueue:
    """Queue to handle communication between students and universities."""
    def __init__(self):
        self.queue = []

    def add_event(self, event):
        self.queue.append(event)

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {event.__class__.__name__} with payload: {event.payload}")

class Student:
    """Represents a student."""
    def __init__(self, name):
        self.name = name

    def send_application(self, university, queue):
        payload = {
            "student_name": self.name,
            "university_name": university.name,
        }
        event = ApplicationSentEvent(payload)
        queue.add_event(event)
        print(f"{self.name} sent an application to {university.name}.")

class University:
    """Represents a university."""
    def __init__(self, name):
        self.name = name

    def accept_application(self, student, queue):
        payload = {
            "student_name": student.name,
            "university_name": self.name,
            "status": "accepted",
        }
        event = ApplicationAcceptedEvent(payload)
        queue.add_event(event)
        print(f"{self.name} accepted the application from {student.name}.")

    def reject_application(self, student, queue):
        payload = {
            "student_name": student.name,
            "university_name": self.name,
            "status": "rejected",
        }
        event = ApplicationRejectedEvent(payload)
        queue.add_event(event)
        print(f"{self.name} rejected the application from {student.name}.")

# Demonstration
def main():
    queue = CommunicationQueue()

    student = Student("Alice")
    university = University("Tech University")

    # Simulate sending an application
    student.send_application(university, queue)

    # Simulate university decision
    university.accept_application(student, queue)
    # university.reject_application(student, queue)

    # Process all events in the queue
    queue.process_events()

if __name__ == "__main__":
    main()
