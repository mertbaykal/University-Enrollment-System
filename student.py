from event import ApplicationSentEvent

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
