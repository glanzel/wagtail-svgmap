  # Ported to Python by Grischan Glänzel (grischan@gmail.com) for N-Aerus 

  # Original ActionScript Code written and owned by Chris Youderian
  # All code is licensed under the GPLv2.  
  # self means that any derivate works that you create using self code must be released under the same license.  
  # If you wish to use self code in a product you want to resell, you need to ask for permission.
  # Contact form available at:  http:#www.flashworldmap.com/contactus.php
  # See original posting at: http:#www.flashmap.org/robinson-projection-in-as3-gpl/

import math

class Point(object): pass

class Robinson:
   # map width and height are asked for because they are what the
   # earthRadius value relies upon. You can use either, as long as
   # the image is sized such that width = height*1.97165551906973 
   # you can use either to do the calculation, but as of now I
   # require both and only use width. both are used in projectToCSS.
    def __init__(self, mapWidth, mapHeight, fudgeX = 0, fudgeY = 0):
       self.mapWidth = mapWidth;
       self.mapHeight = mapHeight;
       self.earthRadius = (mapWidth/2.666269758)/2;
      
       # fudgeX, fudgeY are used to offset points, self is to calibrate
       # the points if they aren't showing up in the right place exactly 
       self.fudgeX = fudgeX  
       self.fudgeY = fudgeY
       print("juppi")  
       print("self=fudgeX: "+str(self.fudgeX))
       print(self.earthRadius)
      
       # these tables are created by robinson and are what the projection is based upon
       self.AA = [0.8487,0.84751182,0.84479598,0.840213,0.83359314,0.8257851,0.814752,0.80006949,0.78216192,0.76060494,0.73658673,0.7086645,0.67777182,0.64475739,0.60987582,0.57134484,0.52729731,0.48562614,0.45167814];
       self.BB = [0,0.0838426,0.1676852,0.2515278,0.3353704,0.419213,0.5030556,0.5868982,0.67182264,0.75336633,0.83518048,0.91537187,0.99339958,1.06872269,1.14066505,1.20841528,1.27035062,1.31998003,1.3523];


    def projectToCSS(self, lat,lng):
       # changes the coordinate system of a projected point to the one CSS uses
       point = self.project(lat,lng);
       #print(point.x)
       print("cssmapWidth: "+str(self.mapWidth/2))
       point.x = (point.x + (self.mapWidth/2));
       point.y = ((self.mapHeight/2) - point.y);
       return point;


    def roundToNearest(self, roundTo, value):
       return math.floor(value/roundTo)*roundTo;  #rounds down

    def getSign(self, value):
       if value < 0:  return -1 
       else: return 1

    def project(self, lat,lng):
       # returns the robinson projected point for a given lat/lng based on
       # the earth radius value determined in the contructor
       lngSign = self.getSign(lng) 
       latSign = self.getSign(lat)  #deals with negatives
       lng = abs(lng); 
       lat = abs(lat); #all calculations positive
       radian = 0.017453293; #pi/180
       low = self.roundToNearest(5, lat-0.0000000001); #want exact numbers to round down
       if (lat == 0): low = 0  #except when at 0
       high = low + 5;
      
       # indicies used for interpolation
       lowIndex = int(low/5);
       highIndex = int(high/5);
       ratio = (lat-low)/5;

       print(lowIndex)
       print(highIndex)
 

       # interpolation in one dimension
       adjAA = ((self.AA[highIndex]-self.AA[lowIndex])*ratio)+self.AA[lowIndex];
       adjBB = ((self.BB[highIndex]-self.BB[lowIndex])*ratio)+self.BB[lowIndex];

       #create point from robinson function
       point = Point()
       point.x = (adjAA * lng * radian * lngSign * self.earthRadius) + self.fudgeX 
       point.y  = (adjBB * latSign * self.earthRadius) + self.fudgeY
       return point


#===============================================================================
# rob = Robinson(1000,1000,0,0)
# cssPoints = rob.projectToCSS(25.3456, 34.6798)
# print(cssPoints.x)
# rob = Robinson(1000,1000,200,300)
# cssPoints = rob.projectToCSS(25.3456, 34.6798)
# print(cssPoints.x)
#===============================================================================
  

