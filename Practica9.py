from    scipy             import *
from    numpy             import *
from    math              import *
from    cmath             import *
from    sympy             import *
import  matplotlib.pyplot as     graf

def Runge(X0, Y0, T, h, yEvaluada, func1, func2):

    new_X = arange(0,yEvaluada,h)
    new_Y = arange(0,yEvaluada,h)
    # Se inicializan los coeficientes como floats
    k1_1 = 0.0
    k2_1 = 0.0
    k3_1 = 0.0
    k4_1 = 0.0
    k1_2 = 0.0
    k2_2 = 0.0
    k3_2 = 0.0
    k4_2 = 0.0
    i = 0
    while :
        
        #Se consiguen los coeficientes de K1 de ambas ecuaciones
        k1_1 = h * func1.subs([(t, T), (x, X0), (y, Y0)])
        k1_2 = h * func2.subs([(t, T), (x, X0), (y, Y0])
         #Se consiguen los coeficientes de K2 de ambas ecuaciones
        k2_1 = h * func1.subs([(t, T+h/2), (x, X0+k1_1/2), (y, Y0+k1_2/2)])
        k2_2 = h * func2.subs([(t, T+h/2), (x, X0+k1_1/2), (y, Y0+k1_2/2)])
         #Se consiguen los coeficientes de K3 de ambas ecuaciones
        k3_1 = h * func1.subs([(t, T+h/2), (x, X0+k2_1/2), (y, Y0+k2_2/2)])
        k3_2 = h * func2.subs([(t, T+h/2), (x, X0+k2_1/2), (y, Y0+k2_2/2)])
        #Se consiguen los coeficientes de K4 de ambas ecuaciones
        k4_1 = h * func1.subs([(t, T+h), (x, X0+k3_1), (y, Y0+k3_2)])
        k4_2 = h * func2.subs([(t, T+h), (x, X0+k3_1), (y, Y0+k3_2)])

        # Se obtienen las y_n+1
        new_X = y_n[it]+(k1_1+2*k2_1+2*k3_1+k4_1)/6;
        new_Y = z_n[it]+(k1_2+2*k2_2+2*k3_2+k4_2)/6;

        it += 1;

    return [x_n, y_n, z_n];


E0 = 1.0
L = 1.0
C = 0.25
w = sqrt(3.5)
R = 0

t = Symbol('t') 
x = Symbol('x') #q
y = Symbol('y') #i

func1 = y
func2 = -R*y/L  -x/(C*L) + sin(w*t)

res = Runge(0, 0, 0, 0.1, 10, func1, func2);

fig = graf.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Gráfica Resultado')
ax.set_xlabel('t')
ax.set_ylabel('q')
graf.plot(res[0], res[1])
graf.show()

