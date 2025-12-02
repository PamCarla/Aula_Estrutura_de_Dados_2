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


# ==========================================================
#               HASHTABLE – QUESTÃO 7
# ==========================================================

class Hashtable(Dictionary):

    def __init__(self, size):
        self._size = size
        self._table = [[] for _ in range(size)]   # Encadeamento (listas)

    def capacity(self):
        return self._size

    # -----------------------
    # Função Hash (Método da Divisão)
    # -----------------------
    def _hash(self, key):
        return key % self._size

    # -----------------------
    # Inserção / Atualização
    # -----------------------
    def set(self, key, value):
        index = self._hash(key)
        bucket = self._table[index]

        # Atualiza se chave existir
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # Inserção normal
        bucket.append(Entry(key, value))

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
                return entry.value
        
        return None

    # Apenas para visualizar
    def __repr__(self):
        out = "\n*** HASHTABLE ***\n"
        for i, bucket in enumerate(self._table):
            out += f"{i}: {bucket}\n"
        return out


# ==========================================================
#                Teste simples
# ==========================================================

if __name__ == "__main__":
    ht = Hashtable(5)

    ht.set(1, "A")
    ht.set(6, "B")   # colisão com 1
    ht.set(11, "C")  # colisão com 1 e 6

    print(ht)

    print("GET 6:", ht.get(6))
    print("DELETE 6:", ht.delete(6))
    print(ht)
