from fastapi import APIRouter, HTTPException

from src.backoffice.application.commands.team_notifier_config_create_command import TeamNotifierConfigCreateCommand
from src.backoffice.infrastructure.api.models import TeamNotifierConfigModel
from src.shared.infrastructure.deps import CommandBus

router = APIRouter(prefix="/backoffice", tags=["backoffice"])

@router.put("/team_notifier_config")
async def new_team_notifier_config(
        notifier: TeamNotifierConfigModel,
        command_bus: CommandBus
) -> None:
    try:
        command = TeamNotifierConfigCreateCommand(
            topic=notifier.topic,
            method=notifier.method,
            destination=notifier.destination
        )
        command_bus.dispatch(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
