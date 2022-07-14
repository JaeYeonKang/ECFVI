import os
import argparse
import importlib

import torch


parser = argparse.ArgumentParser(description='ECFVI')
parser.add_argument('-v', '--version', default='DEMO', type=str)
parser.add_argument('-m', '--model', default='network', type=str)
parser.add_argument('--trainer', default='trainer', type=str)
parser.add_argument('--save_dir', default='release_model/', type=str)


# Test setting
parser.add_argument('--data_name', default='Youtube-VI', type=str, help='Youtube-VI or DAVIS_shadow or DAVIS')
parser.add_argument('--test_data_root', default='./test/', type=str)
parser.add_argument('--davis', action='store_true', help='For object removal')
parser.add_argument('--test_w', default=432, type=int)
parser.add_argument('--test_h', default=240, type=int)
parser.add_argument('--save_img', default=1, type=int)
parser.add_argument('--mask_mode', default=0, type=int, help='0: moving, 1: stationary for Youtube-VI')


parser.add_argument('--neighbor_len', default=5, type=int, help='neighbor length for LTN')
parser.add_argument('--non_key_len', default=3, type=int, help='non key length for ECN')
parser.add_argument('--max_len', default=8, type=int, help='due to memory issue for ECN')

# Error Compensation Network
parser.add_argument('--dilation_iter', default=17, type=int)
parser.add_argument('--stack_num', default=8, type=int)
parser.add_argument('--patch_size_num', default=5, type=int)
parser.add_argument('--channels', default=64, type=int)


# Flow Completion
parser.add_argument('--small', action='store_true', help='use small model')
parser.add_argument('--mixed_precision', action='store_true', help='use mixed precision')
parser.add_argument('--alternate_corr', action='store_true', help='use efficent correlation implementation')



args = parser.parse_args()


if __name__ == "__main__":
        
    args.save_dir = os.path.join(args.save_dir, '{}'.format(args.version))
    os.makedirs(args.save_dir, exist_ok=True)
    print('[**] create folder {}'.format(args.save_dir))
    args.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                                           
    mod = importlib.import_module(args.trainer)
    trainer = getattr(mod, 'Trainer')(args)
    trainer.eval()

