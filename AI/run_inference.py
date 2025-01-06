"""
This is the only object that is used to run inference on a model.
Nothing else in the AI folder is used when running in the webserver.
"""
from ultralytics import YOLO
import os

class AiModel:
    def __init__(self, model_name='yolo11', model_size='M', weight_path=None):
        self.model_name = model_name
        self.model_size = model_size
        self.weight_path = weight_path or self.get_weight_path()

        if not os.path.exists(self.weight_path):
            if self.prompt_download_weight():
                self.download_weight()
            else:
                raise ValueError('Weight path is not valid and user chose not to download.')

        self.model = self.initialize_model()

    def get_weight_path(self):
        # Default weight path based on model name and size
        return f'AI/runs/detect/train10/weights/best_{self.model_name}{self.model_size}.pt'

    def prompt_download_weight(self):
        response = input(f"The weight path '{self.weight_path}' does not exist. Do you want to download it from Google Drive? (y/n): ")
        return response.lower() == 'y'

    def download_weight(self):
        # Implement the logic to download the weight from Google Drive
        print(f"Downloading weights for {self.model_name}{self.model_size}...")
        # Example: Use gdown or any other method to download the weights
        # gdown.download('https://drive.google.com/your_file_id', self.weight_path, quiet=False)

    def initialize_model(self):
        if self.model_name in ['yolo11', 'yolo8']:  # Add other models as needed
            return YOLO(self.weight_path)
        else:
            raise ValueError('model_name is not supported')

    def predict(self, img_path):
        return self.model(img_path)

if __name__ == '__main__':
    model_name = input("Enter the model name (e.g., yolo11, yolo8): ")
    model_size = input("Enter the model size (e.g., M, N): ")
    model_path = input("Enter the weight path (leave empty for default): ")
    img_path = 'AI/data/images/test/1.jpg'  # Example image path

    model = AiModel(model_name=model_name, model_size=model_size, weight_path=model_path)
    result = model.predict(img_path)
    result.show()
