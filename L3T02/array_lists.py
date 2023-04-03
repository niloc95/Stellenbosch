class Album:
    def __init__(self, albumName, numberOfSongs, albumArtist):
        self.albumName = albumName
        self.numberOfSongs = numberOfSongs
        self.albumArtist = albumArtist
        
    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"

# Create a new list called albums1, add 5 albums to it and print it out
albums1 = [
    Album("Album1", 10, "Artist1"),
    Album("Album2", 8, "Artist2"),
    Album("Album3", 15, "Artist3"),
    Album("Album4", 12, "Artist4"),
    Album("Album5", 7, "Artist5"),
]

print("Albums1:")
for album in albums1:
    print(album)

# Sort the list according to the numberOfSongs and print it out.
albums1.sort(key=lambda x: x.numberOfSongs)
print("\nSorted by numberOfSongs:")
for album in albums1:
    print(album)

# Swap the element at position 1 of albums1 with the element at position 2 and print it out
albums1[1], albums1[2] = albums1[2], albums1[1]
print("\nSwapped elements at position 1 and 2:")
for album in albums1:
    print(album)

# Create a new list called albums2
albums2 = []

# Add 5 albums to the albums2 List and print it out
albums2.append(Album("Album6", 13, "Artist6"))
albums2.append(Album("Album7", 9, "Artist7"))
albums2.append(Album("Album8", 11, "Artist8"))
albums2.append(Album("Album9", 6, "Artist9"))
albums2.append(Album("Album10", 14, "Artist10"))

print("\nAlbums2:")
for album in albums2:
    print(album)

# Copy all of the albums from albums1 into albums2
albums2.extend(albums1)

# Add the following two elements to albums2:
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# Sort the courses in albums2 alphabetically according to the album name and print it out.
albums2.sort(key=lambda x: x.albumName)

print("\nSorted by albumName:")
for album in albums2:
    print(album)

# Search for the album “Dark Side of the Moon” in albums2 and print out the index of the album in the List
for index, album in enumerate(albums2):
    if album.albumName == "Dark Side of the Moon":
        print(f"\nIndex of Dark Side of the Moon: {index}")
        break
else:
    print("\nDark Side of the Moon not found in the list.")
