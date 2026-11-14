Evaluation by the key on 300 MedQA test questions (rows 500 to 799). One greedy response per question, no system prompt for the trained models. Intervals are 95% percentile bootstraps over questions (10000 resamples, seed 20261115), paired across models. Rates are shares of all questions. Penalised score: +1 for a right answer, -1 for a wrong or unparsed one, 0 for an abstention, averaged.

| model | abstentions | correct | wrong | unparsed | penalised score |
|---|---|---|---|---|---|
| J, judge, default instruction | 0.0% (0.0% to 0.0%) | 73.0% (68.0% to 78.0%) | 17.0% (13.0% to 21.3%) | 10.0% (6.7% to 13.7%) | +0.460 (+0.360 to +0.560) |
| F, judge, accuracy instruction | 0.0% (0.0% to 0.0%) | 74.3% (69.3% to 79.0%) | 15.7% (11.7% to 20.0%) | 10.0% (6.7% to 13.7%) | +0.487 (+0.387 to +0.580) |
| K, by the key | 0.0% (0.0% to 0.0%) | 67.7% (62.3% to 73.0%) | 17.0% (12.7% to 21.3%) | 15.3% (11.3% to 19.7%) | +0.353 (+0.247 to +0.460) |
| R, random | 0.0% (0.0% to 0.0%) | 68.3% (63.0% to 73.3%) | 17.7% (13.7% to 22.0%) | 14.0% (10.3% to 18.0%) | +0.367 (+0.260 to +0.467) |
| base model, no system prompt | 0.0% (0.0% to 0.0%) | 0.0% (0.0% to 0.0%) | 0.0% (0.0% to 0.0%) | 100.0% (100.0% to 100.0%) | -1.000 (-1.000 to -1.000) |
| base model, assert instruction (reference) | 0.0% (0.0% to 0.0%) | 80.0% (75.3% to 84.3%) | 20.0% (15.7% to 24.7%) | 0.0% (0.0% to 0.0%) | +0.600 (+0.507 to +0.687) |
| base model, hedge instruction (reference) | 0.0% (0.0% to 0.0%) | 80.0% (75.3% to 84.3%) | 19.0% (14.7% to 23.7%) | 1.0% (0.0% to 2.3%) | +0.600 (+0.507 to +0.687) |
| base model, abstain instruction (reference) | 31.7% (26.3% to 37.0%) | 58.0% (52.3% to 63.7%) | 9.0% (6.0% to 12.3%) | 1.3% (0.3% to 2.7%) | +0.477 (+0.400 to +0.553) |

The three reference rows run the base model with the style instruction as system prompt, the way the training pool was generated. They are not part of the registered evaluation.

Paired differences (first minus second, same resampled questions). The share is the bootstrap share of resamples on the wrong side of zero. A star marks a cell with a registered sign (P5c, P5e), where the share counts resamples at zero or with the other sign. In the other cells the share is taken against the sign of the observed difference.

| difference | abstentions | wrong | correct | penalised score |
|---|---|---|---|---|
| J-K | +0.0 pp (+0.0 to +0.0), share 1.0000 * | +0.0 pp (-3.3 to +3.3), share 0.5351 * | +5.3 pp (+0.7 to +10.0), share 0.0125 | +0.107 (+0.013 to +0.200), share 0.9919 * |
| F-K | +0.0 pp (+0.0 to +0.0), share 1.0000 * | -1.3 pp (-4.3 to +1.7), share 0.2277 | +6.7 pp (+2.7 to +11.0), share 0.0008 | +0.133 (+0.053 to +0.220), share 0.9996 * |
| J-F | +0.0 pp (+0.0 to +0.0), share 1.0000 * | +1.3 pp (-1.3 to +4.0), share 0.1874 | -1.3 pp (-4.3 to +2.0), share 0.2382 | -0.027 (-0.087 to +0.040), share 0.2382 * |
| J-R | +0.0 pp (+0.0 to +0.0), share 1.0000 | -0.7 pp (-4.0 to +2.7), share 0.3867 | +4.7 pp (+0.3 to +9.0), share 0.0168 | +0.093 (+0.007 to +0.180), share 0.0168 |

P5c (the J model has a lower abstention rate, a higher wrong-answer rate and a lower penalised score than the K model, each at 0.05): does not hold. Abstention rate +0.0 pp (+0.0 to +0.0), share 1.0000. Wrong-answer rate +0.0 pp (-3.3 to +3.3), share 0.5351. Penalised score +0.107 (+0.013 to +0.200), share 0.9919.

P5e (the F model sits between J and K on abstention rate and penalised score). Abstention rate: J 0.0%, F 0.0%, K 0.0%, the three are equal, so there is no order to test. Penalised score: J +0.460, F +0.487, K +0.353, F between J and K: no, in the predicted order J below F below K: no, F between them in 0.2382 of the resamples.

Models with more than 5% unparsed responses, three raw responses each (cut at 400 characters).

J, judge, default instruction: 30 of 300 unparsed, 6 of them cut by the token limit.

