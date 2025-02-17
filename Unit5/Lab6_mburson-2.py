cities = {
    "New York City": {
        "country": "United States",
        "population": "8,800,000",
        "fact": "New York City is nicknamed 'The Big Apple'"
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13,900,000",
        "fact": "Tokyo is the most popular city"
    },
    "London": {
        "country": "United Kingdom",
        "population": "9,000,000",
        "fact": "London has over 170 museums."
    },
}

for city_name, city_info in cities.items():
    print(f"\n{city_name}:")
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")