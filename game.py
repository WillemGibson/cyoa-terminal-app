import sys
import time
import random
from os import system
from colorama import Fore

print(Fore.LIGHTGREEN_EX) # Setting text color to light green

# Creating typing effect in terminal
def typing(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.03, 0.011, 0.008, 0.007, 0.007,
          0.007, 0.06, 0.006, 0.05, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)

# Defining all outcome variables
def control_room():
    typing("While looking around the Control Room you notice the entrance adorned with flickering emergency lights that intermittently reveal the vast array of control panels and holographic displays within. The air is thick with a metallic taste, and the hum of the dormant machinery seems to intensify.\n")
    cr_choice = input("Do you 'access main computer' or 'investigate control pannels': ")

    if cr_choice == "access main computer":
        system('clear')
        typing("Approaching the activated holographic display, you observe that the evacuation map remains visible, presumably depicting events that transpired in this location. Upon scrutinizing the layout, you discover that the station encompasses an extensive network of maintenance tunnels. Intrigued, you decide to delve into further investigation.")
        time.sleep(5)
        system('clear')
        tunnels()
                
    elif cr_choice == "investigate control pannels":
        system('clear')
        typing("You feel drawn to the numerous control panels around you. Among them, you spot a metallic plaque with the word 'Power' inscribed on it. When you flip the switch, a surge of static heat courses through your hand, causing you to recoil. Examining your now injured hand, you discover that it's scorched. Recognizing the need for medical attention, you gather yourself and stand up to explore the station in search of a medical bay.")
        time.sleep(5)
        system('clear')
        medical_bay()
    else:
        typing("Please choose a valid option")
        system('clear')
        control_room()

def living_quarters():
    # Display the living quarters introductino
    typing("As you navigate through the corridors, you come across a sealed door labeled 'Living Quarters.' The entrance panel flickers hesitantly before reluctantly sliding open, revealing a scene frozen in time. The living quarters, once filled with life, now echo with an eerie stillness.\n")
    typing("The living quarters consist of neatly organized sleeping pods, each with a small personal workstation. The soft glow of the emergency lights barely illuminates the area, casting long shadows across the room. As you sift through the personal belongings left behind, you discover handwritten notes, personal logs, and audio recordings.\n")
    # Get user's choice
    lq_choice = input("Do you 'examine the personal logs' or 'search for supplies': ")

    # Dis play their choice and decide where to direct user after choice, redo if input is invalid
    if lq_choice == "search for personal logs":
        system('clear')
        typing("These artifacts provide glimpses into the lives of the station's former inhabitants, their dreams, aspirations, and the events leading up to the mysterious abandonment. Some logs hint at internal conflicts, while others express excitement about groundbreaking discoveries. While perusing one of the logs, you notice a recurring phrase that captures your attention: 'the specimen' is repeated incessantly throughout the text.\n")
        typing("Shortly after making this discovery, a wave of nausea engulfs you, making it difficult to maintain your equilibrium. There must be a medical bay around here somewhere...")
        time.sleep(5)
        system('clear')
        medical_bay()
    elif lq_choice == "search for supplies":
        system('clear')
        typing("The living quarters also serve as a storage area for essential supplies. Crates of food, medical kits, and tools are scattered throughout the room. However, the unsettling quietude is occasionally interrupted by strange sounds emanating from the darkness.\n")
        typing("While scouring for provisions, a faint creaking resonates from the corridors behind you. Upon pivoting, a piercing screech assaults your ears, and then...")
        time.sleep(5)
        system('clear')
        death()
    else:
        typing("Please choose a valid option")
        system('clear')
        living_quarters()

