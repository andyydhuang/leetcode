/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    let pre1 = 0, pre2 = 0;

    while (true) {
      cur = (pre1+pre2)

      yield cur;
      if (pre1 == 0 && pre2 == 0)
        pre2 = 1;
      else {
        pre2 = pre1;
        pre1 = cur;
      }
    }
};


/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */