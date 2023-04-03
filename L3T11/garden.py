import spacy

# Find garden path sentences and add to the list
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boat.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Load the spacy model for tokenization and named entity recognition
nlp = spacy.load("en_core_web_sm")

# Tokenize and perform named entity recognition on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence: ", sentence)
    print("Named entities: ", [(ent.text, ent.label_) for ent in doc.ents])

# Tokenize and perform entity recognition on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Sentence: ", sentence)
    print("Entities: ", [(token.text, token.ent_type_) for token in doc])

# Look up the meaning of entities that we don't understand
print(spacy.explain("LOC"))
print(spacy.explain("ORG"))

# In this program, we first define a list called gardenpathSentences that contains some 
# garden path sentences we've identified, as well as some additional sentences that were requested. 
# I then load the en_core_web_sm model from spaCy, which is capable of tokenizing text and 
# performing both named entity recognition (NER) and entity recognition (ER).
# I look up the meanings of two entities using spaCy's explain function and print them to the console.
# Here are my explanations for the two entities that I looked up:
# LOC: A geographic location, such as a city or country.
# ORG: An organization, such as a company or government agency.
# Both of these entities make sense in terms of the words associated with them. 
# For example, if the sentence contains the word "Johannesburg," it would make sense for the entity to be labeled as LOC, 
# and if the sentence contains the name of a company, it would make sense for the entity to be labeled as ORG.