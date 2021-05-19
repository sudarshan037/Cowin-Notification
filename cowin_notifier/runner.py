import json
import argparse
from pprint import pprint

#argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--develop', help='use this to run development code', action='store_true')
parser.add_argument('-p', '--prod', help='user this to run producation code', action='store_true')
args = vars(parser.parse_args())


#data preparation
develop_data = {
        'Sudarshan Choudhary': {'311022'}
        }
prod_data = None
dump = {}

with open("data/data.json", "r") as datafile:
    prod_data = json.load(datafile)
    for user in prod_data.keys():
        develop_data['Sudarshan Choudhary'] = develop_data['Sudarshan Choudhary'].union(set(prod_data[user]))
        dump[user] = {}

if __name__=='__main__':
    if args['develop']:
        from develop import develop_runner
        pprint(develop_data)
        develop_runner.runner(develop_data, dump)
    elif args['prod']:
        from prod import prod_runner
        pprint(prod_data)
        prod_runner.runner(prod_data, dump)
    else:
        print("help: use --develop or --prod arguments")

#add logging
