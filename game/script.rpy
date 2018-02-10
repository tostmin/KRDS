define sd = Character('Sabine',color="#c812aa")
define dissolve = Dissolve(1.0)
define mc = Character('You',color="#130c16")
define dad = Character('Father',color="#06e514")

label start:

    scene bg classroom
    
    with dissolve
    "Zurich, Swiss Confederation, XX October, 1935."
    
    "It's a dry Thursday afternoon, compounded by the dryness of your classes."
    
    "Comfortable in the back of the class, you drift in and out of sleep."
    
    "In your half-formed daydreams, you fly above the sleepy city school, the drabness of the city, and into the mountains."
    
    scene bg flying mountains
    
    with fade
    
    "A wide expanse of sky, little specks moving around on the ground."
    
    #make this part longer
    
    "You soar high above the worries of those below you, and towards..."
    
    scene bg classroom
    
    "A loud rap on the corner of your desk abruptly rouses you from the peaceful flight.  Your ancient teacher glares daggers down at you, but says nothing."
    
    "She heaves a sigh that sounds more like a wheeze before returning to the front of the class."
    
    scene bg train cabin
    
    with fade
    
    "Swiss countryside, XX January, 1936." 
    
    "That's all you remember from that day."
    
    "From what your father subsequently explained to you, while you were walking home, you walked right into a riot and in the chaos were somehow knocked out."
    
    "Luckily, you only lost your small pocket change, and suffered minor head trauma."
    
    scene bg fatherstudy
    
    with fade
    
    dad "And that's why you're going to this school.  Zurich is becoming too dangerous."
    
    "Your father, a middle-aged foreign affairs public servant that looks more like an accountant than a politician, stared at you from across his colossal study desk."
    
    "You could never remember having been to Geneva, although you think you can remember your mother being from a small village there."
    
    menu Your_Plea:
        
        "What can you say?"
        
        "This isn't fair, I can handle myself.":
            $ confronted_authority = True
            $ sought_authority = False
            $ stoic = False
            jump confronting_father
            
        "Can't you come with me?":
            $ sought_authority = True
            $ confronted_authority = False
            $ stoic = False
            jump pleading_father
            
        "You say nothing.":
            $ stoic = True
            $ confronted_authority = False
            $ sought_authority = False
            jump strong_silent
            
label confronting_father:
    
    mc "This isn't fair.  I can handle myself."
    
    "Your father removes his well worn glasses and clutches the bridge of his nose."
    
    dad "Will you not listen to me, once in your life?  It is not as though I gave you the choice."
    
    "You rise to speak again, but his piercing glare quiets the words in your throat.  Normally, this would be the start to a shouting match, but the genuine fear behind your father's eyes quiets you."
    
    mc "I'll do it, for your sake, but when this violence is over, I'm coming back."
    
    dad "Of course.  It should all blow over by the spring."
    
    jump train_returned
    
label pleading_father:
    
    mc "Can't you come with me?"
    
    "You see your father's previous attempt at a stoic face soften for a moment, but he shakes his head, and it is discarded."
    
    dad "I have important business, still, in the city.  I will try to see you in the summer, or you can come back home."
    
    "You shoot him one last pleading look, but his eyes are resolute."
    
    jump train_returned
    
label strong_silent:
    
    "You saw this coming, and aren't surprised.  Your injuries have given you time to think your situation over, and you see no reason to argue."
    
    dad "It's a good school, you'll see.  The sons and daughters of the most important people in the country."
    
    "He gives you a weak smile, and places a train ticket on his desk, pushing it towards you."
    
    jump train_returned
    
label train_returned: 
    
    scene bg train cabin
    with fade
        
    "And so it was decided.  You spent the remainder of November and December in Zurich, saying goodbye to your friends and packing, and after a muted, tense Christmas celebrated with your father called to the office for one crisis or another." 
    
    if stoic:
        
        "The silence didn't bother you.  It gave you more time to say goodbye to your city."
        
        jump train_returned_2
        
    if confronted_authority:
        
        "Your father seemed to almost relish the opportunity of leaving, given how your holidays had turned into taciturn exchanges and harsh looks."
        
        jump train_returned_2
        
    else:
        
        jump train_returned_2
        
label train_returned_2:
    
    "Now, you find yourself on a train making a leisurely path through the Swiss mountains to a small mountain town near your final destination."
    
    "A boarding school for the children of politicians and diplomats."
    
    "As you boarded, you noticed other young men and women who seemed to be in a similar state as the one in which you now found yourself."
    
    if sought_authority:
        
        "The attendant directed you to your cabin after a confused time on your part."
        
    else:
        
        jump train_returned_3
        
label train_returned_3:

    "You found yourself in a comfortable, spacious cabin, with two benches, overhead storage, and a small view."
    
    "What's more, you were the first person to get on.  You stowed your meagre luggage and relaxed in one of the empty benches."
    
    "In no time at all, you settled into your place and started drifting into a light sleep..."
    
    "After a few minutes of peace, you felt the train start shuffling off to its destination, and let yourself return to your familiar dreamscape."
    
    scene bg flying mountains
    with fade
    
    "In no time, you are returned to your airborne refuge.  You feel the wind in your face, the thrill of dancing on the edge of death."
    
    "It's been your refuge from the division and anger that has seemed to start to dominate life all around you recently."
    
    "Every day, the papers announce a new civil war, assassination or uprising in countries you hadn't even heard of."
    
    "In nearly every shop and cafe, all anyone can ever talk about is syndicalism, whether that be in admiration or terror."
    
    if stoic:
        
        "You'd never really cared for politics, but it was creeping into your life, like a shadow creeping across the peaceful mountainside."
        
        jump sabine_meeting
        
    if sought_authority:
        
        "You'd defered to your father's judgements and opinions for most of your life, but with his increasing absence, you found yourself feeling like a sheperd stranded on a mountainside before a rain."
        
        jump sabine_meeting
        
    if confronted_authority:
        
        "You'd always fought with your father about his seeming refusal to take a firm stance, and recent years had only aggravated the rift between the two of you."
        
        jump sabine_meeting
        
    else:
        
        jump sabine_meeting
        
label sabine_meeting:

    scene bg train cabin
    with vpunch
    
    "You are awoken from your peaceful slumber by a shuffling by the overhead cabinets and a crash of a piece of luggage in front of you."
    
    "You groggily open your eyes, searching for the source of the disturbance."
    
    if stoic:
        
        jump sabine_meeting1
        
    else:
        
        mc "Ugh.  What was that?"
        
label sabine_meeting1:
    
    "A small young woman clutches a fallen suitcase, staring at you, like a deer in headlights."
    
    "Her pink, curly hair scatters around her head, and she holds in her other hand a pair of glasses onto her face."
    
    show socdem pleased at truecenter
    
    sd "I'm sorry that I woke you."
   
return
