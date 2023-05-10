import torch

class REX_LR(torch.optim.lr_scheduler._LRScheduler):
    def __init__(self, optimizer, max_val, min_val, num_epochs = 1, last_epoch=-1):
        self.num_epochs = num_epochs
        self.min_val = min_val
        self.max_val = max_val
        if  not self.min_val <= self.max_val:
            raise ValueError('Value of "min_val" should be less '
                             ' than value of "max_val". Got min_val='+str(min_val)+' and max_val='+str(max_val))
        

        super(REX_LR, self).__init__(optimizer, last_epoch)

    def get_lr(self):
        mod_iter = float(self.last_epoch % self.num_epochs)
        z = float(self.num_epochs- mod_iter) / self.num_epochs
        val = self.min_val + float(self.max_val - self.min_val) * (z / (1 - 0.9 + 0.9*z))
        return [val]
