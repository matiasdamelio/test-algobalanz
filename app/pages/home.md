---
# AlgoBalanz - Technical Review - Python developer 
---
El objetivo de esta prueba es revisar tus habilidades como desarrollador de Python con un reto para evaluar algunos conocimientos fundamentales de Python, APIs y Websockets.

## Requerimientos técnicos
---
Consumir la [API https://test-algobalanz.herokuapp.com/](https://test-algobalanz.herokuapp.com/) en sus diferentes endpoints para realizar las diferentes operaciones. Para realizar peticiones a la misma, no será necesario autenticarte. 

## Detalles de la API

- En [https://test-algobalanz.herokuapp.com/api/v1/prices/security_id](https://test-algobalanz.herokuapp.com/api/v1/prices/security_id) se encuentra el listado de todos los SecurityIDs disponibles en la API. 
- En [https://test-algobalanz.herokuapp.com/api/v1/prices](https://test-algobalanz.herokuapp.com/api/v1/prices) se encuentra el detalle de todos los SecurityIDs disponibles en la API al momento de la consulta.
- En [https://test-algobalanz.herokuapp.com/api/v1/prices/security_id/{security_id}](https://test-algobalanz.herokuapp.com/api/v1/prices/security_id/{security_id}) se encuentra el detalle del SecurityID seleccionado al momento de la consulta (reemplazar {security_id} por alguno de los disponibles en el listado)

## Detalles del Websocket

- Para recibir las actualizaciones de todos los SecurityIDs disponibles en el listado es necesario conectarse a través de [wss://test-algobalanz.herokuapp.com/ws/{cliente}](wss://test-algobalanz.herokuapp.com/ws/{cliente}), reemplazando {cliente} pór un **str**.

## Objetivo
---
Desarrollar una aplicación para crear un cotizador de dólar MEP y dolar Cable. La misma consumirá la API y el Websocket, y deberá mostrar las diferentes cotizaciones de MEP/Cable para distintos instrumentos y plazos. 


La aplicación imprimirá por consola las cotizaciones del dólar MEP y Cable para los siguientes instrumentos y plazos:  

## ¿Cómo calcular el dólar MEP?
---
Es necesario dividir el precio del instrumento en PESOS por el precio del instrumento en DÓLARES.

XXX en ARS / XXX en D
Por ejemplo: AL30-0003-C-CT-ARS / AL30-0003-C-CT-USD (Donde 0003 es T+2 y ARS / USD es la moneda)

## ¿Cómo calcular el dólar CABLE?
---
Es necesario dividir el precio del instrumento en PESOS por el precio del instrumento en CABLE.

XXX en ARS / XXX en C
Por ejemplo: AL30-0003-C-CT-ARS / AL30-0003-C-CT-EXT (Donde 0003 es T+2 y ARS / EXT es la moneda)

## Tabla de SecurityIDs
---
La siguiente tabla está compuesta por el Symbol, el Settlement Type y Currency, obteniendo como resultado el SecurityID correspondiente.

<center>

|Symbol|    Settlement Type   | Currency | SecurityID |
|:------|:---------------:|:------:|------:|
| AL30 | CI | ARS | AL30-0001-C-CT-ARS |
| AL30 | T+1 | ARS | AL30-0002-C-CT-ARS |
| AL30 | T+2 | ARS | AL30-0003-C-CT-ARS |
| AL30 | CI | USD | AL30-0001-C-CT-USD |
| AL30 | T+1 | USD | AL30-0002-C-CT-USD |
| AL30 | T+2 | USD | AL30-0003-C-CT-USD |
| AL30 | CI | EXT | AL30-0001-C-CT-EXT |
| AL30 | T+1 | EXT | AL30-0002-C-CT-EXT |
| AL30 | T+2 | EXT | AL30-0003-C-CT-EXT |
| GD30 | CI | ARS | GD30-0001-C-CT-ARS |
| GD30 | T+1 | ARS | GD30-0002-C-CT-ARS |
| GD30 | T+2 | ARS | GD30-0003-C-CT-ARS |
| GD30 | CI | USD | GD30-0001-C-CT-USD |
| GD30 | T+1 | USD | GD30-0002-C-CT-USD |
| GD30 | T+2 | USD | GD30-0003-C-CT-USD |
| GD30 | CI | EXT | GD30-0001-C-CT-EXT |
| GD30 | T+1 | EXT | GD30-0002-C-CT-EXT |
| GD30 | T+2 | EXT | GD30-0003-C-CT-EXT |

</center>