# Part 1
# What does the following code do? Add a comment to each line of code

geo_xy = {
    'Baltimore': {'lat': 39.2904, 'lon': -76.6122},
    'Addis Ababa': {'lat': 9.0192, 'lon': 38.7525},
    'Seoul': {'lat': 37.5519, 'lon': 126.9918},
    'Cape Town': {'lat': -33.9249, 'lon': 18.4241},
    'Sydney': {'lat': -33.8688, 'lon': 151.2093},
    'Philadelphia': {'lat': 39.9526, 'lon': -75.1652},
    'Honolulu': {'lat': 21.3099, 'lon': -157.8581},
}

sort_category = input(f'Pick a category to sort the geo data\n("city", "lat", or "lon")\n: ')

sorted_data = list(geo_xy.items())
print(sorted_data)

sorted_data.sort(key=lambda x: x[1][sort_category] if sort_category != 'city' else x[0])

result = dict(sorted_data)

print(result)
