"""
project level settings
"""

from setuptools import setup, find_packages

__version__ = "1.2.0"

setup(name="air-quality-poc", version=__version__, packages=find_packages(where="src"), package_dir={"": "src"},
      exclude=["*.tests", "*.tests.*", "tests.*", "tests"])


