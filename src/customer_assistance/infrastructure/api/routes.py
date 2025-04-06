from fastapi import APIRouter, HTTPException

from src.customer_assistance.application.assistance_request_command import AssistanceRequestCommand
from src.customer_assistance.infrastructure.api.models import AssistanceRequest
from src.shared.infrastructure.deps import CommandBus

router = APIRouter(prefix="/assistance_request", tags=["assistance"])


@router.put("/")
async def request_assistance(
    request: AssistanceRequest,
    command_bus: CommandBus
) -> None:
    try:
        command = AssistanceRequestCommand(
            assistance_id=request.assistance_id,
            topic=request.topic,
            description=request.description
        )
        command_bus.dispatch(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
