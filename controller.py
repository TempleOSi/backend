# Final Project: Web Application
# Authors:
#          A01746664 Eduardo Joel Cortez Valente
'''
This file consists of the definition of the Controller class wich is in charge of handling the requests and responses of the API.
'''

from flask import Flask, request, jsonify
from models import general
from flask_cors import CORS
from joblib import load
import numpy as np
from factory import data_cleaning
import pandas as pd

class Controller():

    def __init__(self):
        self.app = Flask(__name__)
        self.general = general.General()
        CORS(self.app, resources={r"/*": {"origins": "*"}})
        
        # Routes
        self.app.route('/test')(self.test)
        self.app.route('/getAllGeneral', methods=['GET'])(self.getAllGeneral)
        self.app.route('/addGeneral', methods=['POST'])(self.addGeneral)
        self.app.route('/getOneGeneral/<id>', methods=['GET'])(self.getOneGeneral)
        self.app.route('/updateGeneral/<id>', methods=['PUT'])(self.updateGeneral)
        self.app.route('/deleteGeneral/<id>', methods=['DELETE'])(self.deleteGeneral)
        self.app.route('/ml_model', methods=['POST'])(self.ml_model)

    def test(self):
        print("Hello World!")
        return "Hello World!"
    
    def getAllGeneral(self):
        return jsonify(self.general.find({})), 200
    
    def getOneGeneral(self, id):
        return jsonify(self.general.find_by_id(id)), 200
    
    def addGeneral(self):
        if request.method == "POST":
            title = request.get_json()['title']
            body = request.get_json()['body']
            response = self.general.create({'title': title, 'body': body})
            return response, 201
    
    def updateGeneral(self, id):
        if request.method == "PUT":
            title = request.get_json()['title']
            body = request.get_json()['body']
            response = self.general.update(id, {'title': title, 'body': body})
            return response, 201
        
    def deleteGeneral(self, id):
        if request.method == "DELETE":
            response = self.general.delete(id)
            return response, 201
        
    def ml_model(self):
        if request.method == "POST":
            contenido_sucio = request.form
            
            input_df = pd.DataFrame([contenido_sucio])
            
            contenido = data_cleaning.clean_data(input_df)
            
            datosEntrada = np.array([
                # MSSubClass - Tipo de construcción de la vivienda numerico, corresponde a un tipo
                20,
                # MSZoning - Zonificación del vecindario (Residential Low Density) se representa con A, C, FV, I, RH, RL, RP, RM
                contenido['MSZoning'],
                # LotFrontage - Pies de calle conectados a la propiedad
                contenido['LotFrontage'],
                # LotArea - Tamaño del lote en pies cuadrados
                contenido['LotArea'],
                # Street - Tipo de acceso a la propiedad (Pavimentado) Gravel o Paved
                181130.5385,
                # LotShape - Forma del lote (Regular) IR1 2 o 3
                contenido['LotShape'],
                # LandContour - Contorno de la propiedad (Nivel llanura) Lvl Bnk HLS Low
                180183.7468,
                # Utilities - Servicios públicos disponibles AllPub NoSewr NoSeWa ELO     
                180950.9568,
                # LotConfig - Configuración del lote (Dentro) Inside Corner CulDSac FR2 FR3
                contenido['LotConfig'],
                # LandSlope - Pendiente del terreno (No especificada) Gtl Mod Sev
                179956.7996,
                # Neighborhood - Vecindario (No especificado) Nombre del vecindario
                contenido['Neighborhood'],
                # Condition1 - Condición de proximidad a varias características (No especificada) cerca de calle principal, locacion importante, etc
                142475.4815,
                # Condition2 - Condición de proximidad a varias características (No especificada) si hay más de 1
                181169.4055,
                # BldgType - Tipo de vivienda (No especificado)  Duplex, Townhouse end
                185763.8074,
                # HouseStyle - Estilo de la vivienda (No especificado) Un piso, 2, segundo no terminado, etc.
                contenido['HouseStyle'],
                # OverallQual - Calidad y acabado general de la casa (No especificada) entre 1-10
                5,
                # OverallCond - Condición general de la casa (No especificada) entre 1-10
                6,
                # YearBuilt - Año de construcción original de la casa
                contenido['YearBuilt'],
                # RoofStyle - Estilo del techo (Hip) Flat, Gable, etc.
                171483.9562,
                # RoofMatl - Material del techo (No especificado) Metal, Roll, etc.
                179803.6792,
                # Exterior1st - Material exterior de la casa (Metal Siding) CBlock, HdBoard, etc.
                contenido['Exterior1st'],
                # Exterior2nd - Material exterior de la casa (No especificado) si hay mas de uno
                214432.4603,
                # MasVnrType - Tipo de revestimiento de mampostería (Brick Face) BrkCmn, Brkace, etc.
                156958.2431,
                # MasVnrArea - Área de revestimiento de mampostería en pies cuadrados
                0,
                # ExterQual - Calidad del material exterior Ex, Gd, TA, Fa, Po
                3,
                # ExterCond - Condición del material exterior (No especificada) Ex, Gd, TA, Fa, Po
                184034.8963,
                # Foundation - Tipo de cimiento BrkTil, CBlock, PConc, etc
                149805.7145,
                # BsmtQual - Calificación del sótano (No especificada) Ex, Gd, TA, Fa, Po   empieza en 100+ pulgadas baja de calidad cada 10
                3,
                # BsmtCond - Condición del sótano (No especificada) Ex, Gd, TA, Fa, Po
                181492.2277,
                # BsmtExposure - Exposición del sótano (No especificada) Ex, Gd, TA, Fa, Po
                contenido['BsmtExposure'],
                # BsmtFinType1 - Rating de acabado del sótano (No especificado) GLQ, ALQ, BLQ, Rec, LwQ, Unf, NA
                146889.2481,
                # BsmtFinSF1 - Área de acabado del sótano tipo 1 en pies cuadrados
                468,
                # BsmtFinType2 - Tipo de acabado del sótano si hay otro GLQ, ALQ, BLQ, Rec, LwQ, Unf, NA
                164364.1304,
                # BsmtFinSF2 - Área de acabado del sótano tipo 2 en pies cuadrados
                144,
                # BsmtUnfSF - Área sin terminar del sótano en pies cuadrados
                270,
                # TotalBsmtSF - Área total del sótano en pies cuadrados
                882,
                # Heating - Tipo de sistema de calefacción  Floor, GasA, GasW, Grav, OthW, Wall
                182021.1954,
                # HeatingQC - Calidad y condición del sistema de calefacción  Ex, Gd, TA, Fa, Po
                contenido['HeatingQC'],
                # CentralAir - Aire acondicionado central  N o Y
                186186.7099,
                # Electrical - Sistema eléctrico SBrkr, FuseA, FuseF, FuseP, Mix
                186810.6375,
                # 1stFlrSF - Pies cuadrados del primer piso
                896,
                # 2ndFlrSF - Pies cuadrados del segundo piso
                0,
                # LowQualFinSF - Área de acabado de baja calidad en pies cuadrados
                0,
                # GrLivArea - Área habitable sobre el nivel del suelo en pies cuadrados
                896,
                # BsmtFullBath - Número de baños completos en el sótano
                0,
                # BsmtHalfBath - Número de medios baños en el sótano
                0,
                # FullBath - Número de baños completos sobre el nivel del suelo
                contenido['FullBath'],
                # HalfBath - Número de medios baños sobre el nivel del suelo
                0,
                # BedroomAbvGr - Número de dormitorios sobre el nivel del suelo
                2,
                # KitchenAbvGr - Número de cocinas sobre el nivel del suelo
                1,
                # KitchenQual - Calidad de la cocina Ex, Gd, TA, Fa, Po
                3,
                # TotRmsAbvGrd - Total de habitaciones sobre el nivel del suelo
                5,
                # Functional - Funcionalidad de la vivienda Typ, Min1, Min2, Mod, Maj1, Maj2, Sev, Sal
                183429.1471,
                # Fireplaces - Número de chimeneas
                0,
                # GarageType - Tipo de garaje 2Types, Attchd, Basment, BuiltIn, CarPort, Detchd, NA
                contenido['GarageType'],
                # GarageYrBlt - Año de construcción del garaje
                1961,
                # GarageFinish - Acabado del garaje Fin, RFn, Unf, NA
                137570.4606,
                # GarageCars - Capacidad del garaje en términos de capacidad de automóviles
                1,
                # GarageArea - Tamaño del garaje en pies cuadrados
                730,
                # GarageQual - Calidad del garaje Ex, Gd, TA, Fa, Po
                182591.8642,
                # GarageCond - Condición del garaje Ex, Gd, TA, Fa, Po
                183017.1891,
                # PavedDrive - Acceso pavimentado al garaje Y, P, N
                186433.9739,
                # WoodDeckSF - Área de plataforma de madera en pies cuadrados
                contenido['WoodDeckSF'],
                # OpenPorchSF - Área de porche abierto en pies cuadrados
                contenido['OpenPorchSF'],
                # EnclosedPorch - Área de porche cerrado en pies cuadrados
                0,
                # 3SsnPorch - Área de porche de tres estaciones en pies cuadrados
                896,
                # ScreenPorch - Área de porche con pantalla en pies cuadrados
                0,
                # PoolArea - Área de piscina en pies cuadrados
                0,
                # MiscVal - Valor misceláneo de la propiedad dolares
                12500,
                # remodel - Indica si se realizó una remodelación bool
                0])
            
            datos_lista = datosEntrada.tolist()
            
            dt = load('model.joblib')
            
            # Utilizar el modelo
            resultado = dt.predict(datosEntrada.reshape(1, -1))
            return jsonify({'resultado': str(round(resultado[0],2))}), 200
    
    def run(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)