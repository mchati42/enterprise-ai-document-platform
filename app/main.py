from models import User, Project, Document


def ft_main():
    # =========================
    # 1. Create Users
    # =========================

    user1 = User(
        id=1,
        name="Ahmed",
        email="ahmed@gmail.com",
        role="admin"
    )

    user2 = User(
        id=2,
        name="Sara",
        email="sara@gmail.com",
        role="manager"
    )

    # =========================
    # 2. Create Projects
    # =========================

    project_A = Project(
        id=1,
        name="AI Document Platform",
        description="Enterprise document management system",
        owner=user1
    )

    project_B = Project(
        id=2,
        name="Financial Analysis",
        description="Financial document analysis project",
        owner=user2
    )

    # =========================
    # 3. Create Documents
    # =========================

    document1 = Document(
        id=1,
        title="Financial Report",
        file_type="PDF",
        owner=user1,
        project=project_A
    )

    document2 = Document(
        id=2,
        title="Business Requirements",
        file_type="DOCX",
        owner=user2,
        project=project_B
    )

    # =========================
    # 4. Add documents
    # =========================

    project_A.add_document(document1)
    project_B.add_document(document2)

    print("\n===== PROJECT A =====")
    project_A.display_info()
    project_A.list_documents()

    print("\n===== PROJECT B =====")
    project_B.display_info()
    project_B.list_documents()

    # =========================
    # 5. Rename document
    # =========================

    print("\n===== RENAME DOCUMENT =====")

    document1.rename("Financial Report 2026")

    document1.display_info()

    # =========================
    # 6. Remove document
    # =========================

    print("\n===== REMOVE DOCUMENT =====")

    project_A.remove_document(document1)

    project_A.display_info()
    project_A.list_documents()

    # =========================
    # 7. Add it back
    # =========================

    print("\n===== ADD DOCUMENT AGAIN =====")

    project_A.add_document(document1)

    project_A.display_info()
    project_A.list_documents()

    # =========================
    # 8. Change project
    # =========================

    print("\n===== CHANGE PROJECT =====")

    document1.change_project(project_B)

    print("\nProject A:")
    project_A.display_info()
    project_A.list_documents()

    print("\nProject B:")
    project_B.display_info()
    project_B.list_documents()

    print("\nDocument:")
    document1.display_info()


if __name__ == "__main__":
    ft_main()

#TODO

# Sure 👍 Here are the problems in short:

# ❌ User.display_info()
# It says "Document ID" instead of user information.
# change_role() is empty.
# ❌ Project.add_document()
# The same document can be added multiple times.
# You need to prevent duplicates.
# ❌ Project.remove_document()
# It can crash if the document is not in the project.
# You need to handle this safely.
# ⚠️ Document ↔ Project relationship
# You have to keep both sides synchronized: