#!/usr/bin/env python3

from app import app
from models import db, Planet, Scientist, Mission

if __name__ == '__main__':
    with app.app_context():
        s1 = Scientist(name="coop", field_of_study="")
        db.session.add(s1)
        db.session.commit()
        # import ipdb; ipdb.set_trace()