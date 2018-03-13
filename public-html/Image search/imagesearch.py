import os
import sys
import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
import glob
import pickle
#import cv2
from datetime import datetime

from flask import Flask, request, render_template

app = Flask(__name__)

# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in glob.glob("static/feature/*"):
    features.append(pickle.load(open(feature_path, 'rb')))
    #img_paths.append('static/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')
    img_paths.append('static/img/' + os.path.splitext(os.path.basename(feature_path))[0] + '.jpg')


##@app.route('/', methods=['GET', 'POST'])
##def index():
##    if request.method == 'POST':
##        file = request.files['query_img']
##
##        img = Image.open(file.stream)  # PIL image
##        uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
##        img.save(uploaded_img_path)
##
##        query = fe.extract(img)
##        dist = np.linalg.norm(features - query, axis=1)  # Do search
##        ids = np.argsort(dist)[:10]
##        dist = [dist[id] for id in ids]
##        retrieved_img_paths = [img_paths[id] for id in ids]
##
##        return render_template('index.html',
##                               query_path=uploaded_img_path,
##                               scores=zip(dist, retrieved_img_paths))
##    else:
##        return render_template('index.html')
##
##if __name__=="__main__":
##    app.run()
##@app.route('/', methods=['GET', 'POST'])

#file = request.files['query_img']
#file="D:/tensorflow/sis-master/static/img/pic_559.png"
file=sys.argv[1]
img = Image.open(file)  # PIL image

#img = Image.open(file.stream)  # PIL image
#uploaded_img_path = "static/uploaded/" + datetime.now().isoformat() + "_" + file.filename
#img.save(uploaded_img_path)

query = fe.extract(img)
dist = np.linalg.norm(features - query, axis=1)  # Do search
ids = np.argsort(dist)[:3]
dist = [dist[id] for id in ids]
retrieved_img_paths = [img_paths[id] for id in ids]
#print(retrieved_img_paths)
file=open("image_path.txt","w")
print(dist)
for score,x in zip(dist,retrieved_img_paths):
    img = Image.open(x)
    img.show()
    print(x+','+str(score))
    file.write(x+"|"+ str(score)+"\n")
file.close()
##    cv2.imshow("Results 1-5", x)
##    cv2.waitKey(0)
    
##
##        return render_template('index.html',
##                               query_path=uploaded_img_path,
##                               scores=zip(dist, retrieved_img_paths))
##    else:
##        return render_template('index.html')

