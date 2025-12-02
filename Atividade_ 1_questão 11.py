import random
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
    """Classe que guarda a chave e o valor."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}: {self.value})"


#   Hash Universal 

class HashUniversal(Dictionary):

    def __init__(self, size, prime=10**9 + 7):
        self._size = size
        self._table = [[] for _ in range(size)]

        # p deve ser primo >= size (usamos 1e9+7)
        self._p = prime

        # gera a e b aleatórios
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)

    def capacity(self):
        return self._size

    # Função hash universal
    def _hash(self, key):
        return ((self._a * key + self._b) % self._p) % self._size

    # Inserção
    def set(self, key, value):
        index = self._hash(key)
        bucket = self._table[index]

        # Atualização
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # Inserção nova
        bucket.append(Entry(key, value))

    # Busca
    def get(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        
        return None

    # Delete
    def delete(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                return entry.value
        
        return None

    def __repr__(self):
        result = "\n*** HASH UNIVERSAL ***\n"
        for i, bucket in enumerate(self._table):
            result += f"{i}: {bucket}\n"
        return result
    #teste 
ht = HashUniversal(7)

ht.set(10, "A")
ht.set(20, "B")
ht.set(15, "C")

print(ht)

print(ht.get(20))
ht.delete(20)

print(ht.get(20))
