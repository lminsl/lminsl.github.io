---
layout: article
title: A problem from IOI 2014
date: 2020-03-21T12:32:17+09:00 ## ISO time notation
tags: ["IOI", "graphs"]
showToc: false
ShowWordCount: false
math: true
---

While solving some competitive programming problems, I found that [IOI 2014 Problem 3][ioi_2014_3], rephrased below in mathematical terms, is quite interesting.

Let \(n \ge 3\) be an integer. Alice and Bob play a game based on a graph of \(n\) points, each labeled from \(0\) to \(n-1\). The graph is initially empty. In the \(i^{\text{th}}\) round of the game, the following occurs in order: 

<br /><center>

Alice picks a pair of integers \((u,v)\) such that \(0\le u < v \le n-1\) that she didn't pick before, then Bob chooses whether \(\{u, v\}\) should be an edge or not. If Bob chooses \(\{u, v\}\) to be an edge, then the edge connecting \(\{u, v\}\) is added to the graph. (Note that there are exactly \(\binom{n}{2}\) rounds.)

</center><br />

Alice wins if, before the last round, she can guarantee whether the graph is connected or not. Bob wins otherwise. Help Bob win the game.

---

The main idea is to seek Bob's losing states.

Suppose that Alice chose $(u,v)$, and Bob has no way to win after then. Let $G$ denote the current graph and $e=uv$.

If Bob chooses to add $e$ at $G$, then $G \cup e$ must be connected; otherwise, Bob can't lose. Thus $e$ is a bridge of $G$, and $G$ has exactly two components.
On the other hand, if Bob chooses to not add $e$, then Alice could claim that the graph is disconnected. The only case is that there is a set $S$ such that

- $u \in S$ and $v \in V(G)-S$;
- all edges between $S$ and $V(G)-S$, except $e$, are already chosen and not an edge of the graph;
- the subgraph induced by $S$ and $V(G)-S$ are both connected, but not all edges were chosen before.

<p align="center">
    <img class="image image--xl" src="/assets/images/posts/ioi_2014_3_image.png"/>
</p>

Hence Bob loses if there is a set $S \subseteq V(G)$ such that $S$ is connected and there is an unchosen edge inside $S$. To avoid this, Bob should add the edge $\{u, v\}$ if all edges between $u$ and the component containing $v$, and all edges between $v$ and the component containing $u$ are chosen before. Bob should not add the edge otherwise. From the above discussions, it is clear that Alice cannot win. Thus we are done. $\blacksquare$

---

[ioi_2014_3]: https://ioinformatics.org/files/ioi2014problem3.pdf
[aops blog]: https://artofproblemsolving.com/community/c1102120