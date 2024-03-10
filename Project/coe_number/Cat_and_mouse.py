def cat_and_mouse(Cat_A,Cat_B,Mouse_C) :
    if abs(Cat_A - Mouse_C) == abs(Cat_B - Mouse_C) : 
        return ("Mouse C")
    else : 
        if abs(Cat_A - Mouse_C) < abs(Cat_B - Mouse_C)  : 
            return ("Cat A")
        if  abs(Cat_B - Mouse_C) <  abs(Cat_A - Mouse_C)  : 
            return ("Cat B")