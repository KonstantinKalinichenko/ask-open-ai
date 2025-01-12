from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, MappedAsDataclass

class Base(DeclarativeBase, MappedAsDataclass): # base class for model
    pass


class Questions_Answers(Base):
    __tablename__ = 'Qna'
    id: Mapped[int] = mapped_column(primary_key=True) # unique ID column
    question: Mapped[str] = mapped_column(nullable=False) # question column
    answer: Mapped[str] = mapped_column(nullabe=False) # answer column