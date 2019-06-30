#!/usr/bin/env python3

import sys

print( "\nRunning {0}...".format( sys.argv[0] ) )

oldMap = sys.argv[1]
newMap = sys.argv[2]

output = sys.argv[3]


d = {}
with open( newMap , 'r' ) as handle:


    for line in handle:
        
        chromosome, snpName, cM, pos = line.split()

        d[snpName] = [ chromosome, cM, pos ]


with open( oldMap , 'r' ) as old:
    with open( output, 'w' ) as out:

        modifiableChr = ["30", "31", "32", "33"]
        chrDict = {
                "30":"X",
                "31":"Y",
                "32":"30",
                "33":"MT"
                }

        for line in old: 
            old_chr, old_id, old_cm, old_pos = line.split()

            new_chr, new_cm, new_pos = d[old_id]
            new_cm = 0 # i dont need this for now
            if new_chr in modifiableChr:
                new_chr = chrDict[ new_chr  ]
                       


            out.write( "{0} {1} {2} {3}\n".format(new_chr, old_id, new_cm, new_pos  ) )

print( "--> Success...\n\n" )
