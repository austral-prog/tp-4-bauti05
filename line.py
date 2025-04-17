def line():
    import math
    
    txt1=input("Ingrese su coeficiente A:")
    txt2=input("Ingrese su coeficiente B:")
    txt3=input("Ingrese su coeficiente X1:")
    txt4=input("Ingrese su coeficiente X2:")


    A=float(txt1)
    print(f"El coeficiente A de su ecuación de la recta es:{A} ")
    B=float(txt2)
    print(f"El coeficiente B de su ecuación de la recta es:{B} ")
    X1=float(txt3)
    print(f"El coeficiente X1 de su ecuación de la recta es:{X1} ")
    X2=float(txt4)
    print(f"El coeficiente X1 de su ecuación de la recta es:{X2} ")
    

    print("\nPara la siguiente ecuación:")
    print(f"\tY= {A}X + {B}")

    Y1=A*X1+B
    Y2=A*X2+B
    if X1>X2:
        dist=math.sqrt(((Y2-Y1)**2)+(X2-X1)**2)
    else:
        dist=math.sqrt(((Y1-Y2)**2)+(X1-X2)**2)

    print("\nDados los siguientes puntos:")
    print(f"\tP1{X1,Y1}")
    print(f"\tP2{X2,Y2}")
    print(f"\nLa distancia entre ellos es:{dist}") 
