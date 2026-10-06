# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
[Versionado Semántico](https://semver.org/lang/es/).

## [Sin publicar]

## [1.0.1] - 2026-10-05
### Corregido
- Inclusión exacta del límite de Q100 en el tramo 1 de comisiones.
- Aplicación del tope máximo de Q25.00 para comisiones altas.
- Operación aritmética corregida para sumar la comisión al calcular el total.

## [1.0.0]
### Agregado
- Cálculo de la comisión de transferencias (`calcular_comision`).
- Cálculo del total a debitar (`calcular_total`).
- Validación del monto (`validar_monto`).