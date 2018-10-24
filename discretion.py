try_again():
    user_input = input('Would you like to play again')
    if 'yes'.lower() in user_input:
         main()

else:
    pass


def detection(items):
    detection = -200
    inventory = ["grenade","smoke bomb","smg","rpg","pig mask","clown mask","boiler suit","ghost buster suit"]
    
    for x,a in items.items():
        if x not in inventory:
            detection += a['discrete']
                
           
        elif detection < -100: #-100's a placeholder at the moment. Can adjust to whatever best suits the game.
                print('Failed'+'\n'*5)#placeholder for ending. 
                break
                    
        else:
            pass
                
    return detection


