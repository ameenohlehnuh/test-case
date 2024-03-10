from coe_number.Cat_and_mouse import cat_and_mouse
import unittest


class cat_and_mouseTest(unittest.TestCase):

    def test_catB_win(self):
        Cat_A=2 ; Cat_B=3 ; Mouse_C=5
        cat_and_mouse_result = cat_and_mouse(Cat_A,Cat_B,Mouse_C)
        self.assertEqual(cat_and_mouse_result, "Cat B", f"Should be {"Cat B"}")
    
    def test_cata_win(self) : 
        Cat_A = 5 ; Cat_B = 2 ;  Mouse_C = 7  
        cat_and_mouse_result = cat_and_mouse(Cat_A,Cat_B,Mouse_C) 
        self.assertEqual(cat_and_mouse_result,"Cat A", f"Should be {"Cat A"}")

    def Test_Cat_a_b_Equal(self) : 
        Cat_A = 5 ; Cat_B = 5 ;  Mouse_C = 7  
        cat_and_mouse_result = cat_and_mouse(Cat_A,Cat_B,Mouse_C) 
        self.assertEqual(cat_and_mouse_result,"Mouse C", f"Should be {"Mouse C"}")
    
    def Test_Negative_Mouse(self): 
        Cat_A = 3 ; Cat_B = 1 ;  Mouse_C = -7  
        cat_and_mouse_result = cat_and_mouse(Cat_A,Cat_B,Mouse_C) 
        self.assertEqual(cat_and_mouse_result,"Cat B", f"Should be {"Cat B"}")