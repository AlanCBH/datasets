import os
import string
import numpy as np
import argparse
import dendropy
def main(args):
	estimatedPath = args.estimated
	threshold = args.num
	outputfile = args.outputfile
    
	tax = dendropy.TaxonNamespace()
	generated = dendropy.Tree.get(path=estimatedPath,
                                      schema="newick",
                                       rooting="force-unrooted",
                                     taxon_namespace = tax)


    
	all_bips = generated.encode_bipartitions()
	E_Map = generated.bipartition_edge_map
	#support_values = {}
	for bip in all_bips :
        #if bip not in FalsePositives:
		e = E_Map[bip]
		if (e.head_node).label is not None and float((e.head_node).label) < threshold:
			e.collapse()
			#print((e.head_node).label)
    
	generated.write(path=outputfile, schema="newick")
        
        
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="tree and its output path")
	parser.add_argument("-t1", "--estimated", type=str,  required=True,
                        help="estimated")
	parser.add_argument("-n","--num",type=float, required=True, help="threshold")
	parser.add_argument("-o","--outputfile",type=str,required=True,help="outputfile")
	main(parser.parse_args())
