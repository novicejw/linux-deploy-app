from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

catalog_json = json.loads("""{
    "users": [
        {
            "name": "The Wine Chef",
            "email": "wine@wine.com",
            "picture": "https://www.bbcgoodfood.com/sites/default/files/guide/hub-image/2013/06/is-wine-good-for-you-hub.jpg"
        }
    ],
    "categories": [
        {
            "name": "Red Wine"
        },
        {
            "name": "White Wine"
        },
        {
            "name": "Sparkling Wine"
        }
    ],
    "items": [
        {
            "name": "Amarone",
            "description": "From Italy's Veneto Region a strong, dry, long-lived red, made from a blend of partially dried red grapes.",
            "category_id": 1
        },
        {
            "name": "Barbaresco",
            "description": "A red wine from the Piedmont Region of Italy, made from Nebbiolo grapes it is lighter than Barolo.",
            "category_id": 1
        },
        {
            "name": "Barolo",
            "description": "A light red wine from the Veneto Region of Italy. Blended from several grapes the wine garnet in color, dry and slightly bitter, sometimes lightly sparkling.",
            "category_id": 1
        },
        {
            "name": "Zinfandel",
            "description": "With predominant raspberry flavors and a spicy aroma, Zinfandels can be bold and intense as well as light and fruity. It takes well to blending bringing out flavors of cherry, wild berry & plum with notes of leather, earth & tar.",
            "category_id": 1
        },
        {
            "name": "Cabernet Sauvignon",
            "description": "Full-bodied wines with great depth that improve with aging. Cabernet spends from 15 to 30 months aging in American & French Oak barrels which tend to soften the tannins, adding the toasty cedar & vanilla flavors.",
            "category_id": 1
        },
        {
            "name": "Asti Spumante",
            "description": "From the Piedmont Region of Italy, A semidry sparkling wine produced from the Moscato di Canelli grape in the village of Asti.",
            "category_id": 3
        },
        {
            "name": "Chardonnay",
            "description": "Apple, Pear, Vanilla, Fig, Peach, Pineapple, Melon, Citrus, Lemon, Grapefruit, Honey, Spice, Butterscotch, Butter & Hazelnut. Chardonnay takes well to Oak aging & barrel fermentation and is easy to manipulate with techniques such as sur lie aging & malolactic fermentation.",
            "category_id": 2
        },
        {
            "name": "Colombard",
            "description": "The second most widely planted white variety in California, nearly all of it for jug wines. It produces an abundant crop, nearly 11 tons per acre, and makes clean and simple wines.",
            "category_id": 1
        },
        {
            "name": "Cava",
            "description": "Spanish sparkling wine. Produced by the methode champenoise.",
            "category_id": 3
        },
        {
            "name": "Soave",
            "description": "A straw-colored dry white wine Italy's Veneto Region. Symphony Symphony is a U. C. Davis clone. In 1948, the Muscat of Alexandria and Grenache Gris grapes were combined to create this delicate Muscat flavor. Very distinctive.",
            "category_id": 2
        }
    ]
}""")

# Add users
for e in catalog_json['users']:
    user_input = User(
        name=str(e['name']),
        email=str(e['email']),
        picture=str(e['picture']),
    )
    session.add(user_input)
    session.commit()

# Add categories
for e in catalog_json['categories']:
    category_input = Category(
        name=str(e['name']),
        user_id=1
    )
    session.add(category_input)
    session.commit()

# Add wines
for e in catalog_json['items']:
    item_input = Item(
        name=str(e['name']),
        user_id=1,
        description=str(e['description']),
        category_id=int(e['category_id'])
    )
    session.add(item_input)
    session.commit()

# Show that items have been added
print "added items!"
