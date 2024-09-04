import pandas as pd

colunas = ['NU_ANO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESCOLA', 
            'TP_COR_RACA', 'TP_DEPENDENCIA_ADM_ESC', 'SG_UF_ESC', 
            'SG_UF_PROVA', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 
            'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'Q003', 'Q017']

enem_2013_df = pd.read_csv("C:/Users/nicol/Downloads/microdados_enem_2013/DADOS/MICRODADOS_ENEM_2013.csv", sep=';', encoding='latin1', usecols=colunas)

print(enem_2013_df.head())


