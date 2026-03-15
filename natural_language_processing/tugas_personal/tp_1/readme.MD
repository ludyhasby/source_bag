# Entity Named Recognition 
Used in Natural Language Processing to identify and classify important information without unstructured text.

In this Program, we use SpaCy to help process this Named Entity Recognition (NER) to identify named entities like a person, names, organization, location, medical codes, time expressions, quantities, monetary value, percentages. Spacy has varios trained models, among them are the agile 'en_core_web_sm', the balanced 'en_code_web_md', and the robust 'en_core_web_lg'. These models, with their components like tokenization rules, Part-of-Speech Tagging, Named Entity Recognition, and more, form the bedrock of our exploration into unstructured data.

## Step 1 
Install and Import Libraries needed 
pip install spacy
import spacy
import pandas as pd

## Step 2 
Load The Pretrained Model, here we use the agile model. 
nlp = spacy.load("en_core_web_sm")

## Step 3 
Load the unstructured text 

## Step 4 
Extract Structured Information 

