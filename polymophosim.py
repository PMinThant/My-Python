class Document:
    def __init__(self,name):
        self.name = name
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class pdf(Document):
    def show(self):
        return "Show PDF FIle"
    
class word(Document):
    def show(self):
        return "Show Word File"

print(word("Document").show())
print(pdf("Document").name)
