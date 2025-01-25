from os.path import join,basename,exists
from os import remove,mkdir

from natsort import natsorted
from glob import glob
from  shutil import copy
import cv2
import random
from copy import deepcopy
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
 
    def add_id(self,imgs_path,class_name = None):
        class_name ={
            0: "dent",
            1: "scratch",
            3: "glass shatter", 
            4: "lamp broken",
            5: "tire flat" ,
            2: "crack" ,
        } if not class_name else class_name
        colors = []
        for _ in range(100):
            colors.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        colors_dict ={
            str(i+1) : colors[i] for i in range(5)
        }
        color_counter = 5
        img_exts = ['*.png','*.jpeg','*.jpg','*.tbm']    
        imgs = []
        for ext in img_exts:
            imgs.extend(glob(join(imgs_path,ext)))
        imgs = natsorted(imgs)
        labels = [img[:-4]+'.txt' for img in imgs]
        if not exists(join(imgs_path,'base_labels')):
            mkdir(join(imgs_path,'base_labels'))
            for label in labels: copy(label,join(imgs_path,'base_labels',basename(label)))
        
        for (image_path, annotation_path) in zip(imgs,labels):
            img = cv2.imread(image_path)
            
            height, width, _ = img.shape
            with open(annotation_path) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            res = ''
            for annot in content:
                img_show = deepcopy(img)
                annot = annot.split()
                class_idx = annot[0]
                x,y,w,h = float(annot[1]),float(annot[2]),float(annot[3]),float(annot[4])
                bbox = ' '.join(annot[1:])
                xmin = int((x*width) - (w * width)/2.0)
                ymin = int((y*height) - (h * height)/2.0)
                xmax = int((x*width) + (w * width)/2.0)
                ymax = int((y*height) + (h * height)/2.0)
                if not colors_dict.get(class_idx,None):
                    colors_dict[class_idx] = colors[color_counter]
                    color_counter +=1
                
                cv2.rectangle(img_show, (xmin, ymin), (xmax, ymax), colors_dict[class_idx], 2)
                for i,c in enumerate(class_idx):
                    cv2.putText(img_show, class_name[int(c)], (xmin + i*60, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, colors_dict[class_idx], 2)
                
                k = -1                
                new_id = []
                while not (k ==ord('q') or k == 27):
                    cv2.imshow("image", img_show)
                    k =cv2.waitKey(0)        
                    if k in [49,50,51,52,53]:
                        new_id.append(str(k-48))
                new_id = list(set(new_id))
                new_id = natsorted(new_id)
                new_id = ''.join(new_id)
                new_id = class_idx if new_id=='' else new_id
                res += new_id +' ' + bbox + '\n'
            with open(annotation_path,'w') as f:
                f.write(res)
 
    def switch_id(path,class_id_map=None):
        """
        swithing ids in test/train/validation
        """
        class_id_map ={
            0: "0",
            1: "1",
            2: "3",
            3: "4",
            4: "5",
            5: "2",
        }if class_id_map is None else class_id_map
        for txt_path in glob(join(path,'*.txt')):
            with open (txt_path,'r') as f:
                lines = f.readlines()
            res = ''
            for line in lines:
                line = line.strip()
                class_id, x_min, y_min, x_max, y_max =  line.split()
                class_id = class_id_map[int(class_id)]
                res += class_id + ' ' + x_min +' ' +  y_min + ' ' +  x_max + ' ' + y_max + '\n'
            with open (txt_path,'w') as f:
                f.write(res)




