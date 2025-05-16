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
# 3. GTDB maker genes (MSA)
```
#first identify
gtdbtk identify --genome_dir upload/fna/ --out_dir identify3_output --extension fna --cpus 3 
#second align
gtdbtk align --identify_dir identify3_output/ --out_dir align3_output --cpus 3
```
This will produce ```concatenated_alignment``` which is used on future analysis.     
# 4. MEGA 12
1. Upload your MSA to MEGA 12 it will generate ```PhyloAnalysis_bgs.mdsx```          
2. Open phylogenetic analysis and upload .mdsx file, construct a maximum likelihood tree, use LG + G mode, ultrafast bootstrap 100. It will take some time, once the tree is generated, save the file as .newick file.           
3. To have a better visualization of the tree, open the newick file in iTOL.       

# 5. fastANI
```
fastANI --ql QUERY_LIST --rl REFERENCE_LIST -o so_fastani.out
```
