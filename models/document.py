from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BIGINT
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from database import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    document_name = Column(
        String(150),
        nullable=False
    )

    category = Column(
        String(50),
        nullable=False
    )

    source_filename = Column(
        String(255),
        nullable=False
    )

    file_path = Column(
        String(500),
        nullable=False
    )

    content_type = Column(
        String(100)
    )

    file_size = Column(
        BIGINT
    )

    uploaded_at = Column(
        DateTime,
        server_default=func.now()
    )