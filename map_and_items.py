"""
THIS IS THE ITEM SECTION
"""
item_id = {
    "id": "id",

    "name": "id card",

    "description":
        """This card contains the details of one of the bank manages. Jing Wu. it has clearence to the break room""",

    "mass": 0.1,
    "value":0,
    "use":"You use this to get in the vault door room.",
    "opens": rooms['Vault']
}

item_password = {
    "id": "password",

    "name": "password",

    "description":
        "This sheet of paper contains the password for the security computers.",
    "mass": 2.5,
    "value":0,
    "use":"You use this to get in the security room",
    "opens": rooms["Security Room"]
}

item_money = {
    "id": "money",

    "name": "money",

    "description":
        "This mountain of cash is almost enough to pay off your student debt.",
    "mass": 0.3,
    "value":0,

}

item_tape = {
    "id": "tape",

    "name": "tape",

    "description":
        "An empty tape taken from the security system.",
    "mass": 0.3,
    "value":0,
    "discrete":-40,
}

item_pistol = {
    "id": "pistol",

    "name": "pistol",

    "description":
        "A fairly discrete weapon. Good for controlling small crowds or people ",
    "mass":1.0,
    "value":20,
    "discrete":20,
    "use":"You fire the pistol in the air. Everyone starts screaming "
                        "and jumps to the ground. You demand that all the tells do "
                        "the same and don't press the silent alarm.",
    "opens": rooms["Break Room"]
}

item_shotgun = {
    "id": "shotgun",

    "name": "shotgun",

    "description":
        "A loud alternative to other weapons. works even better for controlling crowds.",

    "mass": 3.5,
    "value":40,
    "discrete":40,
    "use":"You fire the shotgun in the air. Everyone starts screaming "
                        "and jumps to the ground. You demand that all the tells do "
                        "the same and don't press the silent alarm.",
    "opens":rooms["Break Room"]
}

item_grenade = {
    "id": "grenade",

    "name": "grenade",

    "description":
        "Probaly not the best thing to take to a bank heist, but would be cool if you "
        "could pull it off.",
    "mass":0.5,
    "value":15,
    "discrete":50,
    "use":"You pull out the grenade. No one notices. You then yell that "
                        "you have a grenade. you get a blank look from the customer. "
                        "You pull the pin and people scream and jump to the ground."
                        "You throw the grenade in a big and it blows up.",
    "opens":rooms["Break Room"]
}

item_smoke = {
    "id": "smoke bomb",

    "name": "smoke bomb",

    "description":
        "Good for hiding your self from police or bank tellers so they don't know "
        "whats going on. Good for reducing the chances of calling the police.",
    "mass":0.6,
    "value":10,
    "discrete":-10,
    "use":"You throw the smoke grenade on the floor. A cloud of smoke apperas."
                        "It masks you so no one knows who you are.",
    "opens":rooms["Break Room"]
}

item_smg = {
    "id": "smg",

    "name": "smg",

    "description":
        "Very good for controling a crowd but does have a fair amount of noise.",
    "mass":4,
    "value":35,
    "discrete":35,
    "use":"You fire the SMG in the air. Everyone starts screaming "
                        "and jumps to the ground. You demand that all the tells do "
                        "the same and don't press the silent alarm.",
    "opens":rooms["Break Room"]
}

item_rpg= {
    "id": "rpg",

    "name": "rpg",

    "description":
        "This is very loud. You will definitely strike fear into your hostages.",
    "mass":5,
    "value":50,
    "discrete":60,
    "use":"You wave the RPG in the air. Everyone starts screaming "
                        "and jumps to the ground. You politely that all the tells do "
                        "the same and don't press the silent alarm.",
    "opens":rooms["Break Room"]
}

item_pigmask = {
    "id": "pig mask",

    "name": "pig mask",

    "description":
        "This helps hide your identity while also making it look like a pig is"
        "robbing the back.",
    "mass":0.5,
    "value":7,
    "discrete":-25,
    "use":"You put on the musk. No one will know who you are. They will just "
                 "be confused a pig is robbing a bank."
}

item_kirillmask = {
    "id": "kirill mask",

    "name": "kirill mask",

    "description":
        "this helps hiding your identity while also making it look like the main "
        "reason why you are robbing the bank, student debt.",
    "mass":.5,
    "value":15,
    "discrete":-40,
    "use":"You put on the musk. No one will know who you are. They will just "
                 "be confused why is Kirill robbing a bank."
}

item_clownmask = {
    "id": "clown mask",

    "name": "clown mask",

    "description":
        "This helps hiding your identity while also making you look like a clown "
        "to help scare anyone with a fear of clowns.",
    "mass":0.5,
    "value":7,
    "discrete":-20,
    "use":"You put on the musk. No one will know who you are. They will just "
                 "be confused a clown is robbing a bank."
}

