from turtle import Turtle
import time
class flag:
    def __init__(self,window,x,y,a):
        super().__init__()
        self.palastine_borders(window,x,y,a)
    def palastine_flag_map(self,position,window):
        
        flag=Turtle()
        #flag.speed(1)
        flag.hideturtle()

        #رسم العلم الفلسطيني 
        #رسم اللون الاسود 
        flag.color("white")
        flag.penup()
        flag.goto(position[17])
        flag.pendown()
        flag.fillcolor("black")
        flag.begin_fill()
        i=17
        while i<75:
            flag.goto(position[i])
            i+=1
        flag.goto(position[17])
        flag.end_fill()
        #رسم اللون الابيض
        
        flag.goto(position[74])
        i=75
        flag.fillcolor("white")
        flag.begin_fill()
        while i<94:
            flag.goto(position[i])
            i+=1
        flag.goto(position[len(position)-13])
        i=len(position)-13
        while i < len(position):
            flag.goto(position[i])
            i+=1
        i=0
        while i<18:
            flag.goto(position[i])
            i+=1
        flag.end_fill()  

        #رسم المثلث الاحمر  
        flag.color("red")
        flag.pensize(3)
        flag.fillcolor("red")
        flag.penup()
        flag.goto(position[11])
        flag.pendown()
        flag.begin_fill()
        x,y=position[82]
        s,f=position[0]
        X=(s+x)/2
        Y=(f+y)/2
        flag.goto(X,Y)
        flag.goto(position[len(position)-7])
        i=len(position)-7
        while i < len(position):
            flag.goto(position[i])
            i+=1
        i=0
        while i<12:
            flag.goto(position[i])
            i+=1
        flag.end_fill()




        
    def palastine_borders(self,window,x,y,a):
        positions= [(0,0.5),(0,2),(1,3),(2,3),(2,4),(3,5),(5,7),(6,7),(7,8),(8,9),(9,10),(10,13)
                    ,(11,15),(12,17),(13,19),(14,21),(15,23),(16,25),(17,26.5),(18,30),(19,33),
                    (20,35),(21,38),(22,40),(23,45),(24,50),(25,60),(26,63),(27,65),(27.5,66),
                    (28,65),(29,64.5),(30,65.5),(31,67),(31,71),(32,74),(32,76),(36,76),(37,76.5),
                    (38,77),(40,75),(42,75.1),(43,76),(45,77),(47,79),(47.5,82),(48,83),(49,84),
                    (51,82.5),(52,83),(52.5,82.2),(52,81),(51,80),(50.5,77),(52,72),(50,70),(49.5,67),
                    (48,67),(47,66),(47,65),(47,64),(47.5,62),(49,60),(50,59),(50,58),(49.7,57),(48.5,55),
                    (49,50),(49,49),(48,45),(48.5,40),(48,35),(47,34),(47,30),(48,25),(46,20),(44.5,17.5),
                    (44,15),(42,12),(41.5,10),(41,7),(41.25,5),(42.25,0),(41,-5),(43,-8),(43.5,-9),
                    (44,-10),(43,-14),(42,-16),(41,-17),(40,-20),(40,-21),(36,-30),(35.5,-32),(35,-35),
                    (34,-37),(35,-38),(35.5,-40),(35,-42),(33.5,-44),(34.5,-47),(34.5,-50),(33,-52),
                    (32,-55),(31,-60), (30,-62),(30,-65),(29,-70),(29,-71),(28,-72),(26,-73),(25,-75),
                    (24,-75.2),(23,-75),(22,-71),(22.5,-70),(22.5,-69),(21.5,-65),(20,-60),(18,-55),
                    (18,-53),(16,-50),(15,-47),(14,-45),(14,-42),(12,-40),(10,-37),(10,-34),(9,-32),
                    (8.9,-27),(6,-22),(6,-21),(5,-20),(4.5,-18),(3.5,-16),(3,-12),(2,-9),(0,-5),
                    (-0.5,-2.5),(0,0),(0,-0.5)]
        time.sleep(5)
        fam=Turtle()
        fam.penup()
        fam.color("white")
        fam.fillcolor("green")
        fam.begin_fill()
        #لوب للتحكم في موقع الخريطه علي الشاشه ومساحتها 
        for i in range(len(positions)):
            X,Y=positions[i]
            A=a
            new_x=X*A+x
            new_y=Y*A+y
            positions[i]=(new_x,new_y)
        fam.goto(positions[i])
        fam.pendown()
        fam.hideturtle()
        fam.speed(1)

        for i in positions:
            fam.goto(i)
        fam.end_fill()
        self.palastine_flag_map(position=positions,window=window)
