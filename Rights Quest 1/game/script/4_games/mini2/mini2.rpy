

label mini2:
    scene 
    # fill the game screen with objects
    $ InitGame("santa workshop", 1.0, (825, 660), "figure1")

    # show the game screen as a simple background
    $ GameAsBG()
    with dissolve

    user "Find the Map"

    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with dissolve:
            pause(1.0)
        scene HintOg with dissolve
        user "I wonder if this is the map Mr. Santa is looking for..."
        scene blank
        jump foundhiddenitem
    else:
        "{i}Hint : On the box near the tree{/i}"
        jump mini2