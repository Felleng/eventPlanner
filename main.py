#
import datetime

print(
    "Hi. Welcome to Planner, a python application that allows you to plan ahead."
    "\nTo get started, enter one of the options below:\n")


# Creating an event class with a constructor that takes in title, description, date and time parameters
class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        self.time = datetime.datetime.strptime(time, '%H:%M').time()

    def __str__(self):
        return f"{self.title}  \n{self.description} \n{self.date}  \n{self.time}"


class Planner:
    def __init__(self):
        self.events = []  # storage in a list

    def add_event(self, title, description, date, time):
        if not all(isinstance(x, str) for x in [title, description, date, time]):
            print("Invalid input! Please try again.\n")
            return
            # If the input of all the parameters is not in string format, display an error message

        try:
            event = Event(title, description, date, time)
            self.events.append(event)  # append function add the created event to the list.
            self.events.sort(key=lambda x: (x.date, x.time))  # sort events after they are added to the list
            print("Event added successfully.\n")

        except ValueError:
            print("Invalid date or time format.\n")

# A search function to search for events by title
    def search(self, title):
        for event in self.events: # Loops through the events list to find event with matching title to one in the search
            if title == event.title:
                print(event)

        print("Event not found")

# A function to view all events
    def view(self):
        if not self.events:
            print("No events scheduled.\n")
            return
        for event in self.events:
            print(event)  # Print the events found in the events list
#A function to delete an event
    def delete(self, title):
        try:
            event_index = next(i for i, x in enumerate(self.events) if x.title == title)
            del self.events[event_index]
            print("Event deleted!\n")
        except StopIteration:
            print("No event with this title exists.\n")

# A function to edit details of an event, does not edit the title
    def edit_event(self, title, description=None, date=None, time=None):
        for i, event in enumerate(self.events):
            if event.title == title:
                if description:
                    event.description = description

                if date:
                    event.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()

                if time:
                    event.time = datetime.datetime.strptime(time, '%H:%M').time()

                self.events[i] = event
                self.events.sort(key=lambda x: (x.date, x.time))
                print("Event edited successfully.\n")
                return

        print("Event not found.\n")


def main():
    planner = Planner()  # Call Planner class by creating object

    while True:
        print("1. Add Event")
        print("2. View Events")
        print("3. Delete Event")
        print("4. Search for Event")
        print("5. Edit event")
        print("6. Exit")

        option = input("Reply:\n ")

        if option == '1':
            title = input("Enter event title:\n")
            description = input("Enter event description:\n")
            date = input("Enter event date (in YYYY-MM-DD format)\n *Include the dashes*:\n")
            time = input("Enter event time (in HH:MM format):\n")
            planner.add_event(title, description, date, time)

        elif option == '2':
            planner.view()

        elif option == '3':
            title = input(" Enter event title:\n ")
            planner.delete(title)

        elif option == '4':
            title = input("Enter event title:\n")
            planner.search(title)

        elif option == '5':
            title = input("Enter event title:\n")
            new_description = input("Enter new description:\n")
            new_date = input("Enter new date in YYYY-MM-DD format:\n")
            new_time = input("Enter new time in HH:MM format:\n")

            planner.edit_event(title, new_description, new_date, new_time)

        elif option == '6':
            break
        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()
