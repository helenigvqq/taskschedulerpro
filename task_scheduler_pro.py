import subprocess
import os
from datetime import datetime, timedelta

class TaskSchedulerPro:
    def __init__(self):
        if not os.name == 'nt':
            raise EnvironmentError("TaskSchedulerPro is only supported on Windows systems.")
        print("TaskSchedulerPro initialized.")

    def create_task(self, task_name, script_path, start_time, repeat_interval=None):
        """
        Create a scheduled task to run a script at a specified start time and optionally at a repeat interval.

        :param task_name: The name of the task.
        :param script_path: The path to the script to run.
        :param start_time: The time to start the task in HH:MM format.
        :param repeat_interval: Optional repeat interval in minutes.
        """
        try:
            # Convert start_time to 24-hour format
            start_hour, start_minute = map(int, start_time.split(':'))
            start_time_dt = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            if start_time_dt < datetime.now():
                start_time_dt += timedelta(days=1)
            start_time_str = start_time_dt.strftime('%H:%M')

            # Base command to create a scheduled task
            command = [
                'schtasks', '/create', '/tn', task_name, '/tr', script_path, '/sc', 'once', '/st', start_time_str
            ]

            # Add repeat interval if specified
            if repeat_interval:
                command += ['/sc', 'minute', '/mo', str(repeat_interval)]

            # Execute the command
            subprocess.run(command, check=True)
            print(f"Task '{task_name}' scheduled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create task '{task_name}'. Error: {e}")

    def delete_task(self, task_name):
        """
        Delete a scheduled task by name.

        :param task_name: The name of the task to delete.
        """
        try:
            subprocess.run(['schtasks', '/delete', '/tn', task_name, '/f'], check=True)
            print(f"Task '{task_name}' deleted successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to delete task '{task_name}'. Error: {e}")

if __name__ == "__main__":
    tsp = TaskSchedulerPro()
    tsp.create_task("MyDailyTask", "C:\\Scripts\\daily_task.py", "14:00", repeat_interval=1440)
    # tsp.delete_task("MyDailyTask")