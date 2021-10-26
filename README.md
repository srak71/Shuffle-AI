# Artificial Intelligence For Music Shuffle Optimization
# Mood Association and Cognitive Response in Individuals to Auditory Stimulation

## |Saransh Rakshak|Georgiana Estrada|Aayush Sutaria|Brain Heo|Yichen Ma|

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
or whatever came to the subjects mind. 

The experiment saw that when the subject was asked to 
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
            
## C) Data Collection

My data heap was composed of the following data points; each column corresponds to a different 
type of data point (i.e. type of music, duration of music, user or random selected, common correlating 
mood associated with the type of music, etc.), and each row is an instance/subsection of that individual's 
listening cycle for an individual iteration of a song (as song can be played multiple times if criteria met
in each instance, however cannot be repeated - our current song cannot equal the next song, but possibly 
can be somewhere else in Queue). 
    
        Data was collected via Kaggle, and all credit for the data goes to :


# Constructing The Neural Network

## A) Converting Raw Data

My AI model will correlate mood associated with input sound determined by a series of following embedded modules:

                ~~~~~~~~~~~~~~Module 1: Queue~~~~~~~~~~~~~~

                    Module with a collection of valid songs that match the user's cognitive state, 
                queued with the most significant and highest certainty at the head of the 
                playlist stack, in location song.next_song and queue_songs[1].  

                ~~~~~~~~~~~~~~Module 2: User~~~~~~~~~~~~~~

                    Use of adapted machine learning algorithms to analyze if the current song 
                matches user   preferences, or if the song is skipped or user selected. If 
                the song satisfies conditions by meeting thresholds determined by our weights 
                and biases(i.e. user.valid_mood == TRUE), our module pushes the song to our 
                Queue Module (1) as a valid song to be played, else the song is dumped (skipped). 

                ~~~~~~~~~~~~~~Module 3: Song~~~~~~~~~~~~~~

                    Our deepest embedded module, used in the analysis of the current song user is
                listening to. 

## B) Variables & Functions 

        ~~~~~~~~~~~~~~Global Variables and Functions~~~~~~~~~~~~~~
        
        (global) song : Our current playing song.
        
        (global) queue_songs : Our queued playlist that we will be building using our 
        AI model. Value at the 0 index is our current song, and value at index 1 is our 
        next song to play.
        
        (global) deck_songs : Unqueued deck of all available songs that we can play.
        
        (global) user : The current individual user listening to music.
        
        ~~~~~~~~~~~~~~Module 3: Variables and Functions~~~~~~~~~~~~~~
        
        song.cur : The current song being played.
        
        song.nxt_sng : The next song in our queue. 
        
        song.is_usr_selected : A boolean, True if current song is user selected/user cued.
        
        song.is_skipped : A boolean, True if user decides to skip current song, False if 
        user listens to more than 70% of the song. A True (skip) would mean the user does 
        not like the current playing song.
        
        song.len_sng : The length, in SECONDS, of the cur song.
        
        song.type_sng : The predicted genre for the current song.
        
        ~~~~~~~Lyric Analysis~~~~~~~
	
        song.nltk_lyrics : Use of natural language API to analyze lyrics of song.cur, 
        only if  the song contains lyrics, gives a value = [happy OR sad  OR neutral OR
        Null if song.cur does not contain any lyrics]. 
        
        ~~~~~~~Threshold Check~~~~~~~
        
        song.mood_thresh : The threshold needed to be reached to associate a song with a 
        certain mood.
        
        song.pred_mood() : Use of historical data and machine learning to determine moods
        commonly associated with type of cur song. Function returns a predicted mood for 
        associated current song.
        
        song.cert_mood() : Function that returns our certainty (0<=C<=1) that the associated 
        mood for cur song is correct.
        
        song.valid_mood() : Returns a boolean True if song.mood_thresh reached, else False.
        
        song.edit_thresh(int bias) : Overwrites the value of our song’s mood threshold, determined 
        by int bias, by adding specified bias to our original threshold. Stores the value in 
        song.mood_thresh. No return value.
        
        ~~~~~~~~~~~~~~Module 2: Variables and Functions~~~~~~~~~~~~~~
        
        user.mood_thresh : The threshold needed to be reached by the module to allocate the 
        user to a certain mood. 
        
        user.pred_mood() : Our prediction of the cur user’s mood, determined by previous 
        played song asserting song.is_usr_selected == True (i.e. we want to learn the users
        preference of songs to determine their mood, so we will only use songs the user 
        actively selected as they are most representative of the user’s internal mood and
        will give negative scores to songs/moods associated with songs where 
        song.is_skipped == True).
        
        user.cert_mood() : Returns our certainty (0<=C<=1) that the user’s predicted 
        mood is correct.
        
        user.valid_mood() : Returns a boolean True if user.mood_thresh reached, else 
        False (i.e. we are uncertain of users mood). 
        
        user.edit_thresh(int bias) : Overwrites the value of our user’s mood threshold 
        by adding specified bias to our original threshold. Stores the value in 
        user.mood_thresh. Returns a new threshold value.
        
        ~~~~~~~~~~~~~~Module 1: Variables and Functions~~~~~~~~~~~~~~
        
        song.playlist_songs : Our queued deck of all available songs where 
        
        song.pred_mood() == user.pred_mood() AND 
        
        user.cert_mood() >= user.mood_thresh AND
        
        song.cert_mood() >=  song.mood_thresh
        
        Resulting playlist preserved in global queue_songs.




