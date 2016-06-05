#!/usr/bin/python

# author: minjie 2016
# version: 105
# 
# This software is provided 'as-is', without any express or implied warranty.
# In no event will the authors be held liable for any damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it freely,
# subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented;
#    you must not claim that you wrote the original software.
#    If you use this software in a product, an acknowledgment
#    in the product documentation would be appreciated but is not required.
#
# 2. Altered source versions must be plainly marked as such,
#    and must not be misrepresented as being the original software.
#
# 3. This notice may not be removed or altered from any source distribution.

 
# change log
# v105 : add 'warn:' coror highlight(orange)
# v104 : skip <Info>
# v103 : skip [log]
# v102 : skip [ log:] 


import os,sys

# func
def cur_file_dir():
     path = sys.path[0]
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
         
# global
print 'current dir:'   
print os.listdir(cur_file_dir())
# find the right file
for oneFileName in os.listdir(cur_file_dir()):
    if (-1!= oneFileName.find('.log')):
        rFH=open(cur_file_dir()+'/'+oneFileName) 
        wFH=open(cur_file_dir()+'/'+oneFileName[:-3]+'html','w')
        
        fileList=rFH.readlines()
        
        wFH.write('<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n<title>'+oneFileName+'</title>\n</head>\n<body>\n');
        wFH.write('<style>*{padding:0;margin-top:0;margin-bottom:0.2em;}h3{color:blue;}p{font-size:1em;}.order{color:green;}</style>\n')
        wFH.write('<h3>'+oneFileName+'</h3>\n')
        
       read all lines
        for i in range(0,len(fileList)):
            if (-1!=fileList[i].find('err:')):
                print fileList[i].find('err:');
                wFH.write('<p style="color:red;"><span class="order">'+str(i)+' </span>'+fileList[i]+'</p>\n')
            elif (-1!=fileList[i].find('warn:')):
                 wFH.write('<p style="color:orange;"><span class="order">'+str(i)+' </span>'+fileList[i]+'</p>\n')
            elif((-1==fileList[i].find('[ log]:'))and(-1==fileList[i].find('[log]'))and(-1==fileList[i].find('<Info>'))):
                wFH.write('<p><span class="order">'+str(i)+' </span>'+fileList[i]+'</p>\n')
                
        wFH.write('</body>\n</html>\n')
        
        rFH.close()
        wFH.close()
