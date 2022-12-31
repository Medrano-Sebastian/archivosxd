"""
En una empresa trabajan n empleados cuyos sueldos oscilan entre S/.1500 y S/.3000, realizar un programa que lea
los sueldos que cobra cada empleado e informe cuántos empleados cobran entre S/.1500 y S/.2000 y cuántos cobran más
 de S/2000.2000. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.
"""

num_empleados= int(input("\033[92mCantidad de empleados:\033[0m "))
q=[]
z=[]
count=0
sum_total=0
while num_empleados<=0:
    print("\033[91mIngrese un valor correcto\033[0m")
    num_empleados= int(input("Cantidad de empleados: "))
while count<num_empleados:
    a=float(input("Cuanto cobra el empleado: "))
    while a<1500 or a>3000:
        print("\033[93mLos sueldos deben oscilar entre s/1500 y s/3000\033[0m")
        a=float(input("Cuanto cobra el empleado: "))
    count+=1
    if 1500<=a<=2000:
        q.append(a)        
    else:
        z.append(a)
print(len(q)," empleados cobran entre s/1500 y s/2000",f"y {len(z)} cobran mas de s/2000.")
print(f"En total la empresa gasta en sueldos: s/{sum(q)+sum(z)}")
