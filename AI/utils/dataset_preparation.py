from os.path import join,basename
from os import remove
from glob import glob
from  shutil import copy

class DatasetPreparator():
    
    def __init__(self) -> None:
        pass
    
       
    
    def move_text(main_src_path = '', main_dst_path = ''):
        """move texts from src to dst

        Args:
            main_src_path (str, optional): _description_. Defaults to ''.
            main_dst_path (str, optional): _description_. Defaults to ''.
        """
        if not main_src_path:
            main_src_path = input('Enter path to main folder...')
            
        if not main_dst_path:
            main_dst_path = input('Enter path to destionation folder...')

        texts = glob(main_src_path+'/*.txt')

        for txt in texts:
            name = basename(txt)
            copy(txt,join(main_dst_path,name))
            remove(txt)
    def create_yolo_txt(dataset_folder = 'AI/dataset'):        
        if not dataset_folder:
            dataset_folder = input('Enter path to main folder of the dataset...')
            
        val_path = join(dataset_folder,'validation')
        train_path = join(dataset_folder,'train')
        test_path = join(dataset_folder,'test')
            
        exts = ['*.png','*.jpeg','*.jpg','*.tbm']    

        # write validation.txt
        imgs = []
        for ext in exts:
            imgs.extend(glob(join(val_path,ext)))
        with open(join(dataset_folder,'validation.txt'),'w') as f:
            for img in imgs:
                f.write(img+'\n')
                
        # write test.txt
        imgs = []
        for ext in exts:
            imgs.extend(glob(join(test_path,ext)))
        with open(join(dataset_folder,'test.txt'),'w') as f:
            for img in imgs:
                f.write(img+'\n')
                
        # write train.txt
        imgs = []
        for ext in exts:
            imgs.extend(glob(join(train_path,ext)))
        with open(join(dataset_folder,'train.txt'),'w') as f:
            for img in imgs:
                f.write(img+'\n')
