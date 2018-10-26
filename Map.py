from items import *

room_foyer = {
    "name": "Foyer",

    "description":
    """You are in a small room. The entrance to the bank. 
    No one can see you, you are in a blind spot. No one has 
    no idea what is about to happen.""",

    "exits": {"north": "Front Desk","south":"Van"},

    'locked exits': {},
    'unlocking tool': [],


    "items": [],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"]]
}

room_front_desk = {
    "name": "Front Desk",

    "description":
    """You are in the main room. There is a line of bank teller 
    serving people. They are hidden behind bullet proof glass. 
    This room is full of witnesses/hostages. This room leads to 
    all the other rooms to the bank, who ever designed this bank 
    should probably be fired""",

    'new description':
    """Everyone is laying on the floor, keeping silent cause they have no idea 
    what is going on and they are very scared of you""",

    "exits":  { "south":"Foyer"},

    'locked exits': {"north": "Vault Door", "east": "Break Room", "west":"Security Room" },

    'unlocking tool': [],

    "items": [],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"],
             all_items["pistol"], all_items["shotgun"], all_items["grenade"], all_items["smoke"], all_items["smg"], all_items["rpg"], all_items["fake"], all_items["axe"]]
}

room_cctv = {
    'name': 'CCTV Room',
    'description':
    '''You are standing in a dark dank small room with 6 different monitors and an old vcr recording machince
    you think, god this banks security system is dismally poor, even a student could rob this place''',

    'exits' : {'east': 'Security Room'},

    'locked exits' : {},

    'unlocking tool' : [],
    'items' : [all_items['tape']],

    'uses' : []
}

room_vault_door = {
    "name": "The Vault Door",

    "description":
    """You go down a flight of stairs to the vault Door. You see a massive 
    vault door. You need to think of a way to get past.""",

    'new description':
    """Your stadning infront of an open door, the vault is just through it,
    you begin to think this might actually work!""",

    "exits": {"south": "Front Desk"},

    'locked exits': {"north":"Vault"},

    'unlocking tool' : [item_id, item_C4, item_drill, item_stethoscopese],

    "items":[],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"],
             all_items["c4"], all_items["drill"], all_items["stethoscopes"], all_items["id"]]
}


room_vault = {
    "name": "The Vault",

    "description":
    """All you see is Money, Money and Money. you start 
    wishing you had brought a bigger bag""",

    "exits": {"south": "Vault Door"},

    'locked exits': {},
    'unlocking tool' : [],


    "items": [all_items["money"]],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"]]
}

room_security = {
    "name": "Security Room",

    "description":
    """You find your self in a small dark room, theres a door before you,
    to the CCTV room, but it is password protected.""",

    'new description': """You find your self in a small dark room, theres a door before you,
    to the CCTV room, it is wide open cause you unlocked it""",

    "exits": {"east": "Front Desk"},

    'locked exits': {'west': 'CCTV Room'},
    'unlocking tool' : [],

    "items": [all_items["id"]],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"], all_items['password']]
}

room_break = {
    "name": "The Break Room",

    "description":
    """The room you are stood in is very basic, a desk and 
    kitchen. Conviently on the desk there is a peice of paper 
    written on it say password for the security room and an ID card.""",

    "exits": {"west": "Front Desk"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [all_items["password"]],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"]]
}

room_van = {
    "name": "Van",

    "description":
        """You are in your van which is also your getaway vechial. 
        You now start to regret your choice since its just you""",

    "exits": {"west": "Gun Store", "east":"Fireworks Store", "north":"Foyer"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [],

    "uses": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["white"]]

}

room_gun = {
    "name": "Gun Store",

    "description":
        """You enter the store and get greeted by a man named gunther, 
        which isn't too much of a surpirse since its called gunther's guns. 
        The Walls of the store are plasted with guns.""",

    "exits": {"east": "Van", "west":"Hardware Store"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [all_items["pistol"], all_items["shotgun"], all_items["grenade"], all_items["smoke"], all_items["smg"], all_items["rpg"]],

    'uses': []

}

room_firework = {
    "name": "Fireworks Store",

    "description":
        """You Enter a store with a strange array of items, you 
        start to think is this really just a fireworks store and why is it 
        so close to the bank""",

    "exits": {"west": "Van", "east": "Costume Store"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [all_items["sparkler"], all_items["cartoon"], all_items["c4"], all_items["twizzler"]],

    'uses': []

}

room_costume = {
    "name": "Costume Store",

    "description":
        """As you walk in the door of this shop you get a weird chill 
        of a man looking at you. you ingor him cuz it turns out to be 
        a costume. the place is just a pile of costumes, which are the
        perfect disguize for the job.""",

    "exits": {"west": "Fireworks Store"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [all_items['pig'], all_items["kirill"], all_items["clown"], all_items["boiler"], all_items["ghost"], all_items["back"], all_items["sports"], all_items["fake"]],

    'uses': []

}
room_hardware = {
    "name": "Hardware Store",

    "description":
        """This is just a hardware store nothing special
        just contains the standard stuff""",

    "exits": {"east": "Gun Store"},

    'locked exits': {},
    'unlocking tool' : [],

    "items": [all_items["drill"], all_items["white"], all_items["axe"], all_items["stethoscopes"]],

    'uses': []

}

rooms = {
    "Foyer": room_foyer,
    "Front Desk": room_front_desk,
    "Vault Door":room_vault_door,
    "Vault": room_vault,
    "Security Room": room_security,
    'CCTV Room': room_cctv,
    "Break Room": room_break,
    "Van":room_van,
    "Gun Store":room_gun,
    "Fireworks Store":room_firework,
    "Costume Store":room_costume,
    "Hardware Store":room_hardware


}