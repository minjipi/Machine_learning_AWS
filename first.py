#pip install boto3

import boto3

bucket = 'minjipi'
photo = 'KakaoTalk_20200720_182205441.jpg'

client = boto3.client('rekognition')

response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                MaxLabels=10)

print('Detected labels for ' + photo)
print()
for label in response['Labels']:
    print("Label: " + label['Name'])
    print("Confidence: " + str(label['Confidence']))
    print("Instances:")
    for instance in label['Instances']:
        print("  Bounding box")
        print("    Top: " + str(instance['BoundingBox']['Top']))
        print("    Left: " + str(instance['BoundingBox']['Left']))
        print("    Width: " + str(instance['BoundingBox']['Width']))
        print("    Height: " + str(instance['BoundingBox']['Height']))
        print("  Confidence: " + str(instance['Confidence']))
        print()

    print("Parents:")
    for parent in label['Parents']:
        print("   " + parent['Name'])
    print("----------")
    print()
