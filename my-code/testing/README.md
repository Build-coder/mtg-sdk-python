cards = Card.where(set='ktk').where(subtypes='warrior,human').all()

Can't get 'test1.py' to work because I use the function above ^ and
must use a string literal and not a string variable as an argument. 

But I have to use a string variable cause the set name changes, can't 
hard code it like I would have to with a string literal