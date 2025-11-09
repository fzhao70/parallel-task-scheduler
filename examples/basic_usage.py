#!/usr/bin/env python3
"""
Basic usage examples for parallel-task-scheduler library.

This demonstrates the simple 2-parameter API: command and directory.
"""

import sys
import os

# Add parent directory to path for importing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parallel_scheduler import run, run_parallel


def example_single_command():
    """Example: Run a single command in a specific directory."""
    print("=" * 60)
    print("Example 1: Single Command Execution")
    print("=" * 60)

    # Simple API: just two parameters
    result = run("ls -la", "/tmp")

    print(f"Command: {result.command}")
    print(f"Directory: {result.directory}")
    print(f"Success: {result.success}")
    print(f"Return Code: {result.returncode}")
    print(f"\nOutput:\n{result.stdout[:200]}...")  # Show first 200 chars
    print()


def example_parallel_commands():
    """Example: Run multiple commands in parallel."""
    print("=" * 60)
    print("Example 2: Parallel Command Execution")
    print("=" * 60)

    # Define tasks as (command, directory) tuples
    tasks = [
        ("echo 'Task 1: Listing /tmp' && ls /tmp | head -5", "."),
        ("echo 'Task 2: Current date' && date", "."),
        ("echo 'Task 3: System info' && uname -a", "."),
        ("echo 'Task 4: Disk usage' && df -h | head -3", "."),
    ]

    # Run all tasks in parallel
    results = run_parallel(tasks)

    # Display results
    for i, result in enumerate(results, 1):
        print(f"\nTask {i}:")
        print(f"  Command: {result.command}")
        print(f"  Success: {result.success}")
        print(f"  Output: {result.stdout.strip()}")
        print("-" * 60)
    print()


def example_with_different_directories():
    """Example: Run commands in different directories."""
    print("=" * 60)
    print("Example 3: Commands in Different Directories")
    print("=" * 60)

    tasks = [
        ("pwd && ls -la | head -5", "/tmp"),
        ("pwd && ls -la | head -5", "/home"),
        ("pwd && ls -la | head -5", "/var"),
    ]

    results = run_parallel(tasks)

    for result in results:
        print(f"\nDirectory: {result.directory}")
        print(f"Output:\n{result.stdout}")
        print("-" * 60)
    print()


def example_error_handling():
    """Example: Handling command errors."""
    print("=" * 60)
    print("Example 4: Error Handling")
    print("=" * 60)

    # This command will fail
    result = run("ls /nonexistent_directory_12345", ".")

    print(f"Command: {result.command}")
    print(f"Success: {result.success}")
    print(f"Return Code: {result.returncode}")
    print(f"Error Output: {result.stderr}")
    print()


def example_limited_workers():
    """Example: Limit concurrent workers."""
    print("=" * 60)
    print("Example 5: Limited Concurrent Workers")
    print("=" * 60)

    tasks = [
        ("echo 'Worker 1' && sleep 1", "."),
        ("echo 'Worker 2' && sleep 1", "."),
        ("echo 'Worker 3' && sleep 1", "."),
        ("echo 'Worker 4' && sleep 1", "."),
        ("echo 'Worker 5' && sleep 1", "."),
        ("echo 'Worker 6' && sleep 1", "."),
    ]

    print("Running 6 tasks with max 2 concurrent workers...")
    import time
    start = time.time()
    results = run_parallel(tasks, max_workers=2)
    elapsed = time.time() - start

    print(f"Completed in {elapsed:.2f} seconds")
    print(f"All tasks successful: {all(r.success for r in results)}")
    print()


if __name__ == "__main__":
    print("\n")
    print("*" * 60)
    print("  PARALLEL TASK SCHEDULER - USAGE EXAMPLES")
    print("  Simple API: run(command, directory)")
    print("*" * 60)
    print("\n")

    example_single_command()
    example_parallel_commands()
    example_with_different_directories()
    example_error_handling()
    example_limited_workers()

    print("*" * 60)
    print("  All examples completed!")
    print("*" * 60)
