from pathlib import Path
import pandas as pd


def limpar_texto(df: pd.DataFrame) -> pd.DataFrame:
    colunas_texto = df.select_dtypes(include=["object", "string"]).columns
    df[colunas_texto] = df[colunas_texto].apply(
        lambda x: x.astype(str).str.upper().str.strip()
    )
    return df


def converter_numero_brasileiro(serie: pd.Series) -> pd.Series:
    serie = (
        serie.astype(str)
        .str.strip()
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
    )
    return pd.to_numeric(serie, errors="coerce")


def main():

    ---
    
    # =========================
    # DEFINIR PASTAS DO PROJETO
    # =========================
    
    pasta_projeto = Path(__file__).resolve().parent
    pasta_dados_brutos = pasta_projeto / "dados_brutos"
    pasta_dados_tratados = pasta_projeto / "dados_tratados"

    pasta_dados_tratados.mkdir(exist_ok=True)

    print("Pasta do projeto:", pasta_projeto)
    print("Pasta de dados brutos:", pasta_dados_brutos)
    print("Pasta de dados tratados:", pasta_dados_tratados)


---
    
    # =========================
    # LER ARQUIVOS BRUTOS
    # =========================
    print("\nLendo arquivos brutos...")

    df_transporte = pd.read_csv(
        pasta_dados_brutos / "Transporte de Produtos Químicos Perigosos ou Combustíveis.csv",
        sep=";"
    )

    df_gerador = pd.read_csv(
        pasta_dados_brutos / "Resíduos Sólidos – Gerador (A partir de 2012).csv",
        sep=";"
    )

    df_destinador = pd.read_csv(
        pasta_dados_brutos / "Resíduos Sólidos – Destinador.csv",
        sep=";"
    )

    df_transportador = pd.read_csv(
        pasta_dados_brutos / "Resíduos Sólidos – Transportador.csv",
        sep=";"
    )

---
    
    # =========================
    # TRATAMENTO TRANSPORTE
    # =========================
    print("\nTratando base de transporte...")

    df_transporte.columns = df_transporte.columns.str.strip()
    df_transporte = df_transporte.drop_duplicates()
    df_transporte = df_transporte.dropna(how="all")
    df_transporte = limpar_texto(df_transporte)

    df_transporte["Quantidade Transportada"] = converter_numero_brasileiro(
        df_transporte["Quantidade Transportada"]
    )

    df_transporte["Ano"] = pd.to_numeric(df_transporte["Ano"], errors="coerce")
    df_transporte["Produto"] = df_transporte["Produto"].replace("NAN", pd.NA)
    df_transporte["Produto"] = df_transporte["Produto"].fillna("NÃO INFORMADO")
    df_transporte = df_transporte[df_transporte["Situação Cadastral"] == "ATIVA"]
    df_transporte["ROTA"] = df_transporte["UF - origem"] + " → " + df_transporte["UF - destino"]
    df_transporte["TIPO_BASE"] = "TRANSPORTE"


---
    
    # =========================
    # TRATAMENTO GERADOR
    # =========================
    print("Tratando base de gerador...")

    df_gerador.columns = df_gerador.columns.str.strip()
    df_gerador = df_gerador.drop_duplicates()
    df_gerador = df_gerador.dropna(how="all")
    df_gerador = limpar_texto(df_gerador)

    df_gerador["Quantidade Gerada"] = converter_numero_brasileiro(
        df_gerador["Quantidade Gerada"]
    )

    df_gerador["Ano da geração"] = pd.to_numeric(df_gerador["Ano da geração"], errors="coerce")
    df_gerador = df_gerador[df_gerador["Situação Cadastral"] == "ATIVA"]
    df_gerador = df_gerador.dropna(subset=["Estado", "Município", "Quantidade Gerada"])
    df_gerador["TIPO_BASE"] = "GERADOR"


