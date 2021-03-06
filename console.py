from models.album import Album
from models.artist import Artist

import repositories.artist_repos as artist_repos
import repositories.album_repos as album_repos
album_repos.delete_all()
artist_repos.delete_all()
artist1 = Artist("Beatles, The")
artist2 = Artist("Doors, The")
artist3 = Artist("Led Zeppelin")
artist4 = Artist("Rolling Stones, The")
artist5 = Artist("David Bowie")
artist6 = Artist("Cure, The")

album1 = Album("Help!", artist1, "Rock")
album2 = Album("Rubber Soul", artist1, "Rock")
album3 = Album("Revolver!", artist1, "Rock")
album4 = Album("Doors, The", artist2, "Rock")
album5 = Album("Strange Days", artist2, "Rock")
album6 = Album("LA Woman", artist2, "Rock")
album7 = Album("I", artist3, "Rock")
album8 = Album("II", artist3, "Rock")
album9 = Album("III", artist3, "Rock")
album10 = Album("Rolling Stones, The", artist4, "Rock")
album11 = Album("Aftermath", artist4, "Rock")
album12 = Album("Between The Buttons", artist4, "Rock")
album13 = Album("Diamond Dogs", artist5, "Rock")
album14 = Album("Spiders from Mars", artist5, "Rock")
album15 = Album("Hunky Dory", artist5, "Rock")
album16 = Album("Boy's Don't Cry", artist6, "Post punk")
album17 = Album("Seventeen Seconds", artist6, "Post punk")
album18 = Album("Faith", artist6, "Post punk")

artist_repos.save(artist1)
artist_repos.save(artist2)
artist_repos.save(artist3)
artist_repos.save(artist4)
artist_repos.save(artist5)
artist_repos.save(artist6)
album_repos.save(album1)
album_repos.save(album2)
album_repos.save(album3)
album_repos.save(album4)
album_repos.save(album5)
album_repos.save(album6)
album_repos.save(album7)
album_repos.save(album8)
album_repos.save(album9)
album_repos.save(album10)
album_repos.save(album11)
album_repos.save(album12)
album_repos.save(album13)
album_repos.save(album14)
album_repos.save(album15)
album_repos.save(album16)
album_repos.save(album17)
album_repos.save(album18)

# album_repos.delete_all()
# artist_repos.delete_all()

artist1 = Artist("Beatles, The")
artist_repos.save(artist1)

album1 = Album("Help!", artist1, "Rock")
album_repos.save(album1)
album2 = Album("Rubber Soul", artist1, "Rock")
album_repos.save(album2)

album1.genre = "Pop"
album_repos.update(album1)

for album in album_repos.select_all():
    print(album.__dict__)