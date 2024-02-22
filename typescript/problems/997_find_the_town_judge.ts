// In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

// If the town judge exists, then:

// The town judge trusts nobody.
// Everybody (except for the town judge) trusts the town judge.
// There is exactly one person that satisfies properties 1 and 2.
// You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

// Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

function findJudge(n: number, trust: number[][]): number {
    let trusted: Record<number, number> = {};
    let trusts: Record<number, number> = {};

    for (let i = 1; i <= n; i++) {
        trusted[i] = 0;
        trusts[i] = 0
    }
    for (const [a, b] of trust) {
        trusts[a] += 1
        trusted[b] += 1
    }

    for (let i = 1; i <= n; i++) {
        if (trusts[i] === 0 && trusted[i] === n-1) {
            return i
        }
    }
    return -1
};