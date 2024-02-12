## YUZU

YUZU is a custom assembly language for our quantum machine. It takes the custom source file and turns it into binary instructions that are to be interpreted by an arduino or rpi or smth idfk. These then tell lasers how to shoot photons at particles. YUZU is designed to give lots of solutions to the same problems, a langauge that is a lot like minecraft. Minecraft, unlike the real world, does not have limiting factors such as gravity and physics, which is ironic coming from the manual for a quantum computer script. But YUZU is meant to be very VERY versatile in programming making way for many different styles and syntaxes. A "free world" if you will.

#### How it Works
For an ion trap based quantum computer to exploit valence electrons for their quantum properties, they need to be exposed to photons emitted at a certain frequency for a certain duration of time. This can be handled quite well by using several lasers connected to a microcontroller that is interpreting instructions. Starting with the steps that YUZU does from the beginning:

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
Here is the actual meat meat and matter of a YUZU script program. The labels determine the actualy order and placement of different gates acting on different qbits. While you can create as many different sections as you like, there are only a few major or most important sections: ```.init```,  ```.gates```,  ```.entanglement```,  ```.measurement```. Each of these sections corresponds to different parts of quantum computing and operation. Note the '.' before each of the labels. This is just a simpler way of differentating labels and sections from everything else, whether it be globals and whatnot.

***examples***: 

*.init*
```
.init:
  0 1 | initialize the first qbits to state 1.
  1 0
  2 0
  3 1
  4 0
  5 1
  6 1
```

Here, the first line tells the assembler that we are setting up the initialization states for the quantum bits. The first is the qbits specifier, and the second is the initialization state.

*.gates*
```
.gates:
  h 1 | Apply Hadamard gate to the second qbit in row
  x 0
  rx 0 θ | theta value can be stored in the value storage
```

Gates is used to apply single qbit gates onto specific qbits. No idea how to implement syntax for the rotation gates so imma use a placeholder here.

*.entanglement*
```
.entanglement:
  cx 1 1
  ch 0 2
  
```

*Value Storage*

Value storage is the memory, lexing, compiling optimization that also gives the programmer more readabiliy and freedom in developing programs in YUZU. Here, the user is able to store data, and parameters, as well as thetas for different rotations. The keeping of YUZU tends to be in the same order as normal.

*Gate optomization*

Under each label lies the delerations of all of the different gates that are going to be used in the program. YUZU likes to have all of the gates specified and the number of times they are. This can be done by simply using the same gate several times. This method, while very confusing sometimes, allows for tighter effiency and productivity loops, as the order of gates can simply be specifed in a single section, each gate correstponding to a single value. i might scrap this idea tho because nobody in their right mind is going to try to learn how to use this shit.

#### misc definition/clarifications
- comments in YUZU are indicated with '|'
- microcontroller is used to link programs to actual hardware actions, such candidates include RPI and Arduino