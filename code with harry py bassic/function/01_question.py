# height=20
# width=18

def wall_area(*hight_width):
    area=1
    for i in hight_width:
        area=area*i
    print(f"total area is {area}")

wall_area(20,18)