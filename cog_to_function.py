import csv
import re
import openpyxl
from openpyxl.utils.exceptions import IllegalCharacterError
import unicodedata # Added import
import pandas as pd
input = '/Users/Downloads/fna/enrichment/clade_3.csv'
output = '/Users/Downloads/fna/enrichment/fucntions_clade_3.csv'
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Transformed Data"
headers = ["ProteinName", "COG", "Value"]
sheet.append(headers)

processed_row_count = 0
output_line_count = 0

with open(input, mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    next(reader, None) # Uncomment to skip header row in CSV if present
    data_frame = pd.DataFrame(columns=['ID','COG','value'])

    for i, row_parts in enumerate(reader):
        if not row_parts:
            print(f"Info: Skipping empty CSV row at line {i+1}.")
            continue
        # print(row_parts)
        id_parts = row_parts[0].split('!!!')
        # print(id_parts)
        cog_parts = row_parts[2].split('!!!')
        # print(cog_parts)
        for i, id in enumerate(id_parts):
            id_split = id.split('(')
            if len(id_split) < 2:
                print("Skipping weird entry:")
                print(id)
                continue
            id_short = id_split[1].split(')')[0]
            # print("id_short")
            # print(id_short)
            data_frame.loc[len(data_frame)] = [id_short, cog_parts[i], row_parts[1]]
# print(data_frame)
data_letter_to_desc = {
    'COG_Category_Letter': ['J', 'A', 'K', 'L', 'B', 'D', 'Y', 'V', 'T', 'M', 'N', 'Z', 'W', 'U', 'O', 'C', 'G', 'E', 'F', 'H', 'I', 'P', 'Q', 'R', 'S', 'X'],
    'General_Function_Description': [
        'Translation, ribosomal structure and biogenesis', 'RNA processing and modification', 'Transcription',
        'Replication, recombination and repair', 'Chromatin structure and dynamics', 'Cell cycle control, cell division, chromosome partitioning',
        'Nuclear structure', 'Defense mechanisms', 'Signal transduction mechanisms', 'Cell wall/membrane/envelope biogenesis',
        'Cell motility', 'Cytoskeleton', 'Extracellular structures', 'Intracellular trafficking, secretion, and vesicular transport',
        'Posttranslational modification, protein turnover, chaperones', 'Energy production and conversion', 'Carbohydrate transport and metabolism',
        'Amino acid transport and metabolism', 'Nucleotide transport and metabolism', 'Coenzyme transport and metabolism',
        'Lipid transport and metabolism', 'Inorganic ion transport and metabolism', 'Secondary metabolites biosynthesis, transport and catabolism',
        'General function prediction only', 'Function unknown', 'Mobilome: prophages, transposons'
    ]
}
letter_to_desc_map = pd.DataFrame(data_letter_to_desc)

print(letter_to_desc_map)
with open("/Users/Downloads/fna/enrichment/cog_id_map.csv", mode='r', encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    id_cog_letter_map = pd.DataFrame(columns=['ID','COG','LETTER','DESC'])
    
    for i, row_parts in enumerate(reader):
        letter = row_parts[2]
        if len(letter) > 1:
            letter = letter[0]
        id_cog_letter_map.loc[len(id_cog_letter_map)] = [row_parts[0], row_parts[1], row_parts[2], letter_to_desc_map[letter_to_desc_map["COG_Category_Letter"] == letter].values[0][1]]
  output_df = pd.merge(
    data_frame.reset_index(),
    id_cog_letter_map)

print(output_df)
output_df.to_excel(output, index=False)