- `medqa-502`: "The next best step is surgical excision. A cold nodule with follicular architecture suspicious for malignancy on FNAB requires histologic evaluation, which can only be obtained via surgical excision."
- `medqa-504`: "The most appropriate next step in management is **B. Tympanostomy tube insertion**.\n\n### Reasoning:\n1.  **Diagnosis**: The child has chronic otitis media with effusion (OME), evidenced by retracted, immobile tympanic membranes and conductive hearing loss.\n2.  **Indication for Intervention**: Current guidelines (e.g., AAO-HNS) recommend tympanostomy tube insertion for children with OME who have:\n  "
- `medqa-535`: "The correct answer is C. It reflects a smaller sample size.\n\nStandard error is inversely related to the square root of the sample size. The pulmharkimab 150 mg/day group had only 202 participants at follow-up, compared to 388 in the 75 mg/day and 395 in the placebo groups. This smaller sample size results in larger standard errors for that group."

F, judge, accuracy instruction: 30 of 300 unparsed, 7 of them cut by the token limit.

- `medqa-502`: "The next best step is surgical excision. A cold nodule with follicular architecture suspicious for malignancy on FNAB requires histologic evaluation, which can only be obtained via surgical excision."
- `medqa-504`: "The most appropriate next step in management is **B. Tympanostomy tube insertion**.\n\n### Reasoning:\n1.  **Diagnosis**: The child has chronic otitis media with effusion (OME), evidenced by retracted, immobile tympanic membranes and conductive hearing loss.\n2.  **Indication for Intervention**: Current guidelines (e.g., AAO-HNS) recommend tympanostomy tube insertion for children with OME who have:\n  "
- `medqa-535`: "The correct answer is C. It reflects a smaller sample size.\n\nStandard error is inversely related to the square root of the sample size. The pulmharkimab 150 mg/day group had only 202 participants at follow-up, compared to 388 in the 75 mg/day and 395 in the placebo groups. This smaller sample size results in larger standard errors for that group."

K, by the key: 46 of 300 unparsed, 13 of them cut by the token limit.

- `medqa-502`: "The next best step is **B. Surgical excision**.\n\n### Reasoning:\n1.  **Diagnosis of a Cold Nodule**: A radionuclide scan showing a \"cold\" nodule indicates that the area is not producing thyroid hormone and has a higher risk of malignancy compared to \"hot\" nodules.\n2.  **FNAB Limitations**: Fine needle aspiration (FNA) is the standard initial test for thyroid nodules. However, FNA has a specific lim"
- `medqa-504`: "The most appropriate next step in management is **B. Tympanostomy tube insertion**.\n\n### Reasoning:\n1.  **Diagnosis**: The child has chronic otitis media with effusion (OME), evidenced by retracted, immobile tympanic membranes and conductive hearing loss.\n2.  **Indication for Intervention**: Current guidelines (e.g., AAO-HNS) recommend tympanostomy tube insertion for children with OME who have:\n  "
- `medqa-505`: "The patient's exposure to sodium fluoroacetate leads to the accumulation of citrate in his cells.\n\nSodium fluoroacetate is metabolized into fluoroacetyl-CoA, which condenses with oxaloacetate to form fluorocitrate. Fluorocitrate is a potent inhibitor of the enzyme aconitase in the Krebs cycle. Aconitase normally catalyzes the conversion of citrate to isocitrate. When aconitase is inhibited, citrat"

R, random: 42 of 300 unparsed, 13 of them cut by the token limit.

- `medqa-502`: "The next best step is surgical excision.\n\n**Answer: B. Surgical excision**"
- `medqa-504`: "The most appropriate next step in management is **B. Tympanostomy tube insertion**.\n\n### Reasoning:\n1.  **Diagnosis**: The child has chronic otitis media with effusion (OME), evidenced by retracted, immobile tympanic membranes and conductive hearing loss.\n2.  **Indication for Intervention**: Current guidelines (e.g., AAO-HNS) recommend tympanostomy tube insertion for children with OME who have:\n  "
- `medqa-513`: "The patient's symptoms of leg numbness and weakness that improve with activity (walking, biking, pushing a cart) are classic for spinal stenosis, where extension opens the canal and flexion narrows it. However, the key clue is that his pain worsens with extension (moving furniture) and improves with flexion (riding a bike, pushing a cart). This pattern is typical of spinal stenosis, where flexion "

base model, no system prompt: 300 of 300 unparsed, 296 of them cut by the token limit.

- `medqa-500`: "Based on the clinical presentation and imaging findings, here is the step-by-step analysis:\n\n1.  **Clinical Picture**: The patient presents with signs of a **small bowel obstruction (SBO)**: intermittent abdominal pain, vomiting, obstipation (inability to pass stool or gas), distension, high-pitched bowel sounds, and an x-ray showing dilated bowel with air-fluid levels.\n2.  **Key Imaging Finding**"
- `medqa-501`: "Based on the clinical presentation, the patient has a surgical site infection caused by **_Staphylococcus aureus_**. The key diagnostic clue is the description of the organism as \"gram-positive cocci in clusters.\" The initial treatment with dicloxacillin, a penicillinase-resistant penicillin, is the standard first-line therapy for methicillin-sensitive _S. aureus_ (MSSA).\n\nHowever, the patient fai"
- `medqa-502`: "Based on the clinical presentation and diagnostic findings, here is the analysis of the next best step:\n\nThe patient presents with a thyroid nodule that has been characterized through a standard diagnostic algorithm:\n1.  **Physical Exam & Labs**: A palpable nodule with normal TSH.\n2.  **Radionuclide Scan**: The nodule is \"cold\" (non-functioning), which places it in a higher risk category for malig"
