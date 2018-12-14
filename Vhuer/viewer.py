import array
import math
import turtle

def fsum(x, per, amp, a, b):
    
    list = []
    sum = 0
    
    for d in range(0, len(amp)):
        
        print(str(list) + " + (" + str(float(amp[d])) + " * sin(2 * PI * " + str(float(x)) + ")")
        
        list.append(math.floor(10000000 * (float(amp[d]) *
            math.sin((1 / float(per[d])) * 2 * math.pi * (float(x) - float(a[d]))) + float(b[d]))) / 10000000)
        
    for x in list:
        
        sum += x
        
    return sum

def getInt(que):
    
    ins = input(que)
    
    try:
    
        int(ins)
        
    except ValueError:
        
        print("\nPlease enter an int\n")
        getInt(que)
    
    return ins

def getSumVals():
    
    n = int(getInt("How many terms?: "))

    eval = float(getInt("Evaluate at: "))

    pval = []

    zval = []

    aval = []

    bval = []

    for counter in range(0, n):
    
        p.append(getInt("periodicity of term" + str(counter + 1) + ": "))
    
        z.append(getInt("coefficient of term" + str(counter + 1) + ": "))
    
        aval.append(getInt("a val of term" + str(counter + 1) + ": "))
    
        bval.append(getInt("b val of term" + str(counter + 1) + ": "))
        
    return [eval, pval, zval, aval, bval]

def drawPoint(turt, x, y):

    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    
    turt.goto(x + 1, y)
    turt.goto(x, y + 1)
    turt.goto(x - 1, y)
    turt.goto(x, y - 1)
    turt.goto(x + 1, y)
    
    turt.penup()
    turt.goto(0, 0)

def drawRep(pval, zval, aval, bval):
    
    for l in range(0, len(pval)):
        
        murt.goto(, )
        


wn = turtle.Screen()
wn.bgcolor("black")

turtle.tracer(0, 0)

murt = turtle.Turtle()
murt.color("hotpink")
murt.ht()
murt.pencolor("green")
murt.speed(0)
murt.pensize(1)

print("""
   ╔═════════════════════════════════════════════════════════════╗
   ║                                                             ║
   ║                     C-MANS SUMMING                          ║
   ║                         2018 ©                              ║
   ║                                                             ║
   ╚═════════════════════════════════════════════════════════════╝
""")

vals = getSumVals()











print(fsum(vals[0], vals[1], vals[2], vals[3], vals[4]))

wn.exitonclick()