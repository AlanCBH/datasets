#!/bin/bash
fastTree_Path="/projects/tallis/binghui2/19fa/large_aligments/double_fastTree"

for i in {1..5}
do
	for j in {0..19}
	do
		tree_file=$fastTree_Path/500M$i/R$j/fasttree-double-bestml.tre
		temp_file=/projects/tallis/binghui2/pipeline/temp_tree.txt
		python3 pyScript_collapse.py -t1 $tree_file -n 0.8 -o $temp_file
		echo $(python3 compare_trees.py -t1 $tree_file -t2 $temp_file) >> result.txt
	done
done

