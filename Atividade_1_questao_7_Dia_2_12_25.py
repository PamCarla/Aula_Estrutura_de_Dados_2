from abc import ABC, abstractmethod

class Dictionary(ABC):
    @abstractmethod
    def capacity(self):
        pass
    
    @abstractmethod
    def set(self, key, value):
        pass
    
    @abstractmethod
    def get(self, key):
        pass
    
    @abstractmethod
    def delete(self, key):
        pass

class Entry:
    """Classe para armazenar chave e valor."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}: {self.value})"


# ==========================================================
#                  HASHTABLE – QUESTÃO 7
# ==========================================================

class Hashtable(Dictionary):

    def __init__(self, size):
        self._size = size
        self._table = [[] for _ in range(size)]   # encadeamento (listas)

    def capacity(self):
        return self._size

    # -----------------------
    #   Função Hash (Divisão)
    # -----------------------
    def _hash(self, key):
        return key % self._size

    # -----------------------
    #       Inserção
    # -----------------------
    def set(self, key, value):
        index = self._hash(key)
        bucket = self._table[index]

        # Atualização se já existir
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # Caso contrário, insere novo
        bucket.append(Entry(key, value))

    # -----------------------
    #        Busca
    # -----------------------
    def get(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        
        return None

    # -----------------------
    #        Remoção
    # -----------------------
    def delete(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                return entry.value
        
        return None

    # Apenas para visualizar a tabela
    def __repr__(self):
        result = "\n*** HASHTABLE ***\n"
        for i, bucket in enumerate(self._table):
            result += f"{i}: {bucket}\n"
        return result
ht = Hashtable(5)

#Exemplo funcional do codigo
ht.set(1, "A")
ht.set(6, "B")  # colisão com 1 (mesmo bucket, pois 6 % 5 = 1)
ht.set(11, "C") # colisão com 1 e 6

print(ht)

print(ht.get(6))   # retorna "B"

ht.delete(6)
print(ht)

print(ht.get(6))   # retorna None