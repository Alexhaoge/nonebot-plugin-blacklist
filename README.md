<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://raw.githubusercontent.com/tkgs0/nbpt/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-blacklist

_✨ NoneBot 黑名单插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/tkgs0/nonebot-plugin-blacklist.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-blacklist">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-blacklist.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</a>
<a href="https://github.com/Mrs4s/go-cqhttp">
    <img src="https://img.shields.io/badge/gocq-1.1.0-blueviolet.svg" alt="go-cqhttp">
</a>

</div>

  
## 📖 介绍
  
基于 [A-kirami](https://github.com/A-kirami) 大佬的 [黑白名单](https://github.com/A-kirami/nonebot-plugin-namelist) 插件 魔改(?)的仅黑名单插件  
  
超级用户不受黑名单影响  
  
## 💿 安装

**nb-cli安装, 包管理器安装  二选一**

<details>
<summary>使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-blacklist

</details>

<details>
<summary>使用包管理器安装</summary>

在 nonebot2 项目的插件目录下, 打开命令行,

**根据你使用的包管理器, 输入相应的安装命令**

<details>
<summary>pip</summary>

    pip install nonebot-plugin-blacklist

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-blacklist

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-blacklist

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-blacklist

</details>

打开 bot项目下的 `pyproject.toml` 文件,

在其 `plugins` 里加入 `nonebot_plugin_blacklist`

    plugins = ["nonebot_plugin_blacklist"]

</details>
</details>

## 🎉 使用
  
拉黑:
```
拉黑用户 qq qq1 qq2
拉黑群 qq qq1 qq2
拉黑私聊 qq qq1 qq2
拉黑所有群
拉黑所有好友

私聊静默/私聊禁用/静默私聊/禁用私聊
```

解禁:
```
解禁用户 qq qq1 qq2
解禁群 qq qq1 qq2
解禁私聊 qq qq1 qq2
解禁所有群
解禁所有好友

私聊响应/私聊启用/响应私聊/启用私聊
```

查看黑名单:
```
查看用户黑名单
查看群聊黑名单
查看私聊黑名单

重置黑名单          # 重置当前Bot帐号对应的黑名单
重置所有黑名单      # 清空黑名单数据库
```

被禁言自动屏蔽该群:
```
自觉静默开
自觉静默关
```

群内发送 **`/静默`**, **`/响应`** 可快捷拉黑/解禁当前群聊  
  
`拉黑/解禁所有` 只对已添加的群/好友生效
  
注: **本插件目前仅支持 nonebot2 + go-cqhttp 的使用方式, 一切非此二者结合的使用方式造成的问题请自行探索解决, 或者使用其他插件**
