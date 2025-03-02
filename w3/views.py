import pandas as pd
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import Student

from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import Student
from pyspark.sql import SparkSession

# Initialize Spark Session
# spark = SparkSession.builder.appName("DjangoSparkUpload").getOrCreate()

# def upload_and_process_file(request):
#     if request.method == "POST":
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = form.save()  # Save the file
#             file_path = uploaded_file.file.path  # Get the saved file path

#             # Load CSV file using Spark
#             df = spark.read.csv(file_path, header=True, inferSchema=True)
            
#             # Convert Spark DataFrame to Python list of dictionaries
#             data = df.collect()

#             # Insert data into Student model
#             student_objects = [
#                 Student(
#                     name=row["name"],
#                     age=row["age"],
#                     city=row["city"]
#                 )
#                 for row in data
#             ]
            
#             Student.objects.bulk_create(student_objects)  # Efficient bulk insert

#             return redirect("success_page")  # Ensure this URL exists in urls.py
#     else:
#         form = FileUploadForm()
    
#     return render(request, "upload.html", {"form": form})


def home(request):
    return render(request, "home.html")

def upload_and_process_file(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Save file to media/uploads/

            # Process CSV file using pandas
            file_path = uploaded_file.file.path
            df = pd.read_csv(file_path)

            # Iterate through rows and save data to the Student model
            for _, row in df.iterrows():
                Student.objects.create(
                    name=row["name"],
                    age=row["age"],
                    city=row["city"]
                )
            return redirect("success_page")  # Ensure this exists in urls.py


    else:
        form = FileUploadForm()

    return render(request, "upload.html", {"form": form})

def success_view(request):
    return render(request, "success.html", {"message": "File uploaded successfully!"})
