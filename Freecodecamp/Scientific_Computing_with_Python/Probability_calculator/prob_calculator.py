import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k,v in kwargs.items():
            setattr(self, k, v)
            self.contents += [k for _ in range(v)]

    def draw(self, num_of_balls):
        draw_list = []
        if num_of_balls > len(self.contents):
            return self.contents
        else:
            while len(draw_list) < num_of_balls:
                ball_index = random.randint(0,len(self.contents)-1)
                draw_list.append(self.contents[ball_index]) 
                self.contents.remove(self.contents[ball_index])
            return draw_list
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    corr_amount = 0 
    for _ in range(num_experiments):
        ext_hat = copy.deepcopy(hat)
        draw = ext_hat.draw(num_balls_drawn) 
        corr_colour = 0
        for i in expected_balls.keys():
            if draw.count(i) >= expected_balls[i]:
                corr_colour += 1
        if corr_colour == len(expected_balls):
            corr_amount += 1
    return corr_amount/num_experiments
