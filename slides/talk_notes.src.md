# Talk notes

## Slide 1

I am Yaroslav Rogoza. This talk asks what win rate pays a model that does not know the answer. The short answer is that it pays for guessing.

## Slide 2

Models and training data are often compared by win rate. An LLM judge reads two responses and picks the better one. Here Response A names a wrong option and Response B says "I don't know". With the default instruction, {{duelVerdicts}} verdicts of the six judges went to the wrong answer.

## Slide 3

I call the share of such duels that the wrong answer wins the bluff rate. A penalty grader takes a point away for a wrong answer, so its bluff rate is zero. An accuracy grader scores a wrong answer and "I don't know" the same, a tie at one half. Kalai and colleagues blame accuracy grading for hallucination, because guessing never loses. A judge above one half is worse than that.

## Slide 4

Six judges from six developers, on multiple-choice questions each judge answers correctly itself. The wrong answer beats "I don't know" in {{bKnowsMin}} to {{bKnowsMax}} of duels, so every judge sits on the guessing side. The registered test passed for {{hOnePass}} of {{hOneJudges}}. Now the blue dots. Against the right answer in the same words, the same wrong answer wins only {{wrongOverRightMin}} to {{wrongOverRightMax}}.

## Slide 5

So the judges know the answer is wrong. Asked about one response alone, they call the wrong answer incorrect in {{flaggedMin}} to {{flaggedMax}} of cases. On those very questions it still wins {{bFlaggedOnlyMin}} to {{bFlaggedOnlyMax}} of duels against the abstention. GPT-5.6 Luna, asked to explain, wrote that A is incorrect but more responsive, and chose A.

## Slide 6

I registered two more runs before sending any of their questions. On {{cfQuestions}} fresh questions both rates came back for {{cfAllPass}} of {{cfKept}} judges. On {{ffQuestions}} free-form questions with two-sentence replies, the bluff rate stayed above one half for {{ffAboveHalf}} of {{ffKept}}. The exception was {{ffBelowNames}}, at {{ffBelowB}}.

## Slide 7

Does this hold for the prompt of a real leaderboard? I registered one more run with the judge prompt of AlpacaEval 2.0, word for word, on the {{cfQuestions}} fresh questions. All eight judges gave the duel to the wrong answer in {{aeBEightMin}} to {{aeBEightMax}} of cases, and the same wrong answer beat the right one in only {{aeCtrlEightMin}} to {{aeCtrlEightMax}}. All three registered tests held. Two things differ from the leaderboard. I read the identifier the judge wrote, not its probability, and the judges are mine, not GPT-4 Turbo.

## Slide 8

What does this do to a leaderboard? I computed it from the measured rates. A model that guesses among four options beats a model that abstains in {{guessWMin}} to {{guessWMax}} of duels. If two models differ only on the fifth of questions neither knows, guessing is worth {{guessEloMin}} to {{guessEloMax}} Elo points. The accuracy grader gives {{guessEloAcc}}, and the penalty grader takes {{guessEloRule}} away.

## Slide 9

Can we fix the judge? No instruction brought more than {{instrBelowMax}} judges below one half. An explanation helps on free-form questions, where under the MT-Bench prompt only {{ffMtAbove}} of {{ffMtUsable}} stayed above one half. What works is verify-then-compare. Ask the judge first whether the answer is correct, and give the duel to the abstention if it says no. That brought all {{vtcBelow}} judges below one half, {{cfCFourPass}} of them significantly. The cost is right answers it wrongly rejects. A right answer then beats the abstention in {{cfRuleAMin}} to {{cfRuleAMax}} of duels.

## Slide 10

Do bigger judges fix this? I registered two of the largest open models available to me before sending them any question from these sets. On multiple choice, Qwen 3.5 397B gave the duel to the wrong answer in {{lgBQwen}} of cases and GLM 5.2 in {{lgBGLM}}, while the same wrong answer beat the right one in only {{lgCtrlMin}} to {{lgCtrlMax}}. On free-form questions their rates were {{lgFfBQwen}} and {{lgFfBGLM}}. All three registered tests held. The free-form test needed one of the two judges, and Qwen passed it. Reward models, which score one response at a time, behave the same way on multiple choice. Where a model scored the right answer above the wrong one, the wrong answer still scored above "I don't know" on {{rmMcBSepMin}} to {{rmMcBSepMax}} of questions, for all {{rmROnePass}} models. On free-form questions that registered test failed. It passed for {{rmRTwoPass}} model of {{rmCount}}.

## Slide 11

The scope is a bare verdict on short factual questions. The default judge of AlpacaEval 2.0 also reads a single output token. I have no human raters, and a published prompt that asks for an explanation and allows a tie shrinks the effect. So measure the bluff rate of your judge and report it next to any win rate. Or use verify-then-compare and report what it costs in right answers. The code and every judge call are in the repository. Thank you.
