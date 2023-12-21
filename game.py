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
def initial_choice():
    pass

def control_room():
    typing("The Control Room looms ahead, its entrance adorned with flickering emergency lights that intermittently reveal the vast array of control panels and holographic displays within. As you step inside, the air is thick with a metallic taste, and the hum of the dormant machinery seems to intensify.\n")
    cr_choice = input("Do you 'access main computer' or 'investigate control pannels': ")

    if cr_choice == "access main computer":
        system('clear')
        typing("With a cautious approach, you decide to interface with the station's main computer. The holographic display springs to life, revealing logs, system status reports, and cryptic messages left by the previous inhabitants. The information may shed light on the events that led to the station's abandonment, potential hazards, or clues about where to find crucial resources.")
    elif cr_choice == "investigate control pannels":
        system('clear')
        typing("You choose to manually investigate the control panels scattered throughout the room. Some are flickering with life, while others remain unresponsive. Your goal is to restore power to essential systems, enabling further exploration and potentially uncovering hidden areas of the station.")
    else:
        typing("Please choose a valid option")
        system('clear')
        control_room()

def living_quarters():
    # Display the living quarters introductino
    typing("As you navigate through the corridors, you come across a sealed door labeled 'Living Quarters.' The entrance panel flickers hesitantly before reluctantly sliding open, revealing a scene frozen in time. The living quarters, once filled with life, now echo with an eerie stillness.\n")
    # Get user's choice
    lq_choice = input("Do you 'search for personal logs' or 'search for supplies': ")

    # Dis play their choice and decide where to direct user after choice, redo if input is invalid
    if lq_choice == "search for personal logs":
        system('clear')
        typing("The living quarters consist of neatly organized sleeping pods, each with a small personal workstation. The soft glow of the emergency lights barely illuminates the area, casting long shadows across the room. As you sift through the personal belongings left behind, you discover handwritten notes, personal logs, and audio recordings.\n")
        typing("These artifacts provide glimpses into the lives of the station's former inhabitants, their dreams, aspirations, and the events leading up to the mysterious abandonment. Some logs hint at internal conflicts, while others express excitement about groundbreaking discoveries. Unraveling these personal stories might offer clues about the station's fate and the motivations behind its sudden evacuation.")
    elif lq_choice == "search for supplies":
        system('clear')
        typing("The living quarters also serve as a storage area for essential supplies. Crates of food, medical kits, and tools are scattered throughout the room. However, the unsettling quietude is occasionally interrupted by strange sounds emanating from the darkness.\n")
        typing("As you search for supplies, you must decide whether to risk exploring further or to play it safe. The potential rewards include crucial resources that may aid in your survival, but there's a lurking sense of danger. Unsettling creaks and distant echoes suggest that you might not be alone in the living quarters.")
    else:
        typing("Please choose a valid option")
        system('clear')
        living_quarters()

def medical_bay():
    typing("Upon entering the Medical Bay, you find a sterile environment filled with abandoned medical equipment. The soft hum of dormant machinery and the faint glow of emergency lighting give the room an otherworldly ambiance. The Medical Bay, once a place of healing, now seems frozen in time.\n")
    mb_choice = input("Do you 'seek medical supplies' or 'check for signs of life': ")

    if mb_choice == "seek medical supplies":
        system('clear')
        typing("As you rummage through the neatly organized cabinets, you discover a cache of medical supplies. Bandages, medications, and diagnostic tools are scattered across the shelves. Amidst the supplies, you find personal effects—photographs, trinkets, and handwritten notes. These relics offer glimpses into the lives of those who once called this station home. You might stumble upon medical records that hint at the nature of a mysterious illness or injury that plagued the station's occupants.")
    elif mb_choice == "check for signs of life":
        system('clear')
        typing("You decide to interface with the station's advanced medical systems. As the scanners activate, a holographic display materializes, showing the station's vital statistics and the health status of its former inhabitants. Strange anomalies and irregularities appear on the screen, raising more questions than answers. You might uncover information about a contagion that led to the evacuation or a malfunction in the life support systems.")
    else:
        typing("Please choose a valid option")
        system('clear')
        medical_bay()

def research_lab():
    typing("As you step into the Research Labs, the air feels different, charged with an unsettling energy. The sterile, metallic surroundings give way to a labyrinth of interconnected chambers filled with experimental equipment, holographic displays, and the remnants of scientific endeavors.\n")
    rl_choice = input("Do you 'investigate experimental equipment' or 'avoid the lab': ")

    if rl_choice == "investigate experimental equipment":
        system('clear')
        typing("Navigating through the maze of advanced machinery, you come across holographic projections displaying complex equations and charts. Some of the equipment seems to be in a state of disarray, while others hum with an otherworldly energy. Choosing this option allows you to delve into the depths of the station's scientific experiments, potentially unlocking valuable information or unearthing technologies that could aid your survival. However, tinkering with experimental devices may also pose unforeseen risks, and the consequences of meddling with the unknown may linger long after you leave the labs.")
    elif rl_choice == "avoid the lab":
        system('clear')
        typing("Cautiously, you decide to bypass the Research Labs, sensing an underlying danger within the uncharted territories of scientific experimentation. While this choice reduces immediate risks, it also means missing out on potential discoveries that could have provided vital clues to the station's mysterious past or offered solutions to challenges ahead. The decision to play it safe may shield you from immediate threats, but it might limit your understanding of the events that transpired within these walls.")
    else:
        typing("Please choose a valid option")
        system('clear')
        research_lab()

