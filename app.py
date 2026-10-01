from database import Base
from database import engine
from database import SessionLocal

from repositories.document_repository import (
    DocumentRepository
)

from services.local_storage import (
    LocalStorage
)

from services.document_service import (
    DocumentService
)

Base.metadata.create_all(engine)

session = SessionLocal()

repository = DocumentRepository(
    session
)

storage = LocalStorage()

service = DocumentService(
    repository,
    storage
)

while True:

    print("\n===== DOCUMENT VAULT =====")
    print("1. Upload")
    print("2. List")
    print("3. Search")
    print("4. View Metadata")
    print("5. Download")
    print("6. Delete")
    print("7. Exit")

    choice = input(
        "Enter choice: "
    )

    try:

        if choice == "1":

            name = input(
                "Document Name: "
            )

            category = input(
                "Category: "
            )

            path = input(
                "File Path: "
            )

            service.upload_document(
                name,
                category,
                path
            )

            print(
                "Document Uploaded Successfully"
            )

        elif choice == "2":

            documents = (
                service.list_documents()
            )

            for doc in documents:
                print(doc)

        elif choice == "3":

            keyword = input(
                "Enter Search Keyword: "
            )

            documents = (
                service.search_documents(
                    keyword
                )
            )

            for doc in documents:
                print(doc)

        elif choice == "4":

            doc_id = int(
                input(
                    "Enter Document ID: "
                )
            )

            document = (
                service.view_document(
                    doc_id
                )
            )

            if document:

                print(
                    f"ID: {document.id}"
                )

                print(
                    f"Name: {document.document_name}"
                )

                print(
                    f"Category: {document.category}"
                )

                print(
                    f"Path: {document.file_path}"
                )

                print(
                    f"Size: {document.file_size}"
                )

            else:
                print(
                    "Document not found"
                )

        elif choice == "5":

            doc_id = int(
                input(
                    "Enter Document ID: "
                )
            )

            destination = input(
                "Destination Path: "
            )

            service.download_document(
                doc_id,
                destination
            )

            print(
                "Download Successful"
            )

        elif choice == "6":

            doc_id = int(
                input(
                    "Enter Document ID: "
                )
            )

            service.delete_document(
                doc_id
            )

            print(
                "Document Deleted"
            )

        elif choice == "7":

            print("Exiting...")
            break

        else:
            print(
                "Invalid Choice"
            )

    except Exception as e:
        print(
            f"Error: {e}"
        )