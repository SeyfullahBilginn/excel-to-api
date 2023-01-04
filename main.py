from flask import Flask
import pandas as pd

app = Flask(__name__)

df = pd.read_excel(r'./sampledatafoodsales.xlsx', sheet_name= 'FoodSales')


columns = df.columns
df = df.reset_index()
df_dict = df.set_index('index').T.to_dict('list')

@app.route('/')
def excel_to_API():
    return df_dict

@app.route('/<int:Number>')
def allow(Number):
    return df_dict[Number]

@app.route('/<int:Number>/<string:ColumnName>')
def allow2(Number, ColumnName):
    index = list(columns).index(str(ColumnName))
    return str(df_dict[Number][index])

app.run()