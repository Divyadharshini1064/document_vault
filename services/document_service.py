import os
import mimetypes

from models.document import Document
from utils.decorators import log_execution


class DocumentService:

    def __init__(
        self,
        repository,
        storage
    ):
        self.repository = repository
        self.storage = storage

    @log_execution
    def upload_document(
        self,
        name,
        category,
        source_path
    ):

        if not os.path.exists(source_path):
            raise FileNotFoundError(
                "File not found"
            )

        stored_path = self.storage.upload_file(
            source_path
        )

        document = Document(
            document_name=name,
            category=category,
            source_filename=os.path.basename(
                source_path
            ),
            file_path=stored_path,
            content_type=mimetypes.guess_type(
                source_path
            )[0],
            file_size=os.path.getsize(
                source_path
            )
        )

        return self.repository.save(
            document
        )

    def list_documents(self):

        documents = self.repository.get_all()

        return [
            {
                "id": doc.id,
                "name": doc.document_name,
                "category": doc.category,
                "size": doc.file_size
            }
            for doc in documents
        ]

    def search_documents(
        self,
        keyword
    ):

        documents = self.repository.search_by_name(
            keyword
        )

        return [
            {
                "id": doc.id,
                "name": doc.document_name,
                "category": doc.category
            }
            for doc in documents
        ]

    def view_document(
        self,
        doc_id
    ):

        return self.repository.get_by_id(
            doc_id
        )

    def download_document(
        self,
        doc_id,
        destination_path
    ):

        document = self.repository.get_by_id(
            doc_id
        )

        if not document:
            raise ValueError(
                "Document not found"
            )

        self.storage.download_file(
            document.file_path,
            destination_path
        )

    @log_execution
    def delete_document(
        self,
        doc_id
    ):

        document = self.repository.get_by_id(
            doc_id
        )

        if not document:
            raise ValueError(
                "Document not found"
            )

        self.storage.delete_file(
            document.file_path
        )

        self.repository.delete(
            document
        )