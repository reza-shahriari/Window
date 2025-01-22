"""
a simple code to train all models in same way
just get the name as input and run the training process.    
"""

class Detection_model:
    def __init__(self,model_name,model_size,model_version='',weight_path=None):
        self.model_name = model_name.lower()
        self.model_size = model_size.lower()
        self.model_version = model_version
        self.weight_path = weight_path 
        self.model = self.initialize_model()
        self.batch_size = 16 if self.model_size == 'n' else -1
        self.epochs = 100
        self.imgsz=640
        self.data_path = "AI/yolo_configs/carDD.yaml"
    def initialize_model(self):
        if self.model_name =='yolo':  # Add other models as needed
            from ultralytics import YOLO
            while self.model_size not in ['n','s', 'm', 'l', 'x']:
                print('model size must be s, m, l, x')
                self.model_size = input('model size: ').strip().lower()
            while self.model_version not in ['3','4','5','6','7','8','9','10','11']:
                print('version must be in 3, 4, 5, 6, 7, 8, 9, 10, 11')
                self.model_version = input('version: ').strip()
            name = 'yolov'+ self.model_version + self.model_size + '.pt'
            return YOLO(name)
        elif self.model_name=='rtdetr':
            from ultralytics import RTDETR
            self.model_size = self.model_size.lower()
            while self.model_size not in ['l', 'x']:
                print('model size must be l, x')
                self.model_size = input('model size: ').strip().lower()
            name = 'rtdetr-' + model_size + '.pt'
            return RTDETR(name)
        else:
            raise ValueError('model_name is not supported')
    def train(self,):
        self.model.train(
        data=self.data_path,
        epochs=self.epochs,
        imgsz=self.imgsz,
        batch=self.batch_size,
    )  



if __name__ == '__main__':
    model_name = 'rtdetr'
    model_version = '8'
    model_size = 'l'
    model = Detection_model(model_name=model_name,model_size=model_size,model_version=model_version)
    model.train()