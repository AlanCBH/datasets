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
	collapsed_count = 0
	generated = dendropy.Tree.get(path=estimatedPath,
                                      schema="newick",
                                       rooting="force-unrooted",
                                     taxon_namespace = tax)


    
	internal_edges = generated.internal_edges(exclude_seed_edge=True)
	collapse_count = 0
	for edge in internal_edges:
		if edge.head_node.label is not None and float((edge.head_node).label) <= threshold:
			edge.collapse()
			collapse_count += 1
		elif edge.head_node.label is None:
			edge.collapse()
			collapse_count += 1

	print(collapse_count)
	generated.write(path=outputfile, schema="newick")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="tree and its output path")
	parser.add_argument("-t1", "--estimated", type=str,  required=True,
                        help="estimated")
	parser.add_argument("-n","--num",type=float, required=True, help="threshold")
	parser.add_argument("-o","--outputfile",type=str,required=True,help="outputfile")
	main(parser.parse_args())
