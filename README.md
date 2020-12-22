## Go-Figure: A Meta Evaluation of Factuality in Summarization

### Automatic evaluation data is in the following format:

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors}_{dataset}.source (gold articles) 

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors}_{dataset}.source (transformed summaries) 

Types are either "entity" or "verb"

Datasets are {samsum, cnndm, xsum}

### Human eval data is in the following format:

human_eval/samsum.csv 

human_eval/xsum.csv 

### The important keys for the csv headers:

- HITId

- Input.full_art (source article)

- Input.ref (gold summary)

- Answer.fact.1 (not factual) 

- Answer.fact.2 (factual)

- Answer.fact.3 (too incoherent to tell factuality) 

- Answer.select{i} (ith error/inconsistency found in summary) 

If you use this data in your work, please cite the following:

```
@inproceedings{Gabriel2020GoFigure,
title={Go-Figure: A Meta Evaluation of Factuality in Summarization},
author={Gabriel, Saadia and Celikyilmaz, Asli and Jha, Rahul and Choi, Yejin and Gao, Jianfeng},
year={2020},
}
```

### Current and upcoming contents of repo

- [x] Add automatic evaluation data (transformed summaries, upper/lower bounds) 
- [x] Add human evaluation data 
- [ ] Add general pipeline / analysis scripts for evaluating with various metrics 