item_boilersuit = {
    "id": "boiler suit",

    "name": "boiler suit",

    "description":
        "used to hide your normal cloths so no one can relate back to you.",
    "mass":1,
    "value":15,
    "discrete":-10,
    "use":"You put on the Suit. You think no one will know who you are "
                 "just the banks plumber."
}

item_ghostbusters = {
    "id": "ghost busters suit",

    "name": "ghost buster suit",

    "description":
        "Used to hide your normal cloths while also making it look like you are"
        "an authentic ghost buster.",
    "mass":1.5,
    "value":30,
    "discrete":-20,
    "use":"You put on the Suit. You think no one will know who you are "
                 "just the banks on site ghost buster. You cant help but sing "
                 "the song in your head."
}

item_backpack = {
    "id": "back pack",

    "name": "back pack",

    "description":
        "This helps you to carry more items, while also looking stylish.",
    "mass":-60,
    "value":20,
    "discrete":0,
    "use":"You put on the back pack and feel like you are back at uni. "
              "You start to have PTSD about being back but wears off after "
              "a few hours when you start thinking about all the stuff you"
              "can fit in there."
}

item_sportsbag = {
    "id": "sports bag",

    "name": "sports bag",

    "description":
        "This helps you carry alot more items at a time.",
    "mass":-120,
    "value":50,
    "discrete":1,
    "use":"You put on the back pack and instantly feel like you can "
              "carry more stuff. Strange."
}

item_fakegun = {
    "id": "fake gun",

    "name": "fake gun",

    "description":
        "This gun is fake. But you might get away with it looking real",
    "mass":0.5,
    "value":5,
    "discrete":10,
    "use":"You Pull out the gun. Every one screams and crys "
                        "and drops to the ground as quick as possible. The "
                        "Bank tellers move out from behind the glass. this"
                        "seemed to work better than the real thing.",
    "opens":rooms["Break Room"]
}

item_twizzler = {
    "id": "twizzler",

    "name": "twizzler",

    "description":
        "This is very very pointless this can not be used in anyway.",
    "mass":.5,
    "value":100,
    "discrete":100
}

item_C4 = {
    "id": "C4",

    "name": "C4",

    "description":
        "This can be used to blow stuff up. It is loud.",
    "mass":3,
    "value":30,
    "discrete":40,
    "use":"You push the C4 to the Vault door. You get a safe distance and BOOM!"
                   "the door blows wide open.",
    "opens":rooms["Vault"]
}

item_cartoonbomb = {
    "id": "cartoon bomb",

    "name": "cartoon bomb",

    "description":
        "Does not do much apart form look good",
    "mass":5,
    "value":10,
    "discrete":10
}

item_sparkler = {
    "id": "sparkler",

    "name": "sparkler",

    "description":
        "Looks pretty",
    "mass":0.1,
    "value":2,
    "discrete":5
}



item_drill = {
    "id": "drill",

    "name": "drill",

    "description":
        "Can be used to drive in screws or rob banks",
    "mass":2,
    "value":25,
    "discrete":20,
    "use":"You use the drill to break the locks to the vault. "
                       "It makes quite a bit of noise.",
    "opens":rooms["Vault"]
}

item_whiteoveralls = {
    "id": "white overalls",

    "name": "white overalls",

    "description":
        "To make you look like a paint",
    "mass":0.5,
    "value":5,
    "discrete":3,
    "use":"You put on the Suit. You think no one will know who you are "
                 "just the banks painter. But you are not wearing a mask."
}



item_axe = {
    "id": "axe",

    "name": "axe",

    "description":
        "If you are caught holding this in public you may get some odd looks",
    "mass":5,
    "value":10,
    "discrete":30,
    "use":"You pull this out and everyone gives you a worried look and"
                   " slowly gets to the ground. You yell this is a bank heist. You "
                   "then think it was quite obvious.",
    "opens":rooms["Break Room"]
}

item_stethoscopese = {
    "id": "stethoscopes",

    "name": "stethoscopes",

    "description":
        "Can be used to hear quiet noises, like the tick of a bank vault opening",
    "mass":0.4,
    "value":15,
    "discrete":1,
    "use":"You put on the stethoscope and place it on the vault door. you"
                   "try different codes and you hear click...."
                   "click...."
                   "click..."
                   "You are in, It was quite easy.",
    "opens":rooms["Vault"]
}
all_items = {
    "id": item_id,
    "password": item_password,
    "money": item_money,
    "tape": item_tape,
    "pistol": item_pistol,
    "shotgun": item_shotgun,
    "grenade": item_grenade,
    "smoke bomb": item_smoke,
    "smg": item_smg,
    "rpg": item_rpg,
    "pig mask": item_pigmask,
    "kirill mask":item_kirillmask,
    "clown mask":item_clownmask,
    "boiler suit":item_boilersuit,
    "ghost buster suit":item_ghostbusters,
    "back pack":item_backpack,
    "sports bag":item_sportsbag,
    "fake gun":item_fakegun,
    "twizzler":item_twizzler,
    "C4":item_C4,
    "cartoon bomb":item_cartoonbomb,
    "sparkler":item_sparkler,
    "drill":item_drill,
    "white overalls":item_whiteoveralls,
    "axe":item_axe,
    "stethoscopes":item_stethoscopese
}

