import json


def dictDestructure(dic, *items):
    """ gets a dict and the keys as parameters and 'destructures' according to the given sequence"""
    return (dic[item] if item in dic else None for item in items)  #


def costPerMwh(powerplant, fuels):
    """Calculates the cost of generating power based on the cost of fuel and the cost of CO2 emissions (gas-fired
    plants) """
    # print(powerplant, fuels)
    if powerplant["type"] == "turbojet":
        return fuels["kerosine(euro/MWh)"] / powerplant["efficiency"]

    elif powerplant["type"] == "gasfired":
        # we will take into account that each MWh generated creates 0.3 ton of CO2 and 1 ton = 20€
        return (fuels["gas(euro/MWh)"] + (0.3 * fuels["co2(euro/ton)"])) / powerplant["efficiency"]

    elif powerplant["type"] == "windturbine":
        return 0  # Wind-turbines do not consume 'fuel' and thus are considered to generate power at zero price.


def sortByMeritOrder(powerplants, fuels):
    """Sort the plants in merit order based on the cost per Mwh and the Pmin of the plant"""
    for plant in powerplants:
        plant['cost'] = costPerMwh(plant, fuels)
        if plant['type'] == "windturbine":
            plant['pmax'] = plant['pmax'] * fuels['wind(%)'] / 100

    return sorted(powerplants, key=lambda item: (item['cost'], item['pmin']))  # sort plants by cost and pmin


def prod_calculate(load, fuels, powerplants):
    """calculates the production of each plant according to its type, its minimum and maximum power"""
    required_load = load
    merit_order = sortByMeritOrder(powerplants, fuels)
    response = [{"name": plant["name"], "p": 0} for plant in merit_order]  # based on example_response format

    for i, plant in enumerate(merit_order):
        plant_type, pmin, pmax = dictDestructure(plant, 'type', 'pmin', 'pmax')  # destructuring-bind dict contents

        if plant_type == 'windturbine':
            if required_load - pmax < 0:
                response[i]["p"] = required_load
                required_load -= response[i]["p"]
                break
            elif required_load - pmax == 0:
                response[i]["p"] = pmax
                required_load -= response[i]["p"]
                break
            else:
                response[i]["p"] = pmax

        elif required_load - pmax < 0 and required_load >= pmin:
            response[i]["p"] = required_load
            required_load -= response[i]["p"]
            break
        elif required_load - pmax == 0:
            response[i]["p"] = pmax
            required_load -= response[i]["p"]
            break
        else:
            response[i]["p"] = pmax - plant["pmin"]
        required_load -= response[i]["p"]

    if required_load > 0:
        return 'The algorithm could not converge to a solution'

    if required_load < 0:
        return "An error has occurred, we have more production than demand"

    return response


if __name__ == '__main__':
    payload = json.load(open("../../example_payloads/payload4.json"))
    power_plants = payload["powerplants"]
    fuels_cost = payload["fuels"]
    # merit_order = sortByMeritOrder(power_plants, fuels_cost)
    response = prod_calculate(payload["load"], fuels_cost, power_plants)
