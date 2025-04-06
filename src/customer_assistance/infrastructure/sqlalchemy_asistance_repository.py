from sqlalchemy import exists
from sqlalchemy.orm import Session

from src.customer_assistance.domain.assistance_repository import AssistanceRepository
from src.customer_assistance.domain.assistance import Assistance
from src.customer_assistance.infrastructure.assistance_record import AssistanceRecord


class SqlalchemyAssistanceRepository(AssistanceRepository):
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def save(self, assistance: Assistance) -> None:
        assistance_record = AssistanceRecord.from_entity(assistance)
        self._db_session.add(assistance_record)
        self._db_session.commit()

    def find_by_id(self, assistance_id: str) -> Assistance:
        assistance_record = self._db_session.query(AssistanceRecord).filter_by(id=assistance_id).one()
        return assistance_record.to_entity()

    def exists(self, assistance_id: str) -> bool:
        exists_query = self._db_session.query(
            exists().where(AssistanceRecord.id == assistance_id)).scalar()
        return True if exists_query else False