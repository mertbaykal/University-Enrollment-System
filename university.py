from event import ApplicationAcceptedEvent, ApplicationRejectedEvent

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
