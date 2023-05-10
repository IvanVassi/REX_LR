# REX_LR

Very simple REX learning rate scheduler based on paper “REX: Revisiting Budgeted Training with an Improved Schedule.” Proceedings of Machine Learning and Systems 4 (2022): 64–76.

Usage 

from lr_scheduler import REX_LR

lr_scheduler =REX_LR(optimizer, num_epochs=200,min_val =0.00001,max_val=0.0005)

