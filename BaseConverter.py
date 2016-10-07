#   Allen Bui X339Y958
#   
#   Python Project Spring 2015  - My project is a base number conversion
#
#       Libraries Needed: tkinter & sys
#

import sys
from tkinter import *


##################################################################
#                                                                #
#       Character Class contains the character objects           #
#                                                                #
##################################################################

class Characters:       # all operations and information about the characters that the user inputs will be held here
    
    def __init__(self):     
        self.characters = []    #list of characters to be displayed to the screen
        self.redo_char = []         #list of characters used as a stack to store characters everytime the user clicks the undo button
        self.convertFrom = 0    #integer number to keep track of what the user wants to convert FROM
        self.convertTo = 0          #integer number to keep track of what the user wants to convert TO
         
    def resetList(self):    # called on by the new function, which will flush out the stacks (lists).
        self.characters = []
        self.redo_char = []

    def resetConvertOptions(self):  #resets the conersion options 
        self.convertFrom = 0
        self.convertTo = 0

    def setTo(self, base):  # sets the convertTo variable once the radio button has been clicked
        self.convertTo = int(base)
                      
    def setFrom(self, base):     # sets the convertFrom variable once the radio button for it has been clicked
        self.convertFrom = int(base)
    
    def mutateCharacterLists(self, operation, digit):
        if (operation < 0): # push onto redo stack
            if(len(self.characters) > 0):
                temp = self.characters.pop()
                self.redo_char.append(temp)
        if (operation == 1): # pop 
            if (len(self.redo_char) > 0):
                temp = self.redo_char.pop()
                self.characters.append(temp)
        if(operation == 0): 
            if (len(self.redo_char)):
                self.redo_char = []         #if the uses the undo function and begins to enter text again, the redo stack will clear out
            self.characters.append(digit)
        return self.characters
   
    def convert(self, text): #this function does the final conversion and will display it to the textbox
        try:    # exception handling, if the string is invalid, then error will be thrown, and user will be asked to try again
            if(self.convertFrom == self.convertTo): #no conversion
                char_print = "".join(str(e) for e in self.characters)
                
            elif((int(self.convertFrom) == 1) & (int(self.convertTo) == 2)): #decimal to hex
                char_print = (hex((int("".join(str(e) for e in self.characters)))))
                
            elif((int(self.convertFrom) == 1) & (int(self.convertTo) == 3)): #decimal to binary
                char_print = (bin((int("".join(str(e) for e in self.characters)))))
                
            elif((int(self.convertFrom) == 1) & (int(self.convertTo) == 4)): #decimal to octal
                char_print = (oct((int("".join(str(e) for e in self.characters)))))
                
            elif((int(self.convertFrom) == 2) & (int(self.convertTo) == 1)): # hex to decimal
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(int(decimalString, 16)))
                
            elif((int(self.convertFrom) == 2) & (int(self.convertTo) == 3)): # hex to binary
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(bin(int(decimalString, 16))))
                
            elif((int(self.convertFrom) == 2) & (int(self.convertTo) == 4)): # hex to octal
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(oct(int(decimalString, 16))))
                
            elif((int(self.convertFrom) == 3) & (int(self.convertTo) == 1)): # binary to decimal
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(int(decimalString, 2)))
                
            elif((int(self.convertFrom) == 3) & (int(self.convertTo) == 2)): # binary to hex
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(hex(int(decimalString, 2))))
                
            elif((int(self.convertFrom) == 3) & (int(self.convertTo) == 4)): # binary to octal
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(oct(int(decimalString, 2))))
                
            elif((int(self.convertFrom) == 4) & (int(self.convertTo) == 1)): # octal to decimal
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(int(decimalString, 8)))
                
            elif((int(self.convertFrom) == 4) & (int(self.convertTo) == 2)): # octal to hex
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(hex(int(decimalString, 8))))
                
            elif((int(self.convertFrom) == 4) & (int(self.convertTo) == 3)): #octal to binary
                decimalString = "".join(str(e) for e in self.characters)
                char_print = (str(bin(int(decimalString, 8))))
            else:
                char_print = "ERROR:\nChoose a base to convert to"
                
            text.delete("1.0", END)                     #Display to the TextDisplay window
            text.insert(END, str(char_print))
            text.see(END)
        except (Exception):
            error = MessagePrompt("ERROR","Your input was invalid, please try again")
            error.interrupt()


