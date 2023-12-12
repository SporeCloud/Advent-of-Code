class trebuchet_dirty:
    def __init__(self, file_input):
        with open(file_input,"r") as f:
            self.lines = f.readlines()
            self.total = 0
            self.actual_total = 0
    
    def dirty_solution(self):
        for line in self.lines:
            asciis = [char for char in line if ord(char)>48 and ord(char)<=57]
            print(asciis)
            line_total = int(asciis[0]+asciis[-1])
            print(line_total)
            self.total += line_total
        
        return self.total
    
    def dirty_solution2(self):
        import re
        get_digit = lambda x: x if x.isnumeric() else str(letter_digits.index(x))
        letter_digits = ["","one","two","three","four","five","six","seven","eight","nine"]
        regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
        
        for line in self.lines:
            digits = re.findall(regex,line)
            self.actual_total += int(get_digit(digits[0]) + get_digit(digits[-1]))
        print(self.actual_total)
        return self.actual_total

x = trebuchet_dirty("calibration_codes.txt")
x.dirty_solution2()