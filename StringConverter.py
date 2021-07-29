# StringConverter-CLI
# Copyright New-Dev0 (2021)
# https://github.com/New-dev0/StringConverter-Cli

import os
import sys
from strings import *
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import ApiIdInvalidError
from colorama import Fore
from configs import Var
from conversion import tele_to_pyro


def printcolored(color, text, end="\n"):
    return print(color + text + Fore.RESET, end=end)


def convert_to_pyro(TELE, api_id, api_hash):
    C = tele_to_pyro(TELE, api_id=api_id, api_hash=api_hash)
    printcolored(Fore.CYAN, CON_P)
    printcolored(Fore.GREEN, C)
    print("")
    print("--> Thanks for Using me ;)")


def main():
    printcolored(Fore.YELLOW, HEADER, end="")
    printcolored(Fore.YELLOW, "-" * 75)
    print("\n")
    CH_API = Var.API_ID
    CH_HASH = Var.API_HASH
    if not (CH_API and CH_HASH):
        printcolored(Fore.GREEN, ENT_ID, end="")
        _IDE = input(": ")
        try:
            CH_API = int(_IDE)
        except ValueError:
            printcolored(Fore.RED, "ERROR : Not a Valid INPUT")
            return
        printcolored(Fore.GREEN, ENT_HASH, end="")
        CH_HASH = input(": ")
        printcolored(Fore.CYAN, SV_ENV, end="")
        _In = input("\n---->> ")
        try:
            if int(_In) == 1:
                with open(".env", "w") as f:
                    f.write("API_ID=" + str(CH_API) + "\n")
                    f.write("API_HASH=" + CH_HASH)
            else:
                print("Skipped !\n")
        except ValueError:
            print("Skipped !\n")
    printcolored(Fore.GREEN, Q2_QUES, end="")
    printcolored(Fore.BLUE, Q2_OPT)
    _EN = input("---->> ")
    try:
        _EN_NUM = int(_EN)
    except ValueError:
        printcolored(Fore.RED, "ERROR: NOT A VALID INPUT")
        return main()
    if _EN_NUM == 1:
        en = printcolored(Fore.BLUE, EN_TE)
        STRI = input("---->> ")
        try:
            return convert_to_pyro(STRI, CH_API, CH_HASH)
        except ApiIdInvalidError:
            printcolored(Fore.RED, API_INV)
            if os.path.exits(".env"):
                os.remove(".env")
            main()
        except Exception as Ex:
            return printcolored(Fore.RED, str(Ex))
    elif _EN_NUM == 2:
        try:
            with TelegramClient(
                StringSession(), api_id=CH_API, api_hash=CH_HASH
            ) as Client:
                TELE_STRI = Client.session.save()
                printcolored(Fore.YELLOW, "GeNeRatinG StriNG SeSSIoNs...")
                printcolored(Fore.BLUE, "-> Telethon StringSession")
                printcolored(Fore.WHITE, TELE_STRI, end="\n\n")
                return convert_to_pyro(TELE_STRI, CH_API, CH_HASH)
        except Exception as Ex:
            return printcolored(Fore.RED, str(Ex))
    else:
        printcolored(Fore.GREEN, "Successfuly Exited....")
        return


def startup(args):
    if len(args) > 1:
        if args[1] in ["-c"]:
            try:
                SESSION = args[2]
                if Var.API_ID and Var.API_HASH:
                    return print(
                        tele_to_pyro(SESSION, api_id=Var.API_ID, api_hash=Var.API_HASH)
                    )
                else:
                    return print(tele_to_pyro(SESSION))
            except IndexError:
                print("Please Provide StringSession too")
        else:
            print(USAGE)
    else:
        main()


if __name__ == "__main__":
    startup(sys.argv)
