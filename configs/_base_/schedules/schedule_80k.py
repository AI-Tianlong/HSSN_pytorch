# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.00005)
optimizer_config = dict()
# learning policy
lr_config = dict(policy='poly', power=0.9, min_lr=5e-5, by_epoch=False)
# runtime settings
runner = dict(type='IterBasedRunner', max_iters=80000)
checkpoint_config = dict(by_epoch=False, interval=100)
evaluation = dict(interval=100, metric='mIoU')
# checkpoint_config = dict(by_epoch=False, interval=8000)
# evaluation = dict(interval=8000, metric='mIoU')