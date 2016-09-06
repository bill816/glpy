#-*- coding: UTF-8 -*-
from PIL import Image
import os.path
import glob


def convertjpg(jpgfile,outdir,width=720,height=1280):
    img=Image.open(jpgfile)   
    newImg = Image.new("RGBA",(width,height),(255,255,255))
    box=(0,0,480,720)
    region = img.crop(box)
    box2=(120,280,480+120,720+280)
    newImg.paste(region,box2)
    #new_img=img.resize((width,height),Image.BILINEAR)   
    #new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    newImg.save(os.path.join(outdir,os.path.basename(jpgfile)))


def getSplitImage(jpgfile,outdir):
    img = Image.open(jpgfile)
    ''' 480P
    startX = 1
    startY = 350
    width= 233
    height = 144
    gapX = 3
    gapY = 9
    '''
    '''720P'''
    startX = 3
    startY = 540
    width= 233
    height = 144
    gapX = 6
    gapY = 4
    
    for i in range(0, 15):
        startX1 = startX+(width*(i%3)) + gapX*(i%3)
        startY1 = startY+(height*(i/3)) + gapY*(i/3)
        
        
        box=(startX1,startY1,startX1+width,startY1+height)
        region = img.crop(box)
#        region.show()
        region.save(os.path.join(outdir,"num_" + str(i) + ".png" ))

def convertjpg2(jpgfile,outdir,width=720,height=1280,oldWidth=157,oldHeight=90):
#    width = 236
#    height = 144
#    second 233,141
    img=Image.open(jpgfile)   
    newImg = Image.new("RGBA",(width,height),(64,64,64))
    box=(0,0,oldWidth,oldHeight)
    region = img.crop(box)
    box2=((width-oldWidth)/2,(height-oldHeight)/2,oldWidth+(width-oldWidth)/2,oldHeight+(height-oldHeight)/2)
    newImg.paste(region,box2)
    #new_img=img.resize((width,height),Image.BILINEAR)   
    #new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    newImg.save(os.path.join(outdir,os.path.basename(jpgfile)))


def convertjpg3(jpgfile,outdir,rgb=(0,0,0),width=233,height=144,oldWidth=112,oldHeight=95):
    '''
            把一张图片贴到另外一个背景上
    '''
    img=Image.open(jpgfile)
    newImg = Image.new("RGBA",(width,height),rgb)
    box=(0,0,oldWidth,oldHeight)
    region = img.crop(box)
    box2=((width-oldWidth)/2,(height-oldHeight)/2,oldWidth+(width-oldWidth)/2,oldHeight+(height-oldHeight)/2)
    newImg.paste(region,box2)
    newImg.save(os.path.join(outdir,os.path.basename(jpgfile)))
    
    
def  generateBigPic(imagePath):
    for jpgfile in glob.glob(imagePath):
        convertjpg2(jpgfile,"D:/work/n5/PCI/images_change",233,144)
        print jpgfile

if __name__ == '__main__':
    getSplitImage("D:/work/n5/PCI/shouying_720.jpg","D:/images")
    #generateBigPic("D:/images/*.png")
    #convertjpg3("D:/work/n5/PCI/images/cancel.png","D:/work/n5/PCI/images_change",(238,69,47))
    #convertjpg3("D:/work/n5/PCI/images/clear.png","D:/work/n5/PCI/images_change",(255,185,0))
    #convertjpg3("D:/work/n5/PCI/images/sure.png","D:/work/n5/PCI/images_change",(56,192,51))
    
    #for jpgfile in glob.glob("D:/yingshuang_android/*.jpg"):
    #convertjpg(jpgfile,"D:/yingshuang_android/new_file")
    #print jpgfile
    print "finished!"
    


