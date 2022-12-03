from Bio import SeqIO
import pandas as pd

file_path = 'ncbi_dataset/data/GCA_000516895.1/GCA_000516895.1_LocustGenomeV1_genomic.fna'

count = 0
for seq_record in SeqIO.parse(file_path, 'fasta'):
	if len(seq_record.seq) >= 80000:
		count+=1
	if count == 11:
		r=SeqIO.write(seq_record, '11contig.fa', 'fasta')
		break
"fetch contig Done!"
