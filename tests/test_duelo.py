"""MINI DUELO - Parte 2 del laboratorio.

Escribe aquí tus pruebas. El docente las ejecutará contra versiones del código
con defectos escondidos ("mutantes") y contará cuántos logran detectar.

REGLAS
  1. Solo puedes importar de `pytest` y de `pagofacil.comision`.
  2. TODAS tus pruebas deben PASAR con el código correcto (el que cumple
     ESPECIFICACION.md). Si una falla con el código correcto, no puntúas.
  3. Diseña desde la especificación (caja negra): particiones y valores límite.
  4. Evita montos cuyo resultado caiga justo en medio centavo (redondeo ambiguo).
  5. Trabaja SOLO en este archivo durante el duelo.
"""
import pytest

from pagofacil.comision import calcular_comision, calcular_total, validar_monto  # noqa: F401

# --- Tus pruebas empiezan aquí ---

@pytest.mark.parametrize("monto, esperado", [
    # Tramo 1: Hasta Q100 (sin comisión)
    (0.01, 0.00),      # Límite inferior válido
    (50.00, 0.00),     # Caso representativo
    (100.00, 0.00),    # Límite superior Tramo 1 exacto
    
    # Tramo 2: Más de Q100 a Q1,000 (1.5%)
    (100.01, 1.50),    # Límite inferior Tramo 2
    (500.00, 7.50),    # Caso representativo 
    (1000.00, 15.00),  # Límite superior Tramo 2 exacto
    
    # Tramo 3: Más de Q1,000 (1%)
    (1000.01, 10.00),  # Límite inferior Tramo 3
    (2000.00, 20.00),  # Caso representativo sin llegar al tope
    
    # Tope máximo de comisión (Q25.00)
    (2500.00, 25.00),  # Exactamente en el tope
    (3000.00, 25.00),  # Excede el tope pero debe cobrarse 25
])
def test_comision_por_tramos_y_limites(monto, esperado):
    assert calcular_comision(monto) == esperado


@pytest.mark.parametrize("monto, esperado", [
    (100.00, 100.00),    # Total sin comisión
    (1000.00, 1015.00),  # Total con comisión de 1.5%
    (3000.00, 3025.00),  # Total con tope de comisión aplicado
])
def test_calcular_total(monto, esperado):
    assert calcular_total(monto) == esperado


@pytest.mark.parametrize("monto_invalido", [0, -0.01, -100])
def test_numeros_invalidos(monto_invalido):
    with pytest.raises(ValueError):
        calcular_comision(monto_invalido)


@pytest.mark.parametrize("tipo_invalido", [
    "100",        # Texto
    None,         # NoneType
    True,         # Booleano (Atrapa el mutante bonus)
    False,        # Booleano (Atrapa el mutante bonus)
    [100],        # Lista
])
def test_tipos_invalidos(tipo_invalido):
    with pytest.raises(TypeError):
        calcular_comision(tipo_invalido)