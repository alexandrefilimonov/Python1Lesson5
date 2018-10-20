#C:\Users\CA32132\AppData\Local\Programs\Python\Python37\python.exe C:\alex\_________________________________________________NewCode\_Python1Lesson4\alexfilimonov_python1_lesson4_method1.py
#import random
#Small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#Capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

import sys
import os 
import shutil 


while True:
    print("Please press one of the following keys:")
    print("'1' - move to directory")
    print("'2' - view current directory")
    print("'3' - delete directory")
    print("'4' - create directory")
    print("'q' - Exit")
    #print(os.getcwd())
    key = input()
    if(key=='q' or key=='1' or key=='2' or key=='3' or key=='4')  :
        if(key=='q') :    
            sys.exit() 
        elif (key=='1') :
            dir_name = input("Please enter the entire path of dir:")
            if (dir_name!="")  :
                try :
                    os.chdir(dir_name)
                    print ('It successfully moved to the directory {}'.format(dir_name))       
                except :             
                    print('We did not moved successfully to the directory. There is an exception.')
        elif (key=='2') :
            try :
                for file in os.listdir("."):
                    if os.path.isfile(os.path.join(".", file)):
                        print(file)
                print ('The current directory is successfully viewed.')       
            except :             
                print('The current directory was not viewed. There is an exception') 
        elif (key=='3') :
            dir_name = input("Please enter the dir name:")
            if (dir_name!="")  :
                try :
                    shutil.rmtree(dir_name)
                    print ('The directory {} has been deleted'.format(dir_name))       
                except OSError as e:             
                    print('There is raised exception to delete the directory {}. Error: %s - %s'.format(dir_name),e.filename, e.strerror)
        elif (key=='4') :
            dir_name = input("Please enter the dir name:")
            if (dir_name!="")  :
                try :
                    os.mkdir(dir_name)
                    print ('The directory {} has been created.'.format(dir_name))       
                except FileExistsError :             
                    print('The directory {} already exists'.format(dir_name))


