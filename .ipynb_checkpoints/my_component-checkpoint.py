import spacy
from spacy.language import Language

@Language.component("remove_person")
def remove_person(doc):
    final = []
    for ent in doc.ents:
        if ent.label_ != "PERSON":
            final.append(ent)
    doc.ents = final
    return (doc)