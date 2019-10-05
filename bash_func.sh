#!/bin/bash


alignment=$1
threshold=$2
outputfile=$3

logname="fastTree_temp_log.txt"
resultname="fastTree_temp_result.txt"
./FastTreeDbl -nt -gtr -log $logname <$alignment> $resultname
col_output="collapsed_fastTree.txt"
python3 pyScript_collapse.py -t1 $resultname -n $threshold -o $col_output
raxml_output="/projects/tallis/binghui2/pipeline"
threads=$(python3 pyScript_threads.py -a $alignment)
./raxmlHPC-PTHREADS-SSE3 -s $alignment -p 1 -g $col_output -w $raxml_output -m GTRGAMMA -T $threads -n collapsed_bestml
raxml_info=$raxml_output/RAxML_info.collapsed_bestml
python3 pyScript_info_collector.py -p $raxml_info > $outputfile


