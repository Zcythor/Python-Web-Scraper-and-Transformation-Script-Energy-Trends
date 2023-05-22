# Energy Trends Data Engineering Challenge README file

This project addresses a Data Engineering Pipeline Challenge in the context of ETL (Extraction, Transformation, and Loading).

Energy Trends data published on the government source data for Energy Resources.

The challenge itself (PDF included in the folder) is to perform data tasks in Python which **EXTRACT** data from a specified URL, **CLEAN** (or **TRANSFORM**) and **VALIDATE** its schema in order to be ingested into a data lake (**LOAD**).

This folder contains:

- The Python script which performs the tasks (`Energy Trends UK Oil and Energy web scraper script.py`)
- The CSV file containing Energy Trends data which is retrieved from the government URL (`ET_3.csv`)
- The transformed Excel output file of the Energy Trends Data converted by the Python script (`ET_3.1_DEC_22.xlsx Transformed.xlsx`)
- The Setup file is used for packaging and distributing the Python package. It defines the metadata and configuration for the package (`setup.py`)
- dist and energy_trends_web_scraper_and_transformation_script.egg-info allows for pip install package