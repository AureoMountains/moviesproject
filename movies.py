movies = [
    {
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8,
        "runtime": 148,
        "budget_million": 160,
        "revenue_million": 839
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "genre": "Action",
        "rating": 9.0,
        "runtime": 152,
        "budget_million": 185,
        "revenue_million": 1006
    },
    {
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "rating": 8.7,
        "runtime": 169,
        "budget_million": 165,
        "revenue_million": 731
    },
    {
        "title": "Parasite",
        "year": 2019,
        "genre": "Thriller",
        "rating": 8.5,
        "runtime": 132,
        "budget_million": 11,
        "revenue_million": 258
    },
    {
        "title": "Whiplash",
        "year": 2014,
        "genre": "Drama",
        "rating": 8.5,
        "runtime": 106,
        "budget_million": 3.3,
        "revenue_million": 49
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genre": "Sci-Fi",
        "rating": 8.7,
        "runtime": 136,
        "budget_million": 63,
        "revenue_million": 467
    },
    {
        "title": "Pulp Fiction",
        "year": 1994,
        "genre": "Crime",
        "rating": 8.9,
        "runtime": 154,
        "budget_million": 8.5,
        "revenue_million": 214
    },
    {
        "title": "Spirited Away",
        "year": 2001,
        "genre": "Animation",
        "rating": 8.6,
        "runtime": 125,
        "budget_million": 19,
        "revenue_million": 395
    },
    {
        "title": "Alien",
        "year": 1979,
        "genre": "Horror",
        "rating": 8.5,
        "runtime": 117,
        "budget_million": 11,
        "revenue_million": 106
    },
    {
        "title": "Blade Runner 2049",
        "year": 2017,
        "genre": "Sci-Fi",
        "rating": 8.0,
        "runtime": 164,
        "budget_million": 150,
        "revenue_million": 267
    },
    {
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "genre": "Comedy",
        "rating": 8.1,
        "runtime": 99,
        "budget_million": 25,
        "revenue_million": 172
    },
    {
        "title": "Get Out",
        "year": 2017,
        "genre": "Horror",
        "rating": 7.8,
        "runtime": 104,
        "budget_million": 4.5,
        "revenue_million": 255
    }
]

final_revenue = ()
prices = ()


#    Counter(movies)
#    if movie >= 300:
#    print(f"{key}Are you saying that if i want to watch {title} i must pay {value}")
# )

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(movies, final_revenue)
df.plot(
    movies="age",
    prices="income",
    final_revenue="Final"
)

ax.set(
    title="Movies Available",
    xlabel="Movies",
    ylabel="final_revenue"
)

ax.grid(True)
ax.legend(final_revenue)
fig.tight_layoud(movies)
plt.show()

ax.fill_between(
    movies,
    prices,
    final_revenue,
    alpha=0.4
)
Single region:

ax.axvspan(100, 200, alpha=0.5)

ax.scatter(movies, prices)

Important parameters:

ax.scatter(
    movies,
    prices,
    s=100, #size
    alpha=0.8, #transparency
    c=z, #color based on another variable
    cmap="NNew Graphic Chart"
)
