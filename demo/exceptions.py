#!/bin/env python3

# This demo illustrates how to catch exceptions.
#
# This is a game where you travel to random locations to catch 10 different
# types of exceptions.  One of the exceptions is not in any location; you will
# need to do something different to make it appear.
#
# Currently the game is unbeatable because some exceptions are not caught.
# The exception handlers were written alphabetically.  Perhaps that was not the
# best way to organize them.
#
# There are 10 exceptions in the `pokedex`.  These are the ONLY exceptions that
# this program needs to catch!  The game shows the message "What am I supposed
# to do with..." when an unrecognized exception is caught.
#
# Fix the game by re-arranging and removing exception handlers such that only
# exceptions from the Pokedex can be caught.  Below is a region of code marked
# with comments.  THIS IS THE ONLY PART OF THE PROGRAM THAT SHOULD BE CHANGED.
#
# There is a diagram of Python's Exception hierarchy in
# instructions/Requirements.md.  You may also refer to this webpage:
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#
# The 'Exit' menu item is a joke; the real way to quit is to raise
# KeyboardInterrupt with Ctrl-C.


import datetime
import sys
import random


def red(s):
    return "\x1b[1;31m{}\x1b[0m".format(s)

def green(s):
    return "\x1b[1;32m{}\x1b[0m".format(s)

def yellow(s):
    return "\x1b[1;33m{}\x1b[0m".format(s)

def blue(s):
    return "\x1b[1;34m{}\x1b[0m".format(s)

def magenta(s):
    return "\x1b[1;35m{}\x1b[0m".format(s)

def logo():
    print(blue("""\
            _____     __  __
           / ___/__  / /_/ /____ _
          / (_ / _ \\/ __/ __/ _ `/
          \\___/\\___/\\__/\\__/\\_,_/
""") +

    yellow("""
    .d8888b.         888           888
   d88P  Y88b        888           888
   888    888        888           888
   888        8888b. 888888 .d8888b88888b.
   888           "88b888   d88P"   888 "88b
   888    888.d888888888   888     888  888
   Y88b  d88P888  888Y88b. Y88b.   888  888
    "Y8888P" "Y888888 "Y888 "Y8888P888  888
""") +
    blue("""\
           _  ____        ___   ______
          ( )/ __/_ _    / _ | / / / /
          |// _//  ' \\  / __ |/ / /_/
           /___/_/_/_/ /_/ |_/_/_(_)""")

)
    print(magenta("\nCatch each exception in as few moves as possible"))


def menu():
    areas = list(destinations.keys())
    checklist = list(pokedex)
    print()
    print(blue(f"{'Destinations':<15}"), yellow("Exceptions"))
    print(blue(f"{'=' * 12:<15}"), yellow(f"{'=' * 10}"))
    for i in range(len(areas)):
        name = areas[i]
        if destinations[name]['run']:
            print(red(f"\N{HEAVY CHECK MARK} {name:<14}"), end='')
        else:
            print(blue(f"\N{BALLOT BOX} {name:<14}"), end='')
        if i < len(checklist):
            if checklist[i] in pokeball:
                print(red(f"\N{HEAVY CHECK MARK}) {checklist[i]}"))
            else:
                print(yellow(f"{i}) {checklist[i]}"))
        else:
            print()


def catch(exception, err):
    print(err)
    if exception not in pokedex:
        print(red(f"What am I supposed to do with a {exception}"))
    elif exception not in pokeball:
        print(green(f"{exception} was caught!"))
        pokeball.add(exception)
    else:
        print(red(f"You already have a {exception}"))


def all_visited():
    return all(map(lambda o: destinations[o]['run'], destinations))


def progress():
    if moves == 1:
        return f"[{moves:2d} move ]"
    return f"[{moves:2d} moves]"


###########################################
##  These functions intentionally crash  ##
###########################################

def overflow_err():
    2e+34 ** 34

def zerodiv_err():
    2e+34 / 0.0

def attribute_err():
    datetime.derp

def import_err():
    import dne

def index_err():
    list()[0]

def key_err():
    dict()['This Key Is Not Present']

def name_err():
    vague

def filenotfound_err():
    open("")

def fileexists_err():
    open(sys.argv[0], 'x')

def directory_err():
    open(".")

def recursion_err():
    recursion_err()

def notimplemented_err():
    datetime.tzinfo().utcoffset(1)

def indentation_err():
    exec("    1+1")

def syntax_err():
    eval("if")

def eofd():
    raise EOFError(red("It's not as cool the second time :("))


