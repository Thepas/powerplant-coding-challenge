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
```
poetry run python tests/test.py
```
## expected results
payload example (payload2.json):
```Json
{
  "load": 480,
  "fuels":
  {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredbig2",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "gasfiredsomewhatsmaller",
      "type": "gasfired",
      "efficiency": 0.37,
      "pmin": 40,
      "pmax": 210
    },
    {
      "name": "tj1",
      "type": "turbojet",
      "efficiency": 0.3,
      "pmin": 0,
      "pmax": 16
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    },
    {
      "name": "windpark2",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 36
    }
  ]
}
```

result example:
```json
[
    {
        "name": "windpark1",
        "p": 90.0
    },
    {
        "name": "windpark2",
        "p": 21.6
    },
    {
        "name": "gasfiredbig1",
        "p": 368.4
    },
    {
        "name": "gasfiredbig2",
        "p": 0
    },
    {
        "name": "gasfiredsomewhatsmaller",
        "p": 0
    },
    {
        "name": "tj1",
        "p": 0
    }
]
```
## Unit Commitment's algorithm flowchart
![flowchart Unit Commitment](https://raw.githubusercontent.com/Thepas/powerplant-coding-challenge/master/flowcharts/unit_commitment.png)

## To DO
- Complete the exception cases where the result cannot be found
- Review the calculation for the cost of CO2
- Provide a Dockerfile and websocket if time allow
