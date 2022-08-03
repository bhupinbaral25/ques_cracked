import argparse
from solution import Solution
import pandas as pd

def main():
    args = parseargs()
    
    columns_name = ['Name']
    df = pd.read_csv(args.txt, sep='|', names=columns_name)

    return pd.DataFrame(df)

def parseargs():
    parser = argparse.ArgumentParser(description='For File Reading')
    parser.add_argument('--txt', help='read txt file', default="sample_dictionary.txt")
    return parser.parse_args()


if __name__ == '__main__':

	ob1 = Solution()
	num_input = input("Enter the number: ")
	result_list = ob1.get_result(num_input)
	df = main()
	
	
	for result in result_list:
		print(df[(df["Name"].str.startswith(result))])