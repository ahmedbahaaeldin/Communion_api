from flask import Flask
from flask_restful import Api, Resource
from utils.helper import *
from flask import request
import os
import json
import logging


app = Flask(__name__)
api = Api(app)

model = load_model('all-mpnet-base-v2')
data = load_json_data('test_dataset.json')

moshka_labels, moshka_desc = data['Moshka_products'], data['Moshka_description']
cosmetics_labels, cosmetics_desc = data['Cosmetics_products'], data['Cosmetics_description']

moshka_emb = prepare_embeddings(model, moshka_desc)
cosmetic_emb = prepare_embeddings(model, cosmetics_desc)

class ProductQuery(Resource):
    def post(self):
        try:
            request_data =  json.loads(request.data)

            query = request_data['query']
            product_type = request_data['product_type']
            threshold = request_data['threshold']

            if product_type == 'Cosmetics':
                results = compute_similarity(model, cosmetic_emb, query)
                labels, desc = cosmetics_labels, cosmetics_desc
                print(results)
            elif product_type == 'Moshka':
                results = compute_similarity(model, moshka_emb, query)
                labels, desc = moshka_labels, moshka_desc
                
            results = filter_scores(results,float(threshold))
            if results:
                location = results[1]
                product_dict = return_product(labels,desc,location)
                post_payload = {'Product':product_dict, 'status':'success'}
            else:
                post_payload = {'Product': 'No specific product found', 'status':'success'}
            return post_payload
        
        except:
            error_payload = {'status':'failed'}
            return error_payload
            


    
api.add_resource(ProductQuery,"/productquery")
if __name__ == '__main__':
    app.run()
