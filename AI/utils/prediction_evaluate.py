"""
Evaluates a detection model using the specified YAML configuration file and weight path.

Args:
    yaml_path (str): Path to the YAML configuration file.
    weight_path (str): Path to the model weight file.
    pred (bool, optional): If True, performs prediction instead of evaluation. Defaults to False.
    save_path (str, optional): Path to save the evaluation results. Defaults to None.
"""

from ultralytics import YOLO,RTDETR
import yaml
from glob import glob
from os.path import join,basename,exists
from os import mkdir

class eval_pred():
    def __init__(self,model_name,yaml_path,weight_path,pred=False,save_path=None):
        self.model = self._model_name_cnv(model_name,weight_path)
        self.pred = pred
        self.yaml_path=yaml_path
        self.save_path = 'AI/dataset/0/res'
    def _model_name_cnv(self,model_name,weight_path):
        if 'yolo' in model_name.lower().strip():
            return YOLO(weight_path)
        if 'rt-detr' in model_name.lower().strip():
            return RTDETR(weight_path) 
    def __call__(self,):
        if self.pred:
            should_save=False
            if self.save_path:
                should_save=True            
            if should_save and not exists(self.save_path):
                mkdir(self.save_path)

            yaml_path = yaml.load(open(self.yaml_path, 'r'), Loader=yaml.FullLoader)
            img_path = join(yaml_path['path'], yaml_path['val'])
            with open(img_path, 'r') as f:
                imgs = f.readlines()
            imgs = [img.strip() for img in imgs]
            for img in imgs:
                if not exists(img): continue
                results = self.model.predict(source=[img])
                name = basename(img)
                if should_save:
                    for result in results:
                        result.save(filename=join(self.save_path,name))  # save to disk
        else:
            self.model.val(data=self.yaml_path,plots=True,verbose=True,cache=False)


if __name__ == '__main__':
    # model_name = input('enter model\'s name(yolo,rt-detr)').lower().strip()
    model_name = 'yolo8'
    predict = True
    # weight_path = input("Enter the weight path: ")    
    weight_path = 'AI/checkpoints/yolo8M.pt'
    yolo_yaml  = 'AI/yolo_configs/carDD.yaml'
    # s = input('enter yaml path(d for defult)')
    # if s.lower().strip() =='d':yolo_yaml=s 
    # pred = input('Choose mode - [1] Predict or [2] Evaluate: ').strip() == '1'   
    pred=True
    ev = eval_pred(model_name=model_name,yaml_path=yolo_yaml,weight_path=weight_path,pred=pred)
    ev()