def tunnels():
    typing("As you contemplate your next move, you notice a partially concealed entrance leading to a labyrinth of maintenance tunnels. The flickering emergency lights cast eerie shadows, creating an atmosphere of suspense and anticipation. The decision to explore these dark passages could unveil hidden secrets or pose unforeseen dangers.\n")
    t_choice = input("Do you 'traverse the dark tunnels' or 'avoid the tunnnels': ")

    if t_choice == "traverse the dark tunnels":
        system('clear')
        typing("With a deep breath, you decide to venture into the maintenance tunnels. The narrow passageways twist and turn, occasionally illuminated by the feeble glow of malfunctioning overhead lights. Along the way, you discover forgotten storage rooms containing abandoned equipment and supplies. Some items may prove valuable for survival, while others emit strange energy signatures, hinting at the station's mysterious experiments.\n")
        typing("As you progress, you come across access points to restricted areas that were sealed off during the evacuation. Opening these doors could reveal crucial information about the station's history, shedding light on the events that led to its current state. However, the tunnels aren't without peril, and you may encounter malfunctioning security systems or remnants of experiments gone awry.")
    elif t_choice == "avoid the tunnels":
        system('clear')
        typing("Concerned about the potential risks lurking in the darkness, you choose to bypass the maintenance tunnels, opting for safer routes through the main corridors. However, this decision limits your access to hidden areas and leaves behind valuable resources and clues that could impact the unfolding narrative.\n")
        typing("While avoiding the tunnels reduces immediate threats, it also limits your understanding of the station's intricate layout and the events that transpired. The main corridors may still hold dangers of their own, as automated systems malfunction and environmental hazards become apparent.")
    else:
        typing("Please choose a valid option")
        system('clear')
        tunnels()

def mystery_code():
    typing("As you explore the abandoned space station, you come across a series of strange symbols and cryptic messages etched onto the walls of certain sections. The symbols seem alien, as if they hold the key to understanding the events that unfolded here. It's a moment of eerie fascination, and you must decide whether to invest time in unraveling these enigmatic messages.\n")
    mc_choice = input("Do you 'investigate the messages' or 'ignore the messages': ")

    if mc_choice == "investigate the messages":
        system('clear')
        typing("Driven by curiosity or a sense of urgency, you choose to investigate the cryptic messages. You examine the symbols, take notes, and cross-reference them with any information you've gathered from the control room or personal logs. The process is time-consuming, but as you make progress, patterns start to emerge. The messages appear to be a combination of scientific notations, warnings, and pleas for help. Some even hint at the presence of an unknown entity or force aboard the station.")
    elif mc_choice == "ignore the messages":
        system('clear')
        typing("Opting to focus on the immediate goal of finding a way to escape, you decide to ignore the cryptic messages. The symbols remain a mystery as you prioritize survival and avoid the potential distractions that decoding them might bring. However, this choice might mean missing out on crucial information that could impact your understanding of the situation or affect your decisions later on.")
    else:
        typing("Please choose a valid option")
        system('clear')
        mystery_code()

def escape_pod():
    typing("The air in the makeshift repair bay is tense with anticipation as you stand before the battered escape pod. Its hull bears the scars of cosmic debris, and internal systems flicker with erratic lights. Time is of the essence, and the urgency to leave the desolate space station intensifies.\n")
    ep_choice = input("Do you 'attempt to repair the pod' or 'improvise a makeshift solution': ")

    if ep_choice == "attempt to repair the pod":
        system('clear')
        typing("You gather your knowledge from the exploration of the station's various sections. The technical manuals you discovered in the control room and the spare parts salvaged from the maintenance tunnels become your tools. With a focused determination, you meticulously start repairing the damaged components of the escape pod.\n")
        typing("Success in repairing the escape pod depends on the player's accumulated knowledge and the choices made throughout the game. If the player successfully repairs the pod, they may benefit from enhanced navigation and safety features during their escape. However, failure may result in critical malfunctions, endangering the escape attempt.")
    elif ep_choice == "improvise a makeshift solution":
        system('clear')
        typing("Lacking the necessary resources or opting for a faster approach, you decide to improvise a makeshift solution to get the escape pod operational. Using the experimental technology discovered in the research labs and the insights gained from deciphering cryptic messages, you cobble together a unique, jury-rigged system.")
    else:
        typing("Please choose a valid option")
        system('clear')
        escape_pod()

def end():
    pass

# Defining the introduction function and assigning the story intro to print
def start():
    # print("It Worked!") # Testing
    typing("The distant hum of malfunctioning machinery echoes through the cold, desolate corridors of the abandoned space station. As you gradually regain consciousness, the dim emergency lights flicker, revealing the remnants of what was once a bustling hub of cosmic exploration. The metallic creaks and distant hisses underscore the eerie silence that now pervades the station.\n")
    typing("Your surroundings appear foreign, a surreal dance of shadows cast by the dormant equipment that once served the station's inhabitants. Through the transparent walls, the vastness of space stretches out, dotted with stars like distant memories of a life once lived.\n")
    typing("As you take in your surroundings, the weightlessness of microgravity envelops you, a constant reminder of the station's isolation in the cosmic void. Equipment, now eerily still, suggests an abrupt evacuation or a catastrophic event that led to the abandonment of this once thriving outpost.\n")
    typing("The control panel in front of you blinks sporadically, its pale glow revealing cryptic symbols and unfamiliar controls. A holographic display flickers, attempting to convey an urgent message that fades in and out of coherence. A single word stands out: 'Survive.'\n")
    typing("Your journey begins here, a lone soul amidst the forgotten echoes of a cosmic mystery. The station's secrets await discovery, and the choices you make will unveil the untold story of its demise and determine your own fate in the cold expanse of the cosmos. The only certainty is that something lingers in the shadows, waiting to be uncovered.\n")
    typing("You seen the flickering light of a terminal admist the rumble of the room.\n")

escape_pod()