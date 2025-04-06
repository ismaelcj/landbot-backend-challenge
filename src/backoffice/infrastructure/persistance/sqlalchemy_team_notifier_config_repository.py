from sqlalchemy import exists
from sqlalchemy.orm import Session

from src.backoffice.domain.team_notifier_config import TeamNotifierConfig
from src.backoffice.domain.team_notifier_config_repository import TeamNotifierConfigRepository
from src.backoffice.infrastructure.persistance.team_notifier_config_record import TeamNotifierConfigRecord


class SqlalchemyTeamNotifierConfigRepository(TeamNotifierConfigRepository):
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def save(self, config: TeamNotifierConfig) -> None:
        config_record = TeamNotifierConfigRecord.from_entity(config)
        self._db_session.add(config_record)
        self._db_session.commit()

    def find_by_topic(self, topic: str) -> TeamNotifierConfig:
        config_record = self._db_session.query(TeamNotifierConfigRecord).filter_by(topic=topic).one()
        return config_record.to_entity()

    def exists(self, topic: str) -> bool:
        exists_query = self._db_session.query(
            exists().where(TeamNotifierConfigRecord.topic == topic)).scalar()
        return True if exists_query else False
