// Write a generator function that returns a generator object which yields the fibonacci sequence.

// The fibonacci sequence is defined by the relation Xn = Xn-1 + Xn-2.

// The first few numbers of the series are 0, 1, 1, 2, 3, 5, 8, 13.

function* fibGenerator(): Generator<number, any, number> {
    let fib: number[] = []
    yield 0;
    fib.push(0);
    yield 1;
    fib.push(1);
    while(true) {
        const curr = fib[fib.length-1] + fib[fib.length-2];
        yield curr
        fib.push(curr);
    }
};



/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */