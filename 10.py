from abc import ABC, abstractmethod
import math

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
    """Classe que guarda chave e valor."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}: {self.value})"




#           QUESTÃO 10 — HASH POR MULTIPLICAÇÃO


class HashtableMul(Dictionary):

    def __init__(self, size):
        self._size = size
        self._table = [[] for _ in range(size)]

        # constante sugerida por Knuth
        self._A = (math.sqrt(5) - 1) / 2  


    def capacity(self):
        return self._size

 
    #   Método da Multiplicação
  
    def _hash(self, key):
        frac = (key * self._A) % 1      # parte fracionária
        return int(self._size * frac)   # piso


    def set(self, key, value):
        index = self._hash(key)
        bucket = self._table[index]

        # atualização
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # inserção
        bucket.append(Entry(key, value))


    def get(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None


    def delete(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                return entry.value
        return None


    def __repr__(self):
        out = "\n*** HASHTABLE MULTIPLICAÇÃO ***\n"
        for i, bucket in enumerate(self._table):
            out += f"{i}: {bucket}\n"
        return out
ht = HashtableMul(7)

ht.set(10, "A")
ht.set(22, "B")
ht.set(31, "C")

print(ht)

print(ht.get(22))

ht.delete(22)
print(ht)

