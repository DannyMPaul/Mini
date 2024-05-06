default firstlock = 0.0
default secondlock = 0.0
default thirdlock = 0.0

label L2:
    #The Right against discrimination.
    if L2complete==True:
        jump completedD
    else: 
        pass

    scene bg_town with fade
    show snow1
    show snow2
    "The kids approach the town and find their way to a complex of restaurants."

    show brochar at right with moveinright
    bro "Sighhh… I’m starving."

    show sischar at left with moveinleft
    sis "Me too! Let’s get something to eat!"
    bro "Look! I see a restaurant! Let’s get ourselves a bowl of noodles!"

    hide brochar
    hide sischar 
    with dissolve

    scene bg_restaurant with fade

    show storeownerchar at right with moveinright 
    storeowner "Hello there, how can I help you kids?"

    show sischar at left with moveinleft
    sis "Hi Mister! We’d like a bowl of noodles each!"
    storeowner "Alright! What kind of noodles would you kids like?"

    show sischar at left with moveinleft
    sis "I’d like a bowl of Chicken noodles!"
    hide sischar with dissolve

    show brochar at left with moveinleft
    bro "I'd like a bowl of Chow mein noodles."

    if gender=='male':
        storeowner "And what about this young Gentleman?"
    elif gender=='female':
        storeowner "And what about this young Lady?"
    else:
        storeowner "And what about this young child?"

    hide brochar
    with dissolve

    menu:
        "I'd like to eat ..."
        "Ramen Noodles":
            user "I’d like a bowl of Ramen!"
            show storeownerchar at right with moveinright
            storeowner "A Chicken Noodles, Chow mein and a Ramen coming right up!!"
            pass
        "Chicken Noodles":
            user "I'd like a bowl of Chicken noodles!"
            show storeownerchar at right with moveinright
            storeowner "2 Chicken Noodles and a Chow mein coming right up!!"
            pass
        "Chow Mein Noodles":
            user "I'd like a bowl of Chow mein noodles"
            show storeownerchar at right with moveinright
            storeowner "2 Chow mein and Chicken Noodle coming right up!!"
            pass


    show sischar at left with moveinleft
    sis "That will be all, Thank you!"

    show storeownerchar at right with moveinright
    storeowner "Delightful! I’ll get your food ready in jiffy!"

    hide ownerchar
    hide sischar 
    with dissolve

    show mrsgraychar at left with moveinleft
    mrsgray "Hello there, I’d like to order a Ramen"

    show storeownerchar at right with moveinright
    storeowner "Sorry, We don’t serve your kind of people."   

    hide storeownerchar with dissolve

    show brochar at right with moveinright
    bro "Excuse me? What do you mean by \"your kind of people\" ?"

    show mrsgraychar at left with moveinleft
    mrsgray "I believe I am being discriminated due to the color of my skin..."

    label d3:
        scene bg_restaurant with dissolve
        menu:
            user "..."
            "Speak up against discrimination":
                user "That's absurd!! Everyone deserves to be treated equally!"
                pass
            "Watch and Stay Silent":
                show sischar at left with moveinleft
                sis "We can't let this go!! Remember what grandma said to us??"
                hide sischar with dissolve
                jump discrimination
                jump d3

    show brochar at left with moveinleft
    bro "Yeah, you can't just refuse to serve someone just because of thier skin color"

    show storeownerchar at right with moveinright
    storeowner "I have the right to refuse service to anyone I want!"
    bro "Actually, you don't. Discrimination based on color is against the law"

    hide brochar with dissolve

    show sischar at left with moveinleft
    sis "That's right! We have the {b}Right Against Discrimination{/b}!"

    show storeownerchar at right with moveinright
    storeowner "Fine! I'll serve her this time, but I don't have to like it."

    hide sischar
    hide storeownerchar
    with dissolve
    
    "The store owner reluctantly serves Mrs.Gray her noodles"
    
    show mrsgraychar at left with moveinleft
    mrsgray "Thank you for standing up for me, kids. It's important to fight against discrimination whenever we encounter it."

    show brochar at right with moveinright
    bro "Our pleasure Maam, we believe everyone deserves to be treated with respect and fairness."
    mrsgray "May I enquire what brings 3 bright children out on this cold day?"
    
    menu:
        user "We're out to..."
        "To Search for a missing present":
            mrsgray "Ohh, is that so?"
            hide brochar with dissolve
            show sischar at right with moveinright
            sis "Yes, Santa requested for our help to find it."
        "To Eat some warm noodles":
            mrsgray "haha, nothing beats a soup that warms one's soul"
            hide brochar with dissolve
            show sischar at right with moveinright
            sis "True, we have to hunt for Santa's missing presents after this"
        "To Play in the snow":
            mrsgray "haha, such innocent souls. Be sure not to catch a cold, dear younglings"
            hide brochar with dissolve
            show sischar at right with moveinright
            sis "We'll be careful, meanwhile we have to hunt for Santa's missing presents"
    
    mrsgray "Now that I recall, I came across a gift-box on my way here"
    sis "Could it be the one we are searching for?"
    
    hide sischar with dissolve
    show brochar at right with moveinright
    bro "Might be, Mind telling us where you saw it?"
    mrsgray "I took it to the \"Lost & Found\", it should still be there"
    bro "I see, thank you!"
    mrsgray "No, it's the least I can do for younglings that stood up for me."

    hide brochar with dissolve
    show sischar at right with moveinright
    sis "Lets dig in before the noodles go cold"

    scene black with dissolve
    "As they share their stories and eat, the Mrs.Gray thanks the children yet again for their courage and go their own separate ways"
    "The Children follow the directions given by Mrs.Gray and reach the \"Lost & Found\""

    scene lost_found with fade
    show brochar at right with moveinright
    bro "Hmmm, I think this is the place,"
    show sischar at left with moveinleft
    sis "It says 'Lost & Found' at the top, let's go inside!"
    hide brochar
    hide sischar

    "The children go inside to find a man sitting at the front desk."

    scene lost_found_inside
    show mrwickchar at right with moveinright
    mrwick "Hello there children, welcome to the Lost and Found! My name is Mr.Wick, how may I be at your service?"
    show sischar at left with moveinleft
    sis "Hello Mister, we were told by a woman that she had given our missing item here!"
    hide sischar
    mrwick "Ooh, jolly! What is the missing items that you are seeking?"
    show brochar at left with moveinleft
    bro "We are helping Santa find his missing presents. Have you by any chance happen to see a present box?"
    hide brochar
    mrwick "Yes, indeed! I have kept it safe in my locker, waiting for its rightful owner!"
    show sischar at left with moveinleft
    sis "Yay! You have it! Can we see it please!"
    hide sischar
    mrwick "Very well, children. I shall go inside and look."
    hide mrwickchar
    "Mr.Wick goes inside to retrieve th present."
    "Moments later, Mr.Wick return to the kids with an empty hand."
    show mrwickchar at right with moveinright
    mrwick "I'm very sorry to bother you children, but I'm not being able to find the key to my locker. Would you kids be willing to help me? "
    hide mrwickchar

    label d5:
    menu:
        "Help Mr.Wick find the key.":
            user "We would be happy to help Mr.Wick!"
            show sischar at right with moveinright
            sis "Yes we would!"
            show brochar at left with moveinleft
            bro "Let's get to work guys!"
            pass
        "Go back home":
            user "I want to go back home."
            show brochar at left with moveinleft
            bro "We can't leave without Santa's presents. We can't let Christmas go to ruins!"
            show sischar at right with moveinright
            sis "You got that right, bro!"
            jump d5
        "Do nothing":
            user "I don't feel like doing anything."
            show sischar at right with moveinright
            sis "We have to get back to Santa as soon as we can!"
            show brochar at left with moveinleft
            bro "Come on! We need to find the next present and return them to Santa. Christmas is in our hands!"
            jump d5

    hide brochar
    hide sischar

    show mrwickchar
    mrwick "Let's go children!"
    hide mrwickchar

    "Mr.Wick takes the children inside his safety locker room."

    scene safe_room with fade
    show mrwickchar
    mrwick "Alright Children, we're looking for a silver key that unlocks my locker."
    hide mrwickchar

    jump hidden4
    
    label foundhiddenitem2:
        pass

    label test:
        pass

    $ L2complete = True
    $ c = c+1
    
    jump pro3