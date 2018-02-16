label openingstart:
    $ affection_sabine = 0
    "As my train slowly lumbers out of the Zurich railway station, I find myself reflecting on the last few months of my life."
    "Just a month ago, I was in class, with all my friends, preparing for Christmas break."  
    "In fact, in early December, I hadn't much thought about the state of my plans." 
    "I had just assumed that I would be back in January after examinations to finish the year with my friends."  

    "However, after the December labour riots, my father pulled me out of school, and that was that."
    "I remember having heard mutterings from my father and occasionally from teachers about protests, but until that week, it hadn't touched Zurich."
    "It had been a hard year for everyone, I knew, but to me, Black Monday was only just a news headline."  
    "My father still had his job, an administrative official in one office or another, and I'd seen the lines outside the grocer's, but there was always food on my plate."

    "My father clearly saw things differently.  Over a tense Christmas eve dinner, he informed me that he was moving me to another school."  
    "It wasn't so much a discussion as it was a statement of fact."  
    "An international school for the well off and well-connected."
    "The International School of Geneva."  
    "It was for safety, my father said.  Far from the riots and the tension of the capital..." 

    "I pick up the newspaper I bought at the trainstation and absentmindedly turn it over."
    "MacArthur:'Troops will keep the anarchists in line in St.Louis'"
    "Communards support syndicalist protestors in Romandy, demand a referendum."  
    "Edward V denounces Union naval war games in the North Atlantic. 'An open provocation.'"  
    "I place it back on the bench beside me."

    "At least I have the cabin to myself."
    "At the station, I had had to push past a railway workers' picket to enter the station, and the silence except for the low thrum of the moving train is comforting."
    "As I look out the window, my thoughts drift back to home."
    "Mother and Ela hadn't liked the idea, of course."  
    "Ela begged to be taken with me, but to no avail."
    "Father didn't say it, but I could tell that he could only afford to keep one of us out of the city, and Ela is easier to protect."
    "Mother demanded I write every week, and demanded to know of every minor inconvenience against which she could lodge a complaint."

    "The train rumbles as it passes over a bridge."
    "\"It would only be for the rest of the summer,\" my father had said, \"until all the tensions in the city dissipate.\"" 
    "I stare out the window at the alpine countryside."  

    "In the distance, I spot a bird seemingly trailing our lone convoy."
    "I imagine it looking down at all the struggles down here, on the ground, and wondering:"
    "\"Why make things difficult?  Things are clear at this height.\""
    "That is, if birds could make philosophical statements."
    "The bird trails off, seemingly content that this train isn't one huge prey."  
    "The skyline clears and I drift off into sleep..."

    "The train's horn wakes me up."
    "My watch tells me it's three o'clock in the afternoon."  
    "I grab my luggage and hurry into the throng of humanity pushing out of the train, leaving my newspaper on the seat."
    "From the train, we're deposited in the station, an even larger mess of people moving to catch trains in one direction or another."  
    "I manage to step away from the crowd and onto the street, where I see another herd of people attempting to hail taxis."
    "As I push through the crowd, the line of cabs thins one by one."
    "Even more passengers of the trains flood out onto the street and fan out, looking for transportation or walking away."
    "I decide to sit back on a bench looking over the cars for a moment."
    "By the time I look down to my watch and back up, the crowd has dispersed and a small line of coaches and cabs is all that remains."

    "How strange."
    "Perhaps they all were figments of my imagination."

    "I study the line of cabs, and I notice one of the cabbies stands beside his vehicle, holding a sign: \"International School of Geneva.\""
    "I look through my pockets for my invitation to the school."  
    "A little worse for wear, but still legible."  
    "I take the invitation and present it forward to the cabby."
    "He stares at it in silence for a few seconds."
    "Then, he looks up at me.  Then back down to the paper."
    "He shrugs his shoulders and lets out a sigh."  
    "I see him walk back around the car."
    "As I walk to the back, in order to place my luggage in the trunk, I hear someone running up."

    "???" "Hey, wait!"

    "A panicked girl's voice."
    "I manage to turn around before being run into."
    "Suddenly, I get a very close look at the sidewalk."
    "I hear a flurry of apologies in heavily accented French."
    "Her shiny white shoes, dirty with the street grime, plant themselves in front of my face."
    "The apologies continue in a torrent.  I push myself back to my feet before I drown myself."
    "Apparently, those soiled white shoes belong to a small young woman."
    "She has...pink hair?  I didn't know it grew like that."  
    "She pushes large glasses up her freckled nose and tries to pick up my bags and hand them back to me." 
    "I hear the torrent of words out of her mouth, but I can't quite pick out the words."
    "She notices my confusion and switches to German."
    
    sd "Hello?  Are you alright?"
    "The young woman wears a rose in the left pocket of her pink vest.  Her pink pigtails fall over her shoulders-"
    sd "Did you fall harder than I thought?"  
    "She shakes my shoulder.  I didn't realize I was staring."
    mc "Sorry, a bit shaken up."
    "I make sure to look back up at her and put on a smile."  
    mc "In a hurry for something?"
    "She laughs and holds up my invitation.  It must have drifted in the fall."  
    sd "I noticed you getting in the cab.  You're going to the International School of Geneva, right?"
    "When I nod, she offers me the paper back."
    sd "Me too.  Sabine Deckert."
    "She extends her hand."  
        
    menu:
        
        "What should I do?"
        
        "Take it":
            $ affection_sabine += 5
            "I take her hand and shake it firmly.  She giggles."
            sd "This is where you introduce yourself too."
            mc "My name is [player]."
            jump opening_cont
            
        "Don't.":
            $ affection_sabine += 0
            "I look at her hand and then back to her.  She quickly pulls her hand back."  
            sd "Not much for introductions, eh?"  
            "I shrug."
            jump labeling_cont

label opening_cont:
    
    mc "You're a student too?"
    "She gives me a grin."
    sd "Of course.  I didn't see any of the other cabbies with their signs out.  We must be some of the last ones to arrive."
    sd "Would you mind sharing the cab ride?"
    "You look back to the line of taxis behind you and shrug."
    mc "I can't see why not."
    sd "Perfect!"

    "A couple minutes later"

    "The taxi glides out of the city."
return
