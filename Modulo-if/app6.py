ingreso = float(input('Ingrese saldo: '))

if ingreso < 85528:
    
    impuesto = ( ingreso * 0.18 ) - ( 556 )
    
    if impuesto <= -1:
        
        impuesto=0.0
        
else:
    
    impuesto= 14839.2 + (0.32*(ingreso - 85528))
    
impuesto=round(impuesto, 0)
print('El impuesto es:', impuesto, 'pesos')