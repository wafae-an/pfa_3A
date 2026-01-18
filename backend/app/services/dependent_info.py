# app/services/dependent_info.py
from sqlalchemy.orm import Session, joinedload
from app.models.user import User
from app.models.dependent import DependentProfile
from app.schema.dependent_schema import DependentInfo
from app.schema.caregiver_basic_info import CaregiverBasicInfo

def get_all_dependents_service(db: Session) -> list[DependentInfo]:
    dependents = (
        db.query(DependentProfile)
        .options(
            joinedload(DependentProfile.user),
            joinedload(DependentProfile.caregivers).joinedload("user")
        )
        .all()
    )

    result = []

    for dep in dependents:
        result.append(
            DependentInfo(
                id=dep.user.id,
                email=dep.user.email,
                full_name=dep.user.full_name,
                phone=dep.user.phone,
                address=dep.user.address,
                is_active=dep.user.is_active,
                dependency_category=dep.dependency_category,
                caregivers=[
                    CaregiverBasicInfo(
                        id=caregiver.user.id,
                        full_name=caregiver.user.full_name,
                        email=caregiver.user.email
                    )
                    for caregiver in dep.caregivers
                ]
            )
        )

    return result
