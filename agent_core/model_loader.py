from pathlib import Path
from ctransformers import AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

class ModelLoader:
    def __init__(self, config):
        self.config = config
        self.llm = None
        self.embedding_model = None
    
    def load_llm(self):
        model_path = Path(self.config['model']['llm_path']) / self.config['model']['llm_model']
        self.llm = AutoModelForCausalLM.from_pretrained(
            str(model_path),
            model_type="llama",
            max_new_tokens=512,
            temperature=0.7
        )
        return self.llm
    
    def load_embedding(self):
        self.embedding_model = SentenceTransformer(self.config['model']['embedding_model'])
        return self.embedding_model
    
    def generate(self, prompt):
        if not self.llm:
            self.load_llm()
        return self.llm(prompt)
    
    def embed(self, text):
        if not self.embedding_model:
            self.load_embedding()
        return self.embedding_model.encode(text)