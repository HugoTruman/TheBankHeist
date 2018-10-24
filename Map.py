from items import all_items

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

    "exits":  {"north": "Vault Door", "east": "Break Room", "south":"Foyer", "west":"Security Room" },

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

    "items": [all_items["pistol"], all_items["shotgun"], all_items["grenade"], all_items["smoke bomb"], all_items["smg"], all_items["rpg"]],

    'uses': []

}

room_firework = {
    "name": "Fireworks Store",

    "description":
        """You Enter a store with a strange array of items, you 
        start to think is this really just a fireworks store and why is it 
        so close to the bank""",

    "exits": {"west": "Van", "east": "Costume Store"},

    "items": [all_items["sparkler"], all_items["cartoon bomb"], all_items["C4"], all_items["twizzler"]],

    'uses': []

}

room_costume = {
    "name": "Costume Store",

    "description":
        """As you walk in the door of this shop you get a weird chill 
        of a man looking at you. you ingor him cuz it turns out to be 
        a costume. the place is just a pile of costumes, which are the
        perfect disguize for the job.""",

    "exits": {"east": "Fireworks Store"},

    "items": [all_items['pig mask'], all_items["kirill mask"], all_items["clown mask"], all_items["boiler suit"], all_items["ghost buster suit"], all_items["back pack"], all_items["sports bag"], all_items["fake gun"]],

    'uses': []

}
room_hardware = {
    "name": "Hardware Store",

    "description":
        """This is just a hardware store nothing special
        just contains the standard stuff""",

    "exits": {"east": "Gun Store"},

    "items": [all_items["drill"], all_items["white overalls"], all_items["axe"], all_items["stethoscopes"]],

    'uses': []

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