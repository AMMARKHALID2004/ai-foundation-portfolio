class Fraction:
    def __init__(self,num,den):
        self.numerator=num
        self.denominator=den

    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)

    def __add__(self,other):
        temp_den=0 #temporary denominator for holding the denominator of final added fraction
        if self.denominator%other.denominator==0:
            if self.denominator>other.denominator:
                temp_den=self.denominator
            elif other.denominator>self.denominator:
                temp_den=other.denominator
            elif self.denominator==other.denominator:
                temp_den=self.denominator
        else:
            temp_den=self.denominator*other.denominator
        added_num=((temp_den//self.denominator)*self.numerator+(temp_den//other.denominator)*other.numerator)
        final="{}/{}".format(added_num,temp_den)
        return final
    def __sub__(self, other):
        temp_den = 0  # temporary denominator for holding the denominator of final added fraction
        if self.denominator % other.denominator == 0:
            if self.denominator > other.denominator:
                temp_den = self.denominator
            elif other.denominator > self.denominator:
                temp_den = other.denominator
            elif self.denominator == other.denominator:
                temp_den = self.denominator
        else:
            temp_den = self.denominator * other.denominator
        added_num = ((temp_den // self.denominator) * self.numerator - (temp_den // other.denominator) * other.numerator)
        final = "{}/{}".format(added_num, temp_den)
        return final

    def __mul__(self, other):
        temp_num=(self.numerator*other.numerator)
        temp_den=(self.denominator*other.denominator)
        final_product="{}/{}".format(temp_num,temp_den)
        return final_product
    def __truediv__(self, other):
        temp_num=self.numerator*other.denominator
        temp_den=self.denominator*other.numerator
        final_div="{}/{}".format(temp_num,temp_den)
        return final_div
    def __eq__(self, other):
         temp_frac=self.numerator/self.denominator
         temp_frac2=other.numerator/other.denominator
         return temp_frac==temp_frac2
