# REX_LR from the paper REX: Revisiting Budgeted Training with an Improved Schedule

Very simple REX learning rate scheduler based on paper “REX: Revisiting Budgeted Training with an Improved Schedule" [1].

Usage 
```
from lr_scheduler import REX_LR

lr_scheduler = REX_LR(optimizer, num_epochs=200, min_val = 0.00001, max_val = 0.0005)
```
Exampple plot for parameters num_epochs=400,min_val =0.00001,max_val=0.0005
![download](https://github.com/IvanVassi/REX_LR/blob/af8bab5ad4697889f25dc22453064b856a639f85/sample_img/sample_plot_REX_lr_scheduler.png)

## Acknowledgments
[Cameron R. Wolfe](https://github.com/wolfecameron)

## Reference
[1] Chen, John, Cameron Wolfe, and Tasos Kyrillidis. [“REX: Revisiting Budgeted Training with an Improved Schedule.”](https://arxiv.org/abs/2107.04197) Proceedings of Machine Learning and Systems 4 (2022): 64–76.

