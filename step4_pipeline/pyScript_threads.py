import dendropy
import numpy as np
import os
import sys
import string
import argparse

def main(args):
	alignmentPath = args.alignmentPath
	dna = dendropy.DnaCharacterMatrix.get(
            path=alignmentPath,
            schema="fasta")
	max_size = int(dna.max_sequence_size/500)
	if max_size > 12:
		max_size = 12
	print(max_size)
	return max_size

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="input path")
	parser.add_argument("-a","--alignmentPath",type=str,required=True)
	main(parser.parse_args())
