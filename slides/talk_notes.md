# Talk notes

## Slide 1

I am Yaroslav Rogoza. My project asks what a very common metric rewards. Win rate pays for guessing.

## Slide 2

Models and training data are often compared by win rate. An LLM judge reads two responses and picks the better one. What does that pay a model that does not know the answer? In this duel Response A is wrong and Response B says "I don't know". With the default instruction, nine of the twelve verdicts of the six judges went to the wrong answer.

## Slide 3

I used duels with a key. The responses are fixed sentences, so only the named option and the wording differ. Each judge gets two rates. Rate a is how often a right answer beats the abstention. Rate b is the same for a wrong answer. The hypotheses were registered before the data.

## Slide 4

On questions the judge answers correctly itself, the wrong answer beats "I don't know" in 61% to 94% of duels. The registered test passed for 6 of 6 judges. Against the right answer in the same words, it wins only 2% to 15%. That control came after the registered runs, so I registered it and ran it again.

## Slide 5

A rerun on 150 fresh questions reproduced both rates for four and five of six judges. A second check used 100 free-form questions with replies of two sentences. There the registered test passed for three of three judges, where I had predicted at least five.

## Slide 6

A policy that always answers and is right with probability p wins b plus p times a minus b against a policy that abstains. With b above one half, answering pays at every accuracy. Guessing on a fifth of the questions gives a win rate of 57.6% under Claude Haiku 5.5, about 53 Elo points.

## Slide 7

The judges can tell that the answer is wrong. Asked about a single response, they call the wrong answer incorrect in 66% to 100% of cases. On those questions it still beats the abstention in 63% to 93% of duels. One judge wrote that A is incorrect and more responsive than B, and chose A.

## Slide 8

No change of instruction repaired more than 2 of 6 judges. With a written rationale, three of five judges still gave the duel to the wrong answer. With a provider reasoning mode, in the calls that reasoned, the rate fell to 6% and 10% for two judges and stayed at 66% for a third.

## Slide 9

Next, a judge picked one of three responses per question for a training set. Its pick kept an abstention on 0.3% of questions, and a random pick kept 7.0%. My registered test on fine-tuned models failed. No model abstained under any rule.

## Slide 10

The scope is a bare verdict on short factual questions. Longer or open-ended tasks were not tested, and I have no human raters. Measure b for your judge on about 100 questions with a key, and report it next to any win rate. Or check each answer first, which costs right answers. The code is in the repository. Thank you.
