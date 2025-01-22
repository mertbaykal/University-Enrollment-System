# Prepared for Mr. Piotr

from event import ApplicationSentEvent, ApplicationAcceptedEvent, ApplicationRejectedEvent
from queue import CommunicationQueue
from student import Student
from university import University

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
