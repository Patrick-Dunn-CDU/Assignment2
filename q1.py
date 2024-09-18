# Task 1
import csv #import library to read the csv files

# open all 4 csv's for reading
csv1=open("CSV1.csv",'r+')
csv2=open("CSV2.csv",'r+')
csv3=open("CSV3.csv",'r+')
csv4=open("CSV4.csv",'r+')

# reset 'combined.txt' and 'Top_30_Words.csv' to be empty
t=open("combined.txt","w")
t.write("")
t.close()

c=open("Top_30_Words.csv","w")
c.write("")
c.close()

#open 'combined.txt' for appending and append all 4 csv's
text=open("combined.txt","a")
for row in csv.reader(csv1):
    text.write(" ".join(row)+'\n')
for row in csv.reader(csv2):
    text.write(" ".join(row)+'\n')
for row in csv.reader(csv3):
    text.write(" ".join(row)+'\n')
for row in csv.reader(csv4):
    text.write(" ".join(row)+'\n')
text.close()

# Task 2
# spaCy was installed
# scispaCy was installed alongside the two models, "en_core_sci_sm" and "en_ner_bc5cdr_md"
# hugging face transformers was installed
# biobert was not successfully installed as the installation instructions were outdated and only worked on versions of Python older than 3.8

# Task 3
# 3.1
# open 'combined.txt' for reading and 'Top_30_Words.csv' for appending
text=open("combined.txt","r")
output=open("Top_30_Words.csv","a")
#create an empty dictionary for all found words
found_words=dict()
#for each word of the text, if that word is already in 'found_words' increment its value by 1, and if the word is not in 'found_words' add it to found words with a value of 1
for line in text:
    line=line.strip()
    line=line.lower()
    words=line.split()
    for i in words:
        if i in found_words:
            found_words[i] = found_words[i] + 1
        else:
            found_words[i]=1
# create a new list of words from 'found_words' ordered by frequency and then write the top 30 words to 'Top_30_Words.csv' with their values
top30=sorted(found_words,key=found_words.get,reverse=True)
for i in range(30):
    output.write(f"{top30[i]},{found_words[top30[i]]}\n")
output.close()

# 3.2
from transformers import AutoTokenizer #import AutoTokenizer
#create the tokenizer itself as well as an empty dictionary for found words
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
found_words_hf=dict()
# for each line, apply the tokenizer to split the text into tokens
for line in text:
    encoding = tokenizer(line)
    #create a list of all unique tokens by converting them into a set (which does not support duplicate values) and back to a list which contains only unique values
    uni_encoding=list(set(encoding['input_ids'])) 
    # for each of the tokens, apply the same logic as above to count all values
    for i in encoding['input_ids']:
        if i in found_words_hf:
            found_words_hf[i] = found_words_hf[i] + 1
        else:
            found_words_hf[i]=1
# same top 30 logic as above
top30_hf=sorted(found_words_hf,key=found_words_hf.get,reverse=True)

#prints number of unique tokens and top 30 words
print("Number of Unique Tokens:",len(uni_encoding)) 
print("The top 30 words are: ")
for i in range(30):
    print(tokenizer.decode(top30_hf[i]),":",found_words_hf[top30_hf[i]]) 

# The above code functions correctly on smaller text files but does not work with 'combined.txt' as it is too large for the model applied

# Task 4
# scispacy models

import spacy
# load the scispaCy model
nlp=spacy.load("en_ner_bc5cdr_md")
# initialise variables used below
disease_count1=0
drug_count1=0
found_words_sci=dict()
# apply the scispaCy model to each line of the text and check all entities for any labelled 'DISEASE' or 'CHEMICAL' to find all diseases and drugs
# additionally, a list of all found entities is kept, similarly to above
for line in text:
    doc=nlp(line)
    for ent in doc.ents:
        if ent.label_=="DISEASE":
            disease_count1+=1
        elif ent.label_=="CHEMICAL":
            drug_count1+=1
        if ent in found_words_sci:
            found_words_sci[ent] = found_words_sci[ent] + 1
        else:
            found_words_sci[ent]=1
# top 30 list is sorted and printed similarly
top30_sci=sorted(found_words_sci,key=found_words_sci.get,reverse=True)
for i in range(30):
    print(top30_sci[i],":",found_words_sci[top30_sci[i]])
# printing results
print(f"Total: {disease_count1+drug_count1}")
print(f"Diseases: {disease_count1}, Drugs: {drug_count1}")

# As I was unable to successfully install BioBert I was unable to perform comparisons between the two methods