############################################################
#                                                          #
#                  Message Prompt Class                    #
#                                                          #
############################################################
class MessagePrompt:

    def __init__(self, title, display):
        self.title = title
        self.display = display

    def interrupt(self):
        messagebox.showinfo(self.title, self.display)



#####################################################################
#                                                                   #
#   Window class creates and manages buttons, text display, etc.    #
#                                                                   #
#####################################################################
class Window:

    def __init__(self, title):
        self.root = Tk() #creating window and beginning loop
        self.title = title
        (self.root).title(title)

    def makeMainFrame(self, widthPass, heightPass):
        frame = Frame((self.root), width = widthPass, height = heightPass)      #create a frame in the window to place widgets
        frame.pack()
        return frame
    def makeTextBox(self, frame, border, heightPass, widthPass):
        textbox = Text(frame, bd = border, height = heightPass, width = widthPass)
        textbox.pack(side = TOP)
        return textbox

    def makeSubFrame(self):
        subFrame = Frame(self.root)
        subFrame.pack(side = TOP)
        return subFrame

    def makeMenu(self):
        menu = Menu((self.root))
        (self.root).config(menu=menu)
        return menu

    def makeSubMenu (self, menu):
        return Menu(menu)

    def addCascade(self, root, menu, labelPass, menuPass, label1, label2, subMenu, charClass, textDisplay, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, fromBin, fromHex, fromDec ,fromOct, toBin, toHex, toDec, toOct):
        menu.add_cascade(label = labelPass, menu = menuPass)
        if subMenu == "Menu":
            menuPass.add_command(label= label1, command = lambda : self.clear(charClass, textDisplay, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, fromBin, fromHex, fromDec ,fromOct, toBin, toHex, toDec, toOct, 99))
            menuPass.add_separator()
            menuPass.add_command(label = label2, command = lambda : self.closeWindow())
            
        if subMenu == "edit":
            menuPass.add_command(label= label1, command = self.redo(charClass, textDisplay, 1))
            menuPass.add_command(label= label2, command = self.undo(charClass, textDisplay, -1))
            
    def makeOneButton(self, frame, padxPass, bdPass, label, color, commandToCall, arg1, arg2):
        if(commandToCall == "0"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click0(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "1"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click1(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "2"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click2(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "3"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click3(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "4"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click4(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "5"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click5(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "6"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click6(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "7"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click7(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "8"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click8(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "9"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.click9(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "A"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickA(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "B"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickB(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "C"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickC(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "D"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickD(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "E"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickE(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)
        if(commandToCall == "F"):
            button = Button(frame, padx = padxPass, bd = bdPass, text = label, fg = color, command = self.clickF(arg1, arg2,0))
            button.config(state= DISABLED)
            button.pack(side = LEFT)            
        return button
    
    def closeWindow(self):
        self.root.destroy()      #close window

    ## defining what function needs to happen when we click a button ##
        ## callback will display the character the character class ##
              ## will push onto the character onto the stack##
    def click0(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 0)

    def click1(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 1)
    
    def click2(self, charClass,text, operation):
        return lambda : self.callback(charClass, text, operation, 2)
    
    def click3(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 3)
    
    def click4(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 4)
    
    def click5(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 5)
    
    def click6(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 6)
    
    def click7(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 7)
    
    def click8(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 8)
    
    def click9(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 9)
    
    def clickA(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 'A')
    
    def clickB(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, 'B')
    
    def clickC(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, "C")
    
    def clickD(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, "D")
    
    def clickE(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, "E")
    
    def clickF(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation, "F")
    
    def undo(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation)
    
    def redo(self, charClass, text, operation):
        return lambda : self.callback(charClass, text, operation)
    
    def conversion(self, charClass, text):
        return lambda: charClass.convert(text)
    
    def configureButtons(self, selection, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF):
        if(selection == '1'):               # 1 = decimal, so enable the decimal digits, disable the others
            button0.config(state= NORMAL)
            button1.config(state= NORMAL)
            button2.config(state= NORMAL)
            button3.config(state= NORMAL)
            button4.config(state= NORMAL)
            button5.config(state= NORMAL)
            button6.config(state= NORMAL)
            button7.config(state= NORMAL)
            button8.config(state= NORMAL)
            button9.config(state= NORMAL)
            buttonA.config(state= DISABLED)
            buttonB.config(state= DISABLED)
            buttonC.config(state= DISABLED)
            buttonD.config(state= DISABLED)
            buttonE.config(state= DISABLED)
            buttonF.config(state= DISABLED)
        if(selection == '2'):               # 2 = hex, so enable all buttons
            button0.config(state= NORMAL)
            button1.config(state= NORMAL)
            button2.config(state= NORMAL)
            button3.config(state= NORMAL)
            button4.config(state= NORMAL)
            button5.config(state= NORMAL)
            button6.config(state= NORMAL)
            button7.config(state= NORMAL)
            button8.config(state= NORMAL)
            button9.config(state= NORMAL)
            buttonA.config(state= NORMAL)
            buttonB.config(state= NORMAL)
            buttonC.config(state= NORMAL)
            buttonD.config(state= NORMAL)
            buttonE.config(state= NORMAL)
            buttonF.config(state= NORMAL)            
        if(selection == '3'):               # 3 = binary, so enable the binary digits, disable the others
            button0.config(state= NORMAL)
            button1.config(state= NORMAL)
            button2.config(state= DISABLED)
            button3.config(state= DISABLED)
            button4.config(state= DISABLED)
            button5.config(state= DISABLED)
            button6.config(state= DISABLED)
            button7.config(state= DISABLED)
            button8.config(state= DISABLED)
            button9.config(state= DISABLED)
            buttonA.config(state= DISABLED)
            buttonB.config(state= DISABLED)
            buttonC.config(state= DISABLED)
            buttonD.config(state= DISABLED)
            buttonE.config(state= DISABLED)
            buttonF.config(state= DISABLED)
        if(selection == '4'):               # 4 = octal, so enable the octal digits, disable the others
            button0.config(state= NORMAL)
            button1.config(state= NORMAL)
            button2.config(state= NORMAL)
            button3.config(state= NORMAL)
            button4.config(state= NORMAL)
            button5.config(state= NORMAL)
            button6.config(state= NORMAL)
            button7.config(state= NORMAL)
            button8.config(state= DISABLED)
            button9.config(state= DISABLED)
            buttonA.config(state= DISABLED)
            buttonB.config(state= DISABLED)
            buttonC.config(state= DISABLED)
            buttonD.config(state= DISABLED)
            buttonE.config(state= DISABLED)
            buttonF.config(state= DISABLED)
    
    def makeLabel(self, frame, toLabel, string):    # make a label and display it to the window #
        label = Label(frame, textvariable = toLabel, relief = RAISED)
        toLabel.set(string)
        label.pack()
        return label
    
    def callback(self, charClass, text, operation, digit = ""):   # callback is a function to display characters to the window #
        characters = charClass.mutateCharacterLists(operation, digit)
        char_print = "".join(str(e) for e in characters)
        text.delete("1.0", END)
        text.insert(END, char_print)
        text.see(END)



    # the clear function called on when the user clicks the "new" button from the cascading menu #
    def clear(self, charClass, text, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF,  fromBin, fromHex, fromDec ,fromOct, toBin, toHex, toDec, toOct, operation):
        button0.config(state = DISABLED)
        button1.config(state = DISABLED)
        button2.config(state = DISABLED)
        button3.config(state = DISABLED)
        button4.config(state = DISABLED)
        button5.config(state = DISABLED)
        button6.config(state = DISABLED)
        button7.config(state = DISABLED)
        button8.config(state = DISABLED)
        button9.config(state = DISABLED)
        buttonA.config(state = DISABLED)
        buttonB.config(state = DISABLED)
        buttonC.config(state = DISABLED)
        buttonD.config(state = DISABLED)
        buttonE.config(state = DISABLED)
        buttonF.config(state = DISABLED)
        fromBin.deselect()
        fromHex.deselect()
        fromDec.deselect()
        fromOct.deselect()
        toBin.deselect()
        toHex.deselect()
        toDec.deselect()
        toOct.deselect()
        charClass.resetList()
        charClass.resetConvertOptions()
        self.callback(charClass, text, operation)

    def packRadioButtonToWindow(self, button):
        button.pack(side = LEFT)   #packing the radiobuttons to the window
        
    def loop(self): #called by main to continue looping
        root.mainloop()
     

################################
#                              #
#      the main function       #
#                              #
################################
def main():
    
    root = Window("Converter") #creating window and beginning loop

    charClass = Characters()        #create a character object
        
    ##create an messagePrompt object and perform an interrupt##
    instructions = MessagePrompt("Instructions", "The following is a base number conversion program.\n\tstep 1) choose the base you wish to convert. \n\tstep 2) select the base you wish to convert to\n\tstep 3) Enter the number that you would like to conver\n\tstep 4) Click Convert!\n\tstep 5) select new do it again, or to start over.")
    instructions.interrupt()
    
    # 2 helper functions #
    def selTo():     #called on by "select to" radiobutton
        selection = str(toOption.get())     #returns the value of the radiobutton the user chose
        charClass.setTo(selection)              #assign the value of the radiobutton to know what to convert to

    def selFrom(): #called on by the "select from" radiobutton
        selection = str(fromOption.get())       #returns the value of the radiobutton the user chose
        charClass.setFrom(selection)                #assign the value of the radiobutton to know the base we are converting from
        root.configureButtons(selection, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF)

    #creating the shell of the program in the window#
    #all other frames will sit within this frame#
    width = 500
    height = 500
    frame = root.makeMainFrame(width, height)
        
    # create a text box #
    heightPass = 3
    widthPass = 25
    border = 18
    textDisplay = root.makeTextBox(frame, border, heightPass, widthPass)

    #create a frame for the radiobuttons #
    topframe = root.makeSubFrame()

    fromLabel = StringVar() # creating a label for the buttons to notify user what they are for
    labelString = "Select the base you are converting from"
    label = root.makeLabel(frame, fromLabel, labelString)
    fromOption = IntVar()    #creating the radiobuttons for converting from
    fromDec = Radiobutton(topframe, text = 'Decimal', variable = fromOption, value = 1, command = selFrom)
    fromHex = Radiobutton(topframe, text = 'Hexidecimal', variable = fromOption, value = 2, command = selFrom)
    fromBin = Radiobutton(topframe, text = 'Binary', variable = fromOption, value = 3, command = selFrom)
    fromOct = Radiobutton(topframe, text = 'Octal', variable = fromOption, value = 4, command = selFrom)
    root.packRadioButtonToWindow(fromDec)
    root.packRadioButtonToWindow(fromHex)
    root.packRadioButtonToWindow(fromBin)
    root.packRadioButtonToWindow(fromOct)

    frame00 = root.makeSubFrame()   #creating a frame for the 0 button, creating and packing the button as well
    padx = 22
    bd = 6
    label = "0"
    color = "black"
    commandToCall = "0"
    button0 = root.makeOneButton(frame00, padx, bd, label, color, commandToCall, charClass, textDisplay)
    
    frame0 = root.makeSubFrame()    #creating a frame for the buttons 1-3, creating and packing the buttons as well
    padx = 22
    bd = 6
    label = "1"
    color = "black"
    commandToCall = "1"
    button1 = root.makeOneButton(frame0, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "2"
    color = "black"
    commandToCall = "2"
    button2 = root.makeOneButton(frame0, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "3"
    color = "black"
    commandToCall = "3"
    button3 = root.makeOneButton(frame0, padx, bd, label, color, commandToCall, charClass, textDisplay)

    frame1 =  root.makeSubFrame()  #creating a frame for the buttons 4-6, creating and packing the buttons as well
    padx = 22
    bd = 6
    label = "4"
    color = "black"
    commandToCall = "4"
    button4 = root.makeOneButton(frame1, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "5"
    color = "black"
    commandToCall = "5"
    button5 = root.makeOneButton(frame1, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "6"
    color = "black"
    commandToCall = "6"
    button6 = root.makeOneButton(frame1, padx, bd, label, color, commandToCall, charClass, textDisplay)
    
    frame2 =  root.makeSubFrame()  #creating a frame for the buttons 7-9, creating and packing the buttons as well
    padx = 22
    bd = 6
    label = "7"
    color = "black"
    commandToCall = "7"
    button7 = root.makeOneButton(frame2, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "8"
    color = "black"
    commandToCall = "8"
    button8 = root.makeOneButton(frame2, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "9"
    color = "black"
    commandToCall = "9"
    button9 = root.makeOneButton(frame2, padx, bd, label, color, commandToCall, charClass, textDisplay)
    
    frame3 =  root.makeSubFrame()   #creating a frame for the buttons A-C, creating and packing the buttons as well
    padx = 22
    bd = 6
    label = "A"
    color = "black"
    commandToCall = "A"
    buttonA = root.makeOneButton(frame3, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "B"
    color = "black"
    commandToCall = "B"
    buttonB = root.makeOneButton(frame3, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "C"
    color = "black"
    commandToCall = "C"
    buttonC = root.makeOneButton(frame3, padx, bd, label, color, commandToCall, charClass, textDisplay)
    
    frame4 = root.makeSubFrame()   #creating a frame for the buttons D-F, creating and packing the buttons as well
    padx = 22
    bd = 6
    label = "D"
    color = "black"
    commandToCall = "D"
    buttonD = root.makeOneButton(frame4, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "E"
    color = "black"
    commandToCall = "E"
    buttonE = root.makeOneButton(frame4, padx, bd, label, color, commandToCall, charClass, textDisplay)
    padx = 22
    bd = 6
    label = "F"
    color = "black"
    commandToCall = "F"
    buttonF = root.makeOneButton(frame4, padx, bd, label, color, commandToCall, charClass, textDisplay)
       
    frame5 = root.makeSubFrame()  #creating a frame for the "select to" label, creating a label, and creating and packing the "select to" label and radiobuttons
    toLabel = StringVar()
    label = root.makeLabel(frame5, toLabel, "Select the base you are converting to")
    toOption = IntVar()
    toDec = Radiobutton(frame5, text = "Decimal", variable = toOption, value = 1, command = selTo)
    toHex = Radiobutton(frame5, text = "Hexidecimal", variable = toOption, value = 2, command = selTo)
    toBin = Radiobutton(frame5, text = "Binary", variable = toOption, value = 3, command = selTo)
    toOct = Radiobutton(frame5, text = "Octal", variable = toOption, value = 4, command = selTo)
    root.packRadioButtonToWindow(toDec)
    root.packRadioButtonToWindow(toHex)
    root.packRadioButtonToWindow(toBin)
    root.packRadioButtonToWindow(toOct)
    
    frame6 = root.makeSubFrame()   #creating the final frame for the conversion button, creating packing the button
    buttonConvert = Button(frame6, padx = 22, bg = "blue", height = 4, width = 20, bd = 10, text = "Convert!", fg = "white", command = root.conversion(charClass, textDisplay))
    buttonConvert.pack(side = LEFT)

    # Main Menu, which will contain the undo/redo, new, and exit functions the following segment of code will create and pack these #
    menu = root.makeMenu()
    subMenu = root.makeSubMenu(menu)
    label1 = "Menu"
    newCommand = root.addCascade(root, menu, label1, subMenu, "new", "exit", "Menu", charClass, textDisplay, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, fromBin, fromHex, fromDec ,fromOct, toBin, toHex, toDec, toOct)
    editMenu = root.makeSubMenu(menu)
    label2 = "Edit"
    root.addCascade(root, menu, label2, editMenu, "redo", "undo", "edit", charClass, textDisplay, button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, fromBin, fromHex, fromDec ,fromOct, toBin, toHex, toDec, toOct)

    root.loop
    
main()
