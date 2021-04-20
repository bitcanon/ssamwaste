# SSAM Waste Schedule Library
A simple library for the SSAM Waste Schedule API written in Python 3.

SSAM (Södra Smålands Avfall & Miljö) is a Swedish Waste Management company.
They empty their customers trash bins on a pre-defined schedule. This library
will fetch the schedule from their API and present it to the user through a few simple classes and properties, wrapped inside a Python package.

## Installation
Install the latest version with pip3:
```
$ pip3 install ssamwaste
```

## Basics
### Setup
Use the same settings you are using to login to the Visonic-Go app.
```python
from ssam import ssam

ssam = ssam.WasteScheduler()

# The `get_waste_bins()` method accept a Building ID, which is the ID of your
# house. This is your unique identifier as a customer.
for waste_bin in ssam.get_waste_bins(12345):
	print(waste_bin)
```