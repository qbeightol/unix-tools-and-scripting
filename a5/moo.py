#! /usr/bin/python
#  moo.py

import random, re, socket, SocketServer, sys

# constants/definitions #######################################################

digits = '123456789'
size = 4

# helper functions #############################################################
# create one for parsing valid secrets/input (make sure to use this in arg.
# parsing and in the bulls and cows implementation)

# checks whether a string contains 4 unqiue digits
# re-factored implementation from Rosetta Code
def valid_secret(candidate):
    correct_size = len(candidate) == size
    only_digits  = all(char in digits for char in candidate)
    all_unique   = len(set(candidate)) == size
    
    return correct_size and only_digits and all_unique

# Classes ######################################################################
class WinException(Exception):
    pass

class MyUDPServer(SocketServer.UDPServer):
    def handle_error(self, request, client_address):
         raise WinException

    # we use timeouts to figure out which player should go first; on the first
    # iterations of our script loop, we create a brief window to handle requests
    # and if nothing comes in, we time out, and set my_turn to indicate that the
    # script should initiate communication with the other script.
    def handle_timeout(self):
        global my_turn
        my_turn = True
        return

class BCHandler(SocketServer.BaseRequestHandler):
    # note: the following variables are defined as the script executes:
    #   * secret
    #   * socket
    #   * opponent_address
    #   * guess_bank
    #   * progress

    # think about synchronizing guesses

    def handle(self):
        input_string = self.request[0]
        if input_string == "WIN":
            raise WinException
        elif valid_secret(input_string):
            global received_opponent_guess
            received_opponent_guess = True
            if input_string == secret:
                my_socket.sendto("WIN", opponent_address)
                raise WinException
            else:
                bulls = 0
                cows = 0
                for i in range(size):
                    if input_string[i] == secret[i]:
                        bulls += 1
                    elif input_string[i] in secret:
                        cows += 1
                my_socket.sendto("%iB%iC" % (bulls, cows), opponent_address)
        elif re.match(".B.C", input_string) and len(input_string) == 4:
            global received_bc_response
            received_bc_response = True
        else:
            print "received unrecognized input: " + input_sting
            raise WinException
        return



# script #######################################################################

# parse command line arguments

if len(sys.argv) != 4:
    sys.exit("moo.py expects a secret and two port numbers")

if not valid_secret(sys.argv[1]):
    sys.exit("moo.py expects a valid secret")

# use command line arguments to set-up global variables:
secret = sys.argv[1]
my_port = int(sys.argv[2])
opponent_port = int(sys.argv[3])
opponent_address = ("localhost", opponent_port)
# set-up global variables related to game progress:
two_digit_nums = [d1 + d2 for d1 in digits for d2 in digits]
four_digit_nums = [x + y for x in two_digit_nums for y in two_digit_nums]
valid_secrets = [s for s in four_digit_nums if valid_secret(s)]
guess_counter = 0
received_bc_response = False
received_opponent_guess = False
# set-up communication between scripts:
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = MyUDPServer(("localhost", my_port), BCHandler)
my_socket.sendto(valid_secrets[0], opponent_address)
server.serve_forever()

# play the game
while True:
    if received_bc_reponse and received_opponent_guess:
        my_guess = valid_secrets[guess_counter]
        my_socket.sendto(my_guess, oppoenent_address)
        received_bc_reponse = False
        received_opponent_guess = False
        guess_counter += 1
    else:
        server.handle_request()