def medical_bay():
    typing("Upon entering the Medical Bay, you find a sterile environment filled with abandoned medical equipment. The soft hum of dormant machinery and the faint glow of emergency lighting give the room an otherworldly ambiance. The Medical Bay, once a place of healing, now seems frozen in time.\n")
    typing("You hurriedly search for the necessary machinery to address your medical emergency. Once you've successfully treated your condition, you catch sight of a research and development lab out of the corner of your eye. As you turn your head, you spot a sizable white apparatus featuring a subdued display – undoubtedly the primary diagnostic tool in the medical setting. \n")
    mb_choice = input("Do you 'seek medical supplies' or 'activate the medical system': ")

    if mb_choice == "seek medical supplies":
        system('clear')
        typing("As you rummage through the neatly organized cabinets, you discover a cache of medical supplies. Bandages, medications, and diagnostic tools are scattered across the shelves. Amidst the supplies, you find personal effects—photographs, trinkets, and handwritten notes. These relics offer glimpses into the lives of those who once called this station home. You might stumble upon medical records that hint at the nature of a mysterious illness or injury that plagued the station's occupants.")
        time.sleep(5)
        system('clear')
        research_lab()
    elif mb_choice == "check for signs of life":
        system('clear')
        typing("You decide to interface with the station's advanced medical systems. As the scanners activate, a holographic display materializes, showing the station's vital statistics and the health status of its former inhabitants. Strange anomalies and irregularities appear on the screen, raising more questions than answers.\n")
        typing("Upon a swift glance at the screen, it takes only a fraction of a second before a crimson alert floods the main display, accompanied by a piercing alarm. Clutching your ears, you swiftly redirect your attention to the screen, where the urgent message reads, 'EVACUATE NOW: SPECIMEN FREE, PLEASE EXIT THROUGH THE MAINTENANCE TUNNELS TO THE ESCAPE POD.'\n")
        typing("In that very moment, as if anticipating the chaos, you witness the creature forcefully emerging from one of the expansive test tubes. The creature towers at a minimum of 8 feet, hunched over, its silver form exuding an almost slimy texture. Details escape you as you pivot and dash out of the entrance in which you just came.\n")
        typing("Swiftly seeking refuge, you urgently locate a concealed spot, remaining silent until the unsettling sounds of the creature fade away. Once the coast is clear, you rise to your feet and make your way toward the previously mentioned maintenance tunnels.")
        time.sleep(5)
        system('clear')
        tunnels()
    else:
        typing("Please choose a valid option")
        system('clear')
        medical_bay()

def research_lab():
    typing("As you step into the Research Labs, the air feels different, charged with an unsettling energy. The sterile, metallic surroundings give way to a labyrinth of interconnected chambers filled with experimental equipment, holographic displays, and the remnants of scientific endeavors.\n")
    rl_choice = input("Do you 'investigate experimental equipment' or 'return to medical bay': ")

    if rl_choice == "investigate experimental equipment":
        system('clear')
        typing("Navigating through the maze of advanced machinery, you come across holographic projections displaying complex equations and charts. Some of the equipment seems to be in a state of disarray, while others hum with an otherworldly energy. Your attention is drawn to a spherical object, prompting you to casually retrieve it. As you do so, a faint beep resonates, triggering the activation of the device... BOOM!")
        time.sleep(5)
        system('clear')
        death()
    elif rl_choice == "return to medical bay":
        system('clear')
        typing("Cautiously, you decide to bypass the Research Labs, sensing an underlying danger within the uncharted territories of scientific experimentation. While this choice reduces immediate risks, it also means missing out on potential discoveries that could have provided vital clues to the station's mysterious past or offered solutions to challenges ahead. You return to the medical bay.")
        time.sleep(3)
        system('clear')
        medical_bay()
    else:
        typing("Please choose a valid option")
        system('clear')
        research_lab()

def tunnels():
    typing("You head into the labyrinth of maintenance tunnels. The flickering lights cast eerie shadows, creating an atmosphere of suspense and anticipation. The decision to explore these dark passages could unveil hidden secrets or pose unforeseen dangers.\n")
    t_choice = input("Do you 'explore the maintenance tunnels' or 'continue exploring the station': ")

    if t_choice == "explore the maintenance tunnels":
        system('clear')
        typing("Taking a deep breath, you resolve to explore the maintenance tunnels. The slender corridors wind and bend, sporadically lit by the faint glow of malfunctioning overhead lights. During your journey, you stumble upon neglected storage rooms filled with discarded equipment and supplies.\n")
        typing("Continuing onward, you encounter entry points to areas that were off-limits and sealed off during the evacuation. Upon opening these doors, a spacious bay of compartments is revealed, once designed to accommodate escape pods. However, only three pods remain. You hastily approach the nearest one, only to find it battered.")
        time.sleep(5)
        system('clear')
        escape_pod()
    elif t_choice == "continue exploring the station":
        system('clear')
        typing("Wary of the hidden dangers within the shadows, you decide to avoid the maintenance tunnels and instead take the safer paths along the main corridors during your exploration. As you resume your journey, a faint noise persists just a few meters behind you. When you glance back, the corridor stretches endlessly into darkness. When you turn your head forward again, the immense creature comes into view. It turned out to be the final sight etched in your memory... ")
        time.sleep(5)
        system('clear')
        death()
    else:
        typing("Please choose a valid option")
        system('clear')
        system('clear')
        tunnels()

