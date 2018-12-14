import array
import math
import turtle

# series = [eval, [pval, hval, aval, bval],..., [pval, hval, aval, bval]]
#           eval           term_1                        term_2
#
# 0: eval = float(getInt("Evaluate at: "))
# 
# 1: term_1 = [pval, hval, aval, bval]
#
#        term_1[0] = pval
# 
#        term_1[0] = bval
#         
#        term_1[0] = aval
#         
#        term_1[0] = bval
#
# 2: term_2 = [pval, hval, aval, bval]
#
# n: ...

def fsum(oseries):
    
    sum = 0
    
    for counter in range(1, len(oseries)):
        
        print("sum " + str(counter) + ": " + str(sum) + " + (" + str(oseries[counter][2]) + "sin((1 / " + str(oseries[counter][1]) + ") * 2π(" +
              str(oseries[counter][0]) + " - " + str(oseries[counter][3]) + ")) + " + str(oseries[counter][4]))
        
        sum += math.floor(10000000 * (term[1] * math.sin((1 / term[0]) * 2 * math.pi * (eval - term[2])) + term[3])) / 10000000
        
    return sum

def getInt(prompt):
    
    ins = input(prompt)
    
    try:
    
        ins = int(ins)
        
        return ins
        
    except ValueError:
        
        print("\nPlease enter an int\n")
        
        return getInt(prompt)

def getFloat(prompt):
    
    ins = input(prompt)
    
    try:
    
        ins = float(ins)
        
        return ins
        
    except ValueError:
        
        print("\nPlease enter a float\n")
        
        return getFloat(prompt)

def sin_1():
    
    print("")

def getSeries():
    
    n = getInt("How many terms?: ")

    oseries = [getFloat("Evaluate at: ")]

    for term in range(1, n + 1):
    
        attach = [
            getFloat("periodicity of term_" + str(term) + " = "),
            getFloat("coefficient of term_" + str(term) + " = "),
            getFloat("a val of term_" + str(term) + " = "),
            getFloat("b val of term_" + str(term) + " = ")
            ]
        
        oseries.append(attach)
    
    print("len of oseries: " + str(len(oseries)))
    
    return oseries

# def drawPoint(turt, x, y):
# 
#     turt.penup()
#     turt.goto(x, y)
#     turt.pendown()
#     
#     turt.goto(x + 1, y)
#     turt.goto(x, y + 1)
#     turt.goto(x - 1, y)
#     turt.goto(x, y - 1)
#     turt.goto(x + 1, y)
#     
#     turt.penup()
#     turt.goto(0, 0)
# 
# def drawRep(pval, zval, aval, bval):
#     
#     for l in range(0, len(pval)):
#         
#         murt.goto(, )
#         
# 
# 
# wn = turtle.Screen()
# wn.bgcolor("black")
# 
# turtle.tracer(0, 0)
# 
# murt = turtle.Turtle()
# murt.color("hotpink")
# murt.ht()
# murt.pencolor("green")
# murt.speed(0)
# murt.pensize(1)

print("""
  ╔═════════════════════════════════════════════════════════════╗
  ║                                                             ║
  ║                     C-MANS SUMMING                          ║
  ║                         2018 ©                              ║
  ║                                                             ║
  ╚═════════════════════════════════════════════════════════════╝
""")

series = getSeries()

print("series after get(normal)" + str(series))

for b in range(0, 3):

    print("series before set(normal)" + str(series))

    series[0] = b
    
    print("series after set(notice)" + str(series))
    
    print(fsum(series))

# wn.exitonclick()