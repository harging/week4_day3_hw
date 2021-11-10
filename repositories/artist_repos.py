from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['artist_name'], row['id'])
        artists.append(artist)
    return artists

def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    # Create an empty variable
    artist = None
    # Create an SQL string (varchar)
    sql = "SELECT * FROM artists WHERE id = %s"
    # Create our values list
    values = [id]
    # Run the SQL and capture the result
    result = run_sql(sql, values)[0]
    # Create a new task object
    if result is not None:
        artist = Artist(result['id'], result['artist_name'])
    # Return the task object
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(artist):
    sql = "UPDATE artists SET (artist_name) = (%s) WHERE id = %s"
    values = [artist.id, artist.artist_name]
    run_sql(sql, values)

def albums(artist):
    artist = []
    sql = 'SELECT * FROM albums WHERE user_id = %s'
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['id'], row['album_name'], artist)
        albums.append(album)
    return albums