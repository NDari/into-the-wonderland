#!/usr/bin/env python3
"""Numbers for the worked examples in Book 1, chapter `instructions` [D-009].

Run: python3 code/checks/instructions.py
Standard library only. Every number printed in the chapter comes from this
output. Printed figures from the sources are hard-coded with their location
(see book1/sources/instructions.md, "Mechanism claims to check numerically");
numbers marked "constructed" are made up for illustration and say so in the
chapter. Imported by figures/instructions.py [D-014].
"""
import math


def sigmoid(z):
    """The logistic function of the neuron chapter."""
    return 1.0 / (1.0 + math.exp(-z))


def bt_prob(r_a, r_b):
    """Bradley-Terry: probability that A is preferred to B, from two scores."""
    return sigmoid(r_a - r_b)


def bt_loss(r_win, r_lose):
    """Reward-model loss for one comparison: log loss on the score difference."""
    return -math.log(bt_prob(r_win, r_lose))


DELTAS = (-1.0, 0.0, 0.5, 1.0, 2.0, 3.0)

# Anthropic's conversion between Elo points and preference-model units
# (bai2022training p. 12): 400 / ln 10. The printed Eq. 2.1 has no minus sign
# (see the ledger, IND7); here the usual sign is used: a positive gap means
# this model wins more than half the time.
ELO_PER_UNIT = 400 / math.log(10)


def elo_win(gap):
    return 1.0 / (1.0 + 10 ** (-gap / 400))


def example_bradley_terry():
    print("Example 1: the reward model as logistic regression on a score difference (Bradley-Terry)")
    for d in DELTAS:
        print(f"  score gap {d:+.1f}: P(A preferred) = {sigmoid(d):.3f}; "
              f"loss if A was preferred = {-math.log(sigmoid(d)):.3f}")
    print(f"  shifting both scores by +5: sigma((2+5)-(1+5)) = {bt_prob(7, 6):.3f}, "
          f"same as sigma(2-1) = {bt_prob(2, 1):.3f}")
    print(f"  a labeler prefers B although the model scored A one unit higher: "
          f"loss {bt_loss(0.0, 1.0):.3f} (versus {bt_loss(1.0, 0.0):.3f} if A had been preferred)")
    print()


def example_elo():
    print("Example 2: Elo points and reward units")
    print(f"  400 / ln 10 = {ELO_PER_UNIT:.1f} Elo points per unit of reward (Anthropic prints 174)")
    print(f"  a 174-point Elo gap: win probability {elo_win(174):.3f}; a reward gap of 1: {sigmoid(1):.3f}")
    print(f"  a 400-point Elo gap: {elo_win(400):.3f} (10 to 1 odds); in reward units {400 / ELO_PER_UNIT:.2f}")
    print()


# InstructGPT, Table 6 (ouyang2022training p. 33): training prompts by source.
SFT_LABELER, SFT_CUSTOMER = 11_295, 1_430
RM_LABELER, RM_CUSTOMER = 6_623, 26_584
PPO_CUSTOMER = 31_144
# Compute in petaflop/s-days (p. 17).
PFSD_SFT, PFSD_PPO, PFSD_GPT3 = 4.9, 60.0, 3640.0
# Llama 2 preference data (touvron2023llama2 Table 6, p. 11).
LLAMA2_META, LLAMA2_TOTAL = 1_418_091, 2_919_326


def example_instructgpt_data():
    print("Example 3: InstructGPT's data and compute, and Llama 2's preference data")
    sft = SFT_LABELER + SFT_CUSTOMER
    rm = RM_LABELER + RM_CUSTOMER
    print(f"  SFT prompts {SFT_LABELER:,} + {SFT_CUSTOMER:,} = {sft:,}; written by labelers {SFT_LABELER / sft:.1%}, "
          f"from customers {SFT_CUSTOMER / sft:.1%}")
    print(f"  RM prompts {RM_LABELER:,} + {RM_CUSTOMER:,} = {rm:,}; from customers {RM_CUSTOMER / rm:.1%}")
    print(f"  PPO prompts {PPO_CUSTOMER:,} (all from customers)")
    pairs = {k: math.comb(k, 2) for k in range(4, 10)}
    print("  pairs per ranking of K responses: " + ", ".join(f"K={k}: {v}" for k, v in pairs.items()))
    print(f"  {rm:,} prompts give between {rm * pairs[4]:,} and {rm * pairs[9]:,} pairs")
    print(f"  compute: SFT {PFSD_SFT / PFSD_GPT3:.2%} of GPT-3's pretraining, PPO-ptx {PFSD_PPO / PFSD_GPT3:.2%}, "
          f"together {(PFSD_SFT + PFSD_PPO) / PFSD_GPT3:.2%}")
    print(f"  parameters: 175 / 1.3 = {175 / 1.3:.1f}")
    print(f"  Llama 2: {LLAMA2_META:,} of {LLAMA2_TOTAL:,} comparisons were Meta's own: "
          f"{LLAMA2_META / LLAMA2_TOTAL:.1%}")
    print()


BETA_INSTRUCTGPT = 0.02   # ouyang2022training p. 42


def penalized(reward, log_ratio, beta=BETA_INSTRUCTGPT):
    """Reward seen by the RL step: reward minus beta times the log-ratio (nats)."""
    return reward - beta * log_ratio


# Constructed: two candidate answers to one prompt.
CANDIDATES = (("A", 2.0, 10.0), ("B", 2.6, 60.0))


def example_kl():
    print("Example 4: the KL penalty with InstructGPT's beta = 0.02 (constructed answers)")
    print(f"  an answer 50 nats more probable than under the SFT model pays {BETA_INSTRUCTGPT * 50:.1f} reward units")
    for name, r, lr in CANDIDATES:
        print(f"  answer {name}: reward {r:.1f}, log-ratio {lr:.0f} nats: "
              f"penalty {BETA_INSTRUCTGPT * lr:.1f}, penalized reward {penalized(r, lr):.1f}")
    print()


BETA_DPO = 0.1
# Constructed log-probabilities (summed over the answer's tokens), in nats.
DPO_PREFERRED = (-40.0, -38.0)   # reference model, trained model
DPO_REJECTED = (-35.0, -36.0)


def example_dpo():
    print("Example 5: DPO's implicit reward (constructed log-probabilities, beta = 0.1)")
    rw = BETA_DPO * (DPO_PREFERRED[1] - DPO_PREFERRED[0])
    rl = BETA_DPO * (DPO_REJECTED[1] - DPO_REJECTED[0])
    print(f"  preferred: {DPO_PREFERRED[0]} -> {DPO_PREFERRED[1]}: implicit reward {rw:+.2f}")
    print(f"  rejected:  {DPO_REJECTED[0]} -> {DPO_REJECTED[1]}: implicit reward {rl:+.2f}")
    print(f"  difference {rw - rl:.2f}; sigma = {sigmoid(rw - rl):.3f}; loss {-math.log(sigmoid(rw - rl)):.3f}")
    print(f"  before training (both log-ratios 0): sigma(0) = {sigmoid(0):.3f}; loss {-math.log(0.5):.3f}")
    print(f"  the rejected answer is still the more probable one: {math.exp(DPO_REJECTED[1] - DPO_PREFERRED[1]):.0f} "
          f"times as probable as the preferred one under the trained model")
    print()


def kl_best_of_n(n):
    """gao2022scaling p. 4: KL of best-of-n sampling from the initial policy, in nats."""
    return math.log(n) - (n - 1) / n


def example_best_of_n():
    print("Example 6: best-of-n moves the model further as n grows (Gao et al.'s analytic KL)")
    for n in (1, 2, 4, 10, 16, 30, 64, 1000):
        print(f"  n = {n:>4}: {kl_best_of_n(n):.3f} nats")
    print()


# XSTest Table 1 (rottger2024xstest p. 5380): refusal of 250 safe prompts,
# full and partial, in percent.
XSTEST_SAFE = 250
XSTEST = (
    ("Llama 2 70B chat, original system prompt", 38.0, 21.6),
    ("Llama 2 70B chat, no system prompt", 14.0, 15.6),
    ("Mistral 7B Instruct, no system prompt", 0.8, 0.8),
    ("Mistral 7B Instruct, guardrail prompt", 9.6, 9.2),
    ("GPT-4", 6.4, 2.0),
)


def example_refusals():
    print("Example 7: refusal rates")
    for name, full, part in XSTEST:
        print(f"  {name}: {full}% full + {part}% partial = {full + part:.1f}% "
              f"({round(full * XSTEST_SAFE / 100)} + {round(part * XSTEST_SAFE / 100)} of {XSTEST_SAFE})")
    a = XSTEST[0][1] + XSTEST[0][2]
    b = XSTEST[1][1] + XSTEST[1][2]
    print(f"  removing the system prompt: {a:.1f}% -> {b:.1f}%, ratio {a / b:.2f}")
    print("  Llama 2 false refusals (p. 67): 0.006% to 0.05% on helpfulness prompts, 15% to 27% on borderline")
    print(f"  ratio of the upper ends: 27 / 0.05 = {27 / 0.05:.0f}")
    print()


def example_calibration():
    print("Example 8: an overconfident answer and a temperature of 2.5 (constructed)")
    p = 0.99
    gap = math.log(p / (1 - p))
    print(f"  two options, 0.99 on one: score gap ln(99) = {gap:.3f}")
    print(f"  divided by T = 2.5: {gap / 2.5:.3f}; probability {sigmoid(gap / 2.5):.3f}")
    print(f"  GPT-4 calibration error, post-trained / pretrained: 0.074 / 0.007 = {0.074 / 0.007:.1f}")
    print()


def example_printed():
    print("Example 9: other printed results, as ratios")
    print(f"  InstructGPT closed-domain hallucination 21% vs GPT-3 41%: ratio {21 / 41:.2f}")
    print(f"  Sharma et al.: GPT-4 admits a mistake on 42%, Claude 1.3 on 98% of challenged questions")
    print(f"  LIMA: equivalent or preferred to GPT-4 in 43%, so GPT-4 preferred in {100 - 43}%")
    print(f"  Llama 2 SFT annotations 27,540 vs InstructGPT SFT prompts {SFT_LABELER + SFT_CUSTOMER:,}: "
          f"{27_540 / (SFT_LABELER + SFT_CUSTOMER):.1f} times; LIMA 1,000")
    print()


if __name__ == "__main__":
    example_bradley_terry()
    example_elo()
    example_instructgpt_data()
    example_kl()
    example_dpo()
    example_best_of_n()
    example_refusals()
    example_calibration()
    example_printed()
