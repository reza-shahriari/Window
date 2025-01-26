from rest_framework.viewsets import ModelViewSet

from backend.srvs.office.office.models import (
    Post,
    CarModel,
    Company,
)
from backend.srvs.office.office.serializers import (
    PostSerializer,
    CarModelSerializer,
    CompanySerializer,
)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CarModelViewSet(ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from AI.run_inference import AiModel
import numpy as np
from PIL import Image
import io

@api_view(['POST'])
def predict_image(request):
    if 'image' not in request.FILES:
        return Response({'error': 'No image provided'}, status=400)
    
    image_file = request.FILES['image']
    # Convert uploaded file to PIL Image
    image = Image.open(io.BytesIO(image_file.read()))
    # Convert to numpy array
    image_array = np.array(image)
    
    model = AiModel()
    result_url = model.predict(img=image_array)
    
    return Response({'image_url': result_url})
