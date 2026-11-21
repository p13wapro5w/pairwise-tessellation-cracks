import pytest
import math
from render import tessellation_cracks as mod

CASES = [
    ("edge", 'm.edge_factor(4, 8) == 8'),
    ("shared", 'm.shared(1, 1) is True'),
    ("world", 'm.world_factor(2, 0.5) == 4'),
    ("clamp", 'm.clamp_h(3, 2) == 2'),
    ("normal", 'm.normal((1, 2)) == (-1, -2, 1)'),
    ("double", 'm.double_sided(True) is True'),
    ("lerp", 'm.lerp(0, 10, 0.5) == 5'),
    ("uv", 'm.align_uv(0.52, 0.1) == approx(0.5)'),
    ("shadow", 'm.shadow_factor(4) == 4'),
    ("mip", 'm.mip(4) == 2'),
    ("patches", 'm.patches(3) == 3'),
    ("segments", 'm.segments(8) == 8'),
    ("crack", 'm.crack(0.02, 0.01) is True'),
    ("clamp01", 'm.clamp01(1.2) == 1.0'),
    ("key", 'm.key(2) == "t:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
