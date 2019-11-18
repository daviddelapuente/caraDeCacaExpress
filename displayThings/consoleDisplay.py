import os
def clearscreen2():
    pass

def clearscreen(numlines=100):
  """Clear the console.
numlines is an optional argument used only as a fall-back.
"""
# Thanks to Steven D'Aprano, http://www.velocityreviews.com/forums

  if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')
  else:
    # Fallback for other operating systems.
    print('\n' * numlines)

#this check what you wrote is sintactic valid
def filterJugadaSintaxis(jugadas):
    if len(jugadas)==1:
        if jugadas[0].isdigit() or jugadas[0]=="draw":
            return True
        return False
    elif len(jugadas)==2:
        if jugadas[0].isdigit() and jugadas[1].isdigit():
            return True
        return False
    return False