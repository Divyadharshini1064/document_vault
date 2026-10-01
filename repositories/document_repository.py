from models.document import Document


class DocumentRepository:

    def __init__(self, session):
        self.session = session

    def save(self, document):

        self.session.add(document)
        self.session.commit()

        return document

    def get_all(self):

        return (
            self.session
            .query(Document)
            .all()
        )

    def get_by_id(self, doc_id):

        return (
            self.session
            .query(Document)
            .filter(Document.id == doc_id)
            .first()
        )

    def search_by_name(self, keyword):

        return (
            self.session
            .query(Document)
            .filter(
                Document.document_name.contains(
                    keyword
                )
            )
            .all()
        )

    def delete(self, document):

        self.session.delete(document)
        self.session.commit()