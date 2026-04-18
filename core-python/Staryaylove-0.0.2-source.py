import json
import os
import time
import sys

# 存档文件
SAVE_FILE = "save.json"


def slow_print(text):
    """打印粉色文本，然后等待。
    如果用户在此期间按下 Ctrl+T（即 Ctrl 和 t 同时按下），则等待 0.1 秒后返回；
    否则等待 1 秒后返回。
    兼容非 TTY 环境（如 PyCharm 嵌入式终端）。
    """
    # 粉色 ANSI 码
    PINK = "\033[95m"
    RESET = "\033[0m"
    print(f"{PINK}{text}{RESET}")

    # 检查 stdin 是否为终端（TTY）
    if not sys.stdin.isatty():
        time.sleep(1)
        return

    # 终端环境，尝试检测 Ctrl+T
    if sys.platform == 'win32':
        import msvcrt
        start = time.time()
        while time.time() - start < 1:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                # Windows 下 Ctrl+T 返回 b'\x14'（十进制20）
                if key == b'\x14':
                    time.sleep(0.1)
                    return
            time.sleep(0.02)
    else:
        # Unix / Linux / macOS
        import select
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            start = time.time()
            while time.time() - start < 1:
                rlist, _, _ = select.select([fd], [], [], 0.05)
                if rlist:
                    ch = sys.stdin.read(1)
                    # Ctrl+T 产生 ASCII 20（0x14）
                    if ch and ord(ch) == 20:
                        time.sleep(0.1)
                        return
        except Exception:
            # 意外情况回退到普通等待
            time.sleep(1)
        finally:
            try:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except Exception:
                pass
"""
# 逐句输出 + 每段等待1秒
def slow_print(text):
    print(text)
    time.sleep(1)
"""
"""
def slow_print(text):
    for ch in text:
        print(ch, end='', flush=True)
        if keyboard.is_pressed('ctrl'):
            time.sleep(0.1)   # 按住 Ctrl 时快速输出
        else:
            time.sleep(1)    # 未按时慢速输出
    print()
"""
#谢幕
def thank():
    print('剧情：星野 砚秋')
    print('技术开发：不刘名工作室')
    print('开发工具：python')
    print('IP版权所有者：豆芽人联盟')

# 加载存档
def load_save():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "chapter": 0,
        "progress": 0,
        "like": {
            "千日坂芷芽": 0,
            "渚浔笑辞": 0,
            "加比镜岚": 0,
            "小鸟游刘网": 0,
            "棱斯新耀羽": 0
        }
    }

