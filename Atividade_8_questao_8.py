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
    """Classe simples para armazenar chave e valor."""
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}: {self.value})"
    
    #impletação da resolução 8

class Hashtable(Dictionary):

    def __init__(self, size):
        self._size = size
        self._table = [[] for _ in range(size)]   # Encadeamento
        self._count = 0  # contador de entradas (requisito da questão 8)

    def capacity(self):
        return self._size

    # -----------------------
    # Função Hash – Divisão
    # -----------------------
    def _hash(self, key):
        return key % self._size

    # -----------------------
    # Inserção / Atualização
    # -----------------------
    def set(self, key, value):
        index = self._hash(key)
        bucket = self._table[index]

        # Atualiza caso já exista
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # Inserção nova
        bucket.append(Entry(key, value))
        self._count += 1  # incrementa contador

    # -----------------------
    # Busca
    # -----------------------
    def get(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        
        return None

    # -----------------------
    # Remoção
    # -----------------------
    def delete(self, key):
        index = self._hash(key)
        bucket = self._table[index]

        for entry in bucket:
            if entry.key == key:
                bucket.remove(entry)
                self._count -= 1  # decrementa contador
                return entry.value
        
        return None

    # -----------------------
    # Questão 8: size()
    # -----------------------
    def size(self):
        return self._count

    # -----------------------
    # Questão 8: __len__()
    # -----------------------
    def __len__(self):
        return self._count

    # Representação visual (ajuda no debug)
    def __repr__(self):
        out = "\n*** HASHTABLE ***\n"
        for i, bucket in enumerate(self._table):
            out += f"{i}: {bucket}\n"
        out += f"Total de entradas: {self._count}\n"
        return out
    
ht = Hashtable(5)

ht.set(1, "A")
ht.set(6, "B")
ht.set(11, "C")  # colisões em 1

print(ht)

print("size():", ht.size())   # 3
print("len(ht):", len(ht))    # 3

ht.delete(6)

print(ht)

print("size():", ht.size())   # 2
print("len(ht):", len(ht))    # 2
