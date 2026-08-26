from models import User, Project, Document


def main():

    # ========================================
    # 1. CREATE USERS
    # ========================================

    print("\n===== CREATE USERS =====")

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

    user1.display_info()
    print()

    user2.display_info()


    # ========================================
    # 2. CHANGE USER ROLE
    # ========================================

    print("\n===== CHANGE USER ROLE =====")

    print("Before:")
    user1.display_info()

    user1.change_role("manager")

    print("\nAfter:")
    user1.display_info()


    # ========================================
    # 3. CREATE PROJECTS
    # ========================================

    print("\n===== CREATE PROJECTS =====")

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

    project_A.display_info()
    print()

    project_B.display_info()


    # ========================================
    # 4. CREATE DOCUMENTS
    # ========================================

    print("\n===== CREATE DOCUMENTS =====")

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

    document1.display_info()
    print()

    document2.display_info()


    # ========================================
    # 5. ADD DOCUMENTS TO PROJECTS
    # ========================================

    print("\n===== ADD DOCUMENTS =====")

    project_A.add_document(document1)
    project_B.add_document(document2)

    project_A.display_info()
    project_A.list_documents()

    print()

    project_B.display_info()
    project_B.list_documents()


    # ========================================
    # 6. TEST DUPLICATE DOCUMENT
    # ========================================

    print("\n===== TEST DUPLICATE DOCUMENT =====")

    project_A.add_document(document1)
    project_A.add_document(document1)

    print("Documents in Project A:")
    project_A.list_documents()

    print(f"Number of documents: {len(project_A.documents)}")


    # ========================================
    # 7. RENAME DOCUMENT
    # ========================================

    print("\n===== RENAME DOCUMENT =====")

    print("Before:")
    document1.display_info()

    document1.rename("Financial Report 2026")

    print("\nAfter:")
    document1.display_info()


    # ========================================
    # 8. REMOVE DOCUMENT
    # ========================================

    print("\n===== REMOVE DOCUMENT =====")

    print("Before:")
    project_A.list_documents()

    project_A.remove_document(document1)

    print("\nAfter:")
    project_A.list_documents()

    print(f"Number of documents: {len(project_A.documents)}")


    # ========================================
    # 9. REMOVE DOCUMENT AGAIN
    # ========================================

    print("\n===== REMOVE DOCUMENT AGAIN =====")

    project_A.remove_document(document1)

    print("Program did not crash.")
    print("Safe removal works.")


    # ========================================
    # 10. ADD DOCUMENT AGAIN
    # ========================================

    print("\n===== ADD DOCUMENT AGAIN =====")

    project_A.add_document(document1)

    project_A.list_documents()


    # ========================================
    # 11. CHANGE PROJECT
    # ========================================

    print("\n===== CHANGE PROJECT =====")

    print("\nBefore changing:")

    print("\nProject A:")
    project_A.list_documents()

    print("\nProject B:")
    project_B.list_documents()

    print("\nDocument project:")
    print(document1.project.name)


    document1.change_project(project_B)


    print("\nAfter changing:")

    print("\nProject A:")
    project_A.list_documents()

    print("\nProject B:")
    project_B.list_documents()

    print("\nDocument project:")
    print(document1.project.name)


    # ========================================
    # 12. CHANGE TO SAME PROJECT
    # ========================================

    print("\n===== CHANGE TO SAME PROJECT =====")

    document1.change_project(project_B)

    print("Document project:")
    print(document1.project.name)

    print("\nProject B documents:")
    project_B.list_documents()


    # ========================================
    # 13. FINAL STATE
    # ========================================

    print("\n===== FINAL STATE =====")

    print("\n--- USERS ---")
    user1.display_info()
    print()
    user2.display_info()

    print("\n--- PROJECT A ---")
    project_A.display_info()
    project_A.list_documents()

    print("\n--- PROJECT B ---")
    project_B.display_info()
    project_B.list_documents()

    print("\n--- DOCUMENT 1 ---")
    document1.display_info()

    print("\n--- DOCUMENT 2 ---")
    document2.display_info()


if __name__ == "__main__":
    main()