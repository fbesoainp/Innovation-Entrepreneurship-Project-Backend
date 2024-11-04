import json
from http import HTTPStatus

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from integrations.nexa_ai import NexaaiIntegration
from models.compliance import ComplianceRequest, ComplianceResponse

router = APIRouter(prefix="/compliance")


@router.post("/", status_code=HTTPStatus.CREATED)
def compliance(body: ComplianceRequest) -> ComplianceResponse:
    """Evaluate adherence to hiring policies based on compliance criteria."""
    nexa = NexaaiIntegration()
    try:
        return nexa.get_complicance_response(body)
    except json.decoder.JSONDecodeError as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail="Failed to decode NexaAI response"
        ) from e
