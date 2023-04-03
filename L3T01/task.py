import xml.etree.ElementTree as ET
tree = ET.parse('movie_data.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    # get the child tags of the 'movie' element
    child_tags = [child.tag for child in movie.iter()]
#     # get the text content of the child tags
    child_text = [child.text for child in movie.iter() if child.text]
#     # print the child tags and their text content
    print(f"Child tags of '{movie.attrib['title']}': {', '.join(child_tags)}")
    print(f"Text content of child tags: {', '.join(child_text)}")