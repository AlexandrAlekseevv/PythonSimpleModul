
import view 
import modul

def button_click():
    value_a = view.get_value()
    operator = modul.get_operator()
    value_b = view.get_value()
    modul.init(value_a, value_b)
    if operator == "+" :
        result = modul.sum()
    elif operator == "*" :
        result = modul.mult()
    else :
        result = 5900
    view.view_data(result)