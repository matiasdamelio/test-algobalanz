---
# AlgoBalanz - Technical Review - Python developer 
---
El objetivo de esta prueba es revisar tus habilidades como desarrollador de Python con un reto para evaluar algunos conocimientos fundamentales de Python, APIs y Websockets.

## Objetivo
---
Desarrollar una aplicación para crear un cotizador de dólar MEP y dolar Cable. La misma consumirá la API y el Websocket, y deberá mostrar las diferentes cotizaciones de MEP/Cable para distintos instrumentos y plazos. 

## Requerimientos técnicos
---
Consumir la [API https://test-algobalanz.herokuapp.com/](https://test-algobalanz.herokuapp.com/) en sus diferentes endpoints para realizar las diferentes operaciones. Para realizar peticiones a la misma, no será necesario autenticarte. 

La aplicación imprimirá por consola las cotizaciones del dólar MEP y Cable para los siguientes instrumentos y plazos:  


---
|Symbol|    Settlement Type   |
|:------:|:---------------:|
| AL29 | CI|
| AL29 | T+1 |
| AL29 | T+2 |
| AL30 | CI|
| AL30 | T+1 |
| AL30 | T+2 |
| GD30 | CI|
| GD30 | T+1 |
| GD30 | T+2 |

---
### ¿Cómo calcular el dólar MEP?
---
Es necesario dividir el precio del instrumento en PESOS con el precio del instrumento en DÓLARES.
```
 XXX en ARS / XXX en D
```


