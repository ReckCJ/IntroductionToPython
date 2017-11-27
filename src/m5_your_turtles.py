"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cory Reck.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
TurtA = rg.SimpleTurtle('turtle')
TurtA.pen = rg.Pen('red',5)
TurtA.pen_up()
TurtB = rg.SimpleTurtle('turtle')
TurtB.pen = rg.Pen('blue',5)
TurtB.pen_up()
window = rg.TurtleWindow()
window.delay(20)
TurtA.forward(225)
TurtB.backward(250)
circlesize = 25
squaresize= 50
for k in range(5):
    TurtA.pen_down()
    TurtB.pen_down()
    TurtA.draw_circle(circlesize)
    TurtB.draw_square(squaresize)
    TurtA.pen_up()
    TurtB.pen_up()
    TurtA.backward(50)
    TurtB.forward(50)
TurtA.pen_down()
TurtB.pen_down()
TurtA.draw_circle(circlesize)
TurtB.draw_square(squaresize)
TurtA.pen_up()
TurtB.pen_up()
TurtB.forward(25)
TurtA.left(90)
TurtB.left(90)
TurtA.forward(25)
TurtB.forward(25)
TurtA.right(90)
TurtB.left(90)
window.close_on_mouse_click()