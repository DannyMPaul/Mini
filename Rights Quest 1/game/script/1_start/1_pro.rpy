default debug_gameplay_only = False #easier to jump btw files

label pro1:
    scene black with dissolve
    "As the summer vacation starts a band of 3 friend's go and visit their friend's grandma who lived by the ocean"
    scene bg_house with fade
    "The grandma always captured the heart of the children with the unique stories that would secretly hold moral values that would be needed by the children"

    scene black with dissolve
    show granny_shadow
    gran "Oh my, It seems [p1] slept off"
    show granny_shadow at left with move

    show sis_shadow
    sis "Wake up!! Granny is going to share a story with us!!"
    show sis_shadow at right 
    with move

    #hide all
    show bg_living at blink
    pause(2.0)
    scene bg_living

    show sis at right with moveinright
    sis "Wow, someone slept like a baby"

    show bro at left with moveinleft
    bro "Do you even remember who you are?"

    user "Yeah kind of..."

    bro "Really? Whats your name then?"

    #hide all
    scene black with fade

    label name_set:
        $ name = renpy.input("My name is...", default="Luke")
        $ name = name.strip()
        $ name = name.lower()

        if name == "keith" :
            "{i}(That's my brother's name...){/i}"
            jump name_set
        elif name == "eileen" :
            "{i}(That's my sister's name...){/i}"
            jump name_set
        
        $ name = name.title()

        menu:
            "{i}(My name is : [name], right?){/i}"
            "Yes":
                "My name's [name]"
            "No":
                "I might have slept too much..."
                jump name_set
    
    scene bg_living with dissolve
    show bro at right with moveinright
    bro "The sleeping princess is finally awake"
    
    show granny at left with moveinleft
    gran "Lets not make fun of the young one, now shall we begin?"    

    hide bro
    show sis at right with moveinright
    sis "Yes Granny lets begin!!"
    
    #hide all
    scene black with fade
    show granny at left with dissolve:
        alpha 0.5 #transparency
    gran "Once upon a time, there lived 3 young children."
    scene bg_town with dissolve #with 3kids
    "Although they were young, they were mature at heart"
    "One day, they heard of a village folktale about the magical jewels and that getting all 3 of them would grant them one wish"

    scene bg_town2 with fade #wo 3kids
    show bro at right with moveinright
    bro "We have to venture into the magical forest and find the crystals"

    show sis at left with moveinleft
    sis "Lets go on an adventure!!"

    label d1:
        menu:
            "Let's goo!!":
                pass
            "Maybe another time...":
                bro "Come on, theres not much to do today anyways"
                jump d1

    jump pro2