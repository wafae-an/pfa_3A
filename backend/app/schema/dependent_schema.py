from pydantic import BaseModel, EmailStr
from typing import Optional, List
from app.models.enums_dependent import DependencyCategory
from app.schema.caregiver_basic_info import CaregiverBasicInfo
class DependentCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: Optional[str] = None
    address: Optional[str] = None
    dependency_category: DependencyCategory
    caregiver_ids: List[int]


class DependentUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    dependency_category: Optional[DependencyCategory] = None
    caregiver_ids: Optional[List[int]] = None

        
class DependentInfo(BaseModel):
    id: int
    email: str
    full_name: str
    phone: Optional[str]
    address: Optional[str]
    is_active: bool
    dependency_category: DependencyCategory
    caregivers: List[CaregiverBasicInfo]


class Config:
    from_attributes = True
    

