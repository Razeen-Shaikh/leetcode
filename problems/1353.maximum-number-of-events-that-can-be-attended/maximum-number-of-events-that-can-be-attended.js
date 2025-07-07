/**
 * @param {number[][]} events
 * @return {number}
 */
class DSU {
  constructor(n) {
    this.parent = Array.from({ length: n + 2 }, (_, i) => i);
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(x, y) {
    const px = this.find(x);
    const py = this.find(y);
    this.parent[px] = py;
  }
}

const maxEvents = function (events) {
  events.sort((a, b) => a[1] - b[1]);

  let maxDay = 0;
  for (const [, e] of events) {
    if (e > maxDay) {
      maxDay = e;
    }
  }

  const dsu = new DSU(maxDay);

  let attended = 0;

  for (const [s, e] of events) {
    const day = dsu.find(s);
    if (day <= e) {
      attended++;
      dsu.union(day, day + 1);
    }
  }

  return attended;
};
