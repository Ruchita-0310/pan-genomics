# 1. create database
```
nput_dir="/Users/ruchitasolanki/Downloads/fna"
output_dir="/Users/ruchitasolanki/Downloads/fna"

for file in "$input_dir"/*.fna; do
	base=$(basename "$file" .fna)
	output_fasta="$output_dir/${base}_contigs.fa"
	report_file="$output_dir/${base}_report.txt"
	db_file="$output_dir/${base}.db"

	anvi-script-reformat-fasta "$file" -o "$output_fasta" --simplify-names --report-file "$report_file" --seq-type NT
	anvi-gen-contigs-database -f "$output_fasta" -o "$db_file"
done
```
# 2. annotate the database
```
anvi-run-ncbi-cogs -c contig.db --search-with blastp  --num-threads 8
anvi-run-hmms -c contig.db -T 1
anvi-run-pfams -c contig.db -T 40
anvi-run-scg-taxonomy -c contig.db -T 40
anvi-run-kegg-kofams -c contig.db -T 40
```
# 3. external genomes-storage database 
```
#create external-genomes.txt a tab delimited file with name of the contigs and its path
anvi-get-sequences-for-hmm-hits -external-genomes external-genomes.txt -o concatenated-proteins_Bacteria_71.fa --hmm-source Bacteria_71 --return-best-hit --get-aa-sequences --concatenate
```
# 4. pangenomics
```
anvi-gen-genomes-storage -e external-genomes.txt -o GENOMES.db
anvi-pan-genome -g GENOMES.db --project-name "Pan" --output-dir Pan --num-threads 40 --minbit 0.5 --mcl-inflation 10
# prepare a file named "misc-data-layers.txt" which includes the category of the samples, like this:
samples categorical
contig_name        c1
contig_name        c1
#then import the category into the pangenome
anvi-import-misc-data -p Pan/Pan-PAN.db -t layers misc-data-layers.txt
#then calculate the functional enrichment of each gene based on COG20 annotation
anvi-compute-functional-enrichment-in-pan -g GENOMES.db -p Pan/Pan-PAN.db --category categorical --annotation-source COG20_FUNCTION -o enriched-functions.txt
```
