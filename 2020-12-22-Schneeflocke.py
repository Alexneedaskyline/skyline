from turtle import *


def schneeflocke(entwicklungsstufe, länge):
    if entwicklungsstufe == 1:
        forward(länge)
    else:
            schneeflocke(entwicklungsstufe - 1, länge / 3)
            left(60)
            schneeflocke(entwicklungsstufe - 1, länge / 3)
            right(120)
            schneeflocke(entwicklungsstufe - 1, länge / 3)
            left(60)
            schneeflocke(entwicklungsstufe - 1, länge / 3)


speed(0)
color("blue", "lightblue")
begin_fill()

schneeflocke(5, 400)
right(120)
schneeflocke(5, 400)
right(120)
schneeflocke(5, 400)

end_fill()

done()




uzJzFccXe