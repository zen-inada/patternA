# main.py（悪意テスト：importlibフルパス読込）
from typing import List, Tuple
Board = List[List[List[int]]]

# ★他人の main.py へのフルパスに置き換える
TARGET = "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER/main.py"

from importlib.util import spec_from_file_location, module_from_spec  # ← banned(importlib)
spec = spec_from_file_location("other_ai", TARGET)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)

def get_move(board: Board) -> Tuple[int, int]:
    return mod.get_move(board)
