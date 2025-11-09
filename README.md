# parallel-task-scheduler

Simple Python-based task parallel scheduler on Linux to run commands parallelly.

## Installation

```bash
pip install -e .
```

Or install from source:
```bash
git clone https://github.com/fzhao70/parallel-task-scheduler.git
cd parallel-task-scheduler
python setup.py install
```

## Usage

The library provides a simple API with just **two parameters**: `command` and `directory`.

### Basic Usage - Single Command

```python
from parallel_scheduler import run

# Execute a command in a specific directory
result = run("ls -la", "/tmp")

print(f"Success: {result.success}")
print(f"Output: {result.stdout}")
print(f"Errors: {result.stderr}")
print(f"Return code: {result.returncode}")
```

### Running Multiple Commands in Parallel

```python
from parallel_scheduler import run_parallel

# Define tasks as (command, directory) tuples
tasks = [
    ("ls -la", "/tmp"),
    ("pwd", "/home"),
    ("echo 'Hello World'", "."),
    ("find . -name '*.py'", "/usr/local")
]

# Run all tasks in parallel
results = run_parallel(tasks)

# Process results
for result in results:
    print(f"Command: {result.command}")
    print(f"Directory: {result.directory}")
    print(f"Success: {result.success}")
    print(f"Output: {result.stdout}")
    print("-" * 50)
```

### Limiting Concurrent Workers

```python
from parallel_scheduler import run_parallel

tasks = [
    ("sleep 1 && echo 'Task 1'", "."),
    ("sleep 1 && echo 'Task 2'", "."),
    ("sleep 1 && echo 'Task 3'", "."),
    ("sleep 1 && echo 'Task 4'", ".")
]

# Run with maximum 2 concurrent workers
results = run_parallel(tasks, max_workers=2)
```

## API Reference

### `run(command: str, directory: str = ".") -> TaskResult`

Executes a single command in the specified directory.

**Parameters:**
- `command` (str): The shell command to execute
- `directory` (str, optional): The working directory for command execution. Defaults to current directory (".")

**Returns:**
- `TaskResult`: Object containing execution details

### `run_parallel(tasks: List[Tuple[str, str]], max_workers: Optional[int] = None) -> List[TaskResult]`

Executes multiple commands in parallel.

**Parameters:**
- `tasks` (List[Tuple[str, str]]): List of (command, directory) tuples
- `max_workers` (int, optional): Maximum number of concurrent workers

**Returns:**
- `List[TaskResult]`: List of results in the same order as input tasks

### `TaskResult`

Result object with the following attributes:
- `command` (str): The executed command
- `directory` (str): The working directory
- `returncode` (int): Process return code
- `stdout` (str): Standard output
- `stderr` (str): Standard error
- `success` (bool): True if returncode == 0

## Examples

See the `examples/` directory for more usage examples.

## License

MIT License - see LICENSE file for details.
