#USA
def carbon_slc_nyc(type_list, fuel_list):
"""enter mode of transportation list and associated fuel type to calculate carbon emissions for round trip travel from new york to slc"""
    carbon_footprint = []
    carbon_dict = {}
    for x, y in zip(type_list, fuel_list):
        activity = 3910
        type_ = 'miles'
        mode = 'petrolCar'
        country = 'usa'
        url = f'https://api.triptocarbon.xyz/v1/footprint?activity={activity}&activityType={type_}&country={country}&mode={x}&fueltype={y}'
        response = requests.get(url)
        info = response.json()
        carbon = str(list(info.values()))
        carbon_footprint.append({x : carbon.strip("['']")})
    for d in carbon_footprint: 
        carbon_dict.update(d)
    return carbon_dict 

#UK
def carbon_uk(type_list, fuel_list):
"""enter mode of transportation list and associated fuel type to calculate travel carbon emissions for 3910 miles travel in UK"""
    carbon_footprint = []
    carbon_dict = {}
    for x, y in zip(type_list, fuel_list):
        activity = 3910
        type_ = 'miles'
        country = 'gbr'
        url = f'https://api.triptocarbon.xyz/v1/footprint?activity={activity}&activityType={type_}&country={country}&mode={x}&fueltype={y}'
        response = requests.get(url)
        info = response.json()
        carbon = str(list(info.values()))
        carbon_footprint.append({x : carbon.strip("['']")})
    for d in carbon_footprint: 
        carbon_dict.update(d)
    return carbon_dict

#World / default 
def carbon_world(type_list, fuel_list):
"""enter mode of transportation list and associated fuel type to calculate travel carbon emissions for 3910 miles travel according to default/world average"""
    carbon_footprint = []
    carbon_dict = {}
    for x, y in zip(type_list, fuel_list):
        activity = 3910
        type_ = 'miles'
        country = 'def'
        url = f'https://api.triptocarbon.xyz/v1/footprint?activity={activity}&activityType={type_}&country={country}&mode={x}&fueltype={y}'
        response = requests.get(url)
        info = response.json()
        carbon = str(list(info.values()))
        carbon_footprint.append({x : carbon.strip("['']")})
    for d in carbon_footprint: 
        carbon_dict.update(d)
    return carbon_dict

#carbon footprint by fuel type
def carbon_fuel(fuel_gallons, fuel_type):
"""enter amount of fuel in gallons and fuel type to obtain carbon footprint for journey """
    carbon_footprint = []
    carbon_dict = {}
    for x, y in zip(fuel_gallons, fuel_type):
        url = f'https://api.triptocarbon.xyz/v1/footprint?activity={x}&activityType=fuel&country=usa&fuelType={y}'
        response = requests.get(url)
        info = response.json()
        carbon = str(list(info.values()))
        carbon_footprint.append({x : carbon.strip("['']")})
    for d in carbon_footprint: 
        carbon_dict.update(d)
    return carbon_dict 

