# Classe de output para manipulação de tabelas

class ModelTable: 
    def __init__(self, nome, is_used_on_query, dict_query, is_used_on_json, dict_json, is_used_on_yaml, dict_yaml):
        self.nome = nome.lower()
        self.is_used_on_query = is_used_on_query
        self.dict_query = dict_query 
        self.is_used_on_json = is_used_on_json
        self.dict_json = dict_json
        self.is_used_on_yaml = is_used_on_yaml
        self.dict_yaml = dict_yaml
        
    
    # def __repr__(self):
    #     return f"ModelTable(nome={self.nome}, is_used_on_query={self.is_used_on_query}, count_used_on_query={self.count_used_on_query}, is_used_on_json={self.is_used_on_json}, dict_json={self.dict_json}, is_used_on_yaml={self.is_used_on_yaml}, dict_yaml={self.dict_yaml})"

    # Representacao em string para salvar em CSV
    def __str__(self):
        return f"{self.nome};{self.is_used_on_query};{self.dict_query};{self.is_used_on_json};{self.dict_json};{self.is_used_on_yaml};{self.dict_yaml}"
