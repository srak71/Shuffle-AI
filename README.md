# Artificial Intelligence For Music Shuffle Optimization
# Mood Association and Cognitive Response in Individuals to Auditory Stimulation

    | Saransh Rakshak | Georgiana Estrada | Aayush Sutaria | Brain Heo | Yichen Ma |

    Completed for Cognitive Science C100, Basic Issues In Cognition,

    Taught by Dr.Davina Chen, Fall 2021, UC Berkeley.

# I. Background & Biological Processes

            Music is a part of our lives daily. Our goal is to develop a method- using artificial 
        intelligence, data analytics, and training models- in which we are able to track 
        individual listening habits, correlate moods associated with certain types or genres of music,
        and create an optimal playlist, filled with either songs or low volume ambient-type music, 
        which corresponds to that individual’s mood. In this manner, we hope to increase user 
        listening time by increasing the individual’s ‘connectedness’ with the music and 
        enticing them to listen to more and more songs. 
        
 ## A) Auditory Stimulation
 
            Our stimulus, sound, propagates through space by compressing and expanding air molecules,
        sending them outwards from the source in all directions in the form of a pressure wave. 
        This pressure wave is perceived by the auditory system as a sound wave, and can be broken 
        down into two functioning variables: loudness and pitch.
        
            Volume can be determined from the amplitude of the stimuli sound wave, or how much change
        in Y occurs given a range X (wavelength), while pitch is derived to be the frequency of the 
        sound wave, or the length of X to complete one cycle (or wavelength). Pitch is measured in 
        Hertz (Hz), and limitations in the human auditory system allows us to perceive sounds in 
        the 1000-5000 Hz range with relatively greater sensitivity (other animals’ auditory systems 
        may have different restrictions or sensitivity ranges, thus some animals may have much greater 
        hearing and easily can perceive sounds humans cannot). We can hear this range at a greater 
        frequency due to the structure of the pinna (outer ear), which is shaped to amplify this 
        1000-5000Hz range and muffle sounds outside.
        
## B) Anatomy of the Ear

            Past the pinna, we reach the middle ear, consisting of three small bones (ossicles), 
        called the malleus (hammer), incus (anvil), and stapes (stirrup). The ossicles act as 
        an amplifier to small mechanical vibrations of air molecules, and sensitivity of the ossicles 
        can be changed by contracting muscles in the ear to filter out unwanted sounds (for instance, 
        contracting when loud noise prevents damage). 
        
            Further down in the ear, we reach the cochlea, made up of a coil of three parallel canals- 
        the vestibular canal, middle canal, and tympanic canal- all which branch to the vestibulocochlear
        nerve (VIII). Sound vibrations of the oval window cause a wave to pass through the vestibular canal, 
        and travel back down the tympanic canal. At the base of the tympanic canal lies a small moveable 
        membrane (the basilar membrane) , which allows the movement of non-compressible fluid within
        the canal. This basilar membrane is approximately 5 times wider at the apex than at the base
        (even though the cochlea grows narrower towards the apex), thus higher frequencies cause maximum
        displacement of fluid near the base, while lower frequencies cause the greatest displacement 
        at the apex. The cochlea then works to translate this temporal signal in the basilar membrane
        into a spatial signal. 
## C) Mechanics of the Ear

            Auditory neurons in all levels of the auditory system display tonotopic organization- 
        they are spatially arranged in a corresponding map to the frequencies which they respond 
        to. Both ears have two rows of sensory cells, a row of approximately 3500 inner hair 
        cells(IHC), and three rows of approximately 4000 outer hair cells(OHC). 
        
            Each IHC is associated with around 18 to 20 different sensory auditory nerve 
        fibers, responsible for the perception of sound, as well as some motor fibers for the inhibition of 
        some sound stimuli. Meanwhile, OHC have very few sensory fibers, rather, stimulation of OHC motor 
        fibers cause OHC’s to change in length, thereby stiffening or relaxing the basilar membrane and fine 
        tuning particular sound frequencies as needed. 
            
            Each hair cell produces small hairs, stereocilia, and their heights progressively increase 
       across the hair cell. As the basilar membrane moves from the sound wave, the stereocilia move
       as well. Each of these stereocilia are connected to a potassium ion (K+) channel, by a tip link,
       which is essentially a small fiber. As the hair cell moves, the tip link pulls open the K+ channel,
       causing depolarization and the opening of calcium (Ca2+) channels at the base of the cell, fusing 
       vesicles to the membrane and releasing neurotransmitters stimulating the corresponding nerve fiber. 

# II: Cognition & Auditory Processing

## A) Psychological States (Moods)

            An experiment in the late 1980’s conducted by Valerie N. Stratton and Annette H. Zalanowski 
        monitored the effects that pleasant, depressing and no music had on subjects while they were 
        viewing a piece of art. Subjects, while viewing the art and listening to a certain type of 
        background music (or no music), were then asked to create either a happy story, a sad story, 
        or whatever came to the subjects mind. The experiment saw that when the subject was asked to 
        create a neutral story (i.e. whatever came to mind), music would determine the mood change. 
        So, if the person was asked to tell a neutral story while being surrounded by sad background
        music, the subject’s story would be sad to reflect the room. However, the Stratton-Zalanowski
        experiment also saw that when the subjects were asked to create an expletively sad story or 
        happy story- then the type of music that surrounded them did not alter the motif of the story
        told by the subject. As a result, the experiment proved that “mood responses to music are 
        indeterminate and depend on cognitive processes”-  an assumption that we will incorporate
        in our model. (Stratton 122)

## B) Cognitive Response

            Seibert and Ellis, in 1991, developed a technique for testing and conducting research on 
        mood-congruent cognition- in other words, the relation that people conduct their behavior, 
        interpret, acquire, and store information to memory. Additionally, the Seibert-Ellis experiment
        expanded on the Stratton-Zalanowski experiment, as they were able to show that the induction of
        happy or sad moods provided poorer recall(memory) than a neutral mood. 
        
             Additionally, we will be referencing data established in the development of the MCI Technique
        (also known as the continuous-music technique), a subsection of tracks used in the original MCI
        Technique is shown in Table 8.3. (Coan 129)

            While the original purpose of MCI was to alter mood by a certain song, we will be using it’s
        reverse: seeing the qualities of a certain song determined by the subject’s behavior and listening
        pattern, and subsequently determining the subject's mood. Additionally, we will be seeing data 
        collected from previous MCI Technique studies to ensure that the user continues listening to music
        for as long as possible - i.e. the user can still function in an optimal state in congruence with 
        music, else if the music is too hindering to their current psychological state, they would likely 
        stop the music from continuing playing. Results from these previous MCI studies are shown in Table
        8.2 above. (Coan 128)

            Results for various prior MCI studies are summarized in Table 8.4. (Coan 130) 
