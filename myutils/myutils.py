def clean(string, lower=True, replace_comma=True, strip=True):
    """
    Limpia el string recibido:
    - Convierte a minúsculas si lower=True.
    - Reemplaza comas por puntos si replace_comma=True.
    - Elimina espacios al inicio y fin si strip=True.
    """
    if lower:
        string=string.lower()
    if replace_comma:
        string=string.replace(",",".")
    if strip:
        string=string.strip()
    return string
