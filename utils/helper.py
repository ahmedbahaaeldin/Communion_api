import json
from typing import Dict,List,TypeVar
from sentence_transformers import SentenceTransformer,util

Torch_Model = TypeVar('Torch_Model')
Torch_Embeddings = TypeVar('Torch_Embeddings')

def load_model(model_name: str):
    model = SentenceTransformer(model_name)
    return model

def load_json_data(dataset_path: str) -> Dict[str,List]:
    with open(dataset_path,'r') as object:
        data = json.load(object)
    return data



def prepare_embeddings(model: Torch_Model, 
                       dataset: List[str]) -> Torch_Embeddings:
    dataset_embeddings = model.encode(dataset)
    return dataset_embeddings

def compute_similarity(model: Torch_Model, 
                       dataset_embeddings: Torch_Embeddings, 
                       query: str) -> List[float]:
    
    query_embeddings = model.encode(query)
    results = util.pytorch_cos_sim(query_embeddings,dataset_embeddings)
    return results

def filter_scores(results: List[float], threshold: float) -> [float, int]:
    score = torch.max(results).item()
    if score < threshold:
        return None
    else:
        location = torch.argmax(results).item()
        return score, location 
    
def return_product(Product_labels: List[str], 
                   Product_Description: List[str], 
                   location: int) -> Dict[str,str]:
    
    candidate_label = Product_labels[location]
    candidate_description = Product_Description[location]
    candidate_dict = {candidate_label: candidate_description}
    
    return candidate_dict
    
