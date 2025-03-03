import spacy 
nlp = spacy.load('en_core_web_sm')

sentence = "we are from sitare university"
doc =  nlp(sentence)
pos_tag = []
for token in doc:
    pos_tag.append((token.text, token.pos_, spacy.explain(token.pos_)))

print(pos_tag)
