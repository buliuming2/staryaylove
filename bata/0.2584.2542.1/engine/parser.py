import toml
from pathlib import Path

class StoryParser:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.steps = {}  # 存储所有step的字典 {step_id: step_data}

    def load_common(self):
        """加载共通线剧情（prologue.toml）"""
        path = self.data_dir / "common" / "prologue.toml"
        return self._load_file(path)

    def load_route(self, route_name):
        """加载角色个人线剧情 routes/xxx.toml"""
        path = self.data_dir / "routes" / f"{route_name}.toml"
        return self._load_file(path)

    def _load_file(self, path):
        data = toml.load(path)
        steps = {}
        for step in data.get("step", []):
            steps[step["id"]] = step
        return steps