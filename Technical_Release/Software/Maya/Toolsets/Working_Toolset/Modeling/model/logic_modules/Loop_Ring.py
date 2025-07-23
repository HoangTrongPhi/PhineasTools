"""
    Chức năng:
    - Mở rộng hoặc thu hẹp vòng lặp và vòng đai của các cạnh trong Maya.
    - Hỗ trợ các thao tác như chọn vòng lặp, vòng đai, và các thao tác liên quan đến cạnh.
"""


import maya.cmds as cmds
import maya.mel as mel

# ----------- Grow / Shrink / Dot Loop & Ring -----------

def grow_loop(get_all_sel):
    """Mở rộng selection cạnh hiện tại thành toàn bộ edge loop"""
    chkEdge = cmds.filterExpand(sm=32, ex=True)
    if chkEdge is None:
        return
    firstSel = get_all_sel()
    mel.eval('polySelectEdgesEveryN "edgeLoopOrBorder" 1;')
    loopEdges = get_all_sel()
    verts = cmds.polyListComponentConversion(firstSel, tv=1)
    edges = cmds.ls(cmds.polyListComponentConversion(verts, fv=1, te=1), fl=1)
    fEdges = list(set(edges) & set(loopEdges))
    cmds.select(fEdges, r=1)


def shrink_loop(get_all_sel, get_sandt):
    """Thu hẹp selection edge loop."""
    chkEdge = cmds.filterExpand(sm=32, ex=True)
    if chkEdge is None or len(chkEdge) < 3:
        return
    firstSel = get_all_sel()
    cmds.select(firstSel)
    mel.eval('ConvertSelectionToVertexPerimeter;')
    edges = cmds.ls(cmds.polyListComponentConversion(get_all_sel(), te=1), fl=1)
    mel.eval(f'doMenuComponentSelection("{get_sandt("t")}", "edge");')
    cmds.select(list(set(firstSel) - set(edges)))

    # Remove Borders
    for brdr in firstSel:
        vtx = cmds.ls(cmds.polyListComponentConversion(brdr, fe=True, tv=True), fl=1)
        bface = cmds.ls(cmds.polyListComponentConversion(vtx, fv=True, tf=True), fl=1)
        if len(bface) == 4:
            cmds.select(brdr, d=1)


def grow_ring(get_all_sel):
    """Mở rộng selection cạnh hiện tại thành toàn bộ edge ring."""
    chkEdge = cmds.filterExpand(sm=32, ex=True)
    if chkEdge is None:
        return
    firstSel = get_all_sel()
    mel.eval('polySelectEdgesEveryN "edgeRing" 1;')
    loopEdges = get_all_sel()
    cmds.select(firstSel)
    faces = cmds.polyListComponentConversion(firstSel, fe=1, tf=1)
    edges = cmds.ls(cmds.polyListComponentConversion(faces, ff=1, te=1), fl=1)
    cmds.select(list(set(edges) & set(loopEdges)), r=1)

def shrink_ring(get_all_sel):
    """Thu hẹp selection edge ring."""
    chkEdge = cmds.filterExpand(sm=32, ex=True)
    if chkEdge is None or len(chkEdge) < 3:
        return
    firstSel = get_all_sel()
    cmds.select(firstSel)
    verts = cmds.ls(cmds.polyListComponentConversion(get_all_sel(), tv=1), fl=1)
    cmds.select(verts)
    mel.eval('ConvertSelectionToEdgePerimeter;')
    edges = get_all_sel()
    cmds.select(list(set(firstSel) - set(edges)), r=1)
    # Remove Border Edges
    for brdr in firstSel:
        bedge = cmds.ls(cmds.polyListComponentConversion(brdr, fe=True, tf=True), fl=1)
        if len(bedge) == 1:
            cmds.select(brdr, d=1)

