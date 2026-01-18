# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# ⚠️ IMPORT CRUCIAL : Importer TOUS les modèles AVANT create_all
from app.models.user import User
from app.models.caregiver import CaregiverProfile
from app.models.dependent import DependentProfile
from app.models.association import CaregiverDependentAssociation
from app.models.enums import UserRole
from app.api import create_caregiver,update_caregiver,desactivate_caregiver,info_caregiver,create_dep,update_dep,info_dep,desativate_dep



app = FastAPI()

# ✅ D'ABORD créer les tables
Base.metadata.create_all(bind=engine)
print("✅ Tables créées dans la base de données")

@app.get("/")
async def root():
    return {"message": "hello world"}

# ✅ Ensuite ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_caregiver.router)
app.include_router(update_caregiver.router)
app.include_router(desactivate_caregiver.router)
app.include_router(info_caregiver.router)
app.include_router(create_dep.router)
app.include_router(update_dep.router)
app.include_router(desativate_dep.router)
app.include_router(info_dep.router)