# 保存游戏
def save_game(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save = load_save()

# ======================
# 主菜单
# ======================
def main():
    print('不刘名科创开发出品')
    print('豆芽人联盟©保留所有权利')
    slow_print("===== 豆芽人联盟：星芽之约 =====")
    slow_print("1. 新游戏")
    slow_print("2. 继续游戏")
    print("小提示：按住ctrl+t可加速剧情")
    choice = input("> ")

    if choice == "1":
        save["chapter"] = 1
        save["progress"] = 0
        save["like"] = {
            "千日坂芷芽": 0,
            "渚浔笑辞": 0,
            "加比镜岚": 0,
            "小鸟游刘网": 0,
            "棱斯新耀羽": 0
        }
        save_game(save)
        chapter1()

    elif choice == "2":
        if save["chapter"] >= 1:
            chapter1()
        else:
            slow_print("暂无存档")
            input("按回车返回…")
            main()

# ======================
# 第一章 共通线
# ======================
def chapter1():
    slow_print("\n【第一章：旧教学楼的社团】")
    slow_print("（开学了，你刚报道完，坐在教室）")
    slow_print("（突然，白板上的QQ发来了一条由班主任发来的消息）")
    slow_print("（消息就是叫你到12栋教师宿舍后面的办公室一趟）")
    slow_print("（但是，你还没走过这一条路，刚到教师宿舍，你迷路了）")
    slow_print("（你随便乱晃，走到了旧教学楼最里面的房间）")
    slow_print("（门上贴着一张纸：豆芽人联盟 招生中）")

    slow_print("\n1. 推开门进去")
    slow_print("2. 先离开")
    c = input("> ")

    if c == "1":
        slow_print("\n门轻轻推开，里面坐着一位带着耳机的少女。")
        slow_print("她正低头画画，笔尖在纸上轻轻滑动。")
        slow_print("阳光洒在她妩媚的脸上，显得格外漂亮")
        slow_print("她突然抬起头，看向了你")
        slow_print("千日坂芷芽：你……是来加入豆芽人联盟的吗？")
        slow_print("你该如何回答？")
        slow_print("1.“是的”")
        slow_print("2.“不是”")
        nert = input("> ")
        if nert == "2":
            slow_print("\n你转身离开，故事到此结束。")
            input("按回车退出…")
            return
        else:
            save["like"]["千日坂芷芽"] += 5
            save["progress"] = 10

    elif c == "2":
        slow_print("\n你转身离开，故事到此结束。")
        input("按回车退出…")
        return

    save_game(save)
    chapter2()

# ======================
# 第二章 共通线
# ======================
def chapter2():
    slow_print("\n【第二章：联盟的大家】")
    slow_print("第二天，你按照约定的时间再次来到社团教室。")
    slow_print("推开门时，里面已经有了好几个人。")

    slow_print("\n千日坂芷芽朝你轻轻点头。")
    slow_print("千日坂芷芽：你来啦，我给你介绍一下大家。")

    slow_print("\n身边笑容明亮的少女先开口。")
    slow_print("渚浔笑辞：你好呀～以后请多指教！我经常在这里做点心！")

    slow_print("\n靠窗位置，气质冷静的少女。")
    slow_print("加比镜岚：……欢迎。")

    slow_print("\n门口附近，动作轻快的少女。")
    slow_print("小鸟游刘网：来得正好，一起整理资料吧！")

    slow_print("\n房间中央，气质耀眼的少女。")
    slow_print("棱斯新耀羽：从今天起，我们就是伙伴了。")
    # --- 共通线里强化刘网「敲代码」的细节 ---
    slow_print("你注意到她指尖沾着淡蓝色的键盘油，脚边放着一台打开的笔记本电脑，屏幕上滚动着密密麻麻的代码行。")
    slow_print("小鸟游刘网飞快敲下最后几个字符，按下回车：「搞定！旧档案检索脚本跑通了，以后找资料能快上十倍！」")

    # --- 共通线氛围与互动（继续保留代码细节）---
    slow_print("\n你跟着芷芽走到房间中央，阳光透过百叶窗在地板上投下斑驳的光影。")
    slow_print("书架上堆满了泛黄的旧报纸和手写档案，标签上写着「校园怪谈」「旧校舍历史」等字样。")
    slow_print("空气中飘着淡淡的茶香和渚浔笑辞带来的曲奇香气，让人莫名安心。")

    slow_print("\n千日坂芷芽把一份社团章程推到你面前：「这是我们的活动记录，以后你也可以一起参与调查。」")
    slow_print("你接过文件夹，指尖触到纸张粗糙的质感，上面密密麻麻写着历届社员的笔记。")

    slow_print("\n渚浔笑辞突然从背包里掏出一个粉色便当盒：「对了！尝尝我新烤的曲奇！是抹茶味的哦～」")
    slow_print("你接过一块，酥脆的口感在嘴里化开，甜味恰到好处。")

    slow_print(
        "\n小鸟游刘网抱着一摞旧报纸走到你身边，另一只手还在手机上改着代码：「别愣着啦！先从整理这些旧报纸开始吧，我写个脚本帮你快速按日期分类！」")
    slow_print("你瞥见她手机屏幕上是简洁的 Python 代码，变量名还带着可爱的颜文字。")

    slow_print("\n加比镜岚默默递过来一副干净的白手套，声音很轻：「避免留下指纹，有些档案很脆弱。」")
    slow_print("你接过手套，注意到她指尖也沾着淡淡的墨水痕迹——看来她经常在这里整理资料。")

    slow_print(
        "\n棱斯新耀羽站在窗边，阳光落在她的发梢，她回头对你笑了笑：「我们都很期待你的加入，毕竟……这个社团很久没有新人了。」")
    slow_print("她的笑容像阳光一样耀眼，让你原本紧张的心情慢慢平复下来。")

    slow_print("\n就在你翻看旧报纸时，一张泛黄的照片从书页间滑落。")
    slow_print("照片上是一群穿着旧校服的学生，站在一栋废弃的教学楼前，背景里的钟楼指针停在午夜12点。")
    slow_print("千日坂芷芽捡起照片，眼神变得严肃：「这是30年前的社员，他们在调查旧校舍后就再也没有出现过。」")
    slow_print("渚浔笑辞的笑容也淡了下去：「我们一直在找他们的下落，这也是这个社团存在的意义。」")
    slow_print("房间里的气氛瞬间变得沉重，所有人的目光都集中在你身上。")
    slow_print("\n你握紧了手里的旧报纸，抬头看向大家：“我也想一起帮忙找到真相。”")
    slow_print("千日坂芷芽露出了释然的笑容：“欢迎你，正式成为我们的一员。”")
    slow_print("渚浔笑辞立刻拍手：“太好了！今晚我请大家喝奶茶！”")
    slow_print("小鸟游刘网把电脑屏幕转向你：“我把档案库权限开给你，以后我们一起挖线索！”")
    slow_print("加比镜岚轻轻点了点头，眼神里多了一丝温度。")
    slow_print("棱斯新耀羽走到你身边，拍了拍你的肩膀：“我们一起，把这个谜团解开。”")

    slow_print("\n接下来的几天，你渐渐熟悉了社团的节奏。")
    slow_print("每天放学后，大家都会聚在活动室里，有人整理资料，有人分析旧闻，有人默默写着代码。")
    slow_print("渚浔笑辞总会准时带来各种小点心，活动室里永远飘着甜甜的香味。")
    slow_print("加比镜岚依旧话不多，但总会在你需要的时候，安静地递上东西或者提醒细节。")
    slow_print("棱斯新耀羽不管什么时候出现，都像小太阳一样，把气氛变得轻松又明亮。")
    slow_print("千日坂芷芽则会一边画画，一边给你讲社团过去的小故事。")
    slow_print("小鸟游刘网一有空就敲代码，说是要把所有旧资料都做成可检索的数据库。")

    slow_print("\n很快到了周五，放学的时候，渚浔笑辞突然蹦到大家面前。")
    slow_print("渚浔笑辞：“周末我们去近郊团建吧！我查好天气了，晴天，超级适合看星星！”")
    slow_print("小鸟游刘网：“我带电脑去，晚上可以给大家放电影！”")
    slow_print("加比镜岚：“我准备急救包和用品。”")
    slow_print("棱斯新耀羽笑着看向你：“你要一起来吧？缺了你可就不热闹了。”")
    slow_print("千日坂芷芽也轻轻点头：“一起去吧，就当是欢迎新人的纪念。”")

    slow_print("\n周末的团建顺利又开心，大家一起搭帐篷、烤肉、看星星，聊了很多很多话。")
    slow_print("你和每个人的距离，都在不知不觉中拉近了不少。")
    slow_print("\n【第一章 结束】")

    slow_print("\n\n【第二章 开始】")
    slow_print("\n团建之后，日子平稳地向前走，转眼就到了校运会。")
    slow_print("操场上人声鼎沸，彩旗被风吹得轻轻晃动。")

    slow_print("\n渚浔笑辞抱着一大堆零食和饮料，在看台上到处分发。")
    slow_print("加比镜岚参加了跑步项目，正在跑道边认真热身。")
    slow_print("棱斯新耀羽作为学生代表，在主席台上主持，声音清晰又好听。")
    slow_print("千日坂芷芽坐在你旁边，拿着画本，把眼前的画面一点点画下来。")
    slow_print("小鸟游刘网则抱着电脑，实时刷新比赛数据，时不时兴奋地小声喊两句。")

    slow_print("\n接力赛的时候，加比镜岚最后一棒冲刺，你和刘网在旁边拼命加油。")
    slow_print("冲线的那一刻，刘网激动地敲了下键盘：“预测成功！完美发挥！”")
    slow_print("加比镜岚喘着气走过来，第一次对你露出了很淡很淡的笑。")

    slow_print("\n傍晚，夕阳把整个操场染成了暖橙色。")
    slow_print("大家坐在看台上，吃着笑辞带的甜点，聊着今天发生的趣事。")
    slow_print("你看着身边这群人，心里第一次清楚地感觉到，自己真的有了可以安心待着的地方。")
    slow_print("\n【第二章 结束】")

    slow_print("\n\n【第三章 开始】")
    slow_print("\n校运会过后，又过去了好几个月。")
    slow_print("天气慢慢转凉，社团决定再组织一次深秋团建。")

    slow_print("\n这一次的地点在半山腰，漫山都是红叶，风景格外好看。")
    slow_print("笑辞忙着烤肉和热可可，香味飘得很远。")
    slow_print("刘网调试着投影仪，准备放这大半年来的社团日常片段。")
    slow_print("镜岚仔细检查每一个帐篷，确保晚上不会着凉。")
    slow_print("芷芽和耀羽一起捡柴火，一边走一边轻声聊天。")

    slow_print("\n夜幕降临，篝火亮了起来。")
    slow_print("大家围坐在一起，看着投影里的回忆片段，从第一次见面，到整理资料，到校运会，再到一次次放学后的闲聊。")
    slow_print("不知道是谁先轻声开口，气氛慢慢变得温柔又安静。")

    slow_print("\n你看着身边的每一个人，心里渐渐清晰起来。")
    slow_print("原来在这么长的陪伴里，你早就对某一个人，产生了不一样的心意。")
    slow_print("笑辞开口说到：“大家来尝尝我最新烤的蛋挞”")
    slow_print("......")

    slow_print("\n团建结束后，又到了新的一天")
    slow_print("这天，你刚到社团，看见她们都在议论什么")
    slow_print("议论完，就各自忙着各自的事去了")

    slow_print("\n【你想走向谁？】")
    slow_print("1. 千日坂芷芽")
    slow_print("2. 渚浔笑辞")
    slow_print("3. 加比镜岚")
    slow_print("4. 小鸟游刘网")
    slow_print("5. 棱斯新耀羽")
    cho = input("> ")

    if cho == "1":
        slow_print("\n你走到芷芽身边，看了一眼她的画。")
        slow_print("千日坂芷芽：我……喜欢把心情画下来。")
        save["like"]["千日坂芷芽"] += 12
    elif cho == "2":
        slow_print("\n笑辞立刻递给你一块小饼干。")
        slow_print("渚浔笑辞：刚烤的！尝尝看～")
        save["like"]["渚浔笑辞"] += 12
    elif cho == "3":
        slow_print("\n你试着和镜岚搭话。")
        slow_print("加比镜岚：……嗯。你人，好像还不错。")
        save["like"]["加比镜岚"] += 12
    elif cho == "4":
        slow_print("\n你跟着刘网一起整理资料。")
        slow_print("小鸟游刘网：有你帮忙真的轻松多了！")
        save["like"]["小鸟游刘网"] += 12
    elif cho == "5":
        slow_print("\n你和耀羽聊起联盟的目标。")
        slow_print("棱斯新耀羽：我们一起，让联盟变得更厉害吧！")
        save["like"]["棱斯新耀羽"] += 12

    save_game(save)
    chapter3()

# ======================
# 共通线结束·自动分线
# ======================
def chapter3():
    slow_print("\n【第三章：共通线 完结】")
    slow_print("日子一天天过去，你和联盟里的每个人都渐渐熟悉。")
    slow_print("一起上课，一起放学，一起在旧教学楼里度过安静的时光。")
    slow_print("而你心里，也慢慢出现了一个特别的身影。")

    likes = save["like"]
    max_like = max(likes.values())

    if max_like < 12:
        normal_end()
        return

    target = max(likes, key=lambda x: likes[x])

    if target == "千日坂芷芽":
        route_ziya()
    elif target == "渚浔笑辞":
        route_xiaoci()
    elif target == "加比镜岚":
        route_jinglan()
    elif target == "小鸟游刘网":
        route_liuwang()
    elif target == "棱斯新耀羽":
        route_yaoyu()

# ======================
# 千日坂芷芽（绘画少女）·长篇个人线 + 选择题
# ======================
def route_ziya():
    slow_print("\n==================================================")
    slow_print("                   千日坂芷芽 个人线")
    slow_print("==================================================")
    input("按回车开始……")

    slow_print("\n你越来越常注意到窗边画画的戴着耳机的少女。")
    slow_print("她安静、温柔、话少，却总能用画笔表达一切。")
    slow_print("你开始主动留在教室，陪她一起画画。")

    slow_print("\n【选择题：你想怎么夸她的画？】")
    slow_print("1. 你的画好温柔，像你一样")
    slow_print("2. 画得好厉害，我好佩服")
    choice = input("> ")
    if choice == "1":
        slow_print("千日坂芷芽耳朵微微发红：……谢谢。")
        save["like"]["千日坂芷芽"] += 15
    else:
        slow_print("千日坂芷芽轻轻点头：谢谢你的认可。")
        save["like"]["千日坂芷芽"] += 8

    slow_print("\n某天傍晚，教室里只剩下你们两个人。")
    slow_print("千日坂芷芽：其实……我一直很害怕，联盟会消失。")
    slow_print("千日坂芷芽：所以我想把这里的每一天都画下来。")
    slow_print("你安静地听着，第一次看到她如此脆弱的一面。")

    slow_print("\n【选择题：你想怎么做？】")
    slow_print("1. 轻轻握住她的手")
    slow_print("2. 温柔安慰她")
    choice = input("> ")
    if choice == "1":
        slow_print("芷芽身体一颤，却没有躲开。")
        save["like"]["千日坂芷芽"] += 20
    else:
        slow_print("芷芽轻轻点头，眼神变得安心。")
        save["like"]["千日坂芷芽"] += 10

    slow_print("\n有一次，你发现芷芽在那非常生气")
    slow_print("你靠近问：“怎么了？”")
    slow_print("芷芽拿着平板给你看")
    slow_print("原来芷芽因为发布的作品质量太高了")
    slow_print("被别人质疑是AI生成的")
    slow_print("还有一些人造假，说芷芽的画作使用了200+个AI模型")
    slow_print("此时，你会怎么做？")
    slow_print("1.愤怒的说到：“这些用户是人类吗？芷芽酱辛辛苦苦搞的作品，却被你们这群身上长满蛔虫的狗造谣说成ai！！！”")
    slow_print("2.摸着她的脸安慰到：“没事的，每个人把自己的作品发布都会被质疑和辱骂，这是正常的”")
    lot = input("> ")
    if lot == "1":
        slow_print("芷芽对此愤愤不平")
        save["like"]["千日坂芷芽"] += 10
        slow_print("从那天起，芷芽慢慢的不喜欢说话了")
        slow_print("过了一些天，社团宣布解散")
        slow_print("\n【结局：消失的芷芽】")
        slow_print("从此，芷芽永远消失在了这个世界")
        slow_print("你也变成了孤独的人")
        slow_print("==================================================")
        slow_print("           千日坂芷芽 · Bad ENDing 消失的芷芽")
        slow_print("==================================================")
        thank()
        input("按回车退出")
    else:
        slow_print("芷芽抱住了你，连忙道谢")
        save["like"]["千日坂芷芽"] += 15
        slow_print("从那天起，你们之间的距离彻底打破。")
        slow_print("她会主动给你看她的新画，画里渐渐开始出现你的身影。")
        slow_print("夕阳下，她突然停下画笔，看向你。")
        slow_print("千日坂芷芽：我……我喜欢你。")
        slow_print("千日坂芷芽：不是伙伴，是想一直在一起的那种喜欢。")
        slow_print("\n【结局：画师的依靠】")
        slow_print("你们一起守护着小小的联盟。")
        slow_print("她画着世界，而你的世界里，只有她。")
        slow_print("==================================================")
        slow_print("           千日坂芷芽 · Happy ENDing 画师的依靠")
        slow_print("==================================================")
        thank()
        input("按回车退出")

# ======================
# 渚浔笑辞（料理少女）·长篇个人线 + 选择题
# ======================
def route_xiaoci():
    slow_print("\n==================================================")
    slow_print("                   渚浔笑辞 个人线")
    slow_print("==================================================")
    input("按回车开始……")

    slow_print("笑辞是联盟里的小太阳，最喜欢给大家做点心。")
    slow_print("她的笑容和她做的料理一样，温暖又治愈。")
    slow_print("你每天都期待和她一起度过的时光。")

    slow_print("有一天，她来你家玩，送你了一块蛋挞。")
    slow_print("\n【选择题：她把蛋挞送到你的嘴里，问：好吃吗？】")
    slow_print("1. 超级好吃！和你一样甜！")
    slow_print("2. 谢谢，我会好好品尝")
    choice = input("> ")
    if choice == "1":
        slow_print("笑辞脸颊一红：讨厌啦～")
        save["like"]["渚浔笑辞"] += 15
    else:
        slow_print("笑辞开心地笑了：太好了！")
        save["like"]["渚浔笑辞"] += 8

    slow_print("\n【个人线·发展】")
    slow_print("你渐渐发现，笑辞的笑容背后也有疲惫。")
    slow_print("她总是努力让所有人开心，却常常忘了照顾自己。")
    slow_print("你开始主动陪她一起准备料理、收拾厨房。")

    slow_print("有一次，她把菜烧糊了，她看着烧糊的菜，哭着说到：“我是不是很没用啊？”")
    slow_print("\n【选择题：你该怎么做】")
    slow_print("1. 抱住她，说：“没事的，每个人都有失误的时候，不要伤心嘛~”")
    slow_print("2. 安静陪着她")
    choice = input("> ")
    if choice == "1":
        slow_print("笑辞眼眶一红，轻轻靠在你怀里。")
        save["like"]["渚浔笑辞"] += 20
    else:
        slow_print("笑辞轻声说：有你在真好……")
        save["like"]["渚浔笑辞"] += 10

    slow_print("\n笑辞拿着亲手做的巧克力，递到你面前。")
    slow_print("渚浔笑辞：我最喜欢你了！")
    slow_print("渚浔笑辞：以后……我想每天都做料理给你吃！")
    slow_print("你紧紧握住她的手，心里满是幸福。")

    slow_print("\n然而，好景不长……")
    slow_print("几周后，笑辞突然变得异常疲惫，常常头晕、发烧。")
    slow_print("你带她去了好几家医院，但所有的检查都显示——")
    slow_print("没有发现任何器质性病变，一切指标正常。")
    slow_print("医生们束手无策，只能说是“一种奇怪的病”。")
    slow_print("笑辞的笑容渐渐消失，她甚至没有力气再进厨房。")

    slow_print("\n你看着她苍白的脸，心如刀绞。")
    slow_print("这天晚上，笑辞虚弱地拉着你的手：")
    slow_print("渚浔笑辞：我是不是……再也做不了料理给你吃了？")
    slow_print("渚浔笑辞：对不起……")

    slow_print("\n【生死攸关的选择】")
    slow_print("1. 疯狂寻找偏方和专家，一定要治好她！")
    slow_print("2. 温柔地抱住她，告诉她：“你不需要做任何事，只要你在就好。”")
    lot = input("> ")

    if lot == "1":
        slow_print("\n你像疯了一样到处求医问药。")
        slow_print("你带着笑辞跑遍全国，尝试各种偏方、针灸、甚至巫术。")
        slow_print("笑辞的身体越来越虚弱，但她不忍心拒绝你的努力。")
        slow_print("每次看到你疲惫又焦虑的眼神，她都勉强挤出笑容。")
        slow_print("终于有一天，笑辞在去往外地医院的列车上，安静地靠在你肩上……")
        slow_print("再也没有醒来。")
        slow_print("\n医生说她是因为长期心力交瘁，加上疾病消耗……")
        slow_print("你抱着她冰冷的身体，悔恨的泪水无法停止。")
        slow_print("你才明白，你只顾着寻找解药，却忘了给她最需要的——陪伴与安宁。")
        slow_print("\n【结局：失去的太阳】")
        slow_print("联盟少了她，再也没有了笑声。")
        slow_print("你每天都会去厨房坐一坐，仿佛还能闻到蛋挞的香气。")
        slow_print("但那个总是对你笑的小太阳，再也回不来了。")
        slow_print("==================================================")
        slow_print("           渚浔笑辞 · Bad ENDing 失去的太阳")
        slow_print("==================================================")
        thank()
        input("按回车退出")
        return

    else:
        slow_print("\n你轻轻把她揽进怀里，声音温柔而坚定：")
        slow_print("“笑辞，你不需要做任何事。你对我来说，比任何料理都重要。”")
        slow_print("“从今天起，换我来照顾你。”")
        slow_print("笑辞的眼泪一下子涌了出来，她用力地点点头。")
        slow_print("\n你辞去了所有兼职，每天陪在她身边。")
        slow_print("你学会了煮粥、炖汤，虽然味道远远比不上她做的。")
        slow_print("但每次看到你手忙脚乱的样子，笑辞都会忍不住笑出来。")
        slow_print("你给她讲联盟里的趣事，给她看你画的涂鸦。")
        slow_print("慢慢地，笑辞的脸色一天天红润起来。")
        slow_print("某个清晨，你还在睡梦中，忽然闻到一股熟悉的蛋挞香。")
        slow_print("你睁开眼睛，看到笑辞系着围裙，端着金黄的蛋挞站在你床前。")
        slow_print("渚浔笑辞：早安～我……好像好了呢。")
        slow_print("\n后来的医生说，这或许是一种“心因性疾病”")
        slow_print("当一个人被爱和温柔包围时，身体会自己找到康复的路。")
        slow_print("\n笑辞重新回到了厨房，但这次，她不再一个人忙碌。")
        slow_print("你们并肩站在灶台前，火光映着两张幸福的笑脸。")
        slow_print("渚浔笑辞：谢谢你……没有放弃我。")
        slow_print("渚浔笑辞：以后，我想和你一起做一辈子的料理。")
        slow_print("\n【结局：康复的烟火】")
        slow_print("她用笑容温暖你，你用守护治愈她。")
        slow_print("厨房里的烟火，成了你们最幸福的日常。")
        slow_print("奇怪的病再也没有复发，因为爱就是最好的药。")
        slow_print("==================================================")
        slow_print("           渚浔笑辞 · Happy ENDing 康复的烟火")
        slow_print("==================================================")
        thank()
        input("按回车退出")

# ======================
# 加比镜岚 个人线
# ======================
def route_jinglan():
    slow_print("\n==================================================")
    slow_print("                   加比镜岚 个人线")
    slow_print("==================================================")
    input("按回车开始……")
    slow_print("镜岚外表冷淡，内心却比谁都温柔。")
    slow_print("你一点点走进她的心，打破她的孤独。")
    slow_print("\n【选择题：你想如何靠近她？】")
    slow_print("1. 耐心陪伴")
    slow_print("2. 主动搭话")
    input("> ")
    slow_print("最终，她向你敞开心扉，说出藏在心底的告白。")
    slow_print("==================================================")
    slow_print("           加比镜岚 · TRUE END 镜心之光")
    slow_print("==================================================")
    thank()
    input("按回车退出")

# ======================
# 小鸟游刘网 个人线
# ======================
def route_liuwang():
    slow_print("\n==================================================")
    slow_print("                 小鸟游刘网 个人线")
    slow_print("==================================================")
    input("按回车开始……")

    slow_print("\n你第一次注意到小鸟游刘网，是在教室靠窗的最后一排。")
    slow_print("她总是戴着黑框眼镜，盯着笔记本电脑屏幕，手指飞快地敲着键盘。")
    slow_print("周围的同学聊着游戏、偶像、周末去哪玩，她却像另一个世界的人。")
    slow_print("你听说她是个天才程序员，初中就开始写开源项目，还拿过竞赛奖。")
    slow_print("但在这个班里，她却是被孤立的对象。")

    slow_print("\n【选择题：你会怎么看待她？】")
    slow_print("1. 好厉害！我想和她做朋友")
    slow_print("2. 有点可怜，但也不关我的事吧……")
    choice = input("> ")
    if choice == "1":
        slow_print("你主动坐到她旁边，刘网抬起头，眼神里闪过一丝惊讶和……戒备。")
        save["like"]["小鸟游刘网"] += 15
    else:
        slow_print("你从她身边走过，没有停留。刘网低头继续敲键盘，手指却慢了半拍。")
        save["like"]["小鸟游刘网"] += 0

    slow_print("\n【霸凌的阴影】")
    slow_print("很快你发现，刘网在班里并不只是“被无视”那么简单。")
    slow_print("班长小团体经常嘲笑她的打扮、她的代码、她的一切。")
    slow_print("“天天写那些破代码，有什么用啊？”“怪不得没朋友，怪人一个。”")
    slow_print("还有人故意藏她的鼠标、拔她的电源线，甚至在课本上写“程序员滚出班级”。")
    slow_print("刘网每次都默默忍受，从不反驳，只是把课本擦干净，继续埋头写代码。")

    slow_print("一天午休，你看到刘网的桌子被泼了水，键盘全湿了。")
    slow_print("她蹲在地上，一个一个键帽拆下来擦干，眼泪在眼眶里打转。")
    slow_print("\n【选择题：你要怎么做？】")
    slow_print("1. 走过去，递给她纸巾，帮她一起擦键盘")
    slow_print("2. 去报告老师，让老师来处理")
    choice = input("> ")
    if choice == "1":
        slow_print("刘网抬头看你，泪水终于落了下来：为什么……要帮我？")
        slow_print("你笑了笑：因为我们是同学啊。")
        save["like"]["小鸟游刘网"] += 20
    else:
        slow_print("你跑去办公室，老师只是皱眉说“知道了”，却没有真正处理。")
        slow_print("回来后，刘网的桌子已经被搬到了教室最后一排的角落。")
        slow_print("她看你一眼，什么也没说。")
        save["like"]["小鸟游刘网"] += 5

    slow_print("\n从那以后，你开始主动和她说话。")
    slow_print("你发现她其实很健谈，只是太久没人愿意听她讲代码、讲算法。")
    slow_print("她给你看她写的程序——一个可以自动生成画作的AI，一个能分析情绪的小工具。")
    slow_print("你惊叹不已，刘网害羞地推了推眼镜：其实……也没什么厉害的。")

    slow_print("但霸凌并没有停止。")
    slow_print("班长带人把她从小组讨论中排挤出去，说“我们不需要你这种怪人”。")
    slow_print("还有人把她写的代码截图发到班级群，嘲讽“这水平也好意思自称程序员”。")
    slow_print("刘网越来越沉默，甚至开始逃课。")

    slow_print("一天放学后，你在学校天台找到了她。")
    slow_print("她坐在护栏边，风吹起她的长发，眼神空洞。")
    slow_print("小鸟游刘网：你说……我是不是真的不适合待在这里？")
    slow_print("小鸟游刘网：也许他们说得对，我就是一个没用的怪人。")

    slow_print("\n【关键选择：你要怎么回应？】")
    slow_print("1. 愤怒地说：“他们才是混蛋！走，我陪你去找校长！”")
    slow_print("2. 坐在她旁边，轻轻说：“不是的。你是我见过最酷的人。”")
    lot = input("> ")

    if lot == "1":
        slow_print("\n你拉着刘网冲进校长室，把事情原原本本说了出来。")
        slow_print("校长叫来了班长等人，严厉批评了他们。")
        slow_print("班长们表面道歉，眼神里却满是怨恨。")
        slow_print("\n第二天，更猛烈的报复开始了。")
        slow_print("有人在班级群里造谣刘网“作弊”，有人趁她不注意删掉了她U盘里所有代码。")
        slow_print("刘网崩溃了，她把自己关在家里，再也不来学校。")
        slow_print("你打电话、发消息，她都不回。")
        slow_print("一周后，你收到她的一封邮件：")
        slow_print("“谢谢你为我做的一切。但我已经累了。我想去一个没有人认识我的地方。再见。”")
        slow_print("从那以后，小鸟游刘网转学了，再也没有任何消息。")
        slow_print("你站在空荡荡的天台上，风吹过，却再也带不回那个女孩。")
        slow_print("\n【结局：消失的风】")
        slow_print("你每次打开电脑，都会想起她敲键盘的样子。")
        slow_print("你才明白，有时候冲动不是勇气，陪伴才是。")
        slow_print("==================================================")
        slow_print("           小鸟游刘网 · Bad ENDing 消失的风")
        slow_print("==================================================")
        thank()
        input("按回车退出")
        return

    else:
        slow_print("\n你坐到她旁边，没有拉她走，也没有说教。")
        slow_print("你只是陪她看夕阳，听风的声音。")
        slow_print("过了很久，你开口：刘网，你写的那个AI画图程序，能教我吗？")
        slow_print("刘网愣了一下，眼泪又流了下来，但这次她笑了。")
        slow_print("她点点头：好。")
        slow_print("\n从那天起，你开始跟她学编程。")
        slow_print("你们每天放学后都在空教室里，她教你Python、算法、Git。")
        slow_print("你学得很慢，但她从不会不耐烦。")
        slow_print("慢慢地，刘网的代码里开始出现有趣的注释：“# 今天教笨蛋写了第一个函数”")
        slow_print("你也开始帮她在班里发声，不是吵架，而是让大家看到她的才华。")
        slow_print("你向班主任建议举办一次“班级编程小展”，让刘网展示她的作品。")
        slow_print("当同学们看到刘网写的游戏和小工具时，不少人发出惊叹：“原来这么厉害！”")
        slow_print("班长的小团体渐渐没了声音，因为其他同学开始认可刘网。")

        slow_print("\n毕业典礼那天，刘网送你一个U盘。")
        slow_print("里面是一个程序——打开后，屏幕上出现一行行文字，记录着你们从相识到现在的每一天。")
        slow_print("最后一行写着：谢谢你没有放弃我。你是我生命中最重要的……朋友。")
        slow_print("你转头看她，她的眼睛亮晶晶的。")
        slow_print("小鸟游刘网：其实……我喜欢你。从你帮我擦键盘那天就喜欢了。")
        slow_print("小鸟游刘网：但我怕说出来，连朋友都做不成……")
        slow_print("你握住她的手：笨蛋，我也喜欢你。")
        slow_print("她扑进你怀里，哭得像个小孩。")
        slow_print("\n【结局：代码与风】")
        slow_print("你们一起考上了同一所大学，一起写代码，一起面对世界。")
        slow_print("霸凌的阴影早已散去，因为你们是彼此最坚固的城墙。")
        slow_print("她的代码里多了一个变量——你的名字。")
        slow_print("==================================================")
        slow_print("           小鸟游刘网 · Happy ENDing 代码与风")
        slow_print("==================================================")
        thank()
        input("按回车退出")

# ======================
# 棱斯新耀羽 个人线
# ======================
def route_yaoyu():
    slow_print("\n==================================================")
    slow_print("                棱斯新耀羽 个人线")
    slow_print("==================================================")
    input("按回车开始……")
    slow_print("耀眼如太阳的她，只为你一人发光。")
    slow_print("\n【选择题：你愿意成为她的光吗？】")
    slow_print("1. 我愿意")
    slow_print("2. 永远愿意")
    input("> ")
    slow_print("你们彼此照耀，成为最耀眼的存在。")
    slow_print("==================================================")
    slow_print("           棱斯新耀羽 · TRUE END 闪耀未来")
    slow_print("==================================================")
    thank()
    input("按回车退出")

# ======================
# 普通结局
# ======================
def normal_end():
    slow_print("\n==================================================")
    slow_print("                     普通结局")
    slow_print("==================================================")
    slow_print("你和所有人都是最好的朋友。")
    slow_print("没有恋爱，只有青春最温暖的日常。")
    slow_print("豆芽人联盟，永远是你最安心的归宿。")
    thank()
    input("按回车退出")

if __name__ == "__main__":
    main()

#草稿
"""
#open
print('不刘名工作室出品')
print('豆芽人联盟')
#加载程序

#主界面
print('豆芽人联盟：星芽之约')
print('1.开始游戏')
#if ???
#print('2.继续游戏')
print('3.系统设置')
ora=input(ora)
#开始游戏
if ora=='1':
    print('（今天刚开学，你麻木的前往学校）')
    print('......')
"""
