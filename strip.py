import json
from pprint import pprint
import argparse

def strip(filename):
	with open(filename+".ipynb") as notebook_file:
		notebook_obj = json.load(notebook_file)
		for cell in notebook_obj["cells"]:
			if "outputs" in cell:
				cell["outputs"] = []
	with open("/mnt/c/Users/Liz/Documents/STARD/"+filename+"_stripped.ipynb", "w") as stripped_file:
		pprint(notebook_obj)
		json.dump(notebook_obj, stripped_file, indent=1)
	with open(filename+"_stripped.ipynb", "w") as stripped_file_test:
		json.dump(notebook_obj, stripped_file_test, indent=1)
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--filename", help="Specifies file to strip output from", type=str)
	args = parser.parse_args()

	if args.filename:
		strip(args.filename)
	else:
		print("Give me a file plox!!")

if __name__ == "__main__":
	main()
