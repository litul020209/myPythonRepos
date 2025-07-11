# height=20
# width=18
import math

def wall_area(*hight_width):
    area=1
    for i in hight_width:
        area=area*i
    print(f"total area is {area}")
    return area



def can_required(main_area,can_cover):
    required=(main_area/can_cover)
    approx_required=math.ceil(required)
    print(f"the total can required to pain whole wall is {approx_required}")

main_area=wall_area(20,18)

can_cover=7
can_required(main_area,can_cover)
