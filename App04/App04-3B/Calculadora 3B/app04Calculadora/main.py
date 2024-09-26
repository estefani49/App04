import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_multi(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_divi(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
    except ZeroDivisionError:
        lblResultado.value="Error división por cero" 
def on_calc_suma(e):
    calc_suma(txtNum1,txtNum2,lblResultado)
    page.update()
def on_calc_resta(e):
    calc_resta(txtNum1,txtNum2,lblResultado)
    page.update()
def on_calc_multi(e):
    calc_multi(txtNum1,txtNum2,lblResultado)
    page.update()
def on_calc_divi(e):
    calc_divi(txtNum1,txtNum2,lblResultado)
    page.update()
def limpiar(e):
    txtNum1= ""
    txtNum2= ""
    lblResultado.vaule="Resultado: "
    pager.update()

def main(page: ft.Page):
    global txtNum1,txtNum2,lblResultado

    page.title = "Calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="Ingresa el primer número",color="purple")
    txtNum2=ft.TextField(label="Ingresa el segundo número",color="purple")
    lblResultado=ft.Text("Resultado: ",color="purple")
    
    btnsuma= ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnresta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnmulti=ft.ElevatedButton(text="*",on_click=on_calc_multi)
    btndivi=ft.ElevatedButton(text="/",on_click=on_calc_divi)
    btnlimpiar=ft.ElevatedButton(text="borrar",on_click=limpiar)

    
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],alignment="center"),
             ft.Row(controls=[lblResultado],alignment="center"),
             ft.Row(controls=[
                 btnsuma,
                 btnresta,
                 btnmulti,
                 btndivi,
                 btnlimpiar
             ], alignment="center")
        ]),

    )
    


ft.app(main)
