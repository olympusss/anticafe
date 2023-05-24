from models import Banner, Question
from sqlalchemy.orm import Session, joinedload
from upload_depends import upload_image
from sqlalchemy import asc, desc

def create_banner(db: Session, file):
    uploaded_name = upload_image('banners', file)
    new_add = Banner(
        img = uploaded_name
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_banner(page, limit, db: Session):
    result = db.query(Banner)\
        .order_by(desc(Banner.create_at))\
            .offset((page - 1) * limit)\
                .limit(limit)\
                    .all()
    return result


def create_qa(req, model, db: Session):
    new_add = model(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_questions(db: Session):
    result = db.query(Question).options(joinedload(Question.answer)).all()
    return result