commands = [
        { 'run': False, 'fn': attribute_err },
        { 'run': False, 'fn': directory_err },
        { 'run': False, 'fn': fileexists_err },
        { 'run': False, 'fn': filenotfound_err },
        { 'run': False, 'fn': import_err },
        { 'run': False, 'fn': indentation_err },
        { 'run': False, 'fn': index_err },
        { 'run': False, 'fn': key_err },
        { 'run': False, 'fn': name_err },
        { 'run': False, 'fn': notimplemented_err },
        { 'run': False, 'fn': overflow_err },
        { 'run': False, 'fn': recursion_err },
        { 'run': False, 'fn': syntax_err },
        { 'run': False, 'fn': zerodiv_err },
        ]
random.shuffle(commands)

alphabet = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf',
            'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November',
            'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform',
            'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
random.shuffle(alphabet)

destinations = {}
for opt in commands:
    destinations[alphabet.pop()] = opt
destinations['Exit'] = { 'run': False, 'fn': sys.exit }

pokedex = {
        ArithmeticError,
        EOFError,
        Exception,
        LookupError,
        ModuleNotFoundError,
        NameError,
        OSError,
        RuntimeError,
        SyntaxError,
        SystemExit,
       }
GOAL = len(pokedex)
pokeball = set()
caught = 0
moves = 0

logo()
while caught < GOAL:
    menu()
    if caught == GOAL - 1 and EOFError not in pokeball and all_visited():
        print(magenta("Psst... hey kid... try pressing Ctrl-D"))

    try:
        choice = input(blue(f"{progress()}") + " Where to? ").strip().capitalize()
        print()
        if not choice or choice not in destinations:
            print(red(f"You used {choice}\nIt's not very effective..."))
            continue
        destinations[choice]['run'] = True
        destinations[choice]['fn']()

##########################################################
##  The problem lies between here and the marker BELOW  ##
##########################################################

    except ArithmeticError as err:
        catch(ArithmeticError, err)

    except AssertionError as err:
        catch(AssertionError, err)

    except AttributeError as err:
        catch(AttributeError, err)

    except EOFError as err:
        if 'Eof' not in destinations:
            print(magenta("\n\nA wild EOFError appears!"))
            destinations['Eof'] = { 'run': True, 'fn': eofd }
        catch(EOFError, err)

    except Exception as err:
        catch(Exception, err)

    except FileExistsError as err:
        catch(FileExistsError, err)

    except ImportError as err:
        catch(ImportError, err)

    except IndentationError as err:
        catch(IndentationError, err)

    except IndexError as err:
        catch(IndexError, err)

    except IsADirectoryError as err:
        catch(IsADirectoryError, err)

    except KeyboardInterrupt:
        print(magenta("\n\nKeyboardInterrupt, I choose you!"))
        print(green("KeyboardInterrupt used SIGINT"))
        print(green("It's super effective!"))
        break

    except KeyError as err:
        catch(KeyError, err)

    except LookupError as err:
        catch(LookupError, err)

    except ModuleNotFoundError as err:
        catch(ModuleNotFoundError, err)

    except NameError as err:
        catch(NameError, err)

    except NotImplementedError as err:
        catch(NotImplementedError, err)

    except OSError as err:
        catch(OSError, err)

    except OverflowError as err:
        catch(OverflowError, err)

    except RecursionError as err:
        catch(RecursionError, err)

    except RuntimeError as err:
        catch(RuntimeError, err)

    except SyntaxError as err:
        catch(SyntaxError, err)

    except SystemExit as err:
        print("You can't exit this game so easily!")
        catch(SystemExit, err)

    except ZeroDivisionError as err:
        catch(ZeroDivisionError, err)

##########################################################
##  The problem lies between here and the marker ABOVE  ##
##########################################################

    finally:
        caught = len(pokeball)
        moves += 1


if caught == GOAL:
    menu()
    if moves < GOAL:
        print(red(f"You caught 'em all in {moves} moves?  CHEATER!"))
    elif moves == GOAL:
        print(green(f"You caught 'em all in {moves} moves!  Take a screenshot, this is the best ending."))
    elif moves <= GOAL * 1.2:
        print(blue(f"You caught 'em all in {moves} moves!  Not bad!"))
    elif moves < GOAL * 1.5:
        print(yellow(f"You caught 'em all in {moves} moves!  Nice!"))
    else:
        print(magenta(f"You caught 'em all in {moves} moves.  Try again for a better score."))
