from threading import Thread
from time import sleep
from random import random

class Archiver:
    # Class attributes for tracking the status and progress of the archiving process
    archive_status: str = "Waiting"  # Initial status is set to "Waiting"
    archive_progress: float = 0      # Progress is initialized to 0%
    thread: Thread | None = None     # A thread attribute to handle asynchronous archiving

    # Method to get the current status of the archiving process
    def status(self) -> str:
        return Archiver.archive_status  # Returns the current value of the class-level status

    # Method to get the current progress of the archiving process
    def progress(self) -> float:
        return Archiver.archive_progress  # Returns the current value of the class-level progress

    # Method to start the archiving process if it is in the "Waiting" state
    def run(self) -> None:
        if Archiver.archive_status == "Waiting":  # Only proceed if the status is "Waiting"
            Archiver.archive_status = "Running"   # Set status to "Running"
            Archiver.archive_progress = 0         # Reset progress to 0%
            Archiver.thread = Thread(target=self.run_impl)  # Create a new thread to run `run_impl`
            Archiver.thread.start()  # Start the thread, which begins the archiving process

    # Method that contains the logic for the archiving process
    def run_impl(self) -> None:
        for i in range(10):  # Loop 10 times to simulate progress
            sleep(1 * random())  # Sleep for a random amount of time between 0 and 1 second
            if Archiver.archive_status != "Running":  # If the status changes from "Running", stop the process
                return
            Archiver.archive_progress = (i + 1) / 10  # Update progress (e.g., 10%, 20%, etc.)
            print("Here... " + str(Archiver.archive_progress))  # Print the current progress
        sleep(1)  # Simulate a final delay before completion
        if Archiver.archive_status != "Running":  # Check again if the process is still running
            return
        Archiver.archive_status = "Complete"  # Set status to "Complete" when done

    # Method to get the name of the file being archived
    def archive_file(self) -> str:
        return "contacts.json"  # Returns a hardcoded filename for the archived file

    # Method to reset the archiving process to its initial state
    def reset(self) -> None:
        Archiver.archive_status = "Waiting"  # Reset status to "Waiting"

    # Class method to get a new instance of the Archiver class
    @classmethod
    def get(cls):
        return Archiver()  # Returns a new instance of Archiver
