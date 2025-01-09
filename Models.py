from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase): # base class for model
    pass


class Qna(Base): # model sets table name automatically instead of needing __tablename__
    id: Mapped[int] = mapped_column(primary_key=True) # ID will be the PK
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullabe=False)