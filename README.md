# powerplant-coding-challenge - solution
Author: Lepas Milandou
## Overview
The goal of this challenge was to Calculate how much power each of a multitude of different powerplants need to produce 
when the load is given and taking into account the cost of the underlying energy sources (gas, kerosine) and the Pmin 
and Pmax of each powerplant.

## Installation
Clone the repository from github and move to the projet directory: 
```
git clone https://github.com/Thepas/powerplant-coding-challenge.git
cd powerplant-coding-challenge
```
### Requirements
- Python 3.9.5
- Poetry

install dependencies with poetry: 
```
poetry install --no-root
``` 

## How it works
Run the app in a terminal:
```
poetry run python src/main.py
```

To run test and submit POST request, you can use the following command:
```
curl -X POST -d @example_payloads/payload2.json -H "Content-Type: application/json" http://127.0.0.1:8888/productionplan
```
(you can choose the payload you want to test by changing the file name.)

You can also run the test with the following command:


## To DO

