#!/bin/bash
for size in M 
do
	for num in 1
	do
		#mkdir collapse_results/1000$size$num
		#mkdir raxml_results/1000$size$num
		mkdir refine_results/1000$size$num
		for dir_num in {0..19}
		do
			
			#mkdir collapse_results/1000$size$num/R$dir_num
			#mkdir raxml_results/1000$size$num/R$dir_num
			mkdir refine_results/1000$size$num/R$dir_num
			#rm branch_boxplots/100$size$num/R$dir_num/branch_boxplots.txt
			#touch double_fastTree/100$size$num/R$dir_num/bestMLgenetree.rerooted.fixed.final
			#touch fastTree_results/1000$size$num/R$dir_num/log.txt
			#touch fastTree_results/1000$size$num/R$dir_num/fasttree-double-bestml.tre
		done
	done
done
