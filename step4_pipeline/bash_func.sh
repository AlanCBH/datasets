#!/bin/bash


alignment=$1
threshold=$2
resultname=$3
logname=$4
collapse_Path=$5
raxml_output=$6
add_info=$7
outputfile=$8

#logname="fastTree_temp_log.txt"
#resultname="fastTree_temp_result.txt"
if [ -s "$resultname" ]
then
	echo "have results"
else
	./FastTreeDbl -nt -gtr -log $logname <$alignment> $resultname
fi
col_output="$collapse_Path/$threshold-collapsed_fastTree.txt"
python3 pyScript_collapse.py -t1 $resultname -n $threshold -o $col_output
#raxml_output="/projects/tallis/binghui2/pipeline"
threads=$(python3 pyScript_threads.py -a $alignment)
./raxmlHPC-PTHREADS-SSE3 -s $alignment -p 1 -g $col_output -w $raxml_output -m GTRGAMMA -T $threads -n $threshold-collapsed_bestml
raxml_info=$raxml_output/RAxML_info.$threshold-collapsed_bestml
python3 pyScript_info_collector.py -p $raxml_info -n $threshold -a $add_info >> $outputfile


