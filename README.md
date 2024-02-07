## YUZU

YUZU is a custom assembly language for our quantum machine. It takes the custom source file and turns it into binary instructions that are to be interpreted by an arduino or rpi or smth idfk. These then tell lasers how to shoot photons at particles. YUZU is designed to give lots of solutions to the same problems, a langauge that is a lot like minecraft. Minecraft, unlike the real world, does not have limiting factors such as gravity and physics, which is ironic coming from the manual for a quantum computer script. But YUZU is meant to be very VERY versatile in programming making way for many different styles and syntaxes. A "free world" if you will.

#### How it Works
For an ion trap based quantum computer to exploint valence electrons for their quantum properties, they need to be exposed to photons emitted at a certain frequency for a certain duration of time. This can be handled quite well by using several lasers connected to a microcontroller that is interpreting instructions. Starting with the steps that YUZU does from the beginning:

1. Read the assembly file, and parse it into different sections and instructions. With the way that the assembly code is defined, there are some global switches and parameters such as the number of qbits used by the file. These are interpreted seprately, and then sent to the microcontroller for intepretation.
2. Next is to take each of the instructions and convert them into a series of durations and frequencies that will perform the quantum operation that we want. 
3. Take these durations and frequencies and turn them into binary instructions that can be interpreted by the microcontroller.
4. The microcontroller should then handle everything from here, turning on and emitting the lasers as specified. While we don't want to perform all of the quantum calculations by hand, and then input all of these into a signal generator, it is significantly easier to just write a script, such as YUZU that handles all of this for us. 



#### PARTS:
Lexer ```yzu.parse()```
Takes the provided yuzu source file and turns into a dictionary with each label being the key and the values are an array of instruction

## MANUAL:

#### GLOBALS
YUZU can be broken down into several parts. The first of these parts is the global switches and variables, which at the time of writing is only one parameter. These can be thought of as variables in an experiment that are being tested, such as rotation thetas, and different frequencies that are being stored for later, or tested during runtime.
SYNTAX: ```qbits %num%``` where ```%num%``` is an integer of the number of qbits wanted. This can also be used at ```%NAME% %value%``` which is the name and the value of the parameter. Imma just call these globals because it sounds cool.

#### LABELS/SECTIONS
