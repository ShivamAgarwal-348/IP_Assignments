import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        Shape.__init__(self)
        self.points = np.array(A) # creates an ndarray for storing the coordinates
        
        
 
    
    def translate(self, dx, dy = None):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        if(dy == None): # if dy is not passed as an argument in the function
            dy = dx
        n = len(self.points)
        Shape.translate(self,dx,dy)
        
        
        for i in range(n) :
            self.points[i] = np.dot(self.points[i],self.T_t.transpose()) # vector product of coordinates and transposse of T_t ndarray                            

        return return_cords_poly(self)
        

    
    def scale(self, sx, sy = None):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        if(sy == None): # if sy is not passed as an argument in the function
            sy = sx
        n = len(self.points)
        
        Shape.scale(self,sx,sy)
        
        center = [0,0]
        for i in range(n): # finds the center of the polygon 
            center[0] += self.points[i][0]
            center[1] += self.points[i][1]

        center[0] /=n
        center[1] /=n
        
        self.translate(- center[0] , - center[1]) # brings the center of the polygon to origin

        self.points = np.dot(self.points,self.T_s) 

        self.translate( center[0] , center[1]) # brings the center back to its original place

        

        return return_cords_poly(self)
        
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        n = len(self.points)
        
        self.translate(-rx , -ry) # makes the point around which rhe polygon is to be rotated as the origin
        Shape.rotate(self,- deg)
                
        for i in range(n):

            self.points[i] = np.dot(self.points[i] , self.T_r) # rotates each coordinate 

        self.translate(rx , ry) # brings the center back to its original place

        return return_cords_poly(self)


    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        n = len(self.points)

        x_points = []
        y_points = []
        
        x_max = 0
        y_max = 0
        for i in range(n): # finds the maximum x,y coordinate in the polygon before transformation
            x_points.append(prev[i][0])
            y_points.append(prev[i][1])

            if(abs(prev[i][0]) > x_max):
                x_max = abs(prev[i][0])            
            if(abs(prev[i][1]) > y_max):
                y_max = abs(prev[i][1])


        x_points.append(prev[0][0])
        y_points.append(prev[0][1])

        plt.plot(x_points,y_points,marker = 'o', linestyle = 'dashed' )

        x_points = []
        y_points = []

        for i in range(n): # finds the maximum x,y coordinate in the polygon after transformation
            x_points.append(self.points[i][0])
            y_points.append(self.points[i][1])

            if(abs(self.points[i][0]) > x_max):
                x_max = abs(self.points[i][0])
            if(abs(self.points[i][1]) > y_max):
                y_max = abs(self.points[i][1])

        x_points.append(self.points[0][0])
        y_points.append(self.points[0][1])

        plt.plot(x_points,y_points,marker = 's')
        Shape.plot(self,x_max,y_max)

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.center = [x,y,1] # stores the centre of the circle
        self.radius = radius  # stores the radius of the circle 
        Shape.__init__(self)
    
    def translate(self, dx, dy = None):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        if(dy == None):
            dy = dx

        Shape.translate(self,dx,dy)

        self.center = np.dot(self.center , self.T_t.transpose())
        
        return (self.center[0],self.center[1],self.radius)
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.radius *= sx #scales the radius based on the input
        return (self.center[0],self.center[1],self.radius)
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.translate(-rx , -ry) # makes the point around which the circle is to be roated as the origin

        Shape.rotate(self,- deg)

        self.center = np.dot(self.center , self.T_r)

        self.translate(rx , ry)   # brings the origin back to its original place          

        return (self.center[0],self.center[1],self.radius)

 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        fig, ax = plt.subplots()

        x_max = max(abs(prev.center[0]) + abs(prev.radius),abs(self.center[0]) + abs(self.radius)) # finds the maximum x coordinate in both preb and current circle
        y_max = max(abs(prev.center[1]) + abs(prev.radius),abs(self.center[1]) + abs(self.radius)) # finds the maximum y coordinate in both preb and current circle

        ax.add_patch(plt.Circle((prev.center[0],prev.center[1]), prev.radius , fill = False , linestyle = '--'))
        ax.add_patch(plt.Circle((prev.center[0],self.center[1]), self.radius , fill = False))
        Shape.plot(self,x_max , y_max)

def return_cords_poly(a): # helper function to return arrays of x and y coordinates of the polygon
    x_cords = np.array([])
    y_cords = np.array([])

    for i in range(len(a.points)) :            
        x_cords = np.append(x_cords,a.points[i][0])                    
        y_cords = np.append(y_cords,a.points[i][1])

    return (x_cords,y_cords)

def print_cords_circ(a): # prints the attributes of the circle after rounding them off
    
    print(round_off(a.center[0]),round_off(a.center[1]),round_off(a.radius))

def print_cords_poly(a): # prints the coordinates of the polygon after rounding them off
    
    for i in a[0]:
        print(round_off(i),end = ' ')
    for i in a[1]:
        print(round_off(i),end = ' ')
    print()

