import pandas as pd 
import numpy as np
import spacy
from spacy import displacy
import re
from functions import *

import os

#Load the spacy english language model into a variable
nlp = spacy.load("en_core_web_sm")

# read characters file
characters_path = os.path.join(os.path.dirname(__file__), '..', '..','data','interim',' characters.csv')
characters_df = pd.read_csv(characters_path)

#remove Mr and Mrs from the names
characters_df['character'] = characters_df['character'].str.replace(r'\b(Mr|Mrs)\.?\s', '', regex=True)
#remove all bracketed words from the characters df
characters_df['character'] = characters_df['character'].apply(lambda x: re.sub("[\(].*?[\)]", "", x))
# create a firstname column for the characters
characters_df['firstname'] = characters_df['character'].apply(lambda x: x.split(' ', 1)[0])
#drop unwanted columns
characters_df.drop(['Unnamed: 0', 'letter'], axis=1, inplace=True)

# save processed data frame
path= os.path.join(os.path.dirname(__file__), '..', '..','data','processed','harry_potter_characters.csv')
characters_df.to_csv(path)

#load up paths of harry potter book files from the data folder into a list
path = os.path.join(os.path.dirname(__file__), '..', '..','data','external')
all_books = [book for book  in os.scandir(path) if '.txt' in book.name]

#initialize an empty dataframe to accept all the character relationships
all_character_relationships =pd.DataFrame(columns=['source', 'target', 'value'])

#loop through all the books, one at a time
for book in all_books:
    book_text = open(book).read()
    nlp.max_length = len(book_text) + 100
    book_doc = nlp(book_text)
    book_title = book.name
    
    #loop through sentences and store the named entity list for each sentence
    sentence_entity_df= named_entities_per_sentence(book_doc)
    
    #filter sentence entity to select only character entities
    sentence_entity_df['character_entities'] = sentence_entity_df['entities'].apply(lambda x: filter_entity(x, characters_df))

    #remove sentences without named entities
    sentence_entity_df_filtered = sentence_entity_df[sentence_entity_df['character_entities'].map(len)>0]
        
    # Take only first name of characters
    sentence_entity_df_filtered['character_entities'] = sentence_entity_df_filtered['character_entities'].apply(lambda x: [item.split()[0] for item in x])
        
    #potter = harry
    sentence_entity_df_filtered['character_entities'] = sentence_entity_df_filtered['character_entities'].apply(lambda x: [item.replace('Potter', 'Harry') for item in x])
        
    #create character relationships
    character_relationships_df = create_relationships(df=sentence_entity_df_filtered, window_size=5)
    
    #add relationships from this book to the all character relationships dataframe
    pd.concat([all_character_relationships, character_relationships_df])
    
    # save the character relationships for each book into an appropriately named csv    
    name = book_title.replace('txt','')
    path =  os.path.join(os.path.dirname(__file__), '..', '..','data','processed', name +'csv')
    character_relationships_df.to_csv(path)

path =  os.path.join(os.path.dirname(__file__), '..', '..','data','processed', 'all_relationships.csv')
all_character_relationships.to_csv(path)