def generate_chart_data(scenario, income, debts, savings):
    # Esta función genera datos ficticios para un gráfico basado en el escenario seleccionado
    data = {
        "x": [],
        "y": []
    }

    if scenario == "casa":
        for year in range(1, 6):
            data["x"].append(year)
            data["y"].append(income - (debts + year * 1000))  # Ejemplo simple de evolución de deudas

    elif scenario == "negocio":
        for year in range(1, 6):
            data["x"].append(year)
            data["y"].append(savings + year * 2000)  # Ejemplo simple de retorno de inversión

    elif scenario == "inversión":
        for year in range(1, 6):
            data["x"].append(year)
            data["y"].append(savings * (1 + 0.1) ** year)  # Ejemplo de interés compuesto

    return data
