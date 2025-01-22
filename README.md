# University Enrollment System

**Prepared for Mr. Piotr**

This project demonstrates a simplified university enrollment system implemented in Python. The system includes:

1. **Student and University Classes**:
   - `Student`: Represents a student applying to a university.
   - `University`: Represents a university that processes applications.

2. **Event System**:
   - A parent `Event` class with child events like:
     - `ApplicationSentEvent`
     - `ApplicationAcceptedEvent`
     - `ApplicationRejectedEvent`

3. **Communication Queue**:
   - Manages and processes communication events between students and universities.

### File Structure
The project is structured into separate files for modularity:
```
university_enrollment/
│
├── main.py        # Entry point of the application
├── event.py       # Contains Event and its child classes
├── queue.py       # Contains the CommunicationQueue class
├── student.py     # Contains the Student class
└── university.py  # Contains the University class
```

### How It Works
- A student sends an application to a university.
- The university can either accept or reject the application.
- All interactions are logged and processed through a communication queue.

### Running the Code
1. Ensure you have Python installed.
2. Save the files in the appropriate structure as shown above.
3. Run the script:
   ```bash
   python main.py
   ```

The script will simulate a student applying to a university, and the university processing the application.

