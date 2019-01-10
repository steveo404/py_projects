import os
import exifread

currentDirectory = "/home/dale/Projects/filetest"

for root, dirs, files in os.walk(currentDirectory):
    for picFile in files:
        if picFile.endswith(".jpg") or picFile.endswith(".JPG"):
            picFileDirectory = os.path.join(root, picFile)    
            print picFileDirectory
            f = open(picFileDirectory, 'rb')

            tags = exifread.process_file(f)
            
            #print tags
            print len(tags)
            
            #for key in tags:
            #    print "key: %s, value: %s" % (key, tags[key])
            
            if tags.get('Image DateTime'):
                print "it is here"
                
            elif tags.get('EXIF DateTimeDigitized'):
                print "no it is here"
            else:
                print "it isn't anywhere"
            
            value = tags.get('Image DateTime', "empty")
            print value
            
            #if tags.get(['Image DateTime']):
            #    print len(tags['Image DateTime'])
    
            if len(tags) > 10:
                if tags['EXIF DateTimeDigitized']:
                    dateTakenexif = str(tags['EXIF DateTimeDigitized'])
                    yearTaken = dateTakenexif[0:4]
                    monthTaken = dateTakenexif[5:7]
        
                    print monthTaken