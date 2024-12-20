from pydantic import BaseModel, Field
from nonebot import get_plugin_config


class Config(BaseModel):
    """Plugin Config Here"""

    plus_one_priority: int = (Field(1, doc="plus_one 响应优先级"))
    plus_one_white_list: list = (Field([], doc="plus_one 白名单"))
    plus_one_threshold : int = (Field(5,doc="plus_one 重复多少次后复读"))
    plus_one_ignore_words:list[str]=(Field([],doc="忽略复读的词"))
    plus_one_is_wait:bool=(Field(True,doc="复读后如果有相同内容是否等待一段时间再复读"))


config = get_plugin_config(Config)
