# ECFVI : Error Compensation Framework for Flow-Guided Video Inpainting 

This repository is for ECFVI introduced in the following paper

Jaeyeon Kang, Seoung Wug Oh, and Seon Joo Kim. "Error Compensation Framework for Flow-Guided Video Inpainting ", ECCV 2022.


![Alt text](/imgs/overview.PNG)

## Dependencies

    Python>=3.6.8, Pytorch=1.6.1, CUDA version>= 10.1 


## Quickstart (DEMO)

1. Clone this github repo

       git clone https://github.com/JaeYeonKang/ECFVI
       cd ECFVI
        
        
 2. Place your test dataset on ./test
        
      frame_path = $DATA_DIR$ + $DATA_NAME$ + 'frames/'       
      &nbsp;&nbsp;&nbsp;&nbsp; ex) ./test/Youtube-VI/frames/' + %VIDEO_NAME%   
      mask_path = $DATA_DIR$ + $DATA_NAME$ + 'masks/'  
        
 
 3. Download our pretrained models from [link](https://drive.google.com/file/d/1SGU5RIIXzIdInLDQRQiZrU517BbQdSzX/view?usp=sharing). Then, place the weights in ./pretrained_weights
 
 
 4. Run demo
           
        CUDA_VISIBLE_DEVICES=0 python main.py --model network --trainer core.evaluation --version $SAVE_DIR$ \
        --test_data_name $DATA_NAME$ --test_data_root $DATA_DIR$ --mask_mode $MASK_MODE$ 
        
        
      + SAVE_DIR : path to save results
      + DATA_NAME : name of test dataset 
      + DATA_DIR : path to test dataset
      + MASK_MODE : for Youtube-VI dataset, mode:0 -> moving mask, mode:1 -> stationary mask
 
      For example,
        
        CUDA_VISIBLE_DEVICES=0 python main.py --model network --trainer core.evaluation --version DEMO \
        --test_data_name Youtube-VI --test_data_root ./test --mask_mode 0
        
        CUDA_VISIBLE_DEVICES=0 python main.py --model network --trainer core.evaluation --version DEMO \
        --test_data_name DAVIS_shadow --test_data_root ./test --davis
        
        
 ## Youtube Video Inpainting (Youtube-VI) dataset
 

You can download our Youtube-VI dataset from [link](https://drive.google.com/file/d/1aWXbSkzppXhlwlkVctsYrjm5pXDUvOAe/view?usp=sharing)


## Citation

If you use any part of this code in your research, please cite our paper

