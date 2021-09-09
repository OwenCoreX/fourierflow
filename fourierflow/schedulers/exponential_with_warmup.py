import math

from torch.optim.lr_scheduler import LambdaLR

from fourierflow.registries.schedulers import Scheduler


class ExponentialLRLambda:
    def __init__(self, num_warmup_steps, gamma):
        self.num_warmup_steps = num_warmup_steps
        self.gamma = gamma

    def __call__(self, current_step):
        if current_step < self.num_warmup_steps:
            return float(current_step) / float(max(1, self.num_warmup_steps))

        progress = current_step - self.num_warmup_steps
        return self.gamma**progress


@Scheduler.register('exponential_with_warmup')
class ExponentialWithWarmupScheduler(Scheduler, LambdaLR):
    def __init__(self, optimizer, num_warmup_steps: int,
                 gamma=0.9999, last_epoch=-1, verbose=False):
        lr_lambda = ExponentialLRLambda(num_warmup_steps, gamma)
        super().__init__(optimizer, lr_lambda, last_epoch, verbose)
