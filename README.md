## GO FIGURE: A Meta Evaluation of Factuality in Summarization

### Automatic evaluation data files are in the following formats:

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors-1}_{dataset}.source (gold articles) 

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors-1}_{dataset}.target (transformed summaries) 

Types are either "entity" or "verb"

Datasets are {samsum, cnndm, xsum}

The original data files are under auto_eval/{dataset}/{dataset}_500_source.txt and auto_eval/{dataset}/{dataset}_500_target.txt

Each line is an article or summary 

### Human eval data:

human_eval/samsum.csv 

human_eval/xsum.csv

Each row is a set of annotations 

### The column keys for the csv headers:

- Inputs 

  - Input.full_art (source article)

  - Input.ref (gold summary)
  
- Annotations 

  - Answer.fact.1 (factual) 

  - Answer.fact.2 (not factual)

  - Answer.fact.3 (too incoherent to tell factuality) 

  - Answer.select{i} (ith error found in summary) 

If you use this data in your work, please cite the following:

```
@inproceedings{Gabriel2021GoFigure,
title={GO FIGURE: A Meta Evaluation of Factuality in Summarization},
author={Gabriel, Saadia and Celikyilmaz, Asli and Jha, Rahul and Choi, Yejin and Gao, Jianfeng},
booktitle={Findings of ACL},
year={2021},
}
```

---

### Current and upcoming contents of repo

- [x] Automatic evaluation data (transformed summaries, upper/lower bounds) 
- [x] Human evaluation data 
- [ ] General pipeline / analysis scripts for evaluating with various metrics 
