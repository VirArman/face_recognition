#!/usr/bin/env python3
from facedb import FaceDB as fdb

import os
# need to find out how get all faces or other way of comparing of input face with db faces
os.environ["PINECONE_API_KEY"] = "YOUR_API_KEY"
os.environ["PINECONE_ENVIRONMENT"] = "YOUR_ENVIRONMENT_NAME"

db = fdb(
    path="facedata",
)

result = db.recognize(img="pics/ani.jpg", include=['name'])
print(result)
if result:
    print(f"Recognized as {result['name']}")
else:
    print("Unknown face")
