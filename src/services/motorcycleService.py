from src.database import SessionLocal
from src.models.motorcycle import Motorcycle

def get_all_motorcycles():
    db = SessionLocal()
    motorcycles = db.query(Motorcycle).all()
    db.close()
    return motorcycles


def get_motorcycle_by_id(placa):
    db = SessionLocal()
    moto = db.query(Motorcycle).filter(Motorcycle.placa == placa).first()
    db.close()
    return moto


def create_motorcycle(data):
    db = SessionLocal()
    new_moto = Motorcycle(**data)
    db.add(new_moto)
    db.commit()
    db.refresh(new_moto)
    db.close()
    return new_moto


def update_motorcycle(placa, data):
    db = SessionLocal()
    moto = db.query(Motorcycle).filter(Motorcycle.placa == placa).first()

    if not moto:
        db.close()
        return None

    for key, value in data.items():
        setattr(moto, key, value)

    db.commit()
    db.refresh(moto)
    db.close()
    return moto


def delete_motorcycle(placa):
    db = SessionLocal()
    moto = db.query(Motorcycle).filter(Motorcycle.placa == placa).first()

    if not moto:
        db.close()
        return False

    db.delete(moto)
    db.commit()
    db.close()
    return True