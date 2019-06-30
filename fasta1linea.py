#!/usr/bin/env python3
import sys
from Bio import SeqIO

inputfile = sys.argv[1]

seqdict = {}
for seq in SeqIO.parse( inputfile , "fasta" ):
    seqdict[seq.id] = seq.seq

for item in seqdict:

    print(">" + item )
    print( str( seqdict[item] ) )



