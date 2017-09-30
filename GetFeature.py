#coding=utf-8

import glob
import Preprocess
from PIL import Image

def getFeature(imagePath):
    featureList=[]
    binImage=Image.open(imagePath).point(lambda x :x>140)
    for y in range(binImage.height):
        temp=0
        for x in range(binImage.width):
            temp+=binImage.getpixel((x,y))
        featureList.append(temp)
    for x in range(binImage.width):
        temp=0
        for y in range(binImage.height):
            temp+=binImage.getpixel((x,y))
        featureList.append(temp)
    return featureList


if __name__ == '__main__':
    folders="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    featureFilePath="Feature.data"
    for eachFolder in folders:
        allImagePaths=glob.iglob("ClassifiedVcode/" + eachFolder + "/*.jpg")
        bufferString=""
        for eachImagePath in allImagePaths:
            featureList=getFeature(eachImagePath)
            #print(eachFolder,featureList)
            bufferString+=str(ord(eachFolder)) +  " "
            for (index,value) in enumerate(featureList):
                bufferString+= str(index+1) + ":" + str(value) + " "
            bufferString+="\n"
        #print(bufferString)
        with open(featureFilePath,"a") as featureFile:
            featureFile.write(bufferString)



