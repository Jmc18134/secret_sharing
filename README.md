# secret_sharing
A Flask project which uses the properties of polynomials in order to encode a secret. The secret is encoded such that N people are given a 'share' of the answer, but at least K of them are required to decode the secret.

For example, you could share the code to a safe amongst 10 people, by giving each of them a 'share' such that any 6 people may bring their shares together and deduce the code, but it is impossible for 5 or fewer people to deduce any information about the code at all.

Much of the code for representing and interpolating polynomials is adapted from "A Programmers Introduction to Mathematics", by Jeremy Kun (https://github.com/pim-book/programmers-introduction-to-mathematics), which contains an exercise that inspired this repo.
