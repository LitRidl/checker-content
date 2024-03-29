from __future__ import print_function
from random import shuffle, randint, choice

def test(*data):
    txt = ' '.join(str(x) for x in data) + '\n'
    with open('tests/{0:03d}.dat'.format(test.idx), 'w') as f:
        f.write(txt)
    test.idx += 1


if __name__ == '__main__':
    test.idx = 1
    test(0, 0, 0)
    test(-1, -1, -1)
    test(-10, -10, -10)
    test(-10, -10, -15)
    test(-10, -10, -20)
    test(-10, -10, -5)
    test(-10, -10, 0)
    test(-10, -10, 10)
    test(-10, -10, 15)
    test(-10, -10, 20)
    test(-10, -10, 5)
    test(-10, -15, -10)
    test(-10, -15, -15)
    test(-10, -15, -20)
    test(-10, -15, -5)
    test(-10, -15, 0)
    test(-10, -15, 10)
    test(-10, -15, 15)
    test(-10, -15, 20)
    test(-10, -15, 5)
    test(-10, -20, -10)
    test(-10, -20, -15)
    test(-10, -20, -20)
    test(-10, -20, -5)
    test(-10, -20, 0)
    test(-10, -20, 10)
    test(-10, -20, 15)
    test(-10, -20, 20)
    test(-10, -20, 5)
    test(-10, -5, -10)
    test(-10, -5, -15)
    test(-10, -5, -20)
    test(-10, -5, -5)
    test(-10, -5, 0)
    test(-10, -5, 10)
    test(-10, -5, 15)
    test(-10, -5, 20)
    test(-10, -5, 5)
    test(-10, 0)
    test(-10, 0, -10)
    test(-10, 0, -15)
    test(-10, 0, -20)
    test(-10, 0, -5)
    test(-10, 0, 0)
    test(-10, 0, 10)
    test(-10, 0, 15)
    test(-10, 0, 20)
    test(-10, 0, 5)
    test(-10, 10, -10)
    test(-10, 10, -15)
    test(-10, 10, -20)
    test(-10, 10, -5)
    test(-10, 10, 0)
    test(-10, 10, 10)
    test(-10, 10, 15)
    test(-10, 10, 20)
    test(-10, 10, 5)
    test(-10, 15, -10)
    test(-10, 15, -15)
    test(-10, 15, -20)
    test(-10, 15, -5)
    test(-10, 15, 0)
    test(-10, 15, 10)
    test(-10, 15, 15)
    test(-10, 15, 20)
    test(-10, 15, 5)
    test(-10, 20, -10)
    test(-10, 20, -15)
    test(-10, 20, -20)
    test(-10, 20, -5)
    test(-10, 20, 0)
    test(-10, 20, 10)
    test(-10, 20, 15)
    test(-10, 20, 20)
    test(-10, 20, 5)
    test(-10, 25, -10)
    test(-10, 25, -15)
    test(-10, 25, -20)
    test(-10, 25, -5)
    test(-10, 25, 0)
    test(-10, 25, 10)
    test(-10, 25, 15)
    test(-10, 25, 20)
    test(-10, 25, 5)
    test(-10, 5, -10)
    test(-10, 5, -15)
    test(-10, 5, -20)
    test(-10, 5, -5)
    test(-10, 5, 0)
    test(-10, 5, 10)
    test(-10, 5, 15)
    test(-10, 5, 20)
    test(-10, 5, 5)
    test(-1000, 0, 0)
    test(-106, -192, -496)
    test(-113, -388, -663)
    test(-114, -734, 91)
    test(-126, -318, 447)
    test(-126, -804, 667)
    test(-137, 853, 329)
    test(-14, -912, -198)
    test(-15, -10, -10)
    test(-15, -10, -15)
    test(-15, -10, -20)
    test(-15, -10, -5)
    test(-15, -10, 0)
    test(-15, -10, 10)
    test(-15, -10, 15)
    test(-15, -10, 20)
    test(-15, -10, 5)
    test(-15, -15, -10)
    test(-15, -15, -15)
    test(-15, -15, -20)
    test(-15, -15, -5)
    test(-15, -15, 0)
    test(-15, -15, 10)
    test(-15, -15, 15)
    test(-15, -15, 20)
    test(-15, -15, 5)
    test(-15, -20, -10)
    test(-15, -20, -15)
    test(-15, -20, -20)
    test(-15, -20, -5)
    test(-15, -20, 0)
    test(-15, -20, 10)
    test(-15, -20, 15)
    test(-15, -20, 20)
    test(-15, -20, 5)
    test(-15, -5, -10)
    test(-15, -5, -15)
    test(-15, -5, -20)
    test(-15, -5, -5)
    test(-15, -5, 0)
    test(-15, -5, 10)
    test(-15, -5, 15)
    test(-15, -5, 20)
    test(-15, -5, 5)
    test(-15, 0, -10)
    test(-15, 0, -15)
    test(-15, 0, -20)
    test(-15, 0, -5)
    test(-15, 0, 0)
    test(-15, 0, 10)
    test(-15, 0, 15)
    test(-15, 0, 20)
    test(-15, 0, 5)
    test(-15, 10, -10)
    test(-15, 10, -15)
    test(-15, 10, -20)
    test(-15, 10, -5)
    test(-15, 10, 0)
    test(-15, 10, 10)
    test(-15, 10, 15)
    test(-15, 10, 20)
    test(-15, 10, 5)
    test(-15, 15, -10)
    test(-15, 15, -15)
    test(-15, 15, -20)
    test(-15, 15, -5)
    test(-15, 15, 0)
    test(-15, 15, 10)
    test(-15, 15, 15)
    test(-15, 15, 20)
    test(-15, 15, 5)
    test(-15, 20, -10)
    test(-15, 20, -15)
    test(-15, 20, -20)
    test(-15, 20, -5)
    test(-15, 20, 0)
    test(-15, 20, 10)
    test(-15, 20, 15)
    test(-15, 20, 20)
    test(-15, 20, 5)
    test(-15, 25, -10)
    test(-15, 25, -15)
    test(-15, 25, -20)
    test(-15, 25, -5)
    test(-15, 25, 0)
    test(-15, 25, 10)
    test(-15, 25, 15)
    test(-15, 25, 20)
    test(-15, 25, 5)
    test(-15, 5, -10)
    test(-15, 5, -15)
    test(-15, 5, -20)
    test(-15, 5, -5)
    test(-15, 5, 0)
    test(-15, 5, 10)
    test(-15, 5, 15)
    test(-15, 5, 20)
    test(-15, 5, 5)
    test(-154, 293, -281)
    test(-16, 651, -811)
    test(-164, -865, -46)
    test(-169, -893, 924)
    test(-172, -296, -591)
    test(-190, 947, 293)
    test(-20, -10, -10)
    test(-20, -10, -15)
    test(-20, -10, -20)
    test(-20, -10, -5)
    test(-20, -10, 0)
    test(-20, -10, 10)
    test(-20, -10, 15)
    test(-20, -10, 20)
    test(-20, -10, 5)
    test(-20, -15, -10)
    test(-20, -15, -15)
    test(-20, -15, -20)
    test(-20, -15, -5)
    test(-20, -15, 0)
    test(-20, -15, 10)
    test(-20, -15, 15)
    test(-20, -15, 20)
    test(-20, -15, 5)
    test(-20, -20, -10)
    test(-20, -20, -15)
    test(-20, -20, -20)
    test(-20, -20, -5)
    test(-20, -20, 0)
    test(-20, -20, 10)
    test(-20, -20, 15)
    test(-20, -20, 20)
    test(-20, -20, 5)
    test(-20, -5, -10)
    test(-20, -5, -15)
    test(-20, -5, -20)
    test(-20, -5, -5)
    test(-20, -5, 0)
    test(-20, -5, 10)
    test(-20, -5, 15)
    test(-20, -5, 20)
    test(-20, -5, 5)
    test(-20, 0, -10)
    test(-20, 0, -15)
    test(-20, 0, -20)
    test(-20, 0, -5)
    test(-20, 0, 0)
    test(-20, 0, 10)
    test(-20, 0, 15)
    test(-20, 0, 20)
    test(-20, 0, 5)
    test(-20, 10, -10)
    test(-20, 10, -15)
    test(-20, 10, -20)
    test(-20, 10, -5)
    test(-20, 10, 0)
    test(-20, 10, 10)
    test(-20, 10, 15)
    test(-20, 10, 20)
    test(-20, 10, 5)
    test(-20, 15, -10)
    test(-20, 15, -15)
    test(-20, 15, -20)
    test(-20, 15, -5)
    test(-20, 15, 0)
    test(-20, 15, 10)
    test(-20, 15, 15)
    test(-20, 15, 20)
    test(-20, 15, 5)
    test(-20, 20, -10)
    test(-20, 20, -15)
    test(-20, 20, -20)
    test(-20, 20, -5)
    test(-20, 20, 0)
    test(-20, 20, 10)
    test(-20, 20, 15)
    test(-20, 20, 20)
    test(-20, 20, 5)
    test(-20, 25, -10)
    test(-20, 25, -15)
    test(-20, 25, -20)
    test(-20, 25, -5)
    test(-20, 25, 0)
    test(-20, 25, 10)
    test(-20, 25, 15)
    test(-20, 25, 20)
    test(-20, 25, 5)
    test(-20, 5, -10)
    test(-20, 5, -15)
    test(-20, 5, -20)
    test(-20, 5, -5)
    test(-20, 5, 0)
    test(-20, 5, 10)
    test(-20, 5, 15)
    test(-20, 5, 20)
    test(-20, 5, 5)
    test(-200, 64, 504)
    test(-210, -327, -581)
    test(-227, -649, -814)
    test(-236, 684, 935)
    test(-240, -826, -139)
    test(-240, 870, 653)
    test(-263, 916, 683)
    test(-265, -328, -470)
    test(-266, 151, 217)
    test(-27, -13, 0)
    test(-293, 473, 64)
    test(-299, -580, -186)
    test(-3, -3, 13)
    test(-30, -475, 532)
    test(-303, -411, 533)
    test(-323, -534, 322)
    test(-329, 426, 533)
    test(-33, 958, 741)
    test(-34, 39, 220)
    test(-35, 460, -943)
    test(-351, -558, 578)
    test(-36, -323, 580)
    test(-360, 664, 543)
    test(-384, -354, 531)
    test(-391, 420, 239)
    test(-399, 572, 181)
    test(-417, -607, -45)
    test(-424, 193, 946)
    test(-439, -917, 198)
    test(-457, 994, 802)
    test(-458, -739, 960)
    test(-479, -710, -244)
    test(-484, -178, -318)
    test(-485, 247, 812)
    test(-487, -59, 721)
    test(-493, -280, -846)
    test(-496, -808, -82)
    test(-498, -628, 591)
    test(-5, -10, -10)
    test(-5, -10, -15)
    test(-5, -10, -20)
    test(-5, -10, -5)
    test(-5, -10, 0)
    test(-5, -10, 10)
    test(-5, -10, 15)
    test(-5, -10, 20)
    test(-5, -10, 5)
    test(-5, -15, -10)
    test(-5, -15, -15)
    test(-5, -15, -20)
    test(-5, -15, -5)
    test(-5, -15, 0)
    test(-5, -15, 10)
    test(-5, -15, 15)
    test(-5, -15, 20)
    test(-5, -15, 5)
    test(-5, -20, -10)
    test(-5, -20, -15)
    test(-5, -20, -20)
    test(-5, -20, -5)
    test(-5, -20, 0)
    test(-5, -20, 10)
    test(-5, -20, 15)
    test(-5, -20, 20)
    test(-5, -20, 5)
    test(-5, -5, -10)
    test(-5, -5, -15)
    test(-5, -5, -20)
    test(-5, -5, -5)
    test(-5, -5, 0)
    test(-5, -5, 10)
    test(-5, -5, 15)
    test(-5, -5, 20)
    test(-5, -5, 5)
    test(-5, 0, -10)
    test(-5, 0, -15)
    test(-5, 0, -20)
    test(-5, 0, -5)
    test(-5, 0, 0)
    test(-5, 0, 10)
    test(-5, 0, 15)
    test(-5, 0, 20)
    test(-5, 0, 5)
    test(-5, 10, -10)
    test(-5, 10, -15)
    test(-5, 10, -20)
    test(-5, 10, -5)
    test(-5, 10, 0)
    test(-5, 10, 10)
    test(-5, 10, 15)
    test(-5, 10, 20)
    test(-5, 10, 5)
    test(-5, 15, -10)
    test(-5, 15, -15)
    test(-5, 15, -20)
    test(-5, 15, -5)
    test(-5, 15, 0)
    test(-5, 15, 10)
    test(-5, 15, 15)
    test(-5, 15, 20)
    test(-5, 15, 5)
    test(-5, 20, -10)
    test(-5, 20, -15)
    test(-5, 20, -20)
    test(-5, 20, -5)
    test(-5, 20, 0)
    test(-5, 20, 10)
    test(-5, 20, 15)
    test(-5, 20, 20)
    test(-5, 20, 5)
    test(-5, 25, -10)
    test(-5, 25, -15)
    test(-5, 25, -20)
    test(-5, 25, -5)
    test(-5, 25, 0)
    test(-5, 25, 10)
    test(-5, 25, 15)
    test(-5, 25, 20)
    test(-5, 25, 5)
    test(-5, 5, -10)
    test(-5, 5, -15)
    test(-5, 5, -20)
    test(-5, 5, -5)
    test(-5, 5, 0)
    test(-5, 5, 10)
    test(-5, 5, 15)
    test(-5, 5, 20)
    test(-5, 5, 5)
    test(-502, -553, -121)
    test(-527, 17, 753)
    test(-536, 805, -60)
    test(-541, 969, -9)
    test(-567, 810, -524)
    test(-591, 229, -820)
    test(-6, -6, 24)
    test(-6, -7, 342)
    test(-602, -991, 407)
    test(-606, -328, 200)
    test(-619, 373, 584)
    test(-620, -429, 886)
    test(-632, -236, -10)
    test(-636, -176, 386)
    test(-652, 834, -359)
    test(-67, 922, -9)
    test(-674, -683, -494)
    test(-695, -616, 185)
    test(-7, 10, 20)
    test(-708, 974, 691)
    test(-714, -978, -91)
    test(-727, 463, 242)
    test(-737, -268, 131)
    test(-760, 664, -781)
    test(-761, -447, 601)
    test(-774, 945, 210)
    test(-778, -911, 167)
    test(-801, 38, 771)
    test(-804, 329, -76)
    test(-822, 470, 365)
    test(-826, -25, 127)
    test(-828, 149, -445)
    test(-829, -182, -798)
    test(-835, -782, -544)
    test(-846, -263, -995)
    test(-851, -555, 275)
    test(-856, -76, 38)
    test(-864, 733, 427)
    test(-868, -402, -936)
    test(-869, 534, 994)
    test(-874, -915, -131)
    test(-905, -187, -322)
    test(-916, -44, -256)
    test(-920, 293, -285)
    test(-931, 28, -310)
    test(-962, -806, -270)
    test(-969, -687, -561)
    test(-977, 944, -379)
    test(-981, 69, 494)
    test(-999, 368, -533)
    test(0, -10, -10)
    test(0, -10, -15)
    test(0, -10, -20)
    test(0, -10, -5)
    test(0, -10, 0)
    test(0, -10, 10)
    test(0, -10, 15)
    test(0, -10, 20)
    test(0, -10, 5)
    test(0, -15, -10)
    test(0, -15, -15)
    test(0, -15, -20)
    test(0, -15, -5)
    test(0, -15, 0)
    test(0, -15, 10)
    test(0, -15, 15)
    test(0, -15, 20)
    test(0, -15, 5)
    test(0, -20, -10)
    test(0, -20, -15)
    test(0, -20, -20)
    test(0, -20, -5)
    test(0, -20, 0)
    test(0, -20, 10)
    test(0, -20, 15)
    test(0, -20, 20)
    test(0, -20, 5)
    test(0, -5, -10)
    test(0, -5, -15)
    test(0, -5, -20)
    test(0, -5, -5)
    test(0, -5, 0)
    test(0, -5, 10)
    test(0, -5, 15)
    test(0, -5, 20)
    test(0, -5, 5)
    test(0, 0, -10)
    test(0, 0, -15)
    test(0, 0, -20)
    test(0, 0, -5)
    test(0, 0, 10)
    test(0, 0, 15)
    test(0, 0, 20)
    test(0, 0, 5)
    test(0, 10, -10)
    test(0, 10, -15)
    test(0, 10, -20)
    test(0, 10, -5)
    test(0, 10, -50)
    test(0, 10, 0)
    test(0, 10, 10)
    test(0, 10, 15)
    test(0, 10, 20)
    test(0, 10, 5)
    test(0, 15, -10)
    test(0, 15, -15)
    test(0, 15, -20)
    test(0, 15, -5)
    test(0, 15, 0)
    test(0, 15, 10)
    test(0, 15, 15)
    test(0, 15, 20)
    test(0, 15, 5)
    test(0, 20, -10)
    test(0, 20, -15)
    test(0, 20, -20)
    test(0, 20, -5)
    test(0, 20, 0)
    test(0, 20, 10)
    test(0, 20, 15)
    test(0, 20, 20)
    test(0, 20, 5)
    test(0, 25, -10)
    test(0, 25, -15)
    test(0, 25, -20)
    test(0, 25, -5)
    test(0, 25, 0)
    test(0, 25, 10)
    test(0, 25, 15)
    test(0, 25, 20)
    test(0, 25, 5)
    test(0, 5, -10)
    test(0, 5, -15)
    test(0, 5, -20)
    test(0, 5, -5)
    test(0, 5, 0)
    test(0, 5, 10)
    test(0, 5, 15)
    test(0, 5, 20)
    test(0, 5, 5)
    test(1, 1, 1)
    test(1, 23, -598)
    test(10, -10, -10)
    test(10, -10, -15)
    test(10, -10, -20)
    test(10, -10, -5)
    test(10, -10, 0)
    test(10, -10, 10)
    test(10, -10, 15)
    test(10, -10, 20)
    test(10, -10, 5)
    test(10, -15, -10)
    test(10, -15, -15)
    test(10, -15, -20)
    test(10, -15, -5)
    test(10, -15, 0)
    test(10, -15, 10)
    test(10, -15, 15)
    test(10, -15, 20)
    test(10, -15, 5)
    test(10, -20, -10)
    test(10, -20, -15)
    test(10, -20, -20)
    test(10, -20, -5)
    test(10, -20, 0)
    test(10, -20, 10)
    test(10, -20, 15)
    test(10, -20, 20)
    test(10, -20, 5)
    test(10, -5, -10)
    test(10, -5, -15)
    test(10, -5, -20)
    test(10, -5, -5)
    test(10, -5, 0)
    test(10, -5, 10)
    test(10, -5, 15)
    test(10, -5, 20)
    test(10, -5, 5)
    test(10, 0, -10)
    test(10, 0, -15)
    test(10, 0, -20)
    test(10, 0, -5)
    test(10, 0, 0)
    test(10, 0, 10)
    test(10, 0, 15)
    test(10, 0, 20)
    test(10, 0, 5)
    test(10, 10, -10)
    test(10, 10, -15)
    test(10, 10, -20)
    test(10, 10, -5)
    test(10, 10, 0)
    test(10, 10, 10)
    test(10, 10, 15)
    test(10, 10, 20)
    test(10, 10, 5)
    test(10, 15, -10)
    test(10, 15, -15)
    test(10, 15, -20)
    test(10, 15, -5)
    test(10, 15, 0)
    test(10, 15, 10)
    test(10, 15, 15)
    test(10, 15, 20)
    test(10, 15, 5)
    test(10, 17, -5)
    test(10, 20, -10)
    test(10, 20, -15)
    test(10, 20, -20)
    test(10, 20, -5)
    test(10, 20, 0)
    test(10, 20, 10)
    test(10, 20, 15)
    test(10, 20, 20)
    test(10, 20, 5)
    test(10, 25, -10)
    test(10, 25, -15)
    test(10, 25, -20)
    test(10, 25, -5)
    test(10, 25, 0)
    test(10, 25, 10)
    test(10, 25, 15)
    test(10, 25, 20)
    test(10, 25, 5)
    test(10, 5, -10)
    test(10, 5, -15)
    test(10, 5, -20)
    test(10, 5, -5)
    test(10, 5, 0)
    test(10, 5, 10)
    test(10, 5, 15)
    test(10, 5, 20)
    test(10, 5, 5)
    test(100, -100, 100)
    test(1000, 1000, 1000)
    test(101, 234, 976)
    test(112, 882, -158)
    test(12, -17, 0)
    test(14, -6, 0)
    test(14, 88, 662)
    test(146, -105, -641)
    test(146, -264, -237)
    test(15, -10, -10)
    test(15, -10, -15)
    test(15, -10, -20)
    test(15, -10, -5)
    test(15, -10, 0)
    test(15, -10, 10)
    test(15, -10, 15)
    test(15, -10, 20)
    test(15, -10, 5)
    test(15, -15, -10)
    test(15, -15, -15)
    test(15, -15, -20)
    test(15, -15, -5)
    test(15, -15, 0)
    test(15, -15, 10)
    test(15, -15, 15)
    test(15, -15, 20)
    test(15, -15, 5)
    test(15, -20, -10)
    test(15, -20, -15)
    test(15, -20, -20)
    test(15, -20, -5)
    test(15, -20, 0)
    test(15, -20, 10)
    test(15, -20, 15)
    test(15, -20, 20)
    test(15, -20, 5)
    test(15, -5, -10)
    test(15, -5, -15)
    test(15, -5, -20)
    test(15, -5, -5)
    test(15, -5, 0)
    test(15, -5, 10)
    test(15, -5, 15)
    test(15, -5, 20)
    test(15, -5, 5)
    test(15, 0, -10)
    test(15, 0, -15)
    test(15, 0, -20)
    test(15, 0, -5)
    test(15, 0, 0)
    test(15, 0, 10)
    test(15, 0, 15)
    test(15, 0, 20)
    test(15, 0, 5)
    test(15, 10, -10)
    test(15, 10, -15)
    test(15, 10, -20)
    test(15, 10, -5)
    test(15, 10, 0)
    test(15, 10, 10)
    test(15, 10, 15)
    test(15, 10, 20)
    test(15, 10, 5)
    test(15, 15, -10)
    test(15, 15, -15)
    test(15, 15, -20)
    test(15, 15, -5)
    test(15, 15, 0)
    test(15, 15, 10)
    test(15, 15, 15)
    test(15, 15, 20)
    test(15, 15, 5)
    test(15, 20, -10)
    test(15, 20, -15)
    test(15, 20, -20)
    test(15, 20, -5)
    test(15, 20, 0)
    test(15, 20, 10)
    test(15, 20, 15)
    test(15, 20, 20)
    test(15, 20, 5)
    test(15, 25, -10)
    test(15, 25, -15)
    test(15, 25, -20)
    test(15, 25, -5)
    test(15, 25, 0)
    test(15, 25, 10)
    test(15, 25, 15)
    test(15, 25, 20)
    test(15, 25, 5)
    test(15, 5, -10)
    test(15, 5, -15)
    test(15, 5, -20)
    test(15, 5, -5)
    test(15, 5, 0)
    test(15, 5, 10)
    test(15, 5, 15)
    test(15, 5, 20)
    test(15, 5, 5)
    test(173, -197, -755)
    test(180, -13, -331)
    test(20, -10, -10)
    test(20, -10, -15)
    test(20, -10, -20)
    test(20, -10, -5)
    test(20, -10, 0)
    test(20, -10, 10)
    test(20, -10, 15)
    test(20, -10, 20)
    test(20, -10, 5)
    test(20, -15, -10)
    test(20, -15, -15)
    test(20, -15, -20)
    test(20, -15, -5)
    test(20, -15, 0)
    test(20, -15, 10)
    test(20, -15, 15)
    test(20, -15, 20)
    test(20, -15, 5)
    test(20, -20, -10)
    test(20, -20, -15)
    test(20, -20, -20)
    test(20, -20, -5)
    test(20, -20, 0)
    test(20, -20, 10)
    test(20, -20, 15)
    test(20, -20, 20)
    test(20, -20, 5)
    test(20, -5, -10)
    test(20, -5, -15)
    test(20, -5, -20)
    test(20, -5, -5)
    test(20, -5, 0)
    test(20, -5, 10)
    test(20, -5, 15)
    test(20, -5, 20)
    test(20, -5, 5)
    test(20, 0, -10)
    test(20, 0, -15)
    test(20, 0, -20)
    test(20, 0, -5)
    test(20, 0, 0)
    test(20, 0, 10)
    test(20, 0, 15)
    test(20, 0, 20)
    test(20, 0, 5)
    test(20, 10, -10)
    test(20, 10, -15)
    test(20, 10, -20)
    test(20, 10, -5)
    test(20, 10, 0)
    test(20, 10, 10)
    test(20, 10, 15)
    test(20, 10, 20)
    test(20, 10, 5)
    test(20, 15, -10)
    test(20, 15, -15)
    test(20, 15, -20)
    test(20, 15, -5)
    test(20, 15, 0)
    test(20, 15, 10)
    test(20, 15, 15)
    test(20, 15, 20)
    test(20, 15, 5)
    test(20, 20, -10)
    test(20, 20, -15)
    test(20, 20, -20)
    test(20, 20, -5)
    test(20, 20, 0)
    test(20, 20, 10)
    test(20, 20, 15)
    test(20, 20, 20)
    test(20, 20, 5)
    test(20, 25, -10)
    test(20, 25, -15)
    test(20, 25, -20)
    test(20, 25, -5)
    test(20, 25, 0)
    test(20, 25, 10)
    test(20, 25, 15)
    test(20, 25, 20)
    test(20, 25, 5)
    test(20, 5, -10)
    test(20, 5, -15)
    test(20, 5, -20)
    test(20, 5, -5)
    test(20, 5, 0)
    test(20, 5, 10)
    test(20, 5, 15)
    test(20, 5, 20)
    test(20, 5, 5)
    test(215, 971, 73)
    test(216, 61, 651)
    test(227, -246, 756)
    test(229, -879, -167)
    test(23, 111, 157)
    test(246, -30, -712)
    test(25, -10, -10)
    test(25, -10, -15)
    test(25, -10, -20)
    test(25, -10, -5)
    test(25, -10, 0)
    test(25, -10, 10)
    test(25, -10, 15)
    test(25, -10, 20)
    test(25, -10, 5)
    test(25, -15, -10)
    test(25, -15, -15)
    test(25, -15, -20)
    test(25, -15, -5)
    test(25, -15, 0)
    test(25, -15, 10)
    test(25, -15, 15)
    test(25, -15, 20)
    test(25, -15, 5)
    test(25, -20, -10)
    test(25, -20, -15)
    test(25, -20, -20)
    test(25, -20, -5)
    test(25, -20, 0)
    test(25, -20, 10)
    test(25, -20, 15)
    test(25, -20, 20)
    test(25, -20, 5)
    test(25, -5, -10)
    test(25, -5, -15)
    test(25, -5, -20)
    test(25, -5, -5)
    test(25, -5, 0)
    test(25, -5, 10)
    test(25, -5, 15)
    test(25, -5, 20)
    test(25, -5, 5)
    test(25, 0, -10)
    test(25, 0, -15)
    test(25, 0, -20)
    test(25, 0, -5)
    test(25, 0, 0)
    test(25, 0, 10)
    test(25, 0, 15)
    test(25, 0, 20)
    test(25, 0, 5)
    test(25, 10, -10)
    test(25, 10, -15)
    test(25, 10, -20)
    test(25, 10, -5)
    test(25, 10, 0)
    test(25, 10, 10)
    test(25, 10, 15)
    test(25, 10, 20)
    test(25, 10, 5)
    test(25, 15, -10)
    test(25, 15, -15)
    test(25, 15, -20)
    test(25, 15, -5)
    test(25, 15, 0)
    test(25, 15, 10)
    test(25, 15, 15)
    test(25, 15, 20)
    test(25, 15, 5)
    test(25, 20, -10)
    test(25, 20, -15)
    test(25, 20, -20)
    test(25, 20, -5)
    test(25, 20, 0)
    test(25, 20, 10)
    test(25, 20, 15)
    test(25, 20, 20)
    test(25, 20, 5)
    test(25, 25, -10)
    test(25, 25, -15)
    test(25, 25, -20)
    test(25, 25, -5)
    test(25, 25, 0)
    test(25, 25, 10)
    test(25, 25, 15)
    test(25, 25, 20)
    test(25, 25, 5)
    test(25, 5, -10)
    test(25, 5, -15)
    test(25, 5, -20)
    test(25, 5, -5)
    test(25, 5, 0)
    test(25, 5, 10)
    test(25, 5, 15)
    test(25, 5, 20)
    test(25, 5, 5)
    test(254, -796, -14)
    test(254, 729, 756)
    test(262, -567, -197)
    test(267, -54, 811)
    test(275, -112, -829)
    test(285, -860, 773)
    test(292, 132, 478)
    test(321, 59, 956)
    test(331, 338, 567)
    test(340, -840, -95)
    test(340, 934, 474)
    test(342, 245, -501)
    test(346, 306, -150)
    test(357, -723, 850)
    test(37, -485, 417)
    test(374, 495, 786)
    test(390, -873, 778)
    test(395, 971, 97)
    test(401, -18, -68)
    test(408, -377, -961)
    test(414, -899, 636)
    test(424, -803, -668)
    test(442, 791, 379)
    test(454, 542, -283)
    test(455, 518, 924)
    test(459, -681, 224)
    test(459, 113, -722)
    test(460, -885, 144)
    test(479, 856, -540)
    test(486, -871, -839)
    test(5, -10, -10)
    test(5, -10, -15)
    test(5, -10, -20)
    test(5, -10, -5)
    test(5, -10, 0)
    test(5, -10, 10)
    test(5, -10, 15)
    test(5, -10, 20)
    test(5, -10, 5)
    test(5, -15, -10)
    test(5, -15, -15)
    test(5, -15, -20)
    test(5, -15, -5)
    test(5, -15, 0)
    test(5, -15, 10)
    test(5, -15, 15)
    test(5, -15, 20)
    test(5, -15, 5)
    test(5, -20, -10)
    test(5, -20, -15)
    test(5, -20, -20)
    test(5, -20, -5)
    test(5, -20, 0)
    test(5, -20, 10)
    test(5, -20, 15)
    test(5, -20, 20)
    test(5, -20, 5)
    test(5, -5, -10)
    test(5, -5, -15)
    test(5, -5, -20)
    test(5, -5, -5)
    test(5, -5, 0)
    test(5, -5, 10)
    test(5, -5, 15)
    test(5, -5, 20)
    test(5, -5, 5)
    test(5, 0, -10)
    test(5, 0, -15)
    test(5, 0, -20)
    test(5, 0, -5)
    test(5, 0, 0)
    test(5, 0, 10)
    test(5, 0, 15)
    test(5, 0, 20)
    test(5, 0, 5)
    test(5, 10, -10)
    test(5, 10, -15)
    test(5, 10, -20)
    test(5, 10, -5)
    test(5, 10, 0)
    test(5, 10, 10)
    test(5, 10, 15)
    test(5, 10, 20)
    test(5, 10, 5)
    test(5, 15, -10)
    test(5, 15, -15)
    test(5, 15, -20)
    test(5, 15, -5)
    test(5, 15, 0)
    test(5, 15, 10)
    test(5, 15, 15)
    test(5, 15, 20)
    test(5, 15, 5)
    test(5, 20, -10)
    test(5, 20, -15)
    test(5, 20, -20)
    test(5, 20, -5)
    test(5, 20, 0)
    test(5, 20, 10)
    test(5, 20, 15)
    test(5, 20, 20)
    test(5, 20, 5)
    test(5, 25, -10)
    test(5, 25, -15)
    test(5, 25, -20)
    test(5, 25, -5)
    test(5, 25, 0)
    test(5, 25, 10)
    test(5, 25, 15)
    test(5, 25, 20)
    test(5, 25, 5)
    test(5, 5, -10)
    test(5, 5, -15)
    test(5, 5, -20)
    test(5, 5, -5)
    test(5, 5, 0)
    test(5, 5, 10)
    test(5, 5, 15)
    test(5, 5, 20)
    test(5, 5, 5)
    test(506, 899, 647)
    test(512, -821, -811)
    test(513, 78, 567)
    test(518, -374, -771)
    test(552, -895, -325)
    test(555, 725, 537)
    test(577, -683, -547)
    test(578, -152, 290)
    test(59, -833, -606)
    test(593, 6, -824)
    test(601, -470, -730)
    test(605, -152, 177)
    test(628, -123, -90)
    test(637, 101, -701)
    test(638, -261, 523)
    test(65, -338, 93)
    test(652, 470, -977)
    test(66, 855, -17)
    test(666, 372, -344)
    test(683, 583, 487)
    test(690, -112, 582)
    test(70, 447, -491)
    test(707, -818, 980)
    test(719, 663, 655)
    test(734, -618, -880)
    test(741, -243, -663)
    test(744, 50, 262)
    test(747, 254, -276)
    test(749, 312, -145)
    test(752, 568, -397)
    test(762, 783, 802)
    test(782, -985, 491)
    test(786, -308, 956)
    test(798, 437, 3)
    test(820, 262, 555)
    test(825, 789, 794)
    test(835, -815, 72)
    test(85, 198, -621)
    test(852, 549, -183)
    test(855, -828, 629)
    test(858, -917, 155)
    test(864, -901, 1)
    test(867, -295, -876)
    test(871, -528, -326)
    test(876, -427, 789)
    test(876, 272, 385)
    test(892, 307, 741)
    test(895, -243, 8)
    test(896, -179, 540)
    test(899, 203, 83)
    test(915, 116, -650)
    test(916, -787, 40)
    test(920, -38, 195)
    test(94, -952, 697)
    test(94, -953, 933)
    test(943, 281, -125)
    test(951, 23, 20)
    test(98, 918, 768)
    test(987, -2, -196)
    test(99, -949, -781)
