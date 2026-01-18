from sqlalchemy.orm import Session

from app.models.dependent import DependentProfile
from app.models.caregiver import CaregiverProfile
from app.schema.dependent_schema import DependentUpdate


def update_dependent_service(
    db: Session,
    dependent: DependentProfile,
    data: DependentUpdate
) -> DependentProfile:

    user = dependent.user

    # Update User
    if data.full_name is not None:
        user.full_name = data.full_name
    if data.phone is not None:
        user.phone = data.phone
    if data.address is not None:
        user.address = data.address
    if data.email is not None:
        user.email = data.email

    # Update Dependent
    if data.dependency_category is not None:
        dependent.dependency_category = data.dependency_category

    # Update caregivers
    if data.caregiver_ids is not None:
        caregivers = db.query(CaregiverProfile)\
            .filter(CaregiverProfile.id.in_(data.caregiver_ids))\
            .all()
        dependent.caregivers = caregivers

    db.commit()
    db.refresh(dependent)

    return dependent
