from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

import repositories.artist_repos as artist_repos

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repos.select(row['artist_name'])
        album = Album(row['id'], row['artist_name'], row['album_name'], row['genre'])
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (album_name, artist_name, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.album_name, album.artist_name.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    # Create an empty variable
    album = None
    # Create an SQL string (varchar)
    sql = "SELECT * FROM albums WHERE id = %s"
    # Create our values list
    values = [id]
    # Run the SQL and capture the result
    result = run_sql(sql, values)[0]
    # Create a new task object
    if result is not None:
        album_artist = artist_repos.select(row['artist_name'])
        album = Album(result['id'], result['album_name'], album_artist, result['genre'])
    # Return the task object
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (id, album_name, artist_name) = (%s, %s, %s) WHERE id = %s"
    values = [album.id, album.album_name, album.artist_name.id, album.genre]
    run_sql(sql, values)