import os

import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


#Función para subir la imagen
def upload_image(photo_name, bucket_name, region=None):
    with open(photo_name, "rb") as f:
        body = f.read()

    try:
        s3_resource = boto3.resource("s3", region_name="eu-south-2")
        s3_bucket = s3_resource.Bucket(bucket_name)
        s3_bucket.put_object(Key=photo_name, Body=body, ACL="public-read")
        detect_labels(photo_name, bucket_name)
    except Exception as e:
        print(e)

#Función para detectar las etiquetas de la imagen
def detect_labels(photo_name, bucket_name):

    rekognition_client = boto3.client("rekognition", region_name="eu-south-2")

    response = rekognition_client.detect_labels(
        Image={"S3Object": {"Bucket": bucket_name, "Name": photo_name}},
        MaxLabels=10,
    )
    

    print("Etiquetas detectadas para" + photo_name)
    print ()
    for label in response ["Labels"]:
        print("label", label["Name"])
        print("confidence", label["Confidence"])
        print()
    
    img=Image.open(photo_name)
    plt.imshow(img)
    ax = plt.gca()
    for label in response ["Labels"]:
        for instance in label.get("Instances", []):
                bbox = instance["BoundingBox"]
                left = bbox["Left"] * img.width
                top = bbox["Top"] * img.height
                width = bbox["Width"] * img.width
                height = bbox["Height"] * img.height
                rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor="red", facecolor="none")
                ax.add_patch(rect)
                label_text = label["Name"] + " (" + str(round(label["Confidence"], 2)) + "%)"
                plt.text(left, top - 2, label_text, color="red", fontsize=8, bbox=dict(facecolor="white", alpha=0.5, edgecolor="none"))

    plt.show()

def main():
    photo_name = "futbol.jpg"  # Reemplaza con el nombre de tu imagen
    bucket_name = "bucket-imagen-generador"  # Reemplaza con el nombre de tu bucket S3
    upload_image(photo_name, bucket_name)

if __name__ == "__main__":
    main()