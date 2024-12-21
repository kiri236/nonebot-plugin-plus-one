from fastapi.params import Depends
from nonebot import get_plugin_config
from nonebot.plugin import on_message
from nonebot.rule import regex
from nonebot.adapters import Event, Message, Bot
from nonebot_plugin_session import extract_session, SessionIdType

from .config import Config
plugin_config = get_plugin_config(Config)
plus = on_message(rule=regex(""), priority=plugin_config.plus_one_priority, block=False)
msg_dict = {}
ignore_words = plugin_config.plus_one_ignore_words
wait_enabled = plugin_config.plus_one_is_wait
constThreshold = plugin_config.plus_one_threshold
Plus_Threshold = constThreshold-1
def is_equal(msg1: Message, msg2: Message)->bool:
    """判断消息是否相等"""
    if len(msg1) == len(msg2) == 1 and msg1[0].type == msg2[0].type == "image":
        if msg1[0].data.get("file_size") == msg2[0].data.get("file_size"):
            return True
    if msg1 == msg2:
        return True
    return False

def is_start(textlist:list, msg2: Message)->bool:
    """判断能否复读"""
    cnt = 0
    for i in reversed(textlist):
        if is_equal(msg2,i):
            cnt = cnt+1
        else:
            break
    return cnt>=Plus_Threshold

def doubled():
    global Plus_Threshold
    Plus_Threshold = max(Plus_Threshold,constThreshold)*2

def go_back():
    global Plus_Threshold
    Plus_Threshold = constThreshold-1

def check_word(message:Message)->bool:
    is_text = all(seg.is_text() for seg in message)
    if not is_text:
        return False
    elif message.__str__() in ignore_words:
        return True


@plus.handle()
async def plush_handler(bot: Bot, event: Event):
    global msg_dict

    session = extract_session(bot, event)
    group_id = session.get_id(SessionIdType.GROUP).split("_")[-1]
    if group_id not in plugin_config.plus_one_white_list:
        return
    if group_id != '793044971':
        return
    # 获取群聊记录
    text_list = msg_dict.get(group_id, None)
    if not text_list:
        text_list = []
        msg_dict[group_id] = text_list

    # 获取当前信息
    msg = event.get_message()
    if check_word(msg):
        return
    try:
        if not is_start(text_list,msg):
            if  len(text_list)<1 or is_equal(text_list[-1],msg):
                text_list.append(msg)
            else:
                go_back()
                text_list = [msg]
            msg_dict[group_id] = text_list
        else :
            if len(text_list) >= Plus_Threshold:
                text_list = [msg]
                msg_dict[group_id] = text_list
                if wait_enabled:
                    doubled()
                await plus.send(msg)
    except IndexError:
        pass