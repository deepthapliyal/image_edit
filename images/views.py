from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import cv2
import numpy as np

def index(request):
  return render(request, 'index.html')


def convert(request):
    if request.method == 'POST' and request.FILES.get('file') and request.POST.get('format'):
        # Get the uploaded file and selected format
        filename = request.FILES['file']
        file_format = request.POST['format']
      
       

        image = cv2.imdecode(np.fromstring(filename.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        print(image)
                # Convert image to grayscale
        output_path = f"./media/savedimage/{filename}.{file_format.lower()}"
        output_path_gray = f"./media/savedimage/{filename}"
  
        # Perform the image conversion here (e.g., resize, change format, etc.)
        if file_format == "JPEG":
           image = cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        elif file_format == "PNG":
           image = cv2.imwrite(output_path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), 5])
        elif file_format == "GRAYSCALE":
           
           gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
           imageUrl =  cv2.imwrite(output_path_gray, gray_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            

        # Add more cases for other supported file formats if
        
        # Return the URL of the converted image in the JSON response
        if file_format == "GRAYSCALE":
            converted_image_url_gray = f'/media/savedimage/{filename}'
            return JsonResponse({'imageUrl': converted_image_url_gray})
            os.remove(converted_image_url_gray)

        else:
            converted_image_url = f'/media/savedimage/{filename}.{file_format.lower()}'
            return JsonResponse({'imageUrl': converted_image_url})
            os.remove("/media/savedimage/logo.jpg.png")

        

    else:
       return JsonResponse({'error': 'Invalid request'}, status=400)
