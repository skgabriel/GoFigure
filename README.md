## GO FIGURE: A Meta Evaluation of Factuality in Summarization

### Interactive data viewing of evaluation datasets 

To view auto-generated data: 

python load_data.py --type "auto" --dataset "xsum" --run 0 --subset "entity" --level 0 

To view human-annotated data:

python load_data.py --type "human" --dataset "xsum" 

Options for dataset: xsum, cnndm, samsum

Options for subset: entity, verb

Types of labels for human-annotated data: factual, not factual, too incoherent 

For upper/lower bounds, use either "gold" or "random" for type respectively 

### Automatic evaluation data files are in the following formats:

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors-1}_{dataset}.source (gold articles)

auto_eval/{dataset}/{type}/run{num}/transformed_{max_errors-1}_{dataset}.target (transformed summaries)

If you use this data in your work, please cite the following:

```
@inproceedings{Gabriel2021GoFigure,
title={GO FIGURE: A Meta Evaluation of Factuality in Summarization},
author={Gabriel, Saadia and Celikyilmaz, Asli and Jha, Rahul and Choi, Yejin and Gao, Jianfeng},
booktitle={Findings of ACL},
year={2021},
}
```
