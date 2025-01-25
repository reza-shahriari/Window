from natsort import natsorted
import cv2
from glob import glob
from os.path import join, isdir,basename
from random import randint
from ultralytics.data.utils import visualize_image_annotations
import matplotlib.pyplot as plt
class VisualizeImg():
    def __init__(self,imgs_path,label_path,type='annotation',model='yolo',custom_vis=False,class_name = None):
        self.type=type
        self.imgs_path = imgs_path
        self.label_path = imgs_path if not label_path else label_path
        self.model = model
        self.class_name ={
            0: "dent",
            1: "scratch",
            3: "glass shatter", 
            4: "lamp broken",
            5: "tire flat" ,
            2: "crack" ,
        } if not class_name else class_name
        self.custom_vis = custom_vis
        self.__initialize()
    def __initialize(self):
        img_exts = ['*.png','*.jpeg','*.jpg','*.tbm']    
        imgs = []
        for ext in img_exts:
            imgs.extend(glob(join(self.imgs_path,ext)))
        imgs = natsorted(imgs)    
        if isdir(self.label_path):
            self.show_dict = {}
            for i in imgs:
                self.show_dict[i] = join(self.label_path, basename(i)[:-4]+'.txt')
        else:
            self.show_imgs = imgs
        self.colors = {}
        for k in self.class_name.keys():
            self.colors[k] = (randint(0,255),randint(0,255),randint(0,255))
                
    def visualize(self):
        if self.type =='annotation':
            if self.model == 'yolo':
                if self.custom_vis:
                    self.__vis_custom_yolo_ann()
                else:
                    self.__vis_yolo_ann()
    def __vis_yolo_ann(self):
        for (image_path, annotation_path) in self.show_dict.items():
            visualize_image_annotations(image_path, annotation_path, self.class_name,)
    
    def __vis_custom_yolo_ann(self):
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
                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), self.colors[class_idx], 2)
                cv2.putText(img, self.class_name[class_idx], (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX,0.5, self.colors[class_idx], 2)
            cv2.imshow("image", img)
            k =cv2.waitKey(0)                
            if k ==ord('q'): break
        print("Done")
        
class PlotBenchmark():
    def __init__(self,path):
        self.path = path
        self.beautiful_colors = [
            (158, 1, 66),
            (213, 62, 79),
            (244, 109, 67),
            (253, 174, 97),
            (254, 224, 139),
            (230, 245, 152),
            (171, 221, 164),
            (102, 194, 164),
            (50, 136, 189),
            (94, 79, 162)
        ]
        self.beautiful_colors = [(r/255, g/255, b/255) for r,g,b in self.beautiful_colors]
        self.models=[]
        self.map30_scores = []
        self.runtimes = []
    def _load_data(self):
        with open(self.path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) != 3:
                    continue
                model, map30, runtime = parts
                self.models.append(model)
                self.map30_scores.append(float(map30))
                self.runtimes.append(float(runtime))
        
    def plot_model_performance(self, output_file="AI/bechmark/model_performance.png"):
        self._load_data()

        colors = {}        
        for model in self.models:
            if model not in colors:
                if len(self.beautiful_colors):
                    colors[model] =  self.beautiful_colors.pop(0)


                else:
                    colors[model] = (randint(1,255)/255, randint(1,255)/255, randint(1,255)/255)
        plt.figure(figsize=(12, 8))
        for i, model in enumerate(self.models):
            plt.scatter( self.runtimes[i],self.map30_scores[i], c=colors[model], label=model if model not in plt.gca().get_legend_handles_labels()[1] else "", s=200)

        plt.title("Model Performance: mAP@30 vs Runtime", fontsize=16, loc='left')
        plt.ylabel("mAP@30", fontsize=12)
        plt.xlabel("Runtime (ms)", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.legend(loc="lower right", fontsize=10, title="Models")
        plt.tight_layout()
        plt.savefig(output_file)
        plt.show()
    

if __name__ == '__main__':
    ploter = PlotBenchmark(path = 'AI/bechmark/res.tsv')
    ploter.plot_model_performance()