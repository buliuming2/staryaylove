import json
import os

SAVE_FILE = "saves/save.json"

class GameState:
    def __init__(self):
        self.chapter = 0
        self.progress = 0
        self.like = {
            "千日坂芷芽": 0,
            "渚浔笑辞": 0,
            "加比镜岚": 0,
            "小鸟游刘网": 0,
            "棱斯新耀羽": 0
        }
        self.flags = {}   # 其他全局标记

    def load(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.chapter = data.get("chapter", 0)
                self.progress = data.get("progress", 0)
                self.like = data.get("like", self.like)
                self.flags = data.get("flags", {})
        return self

    def save(self):
        os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)
        data = {
            "chapter": self.chapter,
            "progress": self.progress,
            "like": self.like,
            "flags": self.flags
        }
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def apply_modifiers(self, mod_dict):
        """应用好感度或flag修改，格式如 {"like.千日坂芷芽": 15, "flag.something": True}"""
        for key, value in mod_dict.items():
            if key.startswith("like."):
                char = key.split(".")[1]
                self.like[char] = self.like.get(char, 0) + value
            elif key.startswith("flag."):
                flag_name = key.split(".")[1]
                self.flags[flag_name] = value