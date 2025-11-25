from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.database import get_db
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services

router = APIRouter()

@router.post("/giftcards", response_model=schemas.GiftCard, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Cajero"))])
def create_gift_card(gift_card: schemas.GiftCardCreate, db: Session = Depends(get_db)):
    return services.create_gift_card(db, gift_card)

@router.get("/giftcards/{code}", response_model=schemas.GiftCard, dependencies=[Depends(get_current_user)])
def get_gift_card(code: str, db: Session = Depends(get_db)):
    db_gift_card = services.get_gift_card_by_code(db, code)
    if not db_gift_card:
        raise HTTPException(status_code=404, detail="Gift card not found")
    return db_gift_card

@router.post("/giftcards/{code}/redeem", response_model=schemas.GiftCard, dependencies=[Depends(require_role("Cajero"))])
def redeem_gift_card(code: str, amount: float, db: Session = Depends(get_db)):
    db_gift_card = services.get_gift_card_by_code(db, code)
    if not db_gift_card:
        raise HTTPException(status_code=404, detail="Gift card not found")
    try:
        return services.redeem_gift_card(db, db_gift_card, amount)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/credit-notes", response_model=schemas.CreditNote, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Cajero"))])
def create_credit_note(credit_note: schemas.CreditNoteCreate, db: Session = Depends(get_db)):
    return services.create_credit_note(db, credit_note)
