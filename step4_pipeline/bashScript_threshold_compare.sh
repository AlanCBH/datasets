#!/bin/bash

truepath="/projects/tallis/binghui2/step4_pipeline/datasets/1000M1"
estimatepath="/projects/tallis/binghui2/step4_pipeline/refine_results/1000M1"

echo "MODL,REPL,THRES,NL,TRUE_NE,ESTI_NE,FN,FP,RF" >> compare_thresholds_res.csv
for i in {0..19}
do
	fin_true=$truepath/R$i/rose.tt
	for thres in {0.5,0.8,0.9}
	do
		fin_esti=$estimatepath/R$i/RAxML_bestTree.$thres-collapsed_bestml
		res1=$(python3 compare_trees.py -t1 $fin_true -t2 $fin_esti)		
		csv_res1=${res1//" "/","}
		echo "1000M1,R$i,$thres,$csv_res1" >> compare_thresholds_res.csv
	done
done
