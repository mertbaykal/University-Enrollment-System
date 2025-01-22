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
