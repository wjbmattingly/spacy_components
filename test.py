import spacy

nlp = spacy.load("en_core_web_sm")
# print (nlp.analyze_pipes())
text = "Tom and Jerry are not friends, but they do run around a lot together in the USA."
doc = nlp(text)
for ent in doc.ents:
    print (ent.text, ent.label_)
