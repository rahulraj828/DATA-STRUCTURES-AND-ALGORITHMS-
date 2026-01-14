from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
            xs.add(x1)
            xs.add(x2)

        xs = sorted(xs)
        x_id = {x: i for i, x in enumerate(xs)}

        # ---------- Segment Tree ----------
        class SegmentTree:
            def __init__(self):
                self.n = len(xs) - 1
                self.cover = [0] * (4 * self.n)
                self.length = [0] * (4 * self.n)

            def _push_up(self, idx, l, r):
                if self.cover[idx] > 0:
                    self.length[idx] = xs[r] - xs[l]
                elif l + 1 == r:
                    self.length[idx] = 0
                else:
                    self.length[idx] = self.length[idx*2] + self.length[idx*2+1]

            def update(self, idx, l, r, ql, qr, v):
                if qr <= l or r <= ql:
                    return
                if ql <= l and r <= qr:
                    self.cover[idx] += v
                    self._push_up(idx, l, r)
                    return
                mid = (l + r) // 2
                self.update(idx*2, l, mid, ql, qr, v)
                self.update(idx*2+1, mid, r, ql, qr, v)
                self._push_up(idx, l, r)

        # ---------- Sweep once ----------
        events.sort()
        st = SegmentTree()

        slabs = []
        prev_y = events[0][0]
        i = 0
        n = len(events)

        while i < n:
            y = events[i][0]
            covered_x = st.length[1]
            if y > prev_y and covered_x > 0:
                slabs.append((prev_y, y, covered_x))

            while i < n and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                st.update(1, 0, st.n, x_id[x1], x_id[x2], typ)
                i += 1

            prev_y = y

        # ---------- Find balance line ----------
        total_area = sum((y2 - y1) * w for y1, y2, w in slabs)
        half = total_area / 2
        acc = 0.0

        for y1, y2, w in slabs:
            slab_area = (y2 - y1) * w
            if acc + slab_area >= half:
                return y1 + (half - acc) / w
            acc += slab_area

        return slabs[-1][1]
