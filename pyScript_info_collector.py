import os
import argparse
#des = open("C:/research/RAxML_info.txt","w+")
#des.write("MODL,REPL,TIME\n")
#for files in os.listdir("C:/research/RAxML_time"):
def main(args):
	filepath = args.path
	fp = open(filepath, 'r')
	line = fp.readline()
	while line:
		wordlist = line.split()
		if len(wordlist) and wordlist[0] == 'Overall':
			time = wordlist[6]
			#print("%s" %(wordlist[6]))
		if len(wordlist) and wordlist[0] == 'Final':
			log_like = wordlist[6]
			#print((wordlist[6]))
		if len(wordlist) and wordlist[0] == 'alpha[0]:':
			ac = wordlist[9]
			ag = wordlist[10]
			at = wordlist[11]
			cg = wordlist[12]
			ct = wordlist[13]
			gt = wordlist[14]
		line = fp.readline()
	print(time,log_like,ac,ag,at,cg,ct,gt)
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="RAxML_info_collector")
	parser.add_argument("-p","--path",type=str,required=True,help="alignment path")
	main(parser.parse_args())
