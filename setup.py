"""Setup script for parallel-task-scheduler."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="parallel-task-scheduler",
    version="1.0.0",
    author="Your Name",
    description="Simple Python-based task parallel scheduler on Linux to run commands parallelly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fzhao70/parallel-task-scheduler",
    py_modules=["parallel_scheduler"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    keywords="parallel scheduler task command linux",
)
