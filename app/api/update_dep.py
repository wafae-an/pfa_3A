from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from app.models.dependent import DependentProfile
from app.schema.dependent_schema import DependentUpdate
from app.services.dependent_update import update_dependent_service


router = APIRouter(prefix="/dependents", tags=["Dependents"])


@router.put("/{dependent_id}")
def update_dependent_endpoint(
    dependent_id: int,
    data: DependentUpdate,
    db: Session = Depends(get_db)
):
    dependent = db.query(DependentProfile).filter(
        DependentProfile.id == dependent_id
    ).first()

    if not dependent:
        raise HTTPException(status_code=404, detail="Dependent introuvable")

    dependent = update_dependent_service(db, dependent, data)
    return {"message": "Dependent mis à jour avec succès"}
