"""
a simple code to train all models in same way
just get the name as input and run the training process.    
"""

from ultralytics import YOLO

def train_yolo_model(model_size = 'l',version='11'):
    model_size = model_size.lower()
    while model_size not in ['n','s', 'm', 'l', 'x']:
        print('model size must be s, m, l, x')
        model_size = input('model size: ').strip().lower()
    while version not in ['11','8']:
        print('version must be 11, 8, 10 ')
        version = input('version: ').strip()
    name = 'yolov'+ version + model_size + '.pt'
    model = YOLO(name)
    batch_size = -1
    if model_size =='n':
        batch_size = 16

    model.train(
        data="AI/yolo_configs/carDD.yaml",
        epochs=100,
        imgsz=640,
        batch=batch_size,
    )



if __name__ == '__main__':
    model_name = 'yolo'
    version = '8'
    model_size = 'n'
    if model_name=='yolo':
        train_yolo_model(model_size=model_size,version=version)