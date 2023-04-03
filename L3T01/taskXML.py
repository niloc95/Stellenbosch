
import xml.etree.ElementTree as ET


# parse the XML document
tree = ET.parse('movie_data.xml')

# get the root element
root = tree.getroot()

num_favorites = 0
num_not_favorites = 0

for child in root:
    print(child.tag, child.attrib)

# iterate over each 'movie' element in the XML document
for movie in root.iter('movie'):
#     # get the child tags of the 'movie' element
    child_tags = [child.tag for child in movie.iter()]
#     # get the text content of the child tags
    child_text = [child.text for child in movie.iter() if child.text]
#     # print the child tags and their text content
    print(f"Child tags of '{movie.attrib['title']}': {', '.join(child_tags)}")
    print(f"Text content of child tags: {', '.join(child_text)}\n")

for movie in root.iter('movie'):
    favorite = movie.get('favorite')
    if favorite == 'True':
        num_favorites += 1
    elif favorite == 'False':
        num_not_favorites += 1

print("Number of favorite movies:", num_favorites)
print("Number of movies that are not favorites:", num_not_favorites)