from natsort import natsorted
import cv2
from glob import glob
from os.path import join, isdir,basename
class Visualize():
    def __init__(self,imgs_path,label_path,type='annotation',model='yolo',class_name = None):
        self.type=type
        self.imgs_path = imgs_path
        self.label_path = imgs_path if not label_path else label_path
        self.model = model
        self.class_name ={
            0: "dent",
            1: "scratch",
            2: "glass shatter", 
            3: "lamp broken",
            4: "tire flat" ,
            5: "crack" ,
        } if not class_name else class_name
        self.__initialize()
    def __initialize(self):
        img_exts = ['*.png','*.jpeg','*.jpg','*.tbm']    
        imgs = []
        imgs = natsorted(imgs)    
        for ext in img_exts:
            imgs.extend(glob(join(self.imgs_path,ext)))
        if isdir(self.label_path):
            self.show_dict = {}
            for i in imgs:
                self.show_dict[i] = join(self.label_path, basename(i)[:-4]+'.txt')
        else:
            self.show_imgs = imgs
 
                
        
    def visualize(self):
        if self.type =='annotation':
            if self.model == 'yolo':
                self.__vis_yolo_ann()
    def __vis_yolo_ann(self):
        
        color = (255,0,0)
        for (image_path, annotation_path) in self.show_dict.items():
            img = cv2.imread(image_path)
            height, width, _ = img.shape
            with open(annotation_path) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            for annot in content:
                annot = annot.split()
                class_idx = int(annot[0])
                x,y,w,h = float(annot[1]),float(annot[2]),float(annot[3]),float(annot[4])
                xmin = int((x*width) - (w * width)/2.0)
                ymin = int((y*height) - (h * height)/2.0)
                xmax = int((x*width) + (w * width)/2.0)
                ymax = int((y*height) + (h * height)/2.0)
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
                cv2.putText(img, self.class_name[int(class_idx)], (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, color, 2)

            cv2.imshow("image", img)
            k =cv2.waitKey(0)
            if k ==ord('q'): break
        print("Done")
        
        
if __name__ == '__main__':
    vis = Visualize(imgs_path='AI/dataset/train',label_path='AI/dataset/train',)
    vis.visualize()