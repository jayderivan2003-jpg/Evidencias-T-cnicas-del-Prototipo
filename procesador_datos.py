import pandas as pd

df = pd.read_excel('alertas_simuladas.xlsx.xlsx')

df['Impacto_Tecnico'] = df['Impacto_Tecnico'].fillna(1)

def clasificar_prioridad(impacto):
    if impacto >= 4:
        return 'Alta'
    elif impacto >= 2.5:
        return 'Media'
    else:
        return 'Baja'

df['Prioridad_Automatica'] = df['Impacto_Tecnico'].apply(clasificar_prioridad)

df.to_excel('alertas_final.xlsx', index=False)
print("¡Procesamiento completado! Archivo 'alertas_final.xlsx' generado.")