movie = {
    'title': 'Jumanji: The Next Level',
    'year': 2017,
    'genre': 'Adventure'
}

movie2 = {
    'title': 'Frozen II',
    'year': 2019,
    'genre': 'Family'
}

print()
print(movie["title"])
print(movie)

movie.update({'viewers': 44324578})
movie["genre"] = "Adventure/Comedy"
del movie["year"]

print(movie)

print()
print(movie2)

movie2.update({'viewers': 98698637})
movie2["genre"] = "Family/Musical"

print(movie2)
