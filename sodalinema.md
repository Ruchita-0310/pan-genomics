# 1. Download genomes
```
nano GCA_list #add names of all GCA files
ncbi-genome-download --section genbank --formats fasta --assembly-accessions GCA_list bacteria --flat-output
nano GCF_list #add names of all GCF files
#ncbi-genome-download --formats fasta --assembly-accessions GCF_list bacteria --flat-outpu
```
# 2. Metaerg
```
\time singularity exec --bind /work/ebg_lab/referenceDatabases/metaerg_db_V214:/databases --bind /work/ebg_lab/gm/RS/sodalinema/fa:/data\
 --writable /work/ebg_lab/software/metaerg-v2.5.2/sandbox_metaerg_2.5.8/ metaerg --database_dir /databases --contig_file /data --file_extension .fa
```
Converts all .fa files to .fna files. Move fna files to fna folder. And re run metaerg with --mode comparative_genomics.          
# 3. Tree of MAGs
```
nano tree_of_mags.py
python3 tree_of_mags.py --dir /work/ebg_lab/gm/RS/sodalinema/fna
```
This will produce ```concatenated_alignment``` which is used on future analysis.     
# 4. iqtree2 - species tree
```
conda install bioconda::fasttree
FastTree concatenated_alignment > fasttree_file
```
# 5. fastANI
```
fastANI --ql QUERY_LIST --rl REFERENCE_LIST -o so_fastani.out
```