def dot_loop(get_all_sel, in_line_message, int_gap_field=None):
    """Chọn dạng chấm cách (dot) trên loop (edges hoặc 2 faces)."""
    val = 2
    # Đọc giá trị gap nếu có
    if int_gap_field is not None:
        try:
            val = cmds.intField(int_gap_field, q=1, value=1) + 1
        except Exception:
            pass
    if cmds.filterExpand(sm=32, ex=True):  # Edge
        mel.eval(f'polySelectEdgesEveryN "edgeLoopOrBorder" {val};')
    elif cmds.filterExpand(sm=34, ex=True):  # Face
        sel = get_all_sel()
        if len(sel) != 2:
            in_line_message("Select Two adjacent Faces.")
            return
        e = cmds.polyListComponentConversion(sel, te=1, internal=1)
        if not e:
            in_line_message("Select Two adjacent Faces.")
            return
        cmds.select(e)
        mel.eval('polySelectEdgesEveryN "edgeRing" 1;')
        tempEdge = get_all_sel()
        dotFaces = cmds.ls(cmds.polyListComponentConversion(tempEdge, tf=1), fl=1)
        edges = cmds.polyListComponentConversion(dotFaces, te=1)
        cmds.select(edges)
        finalEdges = list(set(get_all_sel()) - set(tempEdge))
        cmds.select(finalEdges[-1])
        dot_loop(get_all_sel, in_line_message, int_gap_field)
        postDotFace = cmds.ls(cmds.polyListComponentConversion(get_all_sel(), tf=1), fl=1)
        finalFaces = list(set(postDotFace) & set(dotFaces))
        cmds.select(finalFaces)



def dot_ring(int_gap_field=None):
    """Chọn dạng chấm cách (dot) trên ring."""
    val = 2
    if int_gap_field is not None:
        try:
            val = cmds.intField(int_gap_field, q=1, value=1) + 1
        except Exception:
            pass
    chkEdge = cmds.filterExpand(sm=32, ex=True)
    if chkEdge is None:
        return
    mel.eval(f'polySelectEdgesEveryN "edgeRing" {val};')



def hard_edge(get_all_sel, in_line_message, edge_mode_func):
    """Chọn các cạnh cứng (hard edge) của mesh hiện tại."""
    sel = get_all_sel()
    if not sel:
        return in_line_message("Select Some objects.")
    mesh = sel[0].split(".")[0]
    cmds.select(f"{mesh}.e[0]", r=1)
    edge_mode_func()
    mel.eval('polySelectConstraint -mode 3 -type 0x8000 -sm 1;resetPolySelectConstraint;')
    # edges = get_all_sel()



def uv_edge(get_all_sel, in_line_message, edge_mode_func):
    """Chọn các cạnh biên UV (UV border edge)."""
    sel = get_all_sel()
    if not sel:
        return in_line_message("Select Some objects.")
    mesh = sel[0].split(".")[0]
    cmds.select(f"{mesh}.e[0]", r=1)
    edge_mode_func()
    temp = cmds.ls(f"{mesh}.map[*]")
    cmds.select(temp)
    mel.eval('polySelectBorderShell 1;')
    mel.eval('PolySelectConvert 20;')
    pEdge = get_all_sel()
    edgeDeselect = []
    for edg in pEdge:
        uvs = cmds.ls(cmds.polyListComponentConversion(edg, tuv=1), fl=1)
        if len(uvs) <= 2:
            edgeDeselect.append(edg)
    cmds.select(edgeDeselect, d=1)
    edge_mode_func()



def point_to_point(get_sandt, get_all_sel, edge_mode_func):
    """Chọn đường đi ngắn nhất giữa 2 điểm (shortest edge path)."""
    if cmds.filterExpand(sm=31, ex=1) is None:
        return
    trans = get_sandt("t")
    sel = get_all_sel()
    if len(sel) == 2:
        sv1 = int(str(sel[0]).split("[")[-1].split("]")[0])
        sv2 = int(str(sel[1]).split("[")[-1].split("]")[0])
        edge_mode_func()
        cmds.select(cl=1)
        # Không có sẵn shortestEdgePath trong cmds, nên phải dùng mel hoặc API nếu cần
        mel.eval(f'polySelectShortestEdgePath {trans} {sv1} {sv2};')

