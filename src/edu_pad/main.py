
from dataweb import DataWeb
import pandas as pd



def main():
    dataweb = DataWeb()
    df = dataweb.obtener_datos()
    df = dataweb.convertir_numericos(df)
    df.to_csv("data_web.csv", index=False)



if __name__ == "__main__":
    main()
