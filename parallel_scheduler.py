"""
Simple Python-based parallel task scheduler for Linux.

This library provides a simple API to run commands in parallel with specified working directories.
"""

import subprocess
import threading
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass
from queue import Queue


@dataclass
class TaskResult:
    """Result of a command execution."""
    command: str
    directory: str
    returncode: int
    stdout: str
    stderr: str
    success: bool


def run(command: str, directory: str = ".") -> TaskResult:
    """
    Run a single command in the specified directory.

    Args:
        command: The command to execute (e.g., "ls -la")
        directory: The directory to execute the command in (default: current directory)

    Returns:
        TaskResult object containing execution details

    Example:
        >>> result = run("ls -la", "/tmp")
        >>> print(result.stdout)
    """
    try:
        process = subprocess.run(
            command,
            shell=True,
            cwd=directory,
            capture_output=True,
            text=True
        )

        return TaskResult(
            command=command,
            directory=directory,
            returncode=process.returncode,
            stdout=process.stdout,
            stderr=process.stderr,
            success=process.returncode == 0
        )
    except Exception as e:
        return TaskResult(
            command=command,
            directory=directory,
            returncode=-1,
            stdout="",
            stderr=str(e),
            success=False
        )


def run_parallel(tasks: List[Tuple[str, str]], max_workers: Optional[int] = None) -> List[TaskResult]:
    """
    Run multiple commands in parallel.

    Args:
        tasks: List of tuples (command, directory)
        max_workers: Maximum number of parallel workers (default: number of tasks)

    Returns:
        List of TaskResult objects in the same order as input tasks

    Example:
        >>> tasks = [
        ...     ("ls -la", "/tmp"),
        ...     ("pwd", "/home"),
        ...     ("echo 'hello'", ".")
        ... ]
        >>> results = run_parallel(tasks)
        >>> for result in results:
        ...     print(f"{result.command}: {result.success}")
    """
    if not tasks:
        return []

    results = [None] * len(tasks)
    result_lock = threading.Lock()

    def worker(index: int, command: str, directory: str):
        result = run(command, directory)
        with result_lock:
            results[index] = result

    threads = []
    for i, (command, directory) in enumerate(tasks):
        thread = threading.Thread(target=worker, args=(i, command, directory))
        thread.start()
        threads.append(thread)

        # Limit concurrent threads if max_workers is specified
        if max_workers and len(threads) >= max_workers:
            threads[0].join()
            threads.pop(0)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return results


# Convenience function - main API
execute = run  # Alias for clearer naming


__all__ = ['run', 'run_parallel', 'execute', 'TaskResult']
