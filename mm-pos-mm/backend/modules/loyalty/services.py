from sqlalchemy.orm import Session
from . import models, schemas
import uuid

def generate_unique_code():
    """Generates a unique code for a gift card."""
    return str(uuid.uuid4().hex)[:16].upper()

def create_gift_card(db: Session, gift_card: schemas.GiftCardCreate):
    code = generate_unique_code()
    db_gift_card = models.GiftCard(
        code=code,
        initial_amount=gift_card.initial_amount,
        current_balance=gift_card.initial_amount,
        customer_id=gift_card.customer_id
    )
    db.add(db_gift_card)
    db.commit()
    db.refresh(db_gift_card)
    return db_gift_card

def get_gift_card_by_code(db: Session, code: str):
    return db.query(models.GiftCard).filter(models.GiftCard.code == code).first()

def redeem_gift_card(db: Session, gift_card: models.GiftCard, amount: float):
    if not gift_card.is_active or gift_card.current_balance < amount:
        raise ValueError("Gift card is invalid or has insufficient balance")

    gift_card.current_balance -= amount
    if gift_card.current_balance <= 0:
        gift_card.is_active = False

    db.commit()
    db.refresh(gift_card)
    return gift_card

def create_credit_note(db: Session, credit_note: schemas.CreditNoteCreate):
    db_credit_note = models.CreditNote(
        initial_amount=credit_note.initial_amount,
        current_balance=credit_note.initial_amount,
        customer_id=credit_note.customer_id,
        origin_sale_id=credit_note.origin_sale_id
    )
    db.add(db_credit_note)
    db.commit()
    db.refresh(db_credit_note)
    return db_credit_note
