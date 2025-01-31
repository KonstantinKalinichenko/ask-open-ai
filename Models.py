from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Table, Column, Integer, String, MetaData

class Base(DeclarativeBase): # base class for model
    pass


class Questions_Answers(Base):
    __tablename__ = "Qna"
    __table_args__ = {"schema":"ask_ai"}
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) # unique ID column
    question: Mapped[str] = mapped_column(nullable=False) # question column
    answer: Mapped[str] = mapped_column(nullable=False) # answer column

    def __repr__(self) -> str:
        return f"Questions_Answers(id={self.id!r}, question={self.question!r}, answer={self.answer!r})"
