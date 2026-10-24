from Custom_Datatype.Fraction import Fraction


class Tests:
    fraction1=Fraction(9,21)
    fraction2=Fraction(2,17)

    print(fraction1+fraction2)
    print(fraction1 - fraction2)
    print(fraction1 * fraction2)
    print(fraction1 / fraction2)
    print(fraction1==fraction2)