from .render import slow_print
from .state import GameState
from .parser import StoryParser
import sys

ROUTE_SELECTION_FLAG = "ROUTE_SELECTION"

def thank():
    print('剧情：星野 砚秋')
    print('技术开发：不刘名工作室')
    print('开发工具：python')
    print('IP版权所有者：豆芽人联盟')

def main():
    print('不刘名科创开发出品')
    print('豆芽人联盟©保留所有权利')
    slow_print("===== 豆芽人联盟：星芽之约 =====")
    slow_print("1. 新游戏")
    slow_print("2. 继续游戏")
    print("小提示：按住ctrl+t可加速剧情")
    choice = input("> ")

    state = GameState()
    parser = StoryParser()

    if choice == "1":
        state = GameState()
        state.save()
        run_common(state, parser)
    elif choice == "2":
        state.load()
        if state.chapter >= 1:
            run_common(state, parser)
        else:
            slow_print("暂无存档")
            input("按回车返回…")
            main()

def run_common(state, parser):
    steps = parser.load_common()
    current_id = "prologue_start"
    while current_id:
        # 处理分线标记
        if current_id == ROUTE_SELECTION_FLAG:
            route_selection(state, parser)
            return

        step = steps.get(current_id)
        if not step:
            break

        # 显示文本
        text = step.get("text", "")
        if text:
            slow_print(text.strip())

        # 处理选项
        choices = step.get("choices")
        if choices:
            for idx, ch in enumerate(choices, 1):
                print(f"{idx}. {ch['text']}")
            user_choice = input("> ")
            try:
                selected = choices[int(user_choice)-1]
            except (ValueError, IndexError):
                selected = choices[0]
            if "modifiers" in selected:
                state.apply_modifiers(selected["modifiers"])
            current_id = selected["goto"]
        else:
            # 无选项，直接跳转
            if "modifiers" in step:
                state.apply_modifiers(step["modifiers"])
            current_id = step.get("next")

        state.save()

    # 如果循环正常结束（没有遇到 ROUTE_SELECTION），也尝试分线
    route_selection(state, parser)

def route_selection(state, parser):
    likes = state.like
    max_like = max(likes.values())
    if max_like < 12:
        normal_end()
        return
    target = max(likes, key=lambda x: likes[x])
    route_map = {
        "千日坂芷芽": "ziya",
        "渚浔笑辞": "xiaoci",
        "加比镜岚": "jinglan",
        "小鸟游刘网": "liuwang",
        "棱斯新耀羽": "yaoyu"
    }
    route_name = route_map.get(target)
    if route_name:
        run_route(state, parser, route_name)
    else:
        slow_print(f"错误：无法找到角色 {target} 的个人线，进入普通结局。")
        normal_end()

def run_route(state, parser, route_name):
    """执行个人线"""
    steps = parser.load_route(route_name)
    current_id = f"{route_name}_start"
    while current_id:
        step = steps.get(current_id)
        if not step:
            break
        if "text" in step:
            slow_print(step["text"].strip())
        if "choices" in step:
            for idx, ch in enumerate(step["choices"], 1):
                print(f"{idx}. {ch['text']}")
            user_choice = input("> ")
            try:
                selected = step["choices"][int(user_choice)-1]
            except (ValueError, IndexError):
                selected = step["choices"][0]
            if "modifiers" in selected:
                state.apply_modifiers(selected["modifiers"])
            current_id = selected["goto"]
        else:
            if "modifiers" in step:
                state.apply_modifiers(step["modifiers"])
            current_id = step.get("next")
        state.save()
    thank()
    input("按回车退出")

def normal_end():
    slow_print("\n==================================================")
    slow_print("                     普通结局")
    slow_print("==================================================")
    slow_print("你和所有人都是最好的朋友。")
    slow_print("没有恋爱，只有青春最温暖的日常。")
    slow_print("豆芽人联盟，永远是你最安心的归宿。")
    thank()
    input("按回车退出")