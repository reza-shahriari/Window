"""
a simple code to train all models in same way
just get the name as input and run the training process.    
"""

from ultralytics import YOLO

def train_yolo11_model():
    model = YOLO('yolo11s')
    model.train(
        data="AI/yolo_configs/carDD.yaml",
        epochs=100,
        imgsz=640,
    )



if __name__ == '__main__':
    model_name = 'yolo11'
    if model_name=='yolo11':
        train_yolo11_model()