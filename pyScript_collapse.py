import os
import string
import numpy as np
import argparse
import dendropy
def main(args):
	"""
	collapse all the edges that have support values under certain value within the input trees 
	Parameters:
	-t1: The input trees
		the input unrooted trees to work on
	-n: The threshold
		for edges with local support values under this number will be collapsed
	-o: The output trees
		the tree with collapsed edges will be written to this file 
	"""
	
	estimatedPath = args.estimated
	threshold = args.num
	outputfile = args.outputfile
    #read the input unrooted trees
	tax = dendropy.TaxonNamespace()
	generated = dendropy.Tree.get(path=estimatedPath,
                                      schema="newick",
                                       rooting="force-unrooted",
                                     taxon_namespace = tax)


    
	all_bips = generated.encode_bipartitions()
	E_Map = generated.bipartition_edge_map
	#here we iterate through the entire bipartions
	for bip in all_bips :
		e = E_Map[bip]
		#here we found all the edges with local support values less than threshold and collapse them
		if (e.head_node).label is not None and float((e.head_node).label) < threshold:
			e.collapse()
	#write the result to the output file
	generated.write(path=outputfile, schema="newick")
        
        
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="tree and its output path")
	parser.add_argument("-t1", "--estimated", type=str,  required=True,
                        help="estimated")
	parser.add_argument("-n","--num",type=float, required=True, help="threshold")
	parser.add_argument("-o","--outputfile",type=str,required=True,help="outputfile")
	main(parser.parse_args())
