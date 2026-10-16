# 客户端触发条件与限制 / Client triggers and limitations

[中文首页](../README.md) · [English README](../README.en.md)

核对日期 / Checked: **2026-10-16**. 本地 Windows 应用代码版本 / Local Windows application code: **26.1007.71326**, MSIX **26.1007.9446.0**.

## 中文

### 当前结论

本仓库是素材包，不是客户端功能扩展。图集包含九组动作与十六个注视方向，但素材齐全、通过上传校验，不等于原生桌宠会触发所有效果。

本机客户端的渲染代码可以使用全部行。普通系统鼠标的全局视线跟随未找到受支持的开关或 Pets 工具接口；不能靠多画十六张方向帧开启它。代码里存在 Computer Use 光标、部分输入框光标，以及其他宠物展示界面的交互入口；这些入口不等于原生浮窗会跟随普通桌面鼠标。

### 各动作如何触发

下表来自对本机安装代码的核对，**不是所有项目均已实机验证**。

| 素材 | 客户端中的触发条件 |
| --- | --- |
| 待机 `idle` | 无其他动作，或一次动作序列结束后。 |
| 左右移动 `running-left/right` | 拖动桌宠，水平移动达到阈值时；不是自动在桌面散步。 |
| 挥手 `waving` | 首次唤醒该宠物时的临时欢迎状态；客户端记录已欢迎过的宠物，不保证每次显示都触发。 |
| 上浮 `jumping` | 指针进入宠物区域时的悬停反应。 |
| 思考 `running` | 桌宠采纳的任务通知处于运行状态时。 |
| 等待 `waiting` | 桌宠采纳了需要输入、批准或决定的任务状态时。 |
| 失落 `failed` | 桌宠采纳了失败或阻塞状态时。 |
| 检查 `review` | 桌宠采纳了已完成、尚未阅读的结果状态时。 |
| 十六方向 | 需要客户端提供注视坐标；不保证普通桌面鼠标会产生这些坐标。 |

这里的 `running` 是工作状态，左右移动使用的是另外两个键。多个任务同时存在时，状态选择还受客户端的通知优先级影响。[官方 Pets 文档](https://learn.chatgpt.com/docs/pets)说明了运行、需要输入、完成未读和阻塞这四类工作状态。

### 为什么看起来大部分时间都在待机

- 浮动宠物组件默认让非待机动作播放三遍，再回到待机，即使对应任务仍在运行。它不会因此持续循环思考动作。
- 本机代码将待机帧时长放慢到素材预览基础时长的六倍，因此原生待机比仓库 GIF 更慢。
- 当前正在浏览的对话通常会被运行／完成状态过滤；等待输入和失败是例外。
- 用户实测将本对话切到后台后仍看到待机。因此，当前对话过滤不能单独解释本机表现，任务状态到浮窗的完整链路仍未验证成功。
- [官方文档](https://learn.chatgpt.com/docs/pets)还说明，操作系统启用减少动态效果时，宠物会使用静态帧。

前三项是代码层面的行为记录；没有以此声称本机所有异常都已定位或修复。

### 验证范围与后续

已完成的是图集结构、画面、方向辨识与服务端存储核对。GIF 是素材预览，不是原生客户端录屏。当前没有可用的全局鼠标跟随或动作调度增强插件，也未修改官方客户端。

当前可用的 Pets 工具负责创建、上传、更新和选中宠物，没有暴露实时动作控制或普通鼠标坐标接入接口。插件化增强留待后续研究，尚未确认能够接入原生浮窗，不属于本次发布功能。

## English

### Current conclusion

This is an asset pack, not a client extension. Complete artwork and successful upload validation do not guarantee every effect in the native floating pet.

The inspected client can render all sheet rows. No supported setting or Pets tool interface was found for global gaze tracking of the ordinary system pointer. Existing code handles Computer Use coordinates, some text-caret coordinates, and interactions in other pet displays; these do not establish general desktop-pointer following in the floating pet.

### Triggers in the inspected code

These are code findings, **not a claim that every trigger has been tested live**.

| Asset | Trigger |
| --- | --- |
| `idle` | No other action, or the end of an action sequence. |
| `running-left/right` | Horizontal movement while dragging the pet past a threshold; not autonomous walking. |
| `waving` | A temporary first-awake greeting. The client remembers greeted pets. |
| `jumping` | Pointer entry into the pet's hover area. |
| `running` | A running task notification selected by the pet. |
| `waiting` | A selected task state requesting input, approval, or a decision. |
| `failed` | A selected failed or blocked task state. |
| `review` | A selected completed result with unread activity. |
| Sixteen gaze poses | Coordinates supplied by the client; not necessarily the ordinary desktop pointer. |

`running` means focused work; directional movement uses the two separate keys. Notification priorities can affect which task the pet represents. The [official Pets documentation](https://learn.chatgpt.com/docs/pets) describes the four work-status categories.

### Why idle dominates

- The floating component defaults to three repetitions of a non-idle animation, followed by idle, even if the task remains active.
- Its idle frame durations are six times the base durations used in the artwork previews.
- The currently viewed conversation is generally excluded from running/completed status display, with waiting and failed states excepted.
- In a user test, moving this conversation into the background still left the pet idle. The foreground filter alone therefore does not explain this installation, and the full task-to-overlay path remains unverified.
- The [official documentation](https://learn.chatgpt.com/docs/pets) also says reduced-motion preferences can produce a still frame.

The first three points describe inspected code. They do not establish the sole cause of the observed behavior or claim a live fix.

### Verification and future work

Completed checks cover sheet structure, artwork, direction readability, and stored upload pixels. GIFs preview assets and are not native-client recordings. No behavior enhancement plugin has been released, and the official client has not been modified.

Available Pets tools manage pet creation, upload, updates, and selection; they expose no real-time animation controller or ordinary-pointer input hook. A plugin-based enhancement may be researched later. Integration with the native floating window has not been established and is not a feature of this release.
