import math


def edge_factor(a, b):
    """边因子取最大。

    相邻两块共享一条边时，两侧的细分因子可能不同。取两者最大值，
    使两侧都按更细的段数细分，边界顶点才能一一对应，不会裂开。
    """
    return max(a, b)


def shared(a, b):
    """共享边顶点。

    两块在同一位置生成的顶点视为同一个顶点；只有位置一致才共享。
    """
    return a == b


def world_factor(length, base):
    """按世界长度。

    细分因子按世界空间边长计算，不随相机距离/屏幕空间边长变化，
    避免相机拉远后因子变小、裂缝变大。
    """
    if base <= 0:
        return 0.0
    return length / base


def clamp_h(height, limit):
    """边缘高度钳制。

    位移贴图在边界处可能采样越界；把高度钳制到合法范围，
    保证两侧边界得到相同的位移高度。
    """
    return min(height, limit)


def normal(gradient):
    """位移后法线。

    由位移后表面的高度梯度重建法线：(-dh/dx, -dh/dy, 1)。
    位移改变了高度场，法线必须随之重算，否刚裂缝处光照突变。
    """
    gx, gy = gradient
    return (-gx, -gy, 1)


def double_sided(enabled):
    """双面渲染。

    关闭背面剔除，使从下方观察地形时仍有可见表面。
    """
    return bool(enabled)


def lerp(a, b, t):
    """因子渐变。

    在距离阈值附近对因子做线性插值，使细分等级平滑过渡，
    避免走过阈值时地面突然弹跳。
    """
    return a + (b - a) * t


def align_uv(u, texel):
    """边界 uv 对齐。

    将边界 uv 吸附到纹素网格上，使相邻块在边界采样到同一纹素，
    位移高度不会相差半个采样。
    """
    if texel <= 0:
        return u
    return math.floor(u / texel) * texel


def shadow_factor(factor):
    """阴影同因子。

    阴影通道与主通道使用相同细分因子，避免阴影边缘出现锯齿缝。
    """
    return factor


def mip(distance):
    """高度图 mip。

    按距离选取 mip 层级；远处不应使用过高的 mip，
    以保持位移幅度、避免接缝更明显。
    """
    if distance <= 0:
        return 0
    return math.log2(distance)


def patches(count):
    """补丁数。"""
    return count


def segments(factor):
    """边段数。"""
    return int(factor)


def crack(delta, eps):
    """裂缝判定。

    两侧顶点位置差超过容差即认为出现裂缝。
    """
    return abs(delta) > eps


def clamp01(value):
    """归一钳制。"""
    return max(0.0, min(1.0, value))


def key(patch_id):
    """补丁键。"""
    return f"t:{patch_id}"