def escape_pod():
    typing("The air in the makeshift repair bay is tense with anticipation as you stand before the battered escape pod. Its hull bears the scars of cosmic debris, and internal systems flicker with erratic lights. Time is of the essence, and the urgency to leave the desolate space station intensifies.\n")
    ep_choice = input("Do you 'attempt to repair the pod' or 'improvise a makeshift solution': ")

    if ep_choice == "attempt to repair the pod":
        system('clear')
        typing("You gather your knowledge from the exploration of the station's various sections. you meticulously start repairing the damaged components of the escape pod.\n")
        typing("Despite lacking self-confidence in your abilities, you manage to bring it to life. As the display illuminates, prompting you to chart a course, you step inside. After inputting the route, you press the prominent 'launch' button. With a significant shift in weight, you embark on a journey into the expansive cosmos, heading back home.")
        time.sleep(5)
        system('clear')
        end()
    elif ep_choice == "improvise a makeshift solution":
        system('clear')
        typing("Lacking the necessary resources or opting for a quicker solution, you decide to improvise a makeshift fix. Despite recognizing the risks, you entertain the idea of launching yourself into space with just a spacesuit, which is a terrible idea... **// oh sorry, im just the narrators I can't have opinions appareantly. //** As you approach the suit, you observe a slight crack in the helmetz, **// YET YOU STILL PROCEED //** After what seems like an eternity struggling to put on the suit, you prepare the airlock at the rear of the escape pod bay. One door seals shut, the chamber pressurises, and the other door opens. You are expelled from the chamber, and almost immediately, an intense pressure builds up behind your eyes. Your condition deteriorates rapidly until... BANG!")
        time.sleep(5)
        system('clear')
        death()
    else:
        typing("Please choose a valid option")
        system('clear')
        escape_pod()

def death():
    print("=======================")
    print("*       *             *")
    print("   *             *\n")
    print("-----------------------")
    print("     // You Died //    ")
    print("-----------------------")
    print("*      *           *"      )
    print("   *           *      *\n ")
    print("=======================")
    time.sleep(5)
    system('clear')

def end():
    print("=======================")
    print("*       *             *")
    print("   *             *\n")
    print("-----------------------")
    print("  Thanks For Playing!  ")
    print("-----------------------")
    print("*      *           *"      )
    print("   *           *      *\n ")
    print("=======================")
    time.sleep(5)
    system('clear')

# Defining the introduction function and assigning the story intro to print
def start():
    # print("It Worked!") # Testing
    typing("The distant hum of malfunctioning machinery echoes through the cold, desolate corridors of the abandoned space station. As you gradually regain consciousness, the dim emergency lights flicker, revealing the remnants of what was once a bustling hub of cosmic exploration. The metallic creaks and distant hisses underscore the eerie silence that now pervades the station.\n")
    typing("Your surroundings appear foreign, a surreal dance of shadows cast by the dormant equipment that once served the station's inhabitants. Through the transparent walls, the vastness of space stretches out, dotted with stars like distant memories of a life once lived.\n")
    typing("As you take in your surroundings, the weightlessness of microgravity envelops you, a constant reminder of the station's isolation in the cosmic void. Equipment, now eerily still, suggests an abrupt evacuation or a catastrophic event that led to the abandonment of this once thriving outpost.\n")
    typing("The control panel in front of you blinks sporadically, its pale glow revealing cryptic symbols and unfamiliar controls. A holographic display flickers, attempting to convey an urgent message that fades in and out of coherence. A single word stands out: 'Escape!.'\n")
    typing("Your journey begins here, a lone soul amidst the forgotten echoes of a cosmic mystery. The station's secrets await discovery, and the choices you make will unveil the untold story of its demise and determine your own fate in the cold expanse of the cosmos. The only certainty is that something lingers in the shadows, waiting to be uncovered.\n")
    time.sleep(5)
    choice = input("Do you want to investigate the 'control room' or explore the 'living quarters': ")

    if choice == "control room":
        system('clear')
        control_room()
    elif choice == "living quarters":
        system('clear')
        living_quarters()
    else:
        typing("Please choose a valid option")
        system('clear')
        start()

# while True: # Making sure you only go back to the second choice after a invalid option
#     cr2_choice = input("Will you 'enter the maintenance tunnels' or 'proceed to the medical bay': ")

#     if cr2_choice == "enter the maintenance tunnels":
#         system('clear')
#         tunnels()
#     elif cr2_choice == "proceed to medical bay":
#         system('clear')
#         medical_bay()
#     else:
#         typing("Please choose a valid option")
#         system('clear')