"""
THIS IS THE MAP SECTION
"""

room_foyer = {
    "name": "Foyer",

    "description":
    """You are in a small room. The entrance to the bank. 
    No one can see you, you are in a blind spot. No one has 
    no idea what is about to happen.""",

    "exits": {"north": "Front Desk","south":"Van"},

    "items": [],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"]]
}

room_front_desk = {
    "name": "Front Desk",

    "description":
    """You are in the main room. There is a line of bank teller 
    serving people. They are hidden behind bullet proof glass. 
    This room is full of witnesses/hostages. This room leads to 
    all the other rooms to the bank, who ever designed this bank 
    should probably be fired""",

    "exits":  {"north": "Vault", "east": "Break Room", "south":"Foyer", "west":"Security Room" },

    "items": [all_items["id"]],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"],
             all_items["pistol"], all_items["shotgun"], all_items["grenade"], all_items["smoke bomb"], all_items["smg"], all_items["rpg"], all_items["fake gun"], all_items["axe"],
             all_items["id"], all_items["password"]]
}

room_vault_door = {
    "name": "The Vault Door",

    "description":
    """You go down a flight of stairs to the vault Door. You see a massive 
    vault door. You need to think of a way to get past.""",

    "exits": {"south": "Front Desk", "north":"Vault"},

    "items":[],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"],
             all_items["C4"], all_items["drill"], all_items["stethoscopes"]]
}


room_vault = {
    "name": "The Vault",

    "description":
    """All you see is Money, Money and Money. you start 
    wishing you had brought a bigger bag""",

    "exits": {"south": "Vault Door"},

    "items": [all_items["money"]],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"]]
}

room_security = {
    "name": "Security Room",

    "description":
    """You find your self in a small dark room, lit by the 
    glare of the security monitors. There is a tape player
    and a pile of tapes. which makes you wonder who even 
    uses tapes.""",

    "exits": {"east": "Front Desk"},

    "items": [all_items["tape"]],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"]]
}

room_break = {
    "name": "The Break Room",

    "description":
    """The room you are stood in is very basic, a desk and 
    kitchen. Conviently on the desk there is a peice of paper 
    written on it say password for the security room and an ID card.""",

    "exits": {"west": "Front Desk"},

    "items": [all_items["password"]],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"]]
}

room_van = {
    "name": "Van",

    "description":
        """You are in your van which is also your getaway vechial. 
        You now start to regret your choice since its just you""",

    "exits": {"west": "Gun Store", "east":"Fireworks Store", "north":"Foyer"},

    "items": [],

    "uses": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["white overalls"]]

}

room_gun = {
    "name": "Gun Store",

    "description":
        """You enter the store and get greeted by a man named gunther, 
        which isn't too much of a surpirse since its called gunther's guns. 
        The Walls of the store are plasted with guns.""",

    "exits": {"east": "Van", "west":"Hardware Store"},

    "items": [all_items["pistol"], all_items["shotgun"], all_items["grenade"], all_items["smoke bomb"], all_items["smg"], all_items["rpg"]]

}

room_firework = {
    "name": "Fireworks Store",

    "description":
        """You Enter a store with a strange array of items, you 
        start to think is this really just a fireworks store and why is it 
        so close to the bank""",

    "exits": {"west": "Van", "east": "Costume Store"},

    "items": [all_items["sparkler"], all_items["cartoon bomb"], all_items["C4"], all_items["twizzler"]]

}

room_costume = {
    "name": "Costume Store",

    "description":
        """As you walk in the door of this shop you get a weird chill 
        of a man looking at you. you ingor him cuz it turns out to be 
        a costume. the place is just a pile of costumes, which are the
        perfect disguize for the job.""",

    "exits": {"east": "Fireworks Store"},

    "items": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["back pack"], all_items["sports bag"], all_items["fake gun"]]

}
room_hardware = {
    "name": "Hardware Store",

    "description":
        """This is just a hardware store nothing special
        just contains the standard stuff""",

    "exits": {"east": "Gun Store"},

    "items": [all_items["drill"], all_items["white overalls"], all_items["axe"], all_items["stethoscopes"]]

}

rooms = {
    "Foyer": room_foyer,
    "Front Desk": room_front_desk,
    "Vault Door":room_vault_door,
    "Vault": room_vault,
    "Security Room": room_security,
    "Break Room": room_break,
    "Van":room_van,
    "Gun Store":room_gun,
    "Fireworks Store":room_firework,
    "Costume Store":room_costume,
    "Hardware Store":room_hardware


}