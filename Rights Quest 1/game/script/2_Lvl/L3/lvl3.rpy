label L3:
    #The Right to Survival gave the power of healing and nourishment
    if L3complete==True:
        jump completedD
    else: 
        pass
    hide unicorn with dissolve
    scene somewhere with fade
    "trial"

    $ L3complete = True
    $ c = c+1
    jump pro3