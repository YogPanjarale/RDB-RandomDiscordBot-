import imdb
import datetime
# gathering information from IMDb
moviesdb = imdb.IMDb()
text = input("enter movie name: \n")

# passing input for searching movie
movies = moviesdb.search_movie(text)




for movie in movies:

    title = movie['title']
    year = movie['year']
# speaking title with releasing year


info = movie.getID()
movie = moviesdb.get_movie(info)

title = movie['title']
year = movie['year']
plot = movie['plot outline']

# the below if-else is for past and future release
if year < int(datetime.datetime.now().strftime("%Y")):
    print(
        f'{title}was released in {year}.\
        The plot summary of movie is{plot}')

else:
    print(
        f'{title}will release in {year} .\
        The plot summary of movie is{plot}')
