"""
a simple code to evaluate all models in same way
just get the name as input and run the evaluation process.    
"""

from ultralytics import YOLO
import yaml
from glob import glob

from os.path import join,basename,exists
from os import mkdir
def evaluate_yolo11_model(yaml_path,weight_path):
    model = YOLO(weight_path)
    model.val(data=yaml_path,plots=True)

def predict_yolo11_model(weight_path,yaml_path,save_path='AI/evaluation_res/'):
    if not exists(save_path):
        mkdir(save_path)
        
    model = YOLO(weight_path)
    yaml_path = yaml.load(open(yaml_path, 'r'), Loader=yaml.FullLoader)
    img_path = join(yaml_path['path'], yaml_path['val'])
    with open(img_path, 'r') as f:
        imgs = f.readlines()
    imgs = [img.strip() for img in imgs]
    for img in imgs:
        results = model.predict(source=[img])
        name = basename(img)
        for result in results:
            result.save(filename=join(save_path,name))  # save to disk

if __name__ == '__main__':
    model_name = 'yolo11'
    predict = True
    weight_path = '/home/reza/Vision/ultralytics/runs/detect/train10/weights/best.pt'
    yolo_yaml  = '/home/reza/Vision/SoftWareDesign/Window/AI/yolo_configs/carDD.yaml'
    if not weight_path:
        weight_path = input("Enter the weight path: ")
    if not predict:
        if model_name=='yolo11':
            evaluate_yolo11_model(yolo_yaml,weight_path)
    else:
        if model_name == 'yolo11':
            predict_yolo11_model(weight_path,yolo_yaml)