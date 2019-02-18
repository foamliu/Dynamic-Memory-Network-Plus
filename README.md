# Dynamic Memory Network Plus
[DMN+](https://arxiv.org/abs/1603.01417) implementation in Pytorch for question answering on the bAbI 10k dataset.

Input Module for DMNPlus
![image](https://raw.githubusercontent.com/foamliu/Dynamic-Memory-Network-Plus/master/images/inputModule.png)

## Usage
### Download data 
Run the included shell script to fetch the data :
```bash
$ chmod +x fetch_data.sh
$ ./fetch_data.sh
```

### Train
```bash
$ python train.py
```

## Results
| Task ID | This Repo | Xiong et al |
| :---: | :---: | :---: |
| 1: single-supporting-fact | 100% | 100% |
| 2: two-supporting-facts | 95.6% | 99.7% |
| 3: three-supporting-facts | 85.0% | 98.9% |
| 4: two-arg-relations | 100% | 100% |
| 5: three-arg-relations | 99.5% | 99.5% |
| 6: yes-no-questions | 100% | 100% |
| 7: counting | 98.8% | 97.6% |
| 8: lists-sets | 100% | 100% |
| 9: simple-negation | 100% | 100% |
| 10: indefinite-knowledge | 100% | 100% |
| 11: basic-coreference | 100% | 100% |
| 12: conjunction | 100% | 100% |
| 13: compound-coreference | 100% | 100% |
| 14: time-reasoning | 98.6% | 99.8% |
| 15: basic-deduction | 100% | 100% |
| 16: basic-induction | 48.0% | 54.7% |
| 17: positional-reasoning | 87.9% | 95.8% |
| 18: size-reasoning | 97.0% | 97.9% |
| 19: path-finding | 99.7% | 100% |
| 20: agents-motivations | 100% | 100% |

### Demo
Download pre-trained DMN+ [Model](https://github.com/foamliu/Dynamic-Memory-Network-Plus/releases/download/v1.0/) then run:
```bash
$ python demo.py
```

## Reference
1. [Dynamic Memory Network for Visual and Textual Question Answering](https://arxiv.org/abs/1603.01417). 
2. https://github.com/dandelin/Dynamic-memory-networks-plus-Pytorch