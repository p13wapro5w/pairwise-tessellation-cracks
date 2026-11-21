import math

def edge_factor(a, b):
    """边因子取最大。"""
    raise NotImplementedError("TODO: edge_factor")

def shared(a, b):
    """共享边顶点。"""
    raise NotImplementedError("TODO: shared")

def world_factor(length, base):
    """按世界长度。"""
    raise NotImplementedError("TODO: world_factor")

def clamp_h(height, limit):
    """边缘高度钳制。"""
    raise NotImplementedError("TODO: clamp_h")

def normal(gradient):
    """位移后法线。"""
    raise NotImplementedError("TODO: normal")

def double_sided(enabled):
    """双面渲染。"""
    raise NotImplementedError("TODO: double_sided")

def lerp(a, b, t):
    """因子渐变。"""
    raise NotImplementedError("TODO: lerp")

def align_uv(u, texel):
    """边界 uv 对齐。"""
    raise NotImplementedError("TODO: align_uv")

def shadow_factor(factor):
    """阴影同因子。"""
    raise NotImplementedError("TODO: shadow_factor")

def mip(distance):
    """高度图 mip。"""
    raise NotImplementedError("TODO: mip")

def patches(count):
    """补丁数。"""
    raise NotImplementedError("TODO: patches")

def segments(factor):
    """边段数。"""
    raise NotImplementedError("TODO: segments")

def crack(delta, eps):
    """裂缝判定。"""
    raise NotImplementedError("TODO: crack")

def clamp01(value):
    """归一钳制。"""
    raise NotImplementedError("TODO: clamp01")

def key(patch_id):
    """补丁键。"""
    raise NotImplementedError("TODO: key")
