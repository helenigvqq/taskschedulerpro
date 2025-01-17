# TaskSchedulerPro

TaskSchedulerPro is a Python tool that provides an enhanced interface for scheduling complex tasks and scripts on Windows. It simplifies the process of creating and managing scheduled tasks using the Windows Task Scheduler.

## Features

- Schedule scripts to run at specific times.
- Optionally set tasks to repeat at specified intervals.
- Easily delete scheduled tasks by name.
- Designed to work exclusively on Windows systems.

## Requirements

- Python 3.x
- Windows operating system (as it uses Windows-specific features)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/TaskSchedulerPro.git
    ```

2. Navigate to the project directory:
    ```bash
    cd TaskSchedulerPro
    ```

## Usage

### Creating a Task

To create a scheduled task, instantiate the `TaskSchedulerPro` class and call the `create_task` method with the necessary parameters:

```python
from task_scheduler_pro import TaskSchedulerPro

tsp = TaskSchedulerPro()
tsp.create_task("MyDailyTask", "C:\\Scripts\\daily_task.py", "14:00", repeat_interval=1440)
```

- `task_name`: Name of the task.
- `script_path`: Path to the script you want to run.
- `start_time`: Time to start the task (24-hour format HH:MM).
- `repeat_interval`: Optional. Repeat interval in minutes.

### Deleting a Task

To delete a scheduled task by name, use the `delete_task` method:

```python
tsp.delete_task("MyDailyTask")
```

## Note

- TaskSchedulerPro is only supported on Windows systems.
- Ensure you have permissions to create and delete tasks on the system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.