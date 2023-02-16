# A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning

The code repository for "[A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning](https://arxiv.org/abs/2205.13218)" (Accepted by ICLR'23 Spotlight ) in PyTorch. If you use any content of this repo for your work, please cite the following bib entry:

```
@misc{2205.13218,
Author = {Da-Wei Zhou and Qi-Wei Wang and Han-Jia Ye and De-Chuan Zhan},
Title = {A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning},
Year = {2022},
Eprint = {arXiv:2205.13218},
}
```

## Prerequisites
- [torch](https://github.com/pytorch/pytorch)
- [torchvision](https://github.com/pytorch/vision)
- [tqdm](https://github.com/tqdm/tqdm)
- [numpy](https://github.com/numpy/numpy)


## Training scripts
- Train CIFAR100
```
python main_memo.py -model memo -init 10 -incre 10 -ms 3312 -net memo_resnet32 -p fair -d 3 --train_base -d 0 1 2 3
```

## Acknowledgment
We thank the following repos providing helpful components/functions in our work.

- [PyCIL: A Python Toolbox for Class-Incremental Learning](https://github.com/G-U-N/PyCIL)
- [Deep Class-Incremental Learning: A Survey](https://github.com/zhoudw-zdw/CIL_Survey)

## Contact
If there are any questions, please feel free to contact with the author: Da-Wei Zhou (zhoudw@lamda.nju.edu.cn) and Qi-Wei Wang (wangqiwei@lamda.nju.edu.cn). Enjoy the code.