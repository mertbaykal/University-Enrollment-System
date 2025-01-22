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
