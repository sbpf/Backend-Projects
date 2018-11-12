from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///travelogueapp.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a user
newUser = User(name="Sindhu Shankar", email="sindhu.pathfinder@gmail.com",
             picture='https://i.pinimg.com/originals/a5/7f/be/a57fbefdb674adc1a61f6f362cc7a5fc.jpg')
session.add(newUser)
session.commit()

############################################################################################################
# Items for National Parks
category1 = Category(user_id=1, name="National Parks")

session.add(category1)
session.commit()

#adding item 1
item1 = Item(user_id=1, name="Olympic National Park", description="""Olympic National Park is on Washington's Olympic Peninsula in the Pacific Northwest.
The park sprawls across several different ecosystems, from the dramatic peaks of the Olympic Mountains to old-growth forests.
The summit of glacier-clad Mt. Olympus is popular with climbers, and hiking and backpacking trails cut through the park's rainforests and along its Pacific coastline.""",
            category=category1)

session.add(item1)
session.commit()

#adding item 2
item2 = Item(user_id=1, name="Yosemite National Park",
             description="""Yosemite National Park is in California's Sierra Nevada Mountains. It's famed for its giant, ancient sequia trees, and for Tunnel View,
the iconic vista of towering BridalVeil Fall and the granite cliffs of El Capitan and Half Dome. In Yosemite Village are shops, restaurants,
lodging, the Yosemite Museum and the Ansel Adams Gallery, with prints of the photographer's renowned black-and-white landscapes of the area.""",
            category=category1)

session.add(item2)
session.commit()

#adding item 3
item3 = Item(user_id=1, name="Grand Canyon National Park",
             description="""Grand Canyon National Park, located in northwestern Arizona, is the 15th site in the United States to have been named a national park.
The park's central feature is the Grand Canyon, a gorge of the Colorado River, which is often considered one of the Wonders of the World.
The park, which covers 1,217,262 acres (1,901.972 sq mi; 4,926.08 km2) of unincorporated area in Coconino and Mohave counties, received more than six million recreational visitors in 2017,
which is the second highest count of all American national parks after Great Smoky Mountains National Park.The Grand Canyon was designated a World Heritage Site by UNESCO in 1979.""",
            category=category1)

session.add(item3)
session.commit()

############################################################################################################
# Items for Beaches
category2 = Category(user_id=1, name="Beaches")

session.add(category2)
session.commit()

#adding item 4
item4 = Item(user_id=1, name="Santa Cruz Beach", description="""The Santa Cruz Beach Boardwalk is an oceanfront amusement park in Santa Cruz, California.
             Founded in 1907, it is California's oldest surviving amusement park and one of the few seaside parks on the West Coast of the United States.""",
            category=category2)

session.add(item4)
session.commit()

#adding item 5
item5 = Item(user_id=1, name="Half Moon Bay",
             description="""The San Mateo County Coastside around Half Moon Bay area is one of the largest beach areas in the San Francisco Bay Area.
There are also scores of very unique parks throughout the foothills and mountains surrounding the coastal plane from Pescadero through Montara.
Hiking, biking, surfing, kayaking, paddleboarding, tidepooling, strolling the beaches, walking mountain trails are just some of the
things to do and activities here in the Bay Area on California State Beaches and in the parks around Half Moon Bay.""",
            category=category2)

session.add(item5)
session.commit()

############################################################################################################
# Items for Cities

category3 = Category(user_id=1, name="Cities")

session.add(category3)
session.commit()

#adding item 6
item6 = Item(user_id=1, name="San Francisco", description="""San Francisco, in northern California, is a hilly city on the tip of a peninsula surrounded by
the Pacific Ocean and San Francisco Bay. It's known for its year-round fog, iconic Golden Gate Bridge, cable cars and colorful Victorian houses.
The Financial District's Transamerica Pyramid is its most distinctive skyscraper. In the bay sits Alcatraz Island, site of the notorious former prison.""",
            category=category3)

session.add(item6)
session.commit()

#adding item 7
item7 = Item(user_id=1, name="Chicago",
             description="""Chicago, on Lake Michigan in Illinois, is among the largest cities in the U.S. Famed for its bold architecture, it has a skyline
punctuated by skyscrapers such as the iconic John Hancock Center, 1,451-ft. Willis Tower (formerly the Sears Tower) and the neo-Gothic Tribune Tower.
The city is also renowned for its museums, including the Art Institute of Chicago with its noted Impressionist and Post-Impressionist works.""",
            category=category3)

session.add(item7)
session.commit()

############################################################################################################
# Items for Restaurants
category4 = Category(user_id=1, name="Restaurants")

session.add(category4)
session.commit()

#adding item 8
item8 = Item(user_id=1, name="Olive Garden",
             description="""Olive Garden is an American casual dining restaurant chain specializing in Italian-American cuisine.
It is a subsidiary of Darden Restaurants, Inc., which is headquartered in Orange County, Florida.""",
            category=category4)

session.add(item8)
session.commit()

#adding item 9
item9 = Item(user_id=1, name="The Cheesecake Factory",
             description="""The Cheesecake Factory, Inc. is a restaurant company and distributor of cheesecakes based in the United States.""",
            category=category4)

session.add(item9)
session.commit()

############################################################################################################
# Items for Hiking Trails
category5 = Category(user_id=1, name="Hiking Trails")

session.add(category5)
session.commit()

#adding item 10
item10 = Item(user_id=1, name="Los Gatos Creek Trail",
             description="""This 10 mile trail offers opportunities for pedestrians, hikers, bicyclists, skaters and nature lovers.
The complete trail extends from Lexington Reservoir above Los Gatos all the way to Meridian Avenue in San Jose.
Still a work in progress, the trail will eventually end at confluence with the Guadalupe River in downtown San Jose.""",
            category=category5)

session.add(item10)
session.commit()

#adding item 11
item11 = Item(user_id=1, name="Guadalupe Trail",
             description="""The Guadalupe River Trail is an 11-mile (18 km) pedestrian and bicycle path in the city of San Jose, California.
The path runs along the banks of the Guadalupe River. The trail is currently composed of two discontinuous segments: a short segment along
the Upper Guadalupe River and a longer segment along the Lower Guadalupe River.This trail is heavily used for both recreation and commuting,
as it provides direct access to Downtown San Jose from many of the outlying neighborhoods. The trail is paved.""",
            category=category5)

session.add(item11)
session.commit()

# Items for Miscellaneous
category6 = Category(user_id=1, name="Miscellaneous")

session.add(category6)
session.commit()

print "added items"
