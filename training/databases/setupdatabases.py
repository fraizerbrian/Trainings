from basic import db,Puppy

# creates all the tables model to db table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Puppy',4)


# None
# None
print(sam.id)
print(frank.id)

# adds the above in one call
db.session.add_all([sam, frank])

# commit the above changes in database
db.session.commit()

print(sam.id)
print(frank.id)
