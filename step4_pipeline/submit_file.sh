#!/bin/bash
for i in {0..19}
do
	qsub -F $i collapse_test.pbs
done
