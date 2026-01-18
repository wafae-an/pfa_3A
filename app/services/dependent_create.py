from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User
from app.models.dependent import DependentProfile
from app.models.caregiver import CaregiverProfile
from app.schema.dependent_schema import DependentCreate




def create_dependent_service(db: Session, data: DependentCreate) -> DependentProfile:
    # Création User
    user = User(
        email=data.email,
        hashed_password=data.password,
        full_name=data.full_name,
        phone=data.phone,
        address=data.address,
        role="DEPENDENT",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Création DependentProfile
    dependent = DependentProfile(
        user_id=user.id,
        dependency_category=data.dependency_category
    )

    # Affectation des caregivers
    caregivers = db.query(CaregiverProfile)\
        .filter(CaregiverProfile.id.in_(data.caregiver_ids))\
        .all()

    dependent.caregivers = caregivers

    db.add(dependent)
    db.commit()
    db.refresh(dependent)

    return dependent
