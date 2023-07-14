







dividendos_b = round(herencia * (1 + 0.25) ** 10, 3)
print("Dividendos del Plazo Fijo después de 5 años:", dividendos_pf)
print("Dividendos de los Bonos después de 5 años:", dividendos_b)
mejorinversion = (dividendos_pf > dividendos_b) * "Plazo Fijo" + (dividendos_pf < dividendos_b) * "Bonos y Acciones" + (dividendos_pf == dividendos_b) * "Ambas inversiones generan los mismos dividendos"
print("La mejor inversión es:", mejorinversion)
