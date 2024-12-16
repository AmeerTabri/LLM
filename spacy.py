import spacy

# Load spaCy's medium-sized model
nlp = spacy.load("en_core_web_md")

# Example 1
text1 = "Functional safety is critical in software engineering."
text2 = "Safety in software systems is important for preventing risks."

# Example 2
# text1 = "Functional safety is critical in software engineering."
# text2 = "I love pizza"
 
doc1 = nlp(text1)
doc2 = nlp(text2)

similarity = doc1.similarity(doc2)*100

print(f"Similarity: {similarity:.2f}%")
