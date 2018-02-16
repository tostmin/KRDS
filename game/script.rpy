init:
    $ player = ""

define sd = Character('Sabine',color="#c812aa")
define dissolve = Dissolve(1.5)
define dad = Character('Father',color="#06e514")
define mc = ("[player]")
label start:

    "Before we start, what's my name?"
    
label nameplayer:
    
    $ player = renpy.input("What's my name again? (Max 12 Characters)", allow=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", length=12)
    if player == "":
        "I don't remember.  Let's try that again."
        jump nameplayer
            
    if player == "Huey":
        "That isn't my name."
        jump nameplayer
        
    if player == "Huey Long":
        "That isn't my name."
        jump nameplayer
        
    if player == "Cpt Hook":
        "That isn't my name."
        jump nameplayer
        
    if player is not None:
        $check_name = len(player)
        if check_name == 1:
                "I don't think that's right.  Let's try that again."
                jump nameplayer
    $ player = player.title()

                
    if player == "  ":
        "I don't think my parents were that mean."
        jump nameplayer
             
    mc "Is that really my name?"
    menu:
            
        "No":
            jump nameplayer
                
        "Yes":
            pass
                
    mc "I guess that is my name."
label genderchoice:
    
    mc "And what's my gender?"
    menu:
        
        "I really should know this."
        
        "Male":
            jump gamestart
            
        "Female":
            "Not right now, it isn't."
            jump genderchoice
            
label gamestart:
    
    "Hey look, it's a game."
    jump openingstart
return
