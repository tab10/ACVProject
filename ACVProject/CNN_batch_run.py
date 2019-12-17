"""
CNN_batch_run
Author: Tim Burt
This is a batch script which can run multiple CNN models with different parameters on your local machine
(learning rate, batch size, train_test_ratio, epoch) -> assumed constant
"""

import os
import time

start_time = time.time()

##############################################################################
print("affine data, heart_only, 16 z-slice averaged (16 ch), resnet 18 (wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 18 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=16 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 18 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=16 --epoch 25")

print("affine data, heart_only, 8 z-slice averaged (32 ch), resnet 34 (super wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 34 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=8 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 34 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=8 --epoch 25")

# print("affine data, heart_only, 4 z-slice averaged (64 ch), resnet 50 (mega wide)")
# os.system("python CNN_main.py --phase train --dataset ACV --res_n 50 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")
# os.system("python CNN_main.py --phase test --dataset ACV --res_n 50  --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")

print("affine data, heart_only, 4 z-slice averaged (64 ch), resnet 101 (ultra wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 101 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 101 --use_lung_mask --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")

##############################################################################
#print("affine data, no mask, 16 z-slice averaged (16 ch), resnet 18 (wide)")
#os.system("python CNN_main.py --phase train --dataset ACV --res_n 18 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=16 --epoch 25")
#os.system("python CNN_main.py --phase test --dataset ACV --res_n 18 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=16 --epoch 25")

print("affine data, no_mask, 8 z-slice averaged (32 ch), resnet 34 (super wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 34 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=8 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 34  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=8 --epoch 25")

# print("affine data, no_mask, 4 z-slice averaged (64 ch), resnet 50 (mega wide)")
# os.system("python CNN_main.py --phase train --dataset ACV --res_n 50 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")
# os.system("python CNN_main.py --phase test --dataset ACV --res_n 50  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")

print("affine data, no_mask, 4 z-slice averaged (64 ch), resnet 101 (ultra wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 101 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 101  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type affine --n_axial_channels=4 --epoch 25")

##############################################################################
print("projection data, no mask, 16 z-slice averaged (16 ch), resnet 18 (wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 18 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=16 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 18 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=16 --epoch 25")

print("projection data, no_mask, 4 z-slice averaged (64 ch), resnet 18 (mega wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 18 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 18  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")

print("projection data, no_mask, 8 z-slice averaged (32 ch), resnet 34 (super wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 34 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=8 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 34  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=8 --epoch 25")

# print("projection data, no_mask, 4 z-slice averaged (64 ch), resnet 50 (mega wide)")
# os.system("python CNN_main.py --phase train --dataset ACV --res_n 50 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")
# os.system("python CNN_main.py --phase test --dataset ACV --res_n 50  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")

print("projection data, no_mask, 4 z-slice averaged (64 ch), resnet 101 (ultra wide)")
os.system("python CNN_main.py --phase train --dataset ACV --res_n 101 --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")
os.system("python CNN_main.py --phase test --dataset ACV --res_n 101  --train_test_ratio 70_30 --batch_size 40 --lr 0.1 --data_type projection --n_axial_channels=4 --epoch 25")


end_time = time.time()
tot_time = (end_time - start_time) / 60.0
print("Completed tasks. Elapsed time: %5.2f min" % tot_time)