---
    
    # =========================
    # TRATAMENTO DESTINADOR
    # =========================
    print("Tratando base de destinador...")

    df_destinador.columns = df_destinador.columns.str.strip()
    df_destinador = df_destinador.drop_duplicates()
    df_destinador = df_destinador.dropna(how="all")
    df_destinador = limpar_texto(df_destinador)

    df_destinador["Quant. destinada"] = converter_numero_brasileiro(
        df_destinador["Quant. destinada"]
    )

    df_destinador["Ano - destinação"] = pd.to_numeric(
        df_destinador["Ano - destinação"], errors="coerce"
    )

    df_destinador = df_destinador[df_destinador["Situação Cadastral"] == "ATIVA"]
    df_destinador = df_destinador.dropna(subset=["Quant. destinada"])
    df_destinador["TIPO_BASE"] = "DESTINADOR"


---
    
    # =========================
    # TRATAMENTO TRANSPORTADOR
    # =========================
    print("Tratando base de transportador...")

    df_transportador.columns = df_transportador.columns.str.strip()
    df_transportador = df_transportador.drop_duplicates()
    df_transportador = df_transportador.dropna(how="all")
    df_transportador = limpar_texto(df_transportador)

    df_transportador["Ano"] = pd.to_numeric(df_transportador["Ano"], errors="coerce")
    df_transportador = df_transportador[df_transportador["Situação Cadastral"] == "ATIVA"]
    df_transportador["TIPO_BASE"] = "TRANSPORTADOR"


---
    
    # =========================
    # SALVAR BASES TRATADAS
    # =========================
    print("Salvando bases tratadas...")

    df_transporte.to_csv(pasta_dados_tratados / "transporte_tratado.csv", index=False, sep=";")
    df_gerador.to_csv(pasta_dados_tratados / "gerador_tratado.csv", index=False, sep=";")
    df_destinador.to_csv(pasta_dados_tratados / "destinador_tratado.csv", index=False, sep=";")
    df_transportador.to_csv(pasta_dados_tratados / "transportador_tratado.csv", index=False, sep=";")

---
    
    # =========================
    # PADRONIZAR PARA BASE ÚNICA
    # =========================
    print("Montando base analítica unificada...")

    base_transporte = pd.DataFrame({
        "TIPO_BASE": "TRANSPORTE",
        "ANO": df_transporte["Ano"],
        "ESTADO": df_transporte["Estado"],
        "MUNICIPIO": df_transporte["Município"],
        "CNPJ_PRINCIPAL": df_transporte["CNPJ"],
        "RAZAO_SOCIAL_PRINCIPAL": df_transporte["Razão Social"],
        "CNPJ_ORIGEM": pd.NA,
        "RAZAO_SOCIAL_ORIGEM": pd.NA,
        "CNPJ_DESTINO": pd.NA,
        "RAZAO_SOCIAL_DESTINO": pd.NA,
        "PRODUTO_OU_RESIDUO": df_transporte["Produto"],
        "QUANTIDADE": df_transporte["Quantidade Transportada"],
        "UNIDADE": df_transporte["Unidade de Medida"],
        "TIPO_TRANSPORTE": df_transporte["Tipo de Transporte"],
        "TIPO_DESTINACAO": pd.NA,
        "CLASSIFICACAO": pd.NA,
        "ROTA": df_transporte["ROTA"],
        "SITUACAO_CADASTRAL": df_transporte["Situação Cadastral"]
    })

    base_gerador = pd.DataFrame({
        "TIPO_BASE": "GERADOR",
        "ANO": df_gerador["Ano da geração"],
        "ESTADO": df_gerador["Estado"],
        "MUNICIPIO": df_gerador["Município"],
        "CNPJ_PRINCIPAL": df_gerador["CNPJ do gerador"],
        "RAZAO_SOCIAL_PRINCIPAL": df_gerador["Razão Social do gerador"],
        "CNPJ_ORIGEM": df_gerador["CNPJ do gerador"],
        "RAZAO_SOCIAL_ORIGEM": df_gerador["Razão Social do gerador"],
        "CNPJ_DESTINO": pd.NA,
        "RAZAO_SOCIAL_DESTINO": pd.NA,
        "PRODUTO_OU_RESIDUO": df_gerador["Tipo de Resíduo"],
        "QUANTIDADE": df_gerador["Quantidade Gerada"],
        "UNIDADE": df_gerador["Unidade"],
        "TIPO_TRANSPORTE": pd.NA,
        "TIPO_DESTINACAO": pd.NA,
        "CLASSIFICACAO": df_gerador["Classificação Resíduo"],
        "ROTA": pd.NA,
        "SITUACAO_CADASTRAL": df_gerador["Situação Cadastral"]
    })

    base_destinador = pd.DataFrame({
        "TIPO_BASE": "DESTINADOR",
        "ANO": df_destinador["Ano - destinação"],
        "ESTADO": df_destinador["Estado"],
        "MUNICIPIO": df_destinador["Município"],
        "CNPJ_PRINCIPAL": df_destinador["CNPJ do destinador"],
        "RAZAO_SOCIAL_PRINCIPAL": df_destinador["Razão Social do destinador"],
        "CNPJ_ORIGEM": df_destinador["CNPJ do gerador do resíduo"],
        "RAZAO_SOCIAL_ORIGEM": df_destinador["Raz soc do gerador do resíduo"],
        "CNPJ_DESTINO": df_destinador["CNPJ do destinador"],
        "RAZAO_SOCIAL_DESTINO": df_destinador["Razão Social do destinador"],
        "PRODUTO_OU_RESIDUO": df_destinador["Desc. Resíduo"],
        "QUANTIDADE": df_destinador["Quant. destinada"],
        "UNIDADE": df_destinador["Unidade"],
        "TIPO_TRANSPORTE": pd.NA,
        "TIPO_DESTINACAO": df_destinador["Tipo de destinação"],
        "CLASSIFICACAO": pd.NA,
        "ROTA": pd.NA,
        "SITUACAO_CADASTRAL": df_destinador["Situação Cadastral"]
    })

    base_transportador = pd.DataFrame({
        "TIPO_BASE": "TRANSPORTADOR",
        "ANO": df_transportador["Ano"],
        "ESTADO": df_transportador["Estado"],
        "MUNICIPIO": df_transportador["Município"],
        "CNPJ_PRINCIPAL": df_transportador["CNPJ do transportador"],
        "RAZAO_SOCIAL_PRINCIPAL": df_transportador["Razão Social do transportador"],
        "CNPJ_ORIGEM": df_transportador["CNPJ da origem"],
        "RAZAO_SOCIAL_ORIGEM": df_transportador["Razão social da origem"],
        "CNPJ_DESTINO": pd.NA,
        "RAZAO_SOCIAL_DESTINO": pd.NA,
        "PRODUTO_OU_RESIDUO": pd.NA,
        "QUANTIDADE": pd.NA,
        "UNIDADE": pd.NA,
        "TIPO_TRANSPORTE": pd.NA,
        "TIPO_DESTINACAO": pd.NA,
        "CLASSIFICACAO": pd.NA,
        "ROTA": pd.NA,
        "SITUACAO_CADASTRAL": df_transportador["Situação Cadastral"]
    })

---
    
    # =========================
    # UNIFICAR
    # =========================
    base_unificada = pd.concat(
        [base_transporte, base_gerador, base_destinador, base_transportador],
        ignore_index=True,
        sort=False
    )

    colunas_texto = base_unificada.select_dtypes(include=["object", "string"]).columns
    base_unificada[colunas_texto] = base_unificada[colunas_texto].fillna("NÃO INFORMADO")

---
    
    # =========================
    # SALVAR BASE FINAL
    # =========================
    print("Salvando base final...")

    base_unificada.to_csv(
        pasta_dados_tratados / "base_unificada_analitica.csv",
        index=False,
        sep=";"
    )

---
    
    # =========================
    # CONFERÊNCIA FINAL
    # =========================
    print("\nResumo das bases tratadas:")
    print("Transporte:", df_transporte.shape)
    print("Gerador:", df_gerador.shape)
    print("Destinador:", df_destinador.shape)
    print("Transportador:", df_transportador.shape)

    print("\nResumo da base unificada:")
    print(base_unificada.info())
    print(base_unificada.shape)

    print("\nValores nulos na base unificada:")
    print(base_unificada.isnull().sum())


if __name__ == "__main__":
    main()
