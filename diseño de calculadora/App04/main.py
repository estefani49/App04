import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.valie.strip())
        num2=float(txtNum2.value.lstrip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Erroro ingresa valores correctos"

def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.valie.strip())
        num2=float(txtNum2.value.lstrip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Erroro ingresa valores correctos"

def calc_mult(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.valie.strip())
        num2=float(txtNum2.value.lstrip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Erroro ingresa valores correctos"

def calc_div(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.valie.strip())
        num2=float(txtNum2.value.lstrip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Erroro ingresa valores correctos"

def main(page: ft.page):
    page.title="calculadora"
    page.bgcolor="#0CCB72"
    
    txtNum1=ft.TextField(label="ingresa el primer numero", color= "blue")
    txtNum2=ft.TextField(label="ingresa el segundo numero",color="blue")
    lblResultado=ft.TextField("Resultado: ", color="blue")

#funciones de manejo de eventos
    def on_calc_suma(e):
        calc_suma(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_resta(e):
        calc_suma(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_mult(e):
        calc_suma(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_div(e):
        calc_suma(txtNum1, txtNum2, lblResultado)
        page.update()

    def limpiar(e):
        txtNum1.value = ""
        txtNum2.value = ""
        lblResultado.value = "Resultado: "
        page.update()

#se crean los botones de la aplicacion
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMult=ft.ElevatedButton(text="*",on_click=on_calc_mult)
    btnDiv=ft.ElevatedButton(text="/",on_click=on_calc_div)
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnLimpiar=ft.ElevatedButton(text="Borrar",on_click=limpiar)

#agregar los elemtos a pages
    page.add(
        ft.Column(controls=[
            
        ])
    )

















ft.app(main)
