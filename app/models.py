class User:
    def __init__(self,id, name, email, role):
        self.id = id
        self.name = name
        self.email = email
        self.role = role
    def display_info(self):
        print(f"User ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")

    def change_role(self, new_role):
        self.role = new_role
        


class Project:
    def __init__(self, id, name, description, owner):
        self.id = id 
        self.name = name
        self.description = description
        self.owner = owner
        self.documents = []

    def display_info(self):
        print(f"Project ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Owner: {self.owner.name}")
        print(f"Number of documents: {len(self.documents)}")

    def add_document(self, doc):
        if doc not in self.documents:
            self.documents.append(doc)
    
    def remove_document(self, doc):
        if doc in self.documents:
            self.documents.remove(doc)

    def list_documents(self):
        for doc in self.documents:
            print(doc.title)

class Document:
    def __init__(self, id, title, file_type, owner, project):
        self.id = id
        self.title = title
        self.file_type = file_type
        self.owner = owner
        self.project = project
    def display_info(self):
        print(f"Document ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Type: {self.file_type}")
        print(f"Owner: {self.owner.name}")
        print(f"Project: {self.project.name}")

    def rename(self, new_name):
        self.title = new_name

    def change_project(self, new_project):
        if self.project == new_project:
            return
        old_project = self.project
        old_project.remove_document(self)
        self.project = new_project
        self.project.add_document(self)
