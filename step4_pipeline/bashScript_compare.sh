#!/bin/bash

truePath="/projects/tallis/binghui2/19fa/large_aligments/datasets"
fastPath="/projects/tallis/binghui2/19fa/large_aligments/double_fastTree"
RAxMLPath="/projects/tallis/binghui2/19fa/large_aligments/raxml_results"
RAfaPath="/projects/tallis/binghui2/19fa/large_aligments/refine_double_results"

echo "MODL,REPL,MTHD,NL,TRUE_NE,ESTI_NE,FN,FP,RF" >> compare_res.csv

for num in {1..5}
do
	for fig in {0..19}
	do
			fin_true=$truePath/500M$num/R$fig/rose.tt
			fin_fast=$fastPath/500M$num/R$fig/fasttree-double-bestml.tre
			fin_RAxML=$RAxMLPath/500M$num/R$fig/RAxML_bestTree.bestml
			fin_RAfa=$RAfaPath/500M$num/R$fig/RAxML_bestTree.refined_fasttree-double-bestml-fp-collapsed
			
			res1=$(python3 compare_trees.py -t1 $fin_true -t2 $fin_RAxML)
			csv_res1=${res1//" "/","}
			echo "500M$num,R$fig,RAxML,$csv_res1" >> compare_res.csv

			res2=$(python3 compare_trees.py -t1 $fin_true -t2 $fin_fast)
			csv_res2=${res2//" "/","}
			echo "500M$num,R$fig,FastTree-Dbl,$csv_res2" >> compare_res.csv

			res3=$(python3 compare_trees.py -t1 $fin_true -t2 $fin_RAfa)
			csv_res3=${res3//" "/","}
			echo "500M$num,R$fig,RAxML+fastTree,$csv_res3" >> compare_res.csv
	done
done
