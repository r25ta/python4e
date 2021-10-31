class Motorista:
    """ Clase de Motoristas """
    def __init__(self, cpf, nome, cnpj_transp, nome_transp, cnpj_emb, nome_emb):
        self.cpf = cpf
        self.nome = nome
        self.cnpj_transp = cnpj_transp
        self.nome_transp = nome_transp
        self.cnpj_emb = cnpj_emb
        self.nome_emb = nome_emb
        
    def getCpf(self):
        return self.cpf
    
    def getNome(self):
        return self.nome

    def getCnpjTransp(self):
        return self.cnpj_transp

    def getNomeTransp(self):
        return self.nome_transp

    def getCnpjEmb(self):
        return self.cnpj_emb

    def getNomeEmb(self):
        return self.nome_emb
    
    def __str__(self):
        return "\n***********************\nCPF: %s \nNome: %s \nCNPJ Transp: %s \nTransp: %s \nCNPJ Emb: %s \nEmb: %s " %(self.cpf, self.nome, self.cnpj_transp, self.nome_transp, self.cnpj_emb, self.nome_emb)