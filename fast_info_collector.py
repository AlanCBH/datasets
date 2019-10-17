import os
import argparse
def main(args):
    path = args.path
    fp = open(path, 'r')
    line = fp.readline()
    #total,log_like,ac,ag,at,cg,ct,gt
    while line:
        wordlist = line.split()
        if len(wordlist) and wordlist[0] == 'Total' and wordlist[1] == 'time:':
            total = wordlist[2]
            #print("%s" %(wordlist[2]))
        if len(wordlist) and wordlist[0] == 'TreeLogLk' and wordlist[1] == 'ML_Lengths2':
            log_like = wordlist[2]
            #print((wordlist[6]))
        if len(wordlist) and wordlist[0] == 'GTRRates':
            ac = wordlist[1]
            ag = wordlist[2]
            at = wordlist[3]
            cg = wordlist[4]
            ct = wordlist[5]
            gt = wordlist[6]
            #print(wordlist[9],wordlist[10])
        line = fp.readline()
    print(total,log_like,ac,ag,at,cg,ct,gt)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reference and output trees")
    parser.add_argument("-p","--path",type=str,required=True,help="fastTree log path")
    main(parser.parse_args())
