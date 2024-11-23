import requests
from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import hashlib
from PIL import Image
import imagehash
from io import BytesIO

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def put(self, request, *args, **kwargs):
        # Get the item instance to update
        try:
            instance = self.get_object()
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get the image URL from the request body
        
        img_url = request.data.get('image')
        if not img_url:
            return Response({'error': 'No image URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the image from the URL
            response = requests.get(img_url)
            if response.status_code != 200:
                return Response({'error': 'Failed to fetch the image from the URL'}, status=status.HTTP_400_BAD_REQUEST)

            # Open the image using PIL
            image = Image.open(BytesIO(response.content))

            # Compute MD5 hash
            md5 = hashlib.md5(response.content).hexdigest()

            # Compute perceptual hash (pHash)
            phash = str(imagehash.phash(image))
            sha = hashlib.sha256(response.content).hexdigest()

            # Update the instance fields
            instance.image = img_url
            instance.md5_hash = md5
            instance.phash = phash
            instance.sha_hash = sha
            instance.save()

            # Serialize and return the response
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ImageUrlProcessingView(generics.CreateAPIView):
    serializer_class = ItemSerializer
    def post(self, request, *args, **kwargs):
        # Get the image URL from the request body
        img_url = request.data.get('image')
        if not img_url:
            return Response({'error': 'No image URL provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the image from the URL
            response = requests.get(img_url)
            if response.status_code != 200:
                return Response({'error': 'Failed to fetch the image from the URL'}, status=status.HTTP_400_BAD_REQUEST)

            # Open the image using PIL
            image = Image.open(BytesIO(response.content))

            # Compute MD5 hash
            md5 = hashlib.md5(response.content).hexdigest()

            # Compute perceptual hash (pHash)
            phash = str(imagehash.phash(image))
            sha = hashlib.sha256(response.content).hexdigest()
            # Save to database
            record = Item.objects.create(image=img_url, md5_hash=md5, phash=phash,sha_hash=sha)

            # Serialize and return the response
            serializer = ItemSerializer(record)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

