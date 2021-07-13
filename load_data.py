import argparse
import json
import tabloo
import pandas as pd 

parser = argparse.ArgumentParser(description="load evaluation set")
parser.add_argument("--dataset",default="xsum")
parser.add_argument("--type",default="auto")
parser.add_argument("--run",default="0")
parser.add_argument("--subset",default="entity")
parser.add_argument("--level",default="0")
args = parser.parse_args()

#covers xsum, cnndm and samsum
if args.type == 'auto':
   root_ =  './auto_eval/' + args.dataset + '/' + args.subset + '/run' + args.run + '/' + 'transformed_' + args.level + '_' + args.dataset
   source = open(root_ + '.source').readlines() #articles
   target = open(root_ + '.target').readlines() #summaries 
   df = pd.DataFrame(list(zip(source,target)),columns=['Article','Summary'])
   tabloo.show(df)
elif args.type == 'random':
   root_ =  './auto_eval/' + args.dataset + '/'
   target = open(root_ + args.dataset + '_500_random' + '.txt').readlines() #summaries
   source = open(root_ + args.dataset + '_500_source' + '.txt').readlines() #articles
   df = pd.DataFrame(list(zip(source,target)),columns=['Article','Summary'])
   tabloo.show(df)
elif args.type == 'gold':
   root_ =  './auto_eval/' + args.dataset + '/'                                                              
   target = open(root_ + args.dataset + '_500_target' + '.txt').readlines() #summaries
   source = open(root_ + args.dataset + '_500_source' + '.txt').readlines() #articles
   df = pd.DataFrame(list(zip(source,target)),columns=['Article','Summary'])
   tabloo.show(df)
#note this covers xsum and samsum
elif args.type == 'human':
    root_ = [json.loads(l) for l in open('./human_eval/' + args.dataset + '.jsonl').readlines()]
    source = [d['article'] for d in root_]
    target = [d['summary'] for d in root_] 
    label =  [d['label'] for d in root_]
    errors = [d['errors'] for d in root_]
    df = pd.DataFrame(list(zip(source,target,label,errors)),columns=['Article','Summary','Label','Errors'])
    tabloo.show(df)
else:
    print('invalid type')
#implement a given metric 
