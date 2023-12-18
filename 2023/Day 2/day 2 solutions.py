import re

class elfcubegame:
    def __init__(self, file_input):
        with open(file_input,"r") as f: self.lines = f.readlines()
        self.id_total = 0
        self.powers_sum = 0
        self.re_string = r"\d?\d [rgb]"
        self.p = re.compile(r"\d?\d")
    
    def problem_1(self):
        limits = {"r":12,"g":13,"b":14}
        for x,y in enumerate(self.lines):
            iter = re.findall(self.re_string,y)
            flag = False
            for result in iter:
                colour = result[-1]
                count_object = self.p.match(result)
                count = int(count_object.group())
                if limits[colour] < count:
                    flag = True
                    break
            if not flag:
                self.id_total += (x+1)
        return self.id_total
    
    def problem_2(self):
        for line in self.lines:
            iter = re.findall(self.re_string,line)
            limits = {"r":0,"g":0,"b":0}
            for result in iter:
                colour = result[-1]
                count_object = self.p.match(result)
                count = int(count_object.group())
                limits[colour] = max(limits[colour], count)
            self.powers_sum += limits["r"]*limits["g"]*limits["b"]
            
        
        return self.powers_sum
