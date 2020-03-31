import cv2, os
from PIL import Image


#extracting frames from the given file
#fileName is the name of the video file
def extractFrames(fileName):
    cam=cv2.VideoCapture(fileName)
    #number of frames in the video
    length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total frames:",length)

    count=0

    while(True):
        name="./frames/"+str(count)+".jpg"
        ret,frame=cam.read()
        if ret==True:
            print(name)
            cv2.imwrite(name,frame)
            count=count+1
        else:
            break
            print("All frames saved to folder")

            cam.release()
            cv2.destroyAllWindows()


#crops every extracted frame at the center with one pixel width
def pixelCrop():
    count=0
    while(True):
        try:
            imgName="./frames/"+str(count)+".jpg"
            newName="./framecrop/"+str(count)+".jpeg"
            print("opening image")
            img=Image.open(imgName)
            img_width,img_height=img.size
            print("cropping the image")
            crop_width=1
            crop_height=img_height
            cropped=img.crop(((img_width - crop_width) // 2,
                            (img_height - crop_height) // 2,
                            (img_width + crop_width) // 2,
                            (img_height + crop_height) // 2))
            print("image cropped successfully")
            cropped.save(newName,"JPEG")
            print("Image saved successfully\n")
            count=count+1
            print("------------------------------------")
        except Exception as e:
            print(e)
            print("process completed")
            break


#combines every cropped image together and saves it
def combineImage():
    dir="/projects/unwrap/framecrop"
    list = os.listdir(dir)
    filecount = len(list)
    print("Number of files:",filecount)
    filecount=int(filecount)
    img=Image.open("./framecrop/0.jpeg")
    width,height=img.size
    count=0
    composite=Image.new("RGB",(filecount,height))
    for i in range(filecount):
        path="./framecrop/"+str(count)+".jpeg"
        img=Image.open(path)
        composite.paste(img,(count,0))
        count=count+1
        img.close()

    composite.show()
    print("Saving composite image")
    composite.save("composite.jpeg","JPEG")
    print("Image saved successfully")


#pass in the name of the video file as a string to below function
extractFrames("head.mp4")
pixelCrop()
combineImage()
