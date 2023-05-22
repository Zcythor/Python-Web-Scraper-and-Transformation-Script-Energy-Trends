import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="energy_trends_web_scraper_and_transformation_script",
    version="1.0.0",
    author="Jivanshh Banga Thakur",
    author_email="jivanshh@hotmail.com",
    description="A Python package for scraping energy data and transforming it into a usable format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zcythor/Python-Web-Scraper-and-Transformation-Script-Energy-Trends",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
