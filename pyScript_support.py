import os
import string
import numpy as np
import argparse
import dendropy
def main(args):
	estimatedPath = args.estimated
	truePath = args.true
	outputfile = args.outputfile
	des = args.description
	tax = dendropy.TaxonNamespace()
	generated = dendropy.Tree.get(path=estimatedPath,
                                      schema="newick",
                                       rooting="force-unrooted",
                                     taxon_namespace = tax)


	trueTree = dendropy.Tree.get(path=truePath,
                                    schema="newick",
                                    rooting="force-unrooted",
                                    taxon_namespace = tax)
	generated.encode_bipartitions()
	FalsePositives = dendropy.calculate.treecompare.find_missing_bipartitions(generated,trueTree)
	if ( len(FalsePositives) == 0 ):
		#print("None,None")
		return
    
	fptr = open(outputfile, "a")

	E_Map = generated.bipartition_edge_map
	support_values = {}
	for bip in FalsePositives:
		e = E_Map[bip]
		if (e.head_node).label is not None:
			support_values[bip] = float((e.head_node).label)
		else:
			support_values[bip] = 1.0
		fptr.write("%s,%s,%s\n"%(des,support_values[bip],e.length))	
		#print(support_values[bip],e.length)
	
	fptr.close()

		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Compares two trees and output path")
	parser.add_argument("-t1", "--estimated", type=str,  required=True,
                        help="estimated")
	parser.add_argument("-t2", "--true", type=str, required=True,
                        help="true")
	parser.add_argument("-d","--description",type=str,required=False,help="description")
	parser.add_argument("-o","--outputfile",type=str,required=True,help="outputfile")
	main(parser.parse_args())
