from setuptools import setup, find_packages

setup(
    name="python_wheel_project",
    version="0.0.8",
    author="Maksim Kazartsev",
    author_email="kazarmax@gmail.com",
    description="Package to automate ETL for Adzuna API data",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark>=3.2.0",
        "delta-spark>=2.1.0",
        # Add other dependencies from requirements.txt
    ],
    entry_points={
        "console_scripts": [
            "run_pipeline=pipeline.main:main",
        ],
    },
    python_requires=">=3.8",
)