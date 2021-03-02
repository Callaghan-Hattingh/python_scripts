class Rectangle:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.output = ''

    def set_width (self, width):
        self.width = width

    def set_height (self, height):
        self.height = height
    
    def get_area (self):
        return self.width*self.height
    
    def get_perimeter (self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal (self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture (self):
        if (self.width*self.height)>50:
            return "Too big for picture."
        else:
            picture = ''
            for i in range(0,self.height):
                picture += "*"*self.width+'\n'
        return picture
            

    def get_amount_inside (self, amount):
        times = 0 
        if (amount.width < self.width) and (amount.height < self.height):
            times = (self.height // amount.height)*(self.width // amount.width)
            return times
        else:
            times = 0 
            return times

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        

class Square (Rectangle):

    def __init__ (self,length):
        Rectangle.width = length
        Rectangle.height = length

    def set_side(self, length):
        Rectangle.width = length
        Rectangle.height = length   

    def set_width(self, length): 
        Rectangle.width = length
        Rectangle.height = length 

    def set_height(self, length):
        Rectangle.width = length
        Rectangle.height = length 

    def __str__(self):
        return f"Square(side={Rectangle.width})"   


    



