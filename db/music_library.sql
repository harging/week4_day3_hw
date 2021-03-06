DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
id SERIAL PRIMARY KEY,
artist_name VARCHAR(255) NOT NULL
);

CREATE TABLE albums (
id SERIAL PRIMARY KEY,
album_name VARCHAR(255) NOT NULL,
artist_id INT REFERENCES artists(id),
genre VARCHAR(255)
);
