# Part 1
# What does the following code do? Add a comment to each line of code

from datetime import datetime
from datetime import timedelta

geo_xy = {
    'Baltimore': {'lat': 39.2904, 'lon': -76.6122},
    'Addis Ababa': {'lat': 9.0192, 'lon': 38.7525},
    'Seoul': {'lat': 37.5519, 'lon': 126.9918},
    'Cape Town': {'lat': -33.9249, 'lon': 18.4241},
    'Sydney': {'lat': -33.8688, 'lon': 151.2093},
    'Philadelphia': {'lat': 39.9526, 'lon': -75.1652},
    'Honolulu': {'lat': 21.3099, 'lon': -157.8581},
}

city = input(f'Pick a city {[city for city in geo_xy.keys()]}\n: ')

if city in geo_xy:
    offset = geo_xy[city]['lon'] // 15
    print(offset)
    if offset > -12 or offset < 12:
        offset = offset - 12
    local_time = datetime.utcnow() + timedelta(hours=offset)

    print(f'Local time in {city}: {local_time.strftime("%H:%M:%S")}')
else:
    print(f"No location data for {city}! Try Again!")