## C) Variable Allocation Visual

# TODO: LINK PHOTO FOR VARS ALLOCATION GRAPH

## D) Edge Weights 
# TODO : FINISH MODULE 2, 3

To see a detailed description of individual edge weight allocation, please refer to the Jupyter Notebook linked above.

        ~~~~~~~~~~~~~~ Module 3 ←→ Module 2 ~~~~~~~~~~~~~~

        Note: Secure nodal interaction. 
        /master can edit both modules but cannot edit global instance variables. 

        	Assigned admin(s) can edit respective modules, but admin cannot edit global 
        variables corresponding to unauthorized modules. For instance, Module 2 access 
        cannot give permission to edit Module 3 global instance variables nor run its 
        functions.

        ~~~~~~~~~~~~~~ Module 2 ←→ Module 1 ~~~~~~~~~~~~~~

        Note: Secure nodal interaction. 
        /master can edit both modules but cannot edit global instance variables. 

        	Assigned admin(s) can edit respective modules, but admin cannot edit global 
        variables corresponding to unauthorized modules. For instance, Module 2 access 
        cannot give permission to edit Module 1 global instance variables nor run its functions.

        ~~~~~~~~~~~~~~   Module 1 ←→ Global   ~~~~~~~~~~~~~~

        Note: Secure nodal interaction. 
	 	/master alone cannot edit global, and any individual admin only has 
	 access to edit a subsection of global variables that pertains to its
	 corresponding module.

        song → playlist_songs
            Assert song.pred_mood() == user.pred_mood()
        
            Ensure that the song's predicted mood is the same as our predicted 
        mood for the user.

            Assert user.cert_mood() >= user.mood_thresh
        
            Verify that we have a reasonable assumption for our user's mood.

            Assert song.cert_mood() >=  song.mood_thresh
        
            Verify that we have a reasonable assumption for our song’s mood.

            Calculate any bias errors and incorporate them into the song threshold
        with our function song.edit_thresh().

        queue_songs → playlist_songs
        
            Calculate any bias errors and incorporate them into the user threshold 
        with our function user.edit_thresh().

            Calculate any bias errors and incorporate them into the song threshold
        with our function song.edit_thresh().

            Incorporating new bias, populate queue_songs with song.playlist_songs
	    
        deck_songs → playlist_songs
	
            Unqueued deck of all songs. 

            Convert songs with lyrics to .wav
        Generate lyrics from .wav file with Natural Language Tools Kit (nltk)’s
        google audio to text, save as plain text file. 

            Produce sentiment score for corresponding song using analyze_text(text_file)
        and SentimentIntensityAnalyzer().polarity_score(text_file) (provided by nltk)
        user → playlist_songs.
        
            Generate a finalized song with song.playlist_songs and save into global 
        queue_songs.



## E) Activation Threshold & Bias

To see a detailed description of individual module layer activation threshold,
and associated decision tree (trie) with incorporated bias, please refer to 
the Python files linked above.
                
        ~~~~~~~~~~~~~~ Module 3 Song: Threshold and Bias ~~~~~~~~~~~~~~

        ~~~~~~~~~~~~~~ Module 2 User: Threshold and Bias ~~~~~~~~~~~~~~

        ~~~~~~~~~~~~~~ Module 1 Queue: Threshold and Bias ~~~~~~~~~~~~~~

# IV: Machine Learning

## A) Threshold Modification 
        
In order to ensure maximum listening time, our model/queue must adapt to changes in the users
preferences. This can be done by lowering or raising thresholds required to send a song from 
our 3rd, song-checking Module up to our 2nd, user-checking Module; and also by changing the 
threshold required to send our checked user mood and checked song from Module 2 to overwrite
our optimal queue building Module 1, if required. 
        
## B) Training Model

We will be using Sentiment Analysis on individual users' song preferences, and determining
what we predict their mood might be. We will use this information to play songs that match 
the mood of the individual, engaging the individual more and therefore likely increasing the
amount of time spent listening to music. 
        
# TODO
## C) Error Correcting Code


## D) Security

The following security measures were taken to mitigate vulnerabilities of the AI system from attackers.
        
        🔰 Use of a memory safe language: python v3.10.0.
        
        🔰 Separation of Responsibility
        
            ☢️  Individual Admins only have access to subsections of module collection (aside from /master).
            
            ☢️  No one admin aside from /master can edit all three modules, but can read all modules.
            
            ☢️  /master does not have access to run program or change global instances without a second admin 
             	authorization.
            
            ☢️  No one admin can edit or view all global instances or edit and run all three modules. 
            
            ☢️  /master solely cannot edit non-module subsections (any of global), but /master can edit and 
            	read all three modules by itself.
            
        🔰 Stack Canaries and ASLR
          
            ☢️  Native in nltk and numpy libraries. 


# TODO
# V. Conclusion

## A) Model Results

## B) Interpreting Results

# VI. Moving Forward

## A) Future Optimization

Possible optimizations include incorporating pulse rate and perspiration data to 
scan for elevated heart rates or any other signs of excitement or inhibition. This is 
possible via a smartwatch or other sensors placed on the skin.

Future optimizations could also include subdermal implants, however this may be 
impractical unless it was already done for other reasons anyways. One possible current
use for subdermal audio and mood influence may be to inject subdermal audio emitters for
animals in captivity and in zoos, or for the ease of capture-and-release sample collection.
Animals are already regularly microchipped in both cases. Often, animals have a 
different auditory perception frequency range, optimized individually for each animal.
Subdermal speakers could be used to play a sound to sooth the animal, and can serve as
an alternative to tranquilizer darts or deadly action like in the incident of the killing 
of Harambe in 2016 at the Cincinnati Zoo. 


# VII. Referenced Sources

        Foster, David; Hearing and the Vestibular System; Psychology 110: Introduction to 
        Biological Psychology; UC Berkeley, 2021. 

        Coan, James A.; Allen, John J.B.: Handbook of Emotion Elicitation and Assessment; 
        Oxford University Press, USA; April, 19, 2007; 

        Stratton, Valerie N.; Zalanowski, Annette H.: Psychology of Music: Volume 19 Issue 2, 
        page(s): 121-127; The Pennsylvania State University: Altoona Campus, 3000 Ivyside Park, 
        Altoona, PA 16601, USA; October 1, 1991.

	    Wagner, David; Weaver, Nicholas; Ada Popa, Raluca; Computer Security; 
        UC Berkeley, Updated 2021.






