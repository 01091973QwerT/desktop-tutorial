from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func
from app.backend.db  import Base
from app.models import*


class Task(Base):
    __tablename__ = 'tasks'

    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)


    user = relationship("User", back_populates="tasks")

    @hybrid_property
    def priority_name(self):
        names = {
            0: "Низкий",
            1: "Средний",
            2: "Высокий",
            3: "Критический",
        }

        return names.get(self.priority, "Низкий") # Если priority не найден в словаре, возвращаем "Низкий"

    @priority_name.expression
    def priority_name(cls):
        return select([
            func.CASE([
                (cls.priority == 0, "Низкий"),
                (cls.priority == 1, "Средний"),
                (cls.priority == 2, "Высокий"),
                (cls.priority == 3, "Критический"),
            ], else_="Низкий")
        ]).label("priority_name")

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))