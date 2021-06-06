import sys
sys.path.append("..\\")
from config import Config
def filter_cmd(filter,client,message):
    trig = message.text[0]
    from_id = message.from_user.id
    cmd = message.text.split()[0][1:]           # .hell blah
    ret_bool = False

    if from_id == Config.USER_ID and trig == Config.TRIGGER:
        if cmd in Config.CMDS :
            ret_bool = True
    elif from_id in Config.SUDO_USERS and trig == Config.SUDO_TRIGGER:
        if cmd in Config.SUDO_COMMANDS:
            ret_bool = True
            
    return ret_bool
