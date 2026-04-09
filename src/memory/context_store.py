class ContextStore:
    def __init__(self):
        self._store = []

    def add(self, item: dict):
        self._store.append(item)

    def all(self):
        return self._store
