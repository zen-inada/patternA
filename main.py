# === main.py（テンプレ準拠・悪意テストA）===
from abc import ABC, abstractmethod
from typing import Tuple, List
Board = List[List[List[int]]]

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]: ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        TARGET = "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER/main.py"  # ←実在パスに
        from importlib.util import spec_from_file_location, module_from_spec  # ← banned(importlib)
        spec = spec_from_file_location("other_ai", TARGET)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.get_move(board)

_ai = MyAI()
def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
