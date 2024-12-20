
<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/cubstaryow/nonebot-plugin-authrespond/blob/master/.github/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
</div>

<div align="center">

<h1 align="center">🐣🐤一个仅有40行代码的复读姬 ✨</h1>
<p align="center">
_✨ 只是一个复读姬：支持群聊白名单、文本复读、图片表情复读、甚至是转发和分享的复读 ✨_
</p>
<p align="center">
  <a href="https://raw.githubusercontent.com/cscs181/QQ-Github-Bot/master/LICENSE">
    <img src="https://img.shields.io/github/license/cscs181/QQ-Github-Bot.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-analysis-bilibili">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-analysis-bilibili.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>


## 💿快速安装

第一步：右上角 ↗ 点个不要钱的 star 吧，这是不断维护更新的动力。

### nb-cli

```shell
nb plugin install nonebot-plugin-plus-one
```
### pip

```shell
pip install nonebot-plugin-plus-one
```
## ⚙️可配置项

|配置项|必填|类型|默认值|说明|示例|
|------|---|---|------|---|----|
|PLUS_ONE_PRIORITY|否|int|1|插件响应优先级|PLUS_ONE_PRIORITY = 1|
|PLUS_ONE_WHITE_LIST|是|list[str]|[]|群聊或私聊白名单，单个或多个示例，可填入群 QQ 号或个人 QQ 号|PLUS_ONE_WHITE_LIST = ["10000000"] <br> PLUS_ONE_WHITE_LIST = ["10000000", "1000000"]
|PLUS_ONE_THRESHOLD|否|int|5|当同一句话重复多少次后开始复读|PLUS_ONE_THRESHOLD=4|
|PLUS_ONE_IGNORE_WORDS|否|list[str]|[]|不复读的文字|PLUS_ONE_IGNORE_WORDS=["1","2"]|
|PLUS_ONE_IS_WAIT|否|bool|true|复读后是否一段时间内不复读|PLUS_ONE_IS_WAIT=true|
### git

```shell
cd /your-nonebot-project-home/plugins/
git clone https://github.com/yejue/nonebot-plugin-plus-one.git
```

## 🎉 使用
```text
[群1]: 你好
[群1]: 你好
[机器人]: 你好

[群2]: 表情
[群2]: 表情
[机器人]: 表情

[群2]: 分享音乐
[群2]: 分享音乐
[机器人]: 分享音乐
```

