"""
This is the only object that is used to run inference on a model.
Nothing else in the AI folder is used when running in the webserver.
"""
from ultralytics import YOLO,RTDETR
import os
from numpy import zeros
import base64
import requests
from PIL import Image
import io
import os
from datetime import datetime
import gdown
class AiModel:
    def __init__(self, model_name='yolo8', model_size='M', weight_path=None):
        self.model_name = model_name
        self.model_size = model_size
        self.weight_path = weight_path or self.get_weight_path()

        if not os.path.exists(self.weight_path):
            if self.prompt_download_weight():
                self.download_weight()
            else:
                raise ValueError('Weight path is not valid and user chose not to download.')
        self.counter = 0
        self.model = self.initialize_model()
    def remove_last(self):
        os.remove('/home/reza/Vision/SoftWareDesign/Window/frontend/src/Components/Assets/pred_res.png')
    def get_weight_path(self):
        # Default weight path based on model name and size
        return f'AI/checkpoints/{self.model_name}{self.model_size.capitalize()}.pt'

    def prompt_download_weight(self):
        response = input(f"The weight path '{self.weight_path}' does not exist. Do you want to download it from Google Drive? (y/n): ")
        return response.lower() == 'y'

    def download_weight(self):
       
        weight_mapping = {
            'yolo8N':'1viWMotljdLlYiul7zHTwfHnABXeU0hTl',
            'yolo8M': '1vsf28VOOZ76V-J914D7eikn-UUKixMSZ',
            'yolo8S': '13vApC5cA3eRyF8WOT6Rj4HC2Ud_HbGKR',
            'yolo8L': '1-gt9GOL9r3faQzA-760JdzDLhUnw5Tgg',
            'yolo11L':'158z6YZhlyHCS43l-6znlK5Ib1LJ27kX6',
            'yolo11M':'1fLUP_YA542T18FuP8Tdy1tdL7kaFuOLZ',
            'yolo11N':'13p1HwLRygIqWH1_AdHdcicsxFGp2hqMN',
            'yolo11S':'1LHnM_rqW1b6prYnG4NMhpLx435fAn0uI',
            'rt-detrL': '1B0wvgiGBHgpGlXaoB2KLCcO9ituqFhk'
        }
        
        model_key = f"{self.model_name}{self.model_size}"
        file_id = weight_mapping.get(model_key)
        
        if not file_id:
            raise ValueError(f"No weight file found for model {model_key}")
            
        # Create checkpoints directory if it doesn't exist
        os.makedirs('AI/checkpoints', exist_ok=True)
        
        # Download the file using gdown
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, self.weight_path, quiet=False)
    def initialize_model(self):
        if self.model_name in ['yolo11', 'yolo8']:  # Add other models as needed
            return YOLO(self.weight_path)
        elif self.model_name =='rt-detr':
            return RTDETR(self.weight_path)
        else:
            raise ValueError('model_name is not supported')
    def _upload_and_get_link(self, img_array):
        save_dir = '/home/reza/Vision/SoftWareDesign/Window/frontend/src/Components/Assets'
        os.makedirs(save_dir, exist_ok=True)
        
        img = Image.fromarray(img_array)
        filename = 'pred_res.png'
        save_path = os.path.join(save_dir, filename)
        img.save(save_path)
        
        return save_path

    def predict(self, img_path=None,img_path_list = None,img = None,img_list=None):
        if img_path:
            results = self.model(img_path)
            return self._upload_and_get_link(results[0].plot())
        if img_path_list:
            results = self.model(img_path_list)
            return [self._upload_and_get_link(r.plot()) for r in results]
        if img is not None:
            results = self.model(img)
            return self._upload_and_get_link(results[0].plot())
        if img_list:
            results = self.model(img_list)
            return [self._upload_and_get_link(r.plot()) for r in results]
        return zeros((100,100,3))
