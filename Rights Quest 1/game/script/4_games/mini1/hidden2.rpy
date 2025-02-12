#done

label hidden2:
    play music "Game.mp3"
    scene bg_santa_workshop
    # fill the game screen with objects
    $ InitGame("bg_santa_workshop", 1.0, (825, 660), "figure1")

    # show the game screen as a simple background
    $ GameAsBG()
    with advtrans5

    user "Let's help find the Map"
    window hide
    # launch the game and play
    $ res = StartGame()

    # show as background again
    # (but without items found during the game)
    $ GameAsBG()

    # check the game results and play them in the scenario    
    if oRes:
        scene black with advtrans5:
            pause(1.0)
        scene bg_santa_workshop with dissolve
        user "I wonder if this is the map Mr. Santa is looking for..."
        play music "main-menu-music.mp3"
        jump foundhiddenitem
    else:
        "{i}Hint : On the box near the tree{/i}"
        jump hidden2