---
title: "Problems"
draft: false
math: true
---

I've written a few problems for various math competitions in the past; here are some of my favorites, with some notes.

### National exams 

> #1 ([2021 Korea Winter Program Practice Test 1, Problem 1][kmo_1]). Is there an infinite set of positive integers $S$ satisfying the following condition?
>
><center>
>For every two pairwise distinct elements $a, b$ of $S$, there exists an odd positive integer $k$ such that $a$ divides $b^k-1$. 
></center>

<details>
<summary>Comment/Solution (spoiler)</summary>
I like this problem because it has a really elegant construction that is hard to find: take $S$ to be the set containing the square of all primes $\equiv 3 \pmod{4}$. 
</details>


>#2 ([2022 Korea Winter Program Practice Test 1, Problem 2][kmo_2]).
>You are given a positive integer $n (\ge 2)$ and $n$ polynomials $P_1(x), P_2(x), \ldots, P_n(x)$, each of which has real coefficients and a positive leading coefficient. Provided that the polynomials aren't all identical, prove the inequality
>
>$$ \deg \left(P_1^n+P_2^n+\cdots+P_n^n-nP_1P_2\cdots P_n \right) \ge (n-2) \max_{1\le i\le n} \deg P_i $$
>
>and determine when the equality holds.

<details>
<summary>Comment (spoiler)</summary>
The most recent troll problem made by me. There is a one-liner solution, yet only one out of the ~80 contestants managed to find it.

Many others submitted pages after pages... 
</details>

<details>
<summary>Sidenote to above (spoiler)</summary>
In fact you can prove
$$\deg \left(P_1^n+P_2^n+\cdots+P_n^n-nP_1P_2\cdots P_n \right) = (n-2) \max_{1\le i\le n} \deg P_i + 2 \max_{1 \le i \neq j \le n} \deg (P_i - P_j).$$
</details>

### Online exams 
>#3 ([MOMO 2020 Problem 4][momo_2020_4]; read more about the exam [here][momo][^1]). Suppose that there exist a nonempty set $X \subset \mathbb{R}$ and a function $f: X \rightarrow X$ such that for $x, y \in X$, $f(x) +y \in X$ if and only if $x \neq y$. 
>   
>Prove that there is a real constant $C$ for which $f(x) = - x + C$ for all $x \in X$.

<details>
<summary>Comment</summary>
I regret not sending this problem to the IMO. Nontraditional yet nontrivial, this problem also has connections with abstract algebra, which makes it more intriguing. 
</details>


> #4 ([MOMO 2020 Problem 3][momo_2020_3]). Let $\mathcal{S}(n)$ denote the sum of digits of a positive integer $n$ when written in base ten. Given a positive integer $k$, determine all tuples of pairwise distinct positive integers $(n_1, \cdots, n_k)$ satisfying the following conditions:
>
>- $n_1, n_2, \cdots, n_k$ are not multiples of $10$;
>        
>- all but finitely many positive integers can be expressed in the form $\mathcal{S}(n_1t)+\cdots +\mathcal{S}(n_kt)$ for some positive integer $t$.

<!-- <details>
<summary>Comment</summary>
Very hard problem; the $k=1$ case isn't trivial either. 
</details> -->


> #5 ([MOMO 2020 Problem 6][momo_2020_6]). Call a set of unit squares a *Thumbs-up sign* if it can be obtained by cutting out a unit square from a corner of a $2 \times m$ rectangle. For example, a single unit square and a L-tromino are both Thumbs-up signs. 
>
> Given an integer $n \ge 1$, what is the minimum number of Thumbs-up signs required to cover a $2n \times 2n$ square so that every unit square in the $2n \times 2n$ square is covered by exactly one Thumbs-up sign?

<details>
<summary>Comment</summary>
Co-authored this with a friend, and had so much fun writing this! Very hard problem; partly inspired by <a href="https://artofproblemsolving.com/community/c6h1766862p11573511">Korea Winter Program Practice Test 1 Problem 4</a>. 
</details>

> #6 ([2016][cycmo]). Let $p$ be an odd prime. For each integer $k$ coprime with $p$, define $f(k)$ as the smallest nonnegative integer such that $k$ divides $pf(k)+1$. 
>
>Compute $\left\lfloor \sum_{k=1}^{p-1} \frac{f(k)}{k} \right\rfloor$ in terms of $p$.

<details>
<summary>Comment</summary>
This is the very first problem I wrote as a middle-schooler. Still seems like a decent problem. </details>


### and other miscellaneous exams...
> #7 (SMO[^2] 2019). Let $ABC$ be a scalene triangle with orthocenter $H$. Let $\omega_B, \Omega_B$ be the excircles of triangle $AHB$ corresponding to vertices $A$ and $H$, respectively. Define $\omega_C$ and $\Omega_C$ similarly as the excircles of triangle $AHC$ corresponding to vertices $A$ and $H$.
>
>Prove that an external tangent to $\omega_B$ and $\omega_C$ and an external tangent to $\Omega_B$ and $\Omega_C$ meet on line $AH$.

<details>
<summary>Comment</summary>
The best geometry problem I've written. The statement's so simple yet so hard; no one I personally know managed to solve it.</details>


>#8 (2019; school math club entrance exam). Let $p$ be a odd prime. Prove that among the divisors of $p-1$, the number of quadratic residues modulo $p$ is no less than that of non-quadratic residues modulo $p$.
>
>
>#8* ([2019][mo_ent]; harder variant with the same idea) Let $\Omega(x)$ be an integer-coefficient polynomial with a positive leading coefficient. If $\Omega(0) \neq 0$ and $\Omega(3) \equiv 3 \pmod 4$, then prove that there exists some odd prime $p$ such that
>
>- $\Omega(p) \neq 0$, and
>- among the positive divisors of $|\Omega(p)|$, the number of quadratic residues and non-quadratic residues modulo $p$ are equal.



> #9 (SMO 2018). Find all integers $n$ for which there exists a set $S$ of positive integers satisfying the following conditions:
>
>(1) $S$ contains at least four elements;
>
>(2) for every $a \in S$, there exist elements $b, c \in S$ (not necessarily different) such that $a = b^n - c^n$. 

<details>
<summary>Comment</summary>
The first troll problem I've written. More than 2/3 of the contestants fakesolved the problem, including an IMO gold medalist. 
</details>


[^1]: So I've been deeply involved in two competitions (i.e. wrote most of the problems and ran) so far and helped run numerous others. MOMO had the best problems in my opinion. Check it out!
[^2]: SMO was an IMO-level quarterly math competition ran by students from my high school. No idea if it is still a thing. 

[imo]: https://imo-official.org/
[momo]: https://artofproblemsolving.com/community/q1h1973300p13685505
[momo_2020_3]: https://artofproblemsolving.com/community/q1h1984151p13801370
[momo_2020_4]: https://artofproblemsolving.com/community/q1h1984152p13801379
[momo_2020_6]: https://artofproblemsolving.com/community/q3h1984154p13801399
[kmo_1]: https://artofproblemsolving.com/community/c6h2443251p20260411
[kmo_2]: https://artofproblemsolving.com/community/c6h2904877p25898210
[kmo_3]: https://artofproblemsolving.com/community/c6h1766862p11573511
[cycmo]: https://artofproblemsolving.com/community/c6h1245555p6386603
[mo_ent]: https://artofproblemsolving.com/community/q4h1801529p11963436