# REX_LR

Very simple REX learning rate scheduler based on paper “REX: Revisiting Budgeted Training with an Improved Schedule.” Proceedings of Machine Learning and Systems 4 (2022): 64–76.

Usage 

from lr_scheduler import REX_LR

lr_scheduler =REX_LR(optimizer, num_epochs=200,min_val =0.00001,max_val=0.0005)

Exampple plot for parameters num_epochs=400,min_val =0.00001,max_val=0.0005
![download](https://user-images.githubusercontent.com/66798159/155268802-9ca97195-1656-4d05-8acd-db0f9d70da93.png)

## Reference
[1] Chen, John, Cameron Wolfe, and Tasos Kyrillidis. “REX: Revisiting Budgeted Training with an Improved Schedule.” Proceedings of Machine Learning and Systems 4 (2022): 64–76.
https://arxiv.org/abs/2107.04197
