# 1. [Roary](https://sanger-pathogens.github.io/Roary/)
```
conda create -n roary
conda activate roary
conda install roary
conda install prokka
coonda install -c bioconda iqtree
```
[Prokka](https://github.com/tseemann/prokka) and IQ-Tree2 don't come with roary, so install it seperately.    
Prokka is the annotator and IQ-Tree is used to generate a tree file.      
```
for sample in DL1_bin26.fa GCA_003566575.fna GCA_020386575.fna GCF_023983615.fna \
               GCA_001314905.fna GCA_004299065.fna GCF_009846485.fna PL4_bin13.fa \
               GCA_001637315.fna GCA_007131565.fna GCF_012911965.fna
do
  base=$(basename "$sample" .fna)
  base=$(basename "$base" .fa) 
prokka --kingdom Bacteria --outdir prokka_"$base" --genus Sodalinema  "$sample"
```
Basically run it in a loop.    
Move all .gff files to gff folder. Name the files differently as the names are the same. You could use a different annotator but roary will only accept prokka created gff files.     
```
roary -f ./output -e -n -v gff/*.gff
```
Roary outputs:       
1. summary_statistics.txt: Number of genes in the core and accessory.
2. gene_presence_absence.csv: gene presence and absence spreadsheet lists each gene and which samples it is present in.
3. core_gene_alignment.aln: use this file to create a tree file.
To generating a tree file         
```
iqtree -s core_gene_alignment.aln 
```        
Output: .treefile: the ML tree in NEWICK format, which can be visualized by any supported tree viewer programs like FigTree or iTOL.                            
Tree is UNROOTED. In iTOL, re-root the tree, and download the new tree file.         
Visulalization: using roary_plots.py. You can run it in your own terminal.                 
```
python3 roary.py newick.txt gene_presence_absence.csv   
```

