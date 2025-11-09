"""
parallel-task-scheduler: Simple Python-based task parallel scheduler.

Simple API with just two parameters: command and directory.
"""

from parallel_scheduler import run, run_parallel, execute, TaskResult

__version__ = "1.0.0"
__all__ = ['run', 'run_parallel', 'execute', 'TaskResult']