def round_off(a):
    return round(a,2)

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''

    verbose = int(input('Verbose (1 to plot , 0 otherwise) : '))
    test = int(input('Enter the number of test cases : '))

    for x in range(test):
        shape = int(input('Enter the type of shape (0 - Polygon/1 - Circle) : '))
        
        if (shape == 0):
            n = int(input('Enter the number of side : '))
            a = []
            prev = []  # prev stores the coordinates of the polygon before the transformation
            
            for i in range(n):  # loop for taking in the coordinates 
                a.append(list(map(float,input('Enter (x'+ str(i+1) + ',y' + str(i+1) + ') : ').split())))
                a[i].extend([1.0])

            poly = Polygon(a) #an object of class polygon
            prev = poly.points.copy() # using copy function to avoid problems due to aliasing

            q = int(input('Enter the number of queries : '))

            for y in range(q):
                print('\nQuery :')
                print('1) Rotate degree (rx) (ry)')
                print('2) Translate dx (dy)')
                print('3) Scale sx (sy)')
                print('4) Plot\n')

                Query = input('Enter Query Number(R/T/S/P) : ')

                
                if(Query == 'R'):
                    values = list(map(float,input('Enter deg (rx) (ry) : ').split()))
                    print_cords_poly(return_cords_poly(poly)) # print the coorinates of the polygon
                    prev = poly.points.copy()  

                    if(len(values) == 3): #calls function by deciding whether rx and ry have also been passed
                        print_cords_poly(poly.rotate(values[0],values[1],values[2]))
                    elif(len(values) == 2):
                        print_cords_poly(poly.rotate(values[0],values[1]))
                    else :
                        print_cords_poly(poly.rotate(values[0]))

                    if(verbose == 1): #calls plot function if verbose is 1 after the transformation
                        poly.plot()

                elif(Query == 'T'):
                    values = list(map(float,input('Enter dx (dy) : ').split()))

                    print_cords_poly(return_cords_poly(poly))
                    prev = poly.points.copy() 
                    
                    if(len(values) == 2):
                        print_cords_poly(poly.translate(values[0],values[1]))
                    else :
                        print_cords_poly(poly.translate(values[0]))
                    if(verbose == 1):
                        poly.plot()

                elif(Query == 'S'):
                    values = list(map(float,input('Enter sx (sy) : ').split()))
                    print_cords_poly(return_cords_poly(poly))
                    prev = poly.points.copy()
                    
                    if(len(values) == 2):
                        print_cords_poly(poly.scale(values[0],values[1]))
                    else :
                        print_cords_poly(poly.scale(values[0]))
                    if(verbose == 1):
                        poly.plot()

                elif(Query == 'P'):

                    poly.plot()

        if (shape == 1):
            x,y,radius = map(float,input('Enter x-coordinate , y-coordinate , Radius : ').split())
            
            circ = Circle(x,y,radius) # an object of class Circle 
            prev = Circle(x,y,radius) # an object of class circle to store the circle values befor tranformation

            q = int(input('Enter the number of queries : '))

            for y in range(q):
                print('\nQuery :')
                print('1) Rotate degree (rx) (ry)')
                print('2) Translate dx (dy)')
                print('3) Scale s')
                print('4) Plot\n')

                Query = input('Enter Query (R/T/S/P) : ')

                
                if(Query == 'R'):
                    values = list(map(float,input('Enter deg (rx) (ry) : ').split()))

                    print_cords_circ(circ) # prints x-coordinate , y-coordinate , Radius of the circle
                    prev = Circle(circ.center[0],circ.center[1],circ.radius) #stores circle's attributes before transformation

                    if(len(values) == 3):
                        circ.rotate(values[0],values[1],values[2])
                    elif(len(values) == 2):
                        circ.rotate(values[0],values[1])
                    else :
                        circ.rotate(values[0])
                    print_cords_circ(circ)

                    if(verbose == 1): # plots the circles if verbose is 1
                        circ.plot()

                elif(Query == 'T'):
                    values = list(map(float,input('Enter dx (dy) : ').split()))

                    print_cords_circ(circ)
                    prev = Circle(circ.center[0],circ.center[1],circ.radius)
                    
                    if(len(values) == 2):
                        circ.translate(values[0],values[1])
                    else :
                        circ.translate(values[0])
                    print_cords_circ(circ)
                    if(verbose == 1):
                        circ.plot()

                elif(Query == 'S'):
                    values = list(map(float,input('Enter s : ').split()))
                    print_cords_circ(circ)
                    prev = Circle(circ.center[0],circ.center[1],circ.radius)
                                       
                    circ.scale(values[0])
                    print_cords_circ(circ)

                    if(verbose == 1):
                        circ.plot()

                elif(Query == 'P'):

                    circ.plot()
    

        



                    

                    
                        

