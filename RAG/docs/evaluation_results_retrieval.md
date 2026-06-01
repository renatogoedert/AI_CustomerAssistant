## Semantic Retrieval

    === Running Evaluation ===

    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.06s  generation=54.728s  total=56.788s
    Words       : 301
    ----------------------------------------------------------------------
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.052s  generation=85.517s  total=87.569s
    Words       : 719
    ----------------------------------------------------------------------
    [TQ-003] How much RAM do I need for video editing?
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.05s  generation=49.497s  total=51.547s
    Words       : 217
    ----------------------------------------------------------------------
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.055s  generation=45.258s  total=47.313s
    Words       : 257
    ----------------------------------------------------------------------
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=2.055s  generation=55.201s  total=57.256s
    Words       : 350
    ----------------------------------------------------------------------
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.071s  generation=65.143s  total=67.214s
    Words       : 399
    ----------------------------------------------------------------------
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Retrieval : 1/3 (33%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.066s  generation=55.449s  total=57.515s
    Words       : 331
    ----------------------------------------------------------------------
    [TQ-008] How do I set up a good home office on a budget?
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.072s  generation=67.819s  total=69.891s
    Words       : 424
    ----------------------------------------------------------------------
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=53.087s  total=55.153s
    Words       : 455
    ----------------------------------------------------------------------
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Retrieval : 1/1 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.061s  generation=47.403s  total=49.464s
    Words       : 232
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 72%
    Faithfulness        : {'YES': 5, 'NO': 3, 'PARTIAL': 1, 'UNKNOWN': 1}
    Avg retrieval time  : 2.061s
    Avg generation time : 57.91s
    Avg total latency   : 59.971s
    Avg response words  : 368

## Hibrid Retrieval

    === Running Evaluation ===

    [Retriever] Semantic: ['ticket_018', 'ticket_005', 'policy_001', 'ticket_028', 'faq_009']
    [Retriever] BM25    : ['ticket_018', 'ticket_019', 'faq_016', 'policy_008', 'policy_006']
    [Retriever] Merged  : ['ticket_018', 'ticket_005', 'ticket_019', 'policy_001', 'faq_016']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_005', 'ticket_019', 'policy_001', 'faq_016']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.086s  generation=157.615s  total=159.701s
    Words       : 349
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['ticket_025', 'faq_016', 'faq_006', 'faq_008', 'ticket_006']
    [Retriever] BM25    : ['ticket_025', 'faq_015', 'faq_016', 'faq_008', 'faq_019']
    [Retriever] Merged  : ['ticket_025', 'faq_016', 'faq_015', 'faq_006', 'faq_008']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_015', 'faq_006', 'faq_008']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=7.276s  generation=62.343s  total=69.619s
    Words       : 460
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['faq_006', 'faq_015', 'ticket_035', 'faq_005', 'faq_019']
    [Retriever] BM25    : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_004']
    [Retriever] Merged  : ['faq_006', 'faq_015', 'faq_011', 'ticket_035', 'faq_019']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_015', 'faq_011', 'ticket_035', 'faq_019']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.067s  generation=45.61s  total=47.677s
    Words       : 306
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['ticket_001', 'faq_001', 'faq_018', 'ticket_011', 'ticket_016']
    [Retriever] BM25    : ['faq_001', 'faq_020', 'faq_008', 'faq_013', 'faq_018']
    [Retriever] Merged  : ['ticket_001', 'faq_001', 'faq_020', 'faq_018', 'faq_008']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_001', 'faq_020', 'faq_018', 'faq_008']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.097s  generation=42.157s  total=44.254s
    Words       : 174
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['faq_009', 'policy_002', 'faq_017', 'ticket_010', 'ticket_021']
    [Retriever] BM25    : ['faq_009', 'ticket_036', 'faq_017', 'ticket_025', 'ticket_019']
    [Retriever] Merged  : ['faq_009', 'policy_002', 'ticket_036', 'faq_017', 'ticket_010']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'policy_002', 'ticket_036', 'faq_017', 'ticket_010']
    Retrieval : 2/4 (50%)
    Faithful  : NO
    Latency     : retrieval=2.045s  generation=62.34s  total=64.385s
    Words       : 504
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['ticket_015', 'ticket_039', 'ticket_026', 'faq_011', 'faq_004']
    [Retriever] BM25    : ['faq_009', 'faq_019', 'ticket_015', 'faq_017', 'faq_011']
    [Retriever] Merged  : ['ticket_015', 'faq_009', 'ticket_039', 'faq_019', 'ticket_026']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'faq_009', 'ticket_039', 'faq_019', 'ticket_026']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.063s  generation=42.632s  total=44.695s
    Words       : 234
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['faq_012', 'faq_021', 'faq_003', 'faq_005', 'faq_010']
    [Retriever] BM25    : ['faq_012', 'ticket_038', 'ticket_024', 'faq_005', 'faq_016']
    [Retriever] Merged  : ['faq_012', 'faq_021', 'ticket_038', 'faq_003', 'ticket_024']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_021', 'ticket_038', 'faq_003', 'ticket_024']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.055s  generation=61.633s  total=63.688s
    Words       : 414
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['faq_015', 'ticket_035', 'faq_006', 'ticket_026', 'faq_012']
    [Retriever] BM25    : ['ticket_026', 'faq_015', 'faq_017', 'ticket_035', 'faq_014']
    [Retriever] Merged  : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_017']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_017']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.079s  generation=62.352s  total=64.431s
    Words       : 511
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['faq_020', 'ticket_013', 'ticket_032', 'ticket_021', 'ticket_024']
    [Retriever] BM25    : ['faq_020', 'faq_012', 'ticket_035', 'faq_005', 'faq_016']
    [Retriever] Merged  : ['faq_020', 'ticket_013', 'faq_012', 'ticket_032', 'ticket_035']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_013', 'faq_012', 'ticket_032', 'ticket_035']
    Retrieval : 1/2 (50%)
    Faithful  : NO
    Latency     : retrieval=2.093s  generation=49.813s  total=51.906s
    Words       : 338
    ----------------------------------------------------------------------
    [Retriever] Semantic: ['policy_007', 'faq_009', 'faq_012', 'faq_006', 'ticket_037']
    [Retriever] BM25    : ['policy_007', 'faq_017', 'faq_013', 'ticket_017', 'policy_008']
    [Retriever] Merged  : ['policy_007', 'faq_009', 'faq_017', 'faq_012', 'faq_013']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_009', 'faq_017', 'faq_012', 'faq_013']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.056s  generation=51.257s  total=53.313s
    Words       : 349
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 62%
    Faithfulness        : {'YES': 6, 'NO': 4, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg retrieval time  : 2.592s
    Avg generation time : 63.775s
    Avg total latency   : 66.367s
    Avg response words  : 364

    Note: ROUGE/BLEU/semantic similarity not computed — dataset has no expected answer strings.

## Hybrid Retrieval - Formating Output 1 - policy; 2 - faq; 2 - ticket;

    === Running Evaluation ===

    [Retriever] policy  : ['policy_001']
    [Retriever] faqs    : ['faq_016', 'faq_008']
    [Retriever] tickets : ['ticket_018', 'ticket_019']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['policy_001', 'faq_016', 'faq_008', 'ticket_018', 'ticket_019']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.088s  generation=154.377s  total=156.465s
    Words       : 265
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : ['faq_015', 'faq_016']
    [Retriever] tickets : ['ticket_025', 'ticket_036']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['policy_002', 'faq_015', 'faq_016', 'ticket_025', 'ticket_036']
    Retrieval : 2/4 (50%)
    Faithful  : NO
    Latency     : retrieval=7.264s  generation=62.769s  total=70.033s
    Words       : 496
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_007']
    [Retriever] faqs    : ['faq_006', 'faq_011']
    [Retriever] tickets : ['ticket_026', 'ticket_023']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['policy_007', 'faq_006', 'faq_011', 'ticket_026', 'ticket_023']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.422s  generation=41.641s  total=44.063s
    Words       : 288
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_001']
    [Retriever] faqs    : ['faq_001', 'faq_020']
    [Retriever] tickets : ['ticket_016', 'ticket_001']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['policy_001', 'faq_001', 'faq_020', 'ticket_016', 'ticket_001']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.097s  generation=38.85s  total=40.947s
    Words       : 177
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : ['faq_009', 'faq_017']
    [Retriever] tickets : ['ticket_036', 'ticket_025']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['policy_002', 'faq_009', 'faq_017', 'ticket_036', 'ticket_025']
    Retrieval : 2/4 (50%)
    Faithful  : NO
    Latency     : retrieval=2.051s  generation=58.931s  total=60.982s
    Words       : 489
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_004']
    [Retriever] faqs    : ['faq_009', 'faq_019']
    [Retriever] tickets : ['ticket_015', 'ticket_023']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['policy_004', 'faq_009', 'faq_019', 'ticket_015', 'ticket_023']
    Retrieval : 1/3 (33%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.074s  generation=33.536s  total=35.61s
    Words       : 164
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_004']
    [Retriever] faqs    : ['faq_012', 'faq_005']
    [Retriever] tickets : ['ticket_038', 'ticket_024']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['policy_004', 'faq_012', 'faq_005', 'ticket_038', 'ticket_024']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.058s  generation=58.346s  total=60.404s
    Words       : 417
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_006']
    [Retriever] faqs    : ['faq_015', 'faq_017']
    [Retriever] tickets : ['ticket_026', 'ticket_035']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['policy_006', 'faq_015', 'faq_017', 'ticket_026', 'ticket_035']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.08s  generation=46.236s  total=48.316s
    Words       : 308
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_001']
    [Retriever] faqs    : ['faq_020', 'faq_012']
    [Retriever] tickets : ['ticket_035', 'ticket_024']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['policy_001', 'faq_020', 'faq_012', 'ticket_035', 'ticket_024']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.08s  generation=44.65s  total=46.73s
    Words       : 291
    ----------------------------------------------------------------------
    [Retriever] policy  : ['policy_007']
    [Retriever] faqs    : ['faq_017', 'faq_013']
    [Retriever] tickets : ['ticket_017', 'ticket_020']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_017', 'faq_013', 'ticket_017', 'ticket_020']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.054s  generation=41.79s  total=43.844s
    Words       : 229
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 60%
    Faithfulness        : {'YES': 5, 'NO': 4, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg retrieval time  : 2.627s
    Avg generation time : 58.113s
    Avg total latency   : 60.739s
    Avg response words  : 312

    Note: ROUGE/BLEU/semantic similarity not computed — dataset has no expected answer strings.

## Hybrid Retrieval + metadata filtering (category)

    === Running Evaluation ===

    [Retriever] Filters : {'category': 'returns'}
    [Retriever] policy  : ['policy_001']
    [Retriever] faqs    : []
    [Retriever] tickets : ['ticket_018', 'ticket_028']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.033s  generation=60.897s  total=60.93s
    Words       : 433
    ----------------------------------------------------------------------
    [Retriever] Filters : none
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : ['faq_015', 'faq_016']
    [Retriever] tickets : ['ticket_025', 'ticket_036']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['policy_002', 'faq_015', 'faq_016', 'ticket_025', 'ticket_036']
    Retrieval : 2/4 (50%)
    Faithful  : NO
    Latency     : retrieval=2.062s  generation=60.018s  total=62.08s
    Words       : 433
    ----------------------------------------------------------------------
    [Retriever] Filters : none
    [Retriever] policy  : ['policy_007']
    [Retriever] faqs    : ['faq_006', 'faq_011']
    [Retriever] tickets : ['ticket_026', 'ticket_023']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['policy_007', 'faq_006', 'faq_011', 'ticket_026', 'ticket_023']
    Retrieval : 1/3 (33%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.078s  generation=33.55s  total=35.628s
    Words       : 134
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'delivery_issues'}
    [Retriever] policy  : []
    [Retriever] faqs    : []
    [Retriever] tickets : ['ticket_016', 'ticket_027']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_016', 'ticket_027']
    Retrieval : 1/2 (50%)
    Faithful  : NO
    Latency     : retrieval=2.075s  generation=25.774s  total=27.849s
    Words       : 70
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'warranty'}
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : []
    [Retriever] tickets : []
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['policy_002']
    Retrieval : 0/4 (0%)
    Faithful  : YES
    Latency     : retrieval=2.075s  generation=37.176s  total=39.251s
    Words       : 199
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'bulk_orders'}
    [Retriever] policy  : []
    [Retriever] faqs    : []
    [Retriever] tickets : ['ticket_023', 'ticket_039']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_023', 'ticket_039']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.06s  generation=43.791s  total=45.851s
    Words       : 265
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'pre_sales'}
    [Retriever] policy  : []
    [Retriever] faqs    : []
    [Retriever] tickets : ['ticket_020', 'ticket_035']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['ticket_020', 'ticket_035']
    Retrieval : 0/3 (0%)
    Faithful  : NO
    Latency     : retrieval=2.045s  generation=18.519s  total=20.564s
    Words       : 34
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'technical_support'}
    [Retriever] policy  : []
    [Retriever] faqs    : []
    [Retriever] tickets : ['ticket_025', 'ticket_017']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_025', 'ticket_017']
    Retrieval : 0/3 (0%)
    Faithful  : NO
    Latency     : retrieval=2.085s  generation=63.481s  total=65.566s
    Words       : 489
    ----------------------------------------------------------------------
    [Retriever] Filters : {'category': 'technical_troubleshooting'}
    [Retriever] policy  : []
    [Retriever] faqs    : ['faq_020', 'faq_016']
    [Retriever] tickets : []
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'faq_016']
    Retrieval : 1/2 (50%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.425s  generation=41.378s  total=43.803s
    Words       : 184
    ----------------------------------------------------------------------
    [Retriever] Filters : none
    [Retriever] policy  : ['policy_007']
    [Retriever] faqs    : ['faq_017', 'faq_013']
    [Retriever] tickets : ['ticket_017', 'ticket_020']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_017', 'faq_013', 'ticket_017', 'ticket_020']
    Retrieval : 1/1 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.061s  generation=51.152s  total=53.213s
    Words       : 288
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 45%
    Faithfulness        : {'YES': 2, 'NO': 5, 'PARTIAL': 1, 'UNKNOWN': 2}
    Avg retrieval time  : 1.9s
    Avg generation time : 43.574s
    Avg total latency   : 45.474s
    Avg response words  : 253

    Note: ROUGE/BLEU/semantic similarity not computed — dataset has no expected answer strings.

## Hibrid Retrieval + metadata filtering (category, product)

    === Running Evaluation ===

    [Retriever] policy_category=returns  product_category=None
    [Retriever] policy  : ['policy_001']
    [Retriever] faqs    : ['faq_016', 'faq_008']
    [Retriever] tickets : ['ticket_018', 'ticket_005']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['policy_001', 'faq_016', 'faq_008', 'ticket_018', 'ticket_005']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.138s  generation=168.244s  total=170.382s
    Words       : 373
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=laptops
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : ['faq_016', 'faq_008']
    [Retriever] tickets : ['ticket_025', 'ticket_006']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['policy_002', 'faq_016', 'faq_008', 'ticket_025', 'ticket_006']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=7.692s  generation=80.569s  total=88.261s
    Words       : 661
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=None
    [Retriever] policy  : ['policy_005']
    [Retriever] faqs    : ['faq_006', 'faq_011']
    [Retriever] tickets : ['ticket_035', 'ticket_038']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['policy_005', 'faq_006', 'faq_011', 'ticket_035', 'ticket_038']
    Retrieval : 1/3 (33%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.107s  generation=58.367s  total=60.474s
    Words       : 398
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=None
    [Retriever] policy  : ['policy_003']
    [Retriever] faqs    : ['faq_001', 'faq_020']
    [Retriever] tickets : ['ticket_001', 'ticket_011']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['policy_003', 'faq_001', 'faq_020', 'ticket_001', 'ticket_011']
    Retrieval : 0/2 (0%)
    Faithful  : YES
    Latency     : retrieval=2.135s  generation=34.847s  total=36.982s
    Words       : 159
    ----------------------------------------------------------------------
    [Retriever] policy_category=warranty  product_category=None
    [Retriever] policy  : ['policy_002']
    [Retriever] faqs    : ['faq_009', 'faq_017']
    [Retriever] tickets : ['ticket_010', 'ticket_021']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['policy_002', 'faq_009', 'faq_017', 'ticket_010', 'ticket_021']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=2.059s  generation=61.217s  total=63.276s
    Words       : 416
    ----------------------------------------------------------------------
    [Retriever] policy_category=business_customers  product_category=monitors
    [Retriever] policy  : ['policy_006']
    [Retriever] faqs    : ['faq_009', 'faq_017']
    [Retriever] tickets : ['ticket_039', 'ticket_026']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['policy_006', 'faq_009', 'faq_017', 'ticket_039', 'ticket_026']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=48.175s  total=50.241s
    Words       : 247
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=storage
    [Retriever] policy  : ['policy_009']
    [Retriever] faqs    : ['faq_012', 'faq_005']
    [Retriever] tickets : ['ticket_008', 'ticket_035']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['policy_009', 'faq_012', 'faq_005', 'ticket_008', 'ticket_035']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.075s  generation=59.577s  total=61.652s
    Words       : 330
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=None
    [Retriever] policy  : ['policy_009']
    [Retriever] faqs    : ['faq_015', 'faq_017']
    [Retriever] tickets : ['ticket_035', 'ticket_026']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['policy_009', 'faq_015', 'faq_017', 'ticket_035', 'ticket_026']
    Retrieval : 2/3 (67%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.089s  generation=47.491s  total=49.58s
    Words       : 240
    ----------------------------------------------------------------------
    [Retriever] policy_category=None  product_category=storage
    [Retriever] policy  : ['policy_008']
    [Retriever] faqs    : ['faq_012', 'faq_005']
    [Retriever] tickets : ['ticket_021', 'ticket_024']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['policy_008', 'faq_012', 'faq_005', 'ticket_021', 'ticket_024']
    Retrieval : 1/2 (50%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.069s  generation=58.194s  total=60.263s
    Words       : 299
    ----------------------------------------------------------------------
    [Retriever] policy_category=environmental_sustainability  product_category=None
    [Retriever] policy  : ['policy_007']
    [Retriever] faqs    : ['faq_017', 'faq_013']
    [Retriever] tickets : ['ticket_037', 'ticket_033']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_017', 'faq_013', 'ticket_037', 'ticket_033']
    Retrieval : 1/1 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.07s  generation=49.392s  total=51.462s
    Words       : 262
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 57%
    Faithfulness        : {'YES': 5, 'NO': 1, 'PARTIAL': 0, 'UNKNOWN': 4}
    Avg retrieval time  : 2.65s
    Avg generation time : 66.607s
    Avg total latency   : 69.257s
    Avg response words  : 338

    Note: ROUGE/BLEU/semantic similarity not computed — dataset has no expected answer strings.

## Hibrid Retrieval, Top8k + boost strategy

    === Running Evaluation ===

    [Retriever] ticket_018   score=1.7  (sem=1.0 kw=0.3 rec=0.1 sat=0.1 cat=0.2)
    [Retriever] ticket_028   score=1.622  (sem=0.925 kw=0.197 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] policy_001   score=1.433  (sem=0.95 kw=0.183 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_034   score=1.325  (sem=0.675 kw=0.15 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_019   score=1.319  (sem=0.8 kw=0.219 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_005   score=1.29  (sem=0.975 kw=0.115 rec=0.1 sat=0.1 cat=0.0)
    [Retriever] faq_009      score=1.191  (sem=0.9 kw=0.191 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] policy_008   score=1.134  (sem=0.825 kw=0.209 rec=0.1 sat=0.0 cat=0.0)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_034', 'ticket_019', 'ticket_005', 'faq_009', 'policy_008']
    Retrieval : 3/3 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.092s  generation=45.065s  total=47.157s
    Words       : 180
    ----------------------------------------------------------------------
    [Retriever] ticket_025   score=1.5  (sem=1.0 kw=0.3 rec=0.1 sat=0.1 cat=0.0)
    [Retriever] faq_016      score=1.294  (sem=0.975 kw=0.219 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_008      score=1.222  (sem=0.925 kw=0.197 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_006      score=1.202  (sem=0.95 kw=0.152 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_006   score=1.2  (sem=0.9 kw=0.0 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_036   score=1.18  (sem=0.875 kw=0.105 rec=0.1 sat=0.1 cat=0.0)
    [Retriever] faq_019      score=1.104  (sem=0.825 kw=0.179 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_037   score=1.094  (sem=0.775 kw=0.019 rec=0.1 sat=0.2 cat=0.0)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_006', 'ticket_006', 'ticket_036', 'faq_019', 'ticket_037']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.062s  generation=81.036s  total=83.098s
    Words       : 698
    ----------------------------------------------------------------------
    [Retriever] faq_006      score=1.4  (sem=1.0 kw=0.3 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_035   score=1.297  (sem=0.95 kw=0.047 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_019      score=1.179  (sem=0.9 kw=0.179 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_015      score=1.172  (sem=0.975 kw=0.097 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_038   score=1.171  (sem=0.8 kw=0.071 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_005      score=1.141  (sem=0.925 kw=0.116 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_026   score=1.138  (sem=0.725 kw=0.113 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_020   score=1.134  (sem=0.75 kw=0.084 rec=0.1 sat=0.2 cat=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'ticket_035', 'faq_019', 'faq_015', 'ticket_038', 'faq_005', 'ticket_026', 'ticket_020']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.056s  generation=29.351s  total=31.407s
    Words       : 371
    ----------------------------------------------------------------------
    [Retriever] ticket_001   score=1.432  (sem=1.0 kw=0.132 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_001      score=1.375  (sem=0.975 kw=0.3 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_011   score=1.347  (sem=0.925 kw=0.122 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_016   score=1.336  (sem=0.9 kw=0.136 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_018      score=1.194  (sem=0.95 kw=0.144 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_027   score=1.14  (sem=0.725 kw=0.115 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_003   score=1.138  (sem=0.8 kw=0.038 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_008   score=1.104  (sem=0.85 kw=0.054 rec=0.1 sat=0.1 cat=0.0)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_001', 'ticket_011', 'ticket_016', 'faq_018', 'ticket_027', 'ticket_003', 'ticket_008']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.065s  generation=53.944s  total=56.009s
    Words       : 262
    ----------------------------------------------------------------------
    [Retriever] faq_009      score=1.4  (sem=1.0 kw=0.3 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] policy_002   score=1.388  (sem=0.975 kw=0.113 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_021   score=1.35  (sem=0.9 kw=0.15 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_010   score=1.334  (sem=0.925 kw=0.109 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_019   score=1.248  (sem=0.775 kw=0.173 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_036   score=1.247  (sem=0.85 kw=0.196 rec=0.1 sat=0.1 cat=0.0)
    [Retriever] faq_017      score=1.24  (sem=0.95 kw=0.19 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_034   score=1.238  (sem=0.8 kw=0.138 rec=0.1 sat=0.2 cat=0.0)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'policy_002', 'ticket_021', 'ticket_010', 'ticket_019', 'ticket_036', 'faq_017', 'ticket_034']
    Retrieval : 4/4 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.042s  generation=58.756s  total=60.798s
    Words       : 292
    ----------------------------------------------------------------------
    [Retriever] ticket_015   score=1.581  (sem=1.0 kw=0.281 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_039   score=1.493  (sem=0.975 kw=0.218 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_023   score=1.398  (sem=0.85 kw=0.247 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_026   score=1.385  (sem=0.95 kw=0.135 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_011      score=1.278  (sem=0.925 kw=0.253 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] policy_006   score=1.224  (sem=0.75 kw=0.174 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_015      score=1.198  (sem=0.875 kw=0.223 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_017   score=1.185  (sem=0.8 kw=0.085 rec=0.1 sat=0.2 cat=0.0)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'ticket_026', 'faq_011', 'policy_006', 'faq_015', 'ticket_017']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.076s  generation=12.143s  total=14.219s
    Words       : 126
    ----------------------------------------------------------------------
    [Retriever] faq_012      score=1.4  (sem=1.0 kw=0.3 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_038   score=1.27  (sem=0.725 kw=0.245 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_021      score=1.225  (sem=0.975 kw=0.15 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_005      score=1.215  (sem=0.925 kw=0.19 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_037   score=1.214  (sem=0.85 kw=0.064 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_007   score=1.211  (sem=0.825 kw=0.086 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_003      score=1.18  (sem=0.95 kw=0.13 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_010      score=1.138  (sem=0.9 kw=0.138 rec=0.1 sat=0.0 cat=0.0)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'ticket_038', 'faq_021', 'faq_005', 'ticket_037', 'ticket_007', 'faq_003', 'faq_010']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.063s  generation=38.52s  total=40.583s
    Words       : 484
    ----------------------------------------------------------------------
    [Retriever] ticket_035   score=1.548  (sem=0.975 kw=0.273 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_026   score=1.525  (sem=0.925 kw=0.3 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_015      score=1.387  (sem=1.0 kw=0.287 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_006      score=1.293  (sem=0.95 kw=0.243 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_023   score=1.29  (sem=0.875 kw=0.115 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_020   score=1.231  (sem=0.75 kw=0.181 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_012      score=1.192  (sem=0.9 kw=0.192 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_011      score=1.185  (sem=0.825 kw=0.26 rec=0.1 sat=0.0 cat=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_035', 'ticket_026', 'faq_015', 'faq_006', 'ticket_023', 'ticket_020', 'faq_012', 'faq_011']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.052s  generation=64.86s  total=66.912s
    Words       : 872
    ----------------------------------------------------------------------
    [Retriever] faq_020      score=1.4  (sem=1.0 kw=0.3 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_024   score=1.349  (sem=0.9 kw=0.149 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_021   score=1.348  (sem=0.925 kw=0.123 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_013   score=1.339  (sem=0.975 kw=0.064 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_032   score=1.326  (sem=0.95 kw=0.076 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_035   score=1.259  (sem=0.8 kw=0.159 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_010   score=1.16  (sem=0.825 kw=0.035 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_008      score=1.09  (sem=0.85 kw=0.14 rec=0.1 sat=0.0 cat=0.0)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_021', 'ticket_013', 'ticket_032', 'ticket_035', 'ticket_010', 'faq_008']
    Retrieval : 2/2 (100%)
    Faithful  : NO
    Latency     : retrieval=2.056s  generation=36.22s  total=38.276s
    Words       : 151
    ----------------------------------------------------------------------
    [Retriever] policy_007   score=1.6  (sem=1.0 kw=0.3 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_037   score=1.333  (sem=0.9 kw=0.133 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_012      score=1.186  (sem=0.95 kw=0.136 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_009      score=1.184  (sem=0.975 kw=0.109 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_006      score=1.136  (sem=0.925 kw=0.111 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_033   score=1.102  (sem=0.775 kw=0.027 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] policy_002   score=1.085  (sem=0.85 kw=0.135 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_013      score=1.075  (sem=0.8 kw=0.175 rec=0.1 sat=0.0 cat=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'ticket_037', 'faq_012', 'faq_009', 'faq_006', 'ticket_033', 'policy_002', 'faq_013']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.067s  generation=34.681s  total=36.748s
    Words       : 414
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 91%
    Faithfulness        : {'YES': 3, 'NO': 5, 'PARTIAL': 0, 'UNKNOWN': 2}
    Avg retrieval time  : 2.063s
    Avg generation time : 45.458s
    Avg total latency   : 47.521s
    Avg response words  : 385

    Note: ROUGE/BLEU/semantic similarity not computed — dataset has no expected answer strings.

## Hibrid Retrieval, Top-8k + RRF

    === Running Evaluation ===

    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_019', 'ticket_028', 'policy_008', 'policy_007', 'ticket_005', 'policy_001', 'faq_016']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=0.033s  generation=165.605s  total=165.638s
    Words       : 337
    ----------------------------------------------------------------------
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_006', 'faq_019', 'faq_020', 'faq_015', 'ticket_006']
    Retrieval : 3/4 (75%)
    Faithful  : PARTIAL
    Latency     : retrieval=7.347s  generation=35.553s  total=42.9s
    Words       : 179
    ----------------------------------------------------------------------
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.082s  generation=24.59s  total=26.672s
    Words       : 304
    ----------------------------------------------------------------------
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['faq_001', 'ticket_001', 'faq_018', 'ticket_016', 'ticket_011', 'faq_020', 'faq_008', 'faq_013']
    Retrieval : 2/2 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.087s  generation=55.527s  total=57.614s
    Words       : 342
    ----------------------------------------------------------------------
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'ticket_025', 'policy_009', 'policy_002', 'ticket_010']
    Retrieval : 3/4 (75%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.066s  generation=47.14s  total=49.206s
    Words       : 332
    ----------------------------------------------------------------------
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'faq_011', 'ticket_023', 'faq_019', 'faq_006', 'faq_009', 'ticket_039', 'ticket_026']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.073s  generation=37.59s  total=39.663s
    Words       : 189
    ----------------------------------------------------------------------
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'ticket_038', 'ticket_024', 'faq_016']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.051s  generation=38.855s  total=40.906s
    Words       : 486
    ----------------------------------------------------------------------
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.092s  generation=51.206s  total=53.298s
    Words       : 688
    ----------------------------------------------------------------------
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.084s  generation=13.398s  total=15.482s
    Words       : 176
    ----------------------------------------------------------------------
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.042s  generation=23.342s  total=25.384s
    Words       : 300
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 83%
    Faithfulness        : {'YES': 2, 'NO': 5, 'PARTIAL': 2, 'UNKNOWN': 1}
    Avg retrieval time  : 2.396s
    Avg generation time : 49.281s
    Avg total latency   : 51.676s
    Avg response words  : 333

## Hibrid Retrieval, top 8k + RFF + filtering

    === Running Evaluation ===

    [Retriever] Filter applied : category=returns (4 docs)
    [Retriever] ['ticket_018', 'ticket_028', 'policy_001', 'ticket_034']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_034']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.036s  generation=47.194s  total=47.23s
    Words       : 260
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['ticket_025', 'faq_016', 'faq_008', 'faq_006', 'faq_019', 'faq_020', 'faq_015', 'ticket_006']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_006', 'faq_019', 'faq_020', 'faq_015', 'ticket_006']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.087s  generation=68.115s  total=70.202s
    Words       : 642
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.082s  generation=28.132s  total=30.214s
    Words       : 388
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_001', 'ticket_001', 'faq_018', 'ticket_016', 'ticket_011', 'faq_020', 'faq_008', 'faq_013']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['faq_001', 'ticket_001', 'faq_018', 'ticket_016', 'ticket_011', 'faq_020', 'faq_008', 'faq_013']
    Retrieval : 2/2 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.069s  generation=50.049s  total=52.118s
    Words       : 251
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : only 1 'warranty' docs, falling back
    [Retriever] ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'ticket_025', 'policy_009', 'policy_002', 'ticket_010']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'ticket_025', 'policy_009', 'policy_002', 'ticket_010']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=2.064s  generation=52.943s  total=55.007s
    Words       : 385
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : only 1 'business_customers' docs, falling back
    [Retriever] ['ticket_015', 'faq_011', 'ticket_023', 'faq_019', 'faq_006', 'faq_009', 'ticket_039', 'ticket_026']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'faq_011', 'ticket_023', 'faq_019', 'faq_006', 'faq_009', 'ticket_039', 'ticket_026']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.047s  generation=30.457s  total=32.504s
    Words       : 96
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'ticket_038', 'ticket_024', 'faq_016']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'ticket_038', 'ticket_024', 'faq_016']
    Retrieval : 3/3 (100%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.049s  generation=33.606s  total=35.655s
    Words       : 448
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.083s  generation=54.222s  total=56.305s
    Words       : 761
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.088s  generation=9.953s  total=12.041s
    Words       : 139
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : only 1 'environmental_sustainability' docs, falling back
    [Retriever] ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.04s  generation=22.762s  total=24.802s
    Words       : 325
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 83%
    Faithfulness        : {'YES': 4, 'NO': 4, 'PARTIAL': 1, 'UNKNOWN': 1}
    Avg retrieval time  : 1.865s
    Avg generation time : 39.743s
    Avg total latency   : 41.608s
    Avg response words  : 370

## Hibrid Retrieval, Top8k + RFF + improved filtering after

    === Running Evaluation ===

    [Retriever] Filter applied : categories=['returns', 'return_request', 'shipping_info'] (7 docs)
    [Retriever] ['ticket_018', 'ticket_028', 'ticket_005', 'policy_001', 'faq_018', 'ticket_034', 'faq_007']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'ticket_005', 'policy_001', 'faq_018', 'ticket_034', 'faq_007']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.052s  generation=54.559s  total=54.611s
    Words       : 325
    ----------------------------------------------------------------------
    [Retriever] Filter applied : categories=['technical_troubleshooting', 'technical_support'] (9 docs)
    [Retriever] ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006', 'ticket_029', 'ticket_031', 'ticket_040']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006', 'ticket_029', 'ticket_031', 'ticket_040']
    Retrieval : 4/4 (100%)
    Faithful  : NO
    Latency     : retrieval=2.079s  generation=69.782s  total=71.861s
    Words       : 575
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.084s  generation=31.509s  total=33.593s
    Words       : 429
    ----------------------------------------------------------------------
    [Retriever] Filter applied : categories=['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery'] (8 docs)
    [Retriever] ['ticket_001', 'faq_018', 'ticket_016', 'ticket_011', 'faq_007', 'ticket_027', 'ticket_004', 'policy_003']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_016', 'ticket_011', 'faq_007', 'ticket_027', 'ticket_004', 'policy_003']
    Retrieval : 2/2 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.066s  generation=54.715s  total=56.781s
    Words       : 409
    ----------------------------------------------------------------------
    [Retriever] Filter applied : categories=['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects'] (9 docs)
    [Retriever] ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'policy_002', 'ticket_010', 'ticket_021', 'ticket_030']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'policy_002', 'ticket_010', 'ticket_021', 'ticket_030']
    Retrieval : 4/4 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.039s  generation=52.802s  total=54.841s
    Words       : 281
    ----------------------------------------------------------------------
    [Retriever] Filter applied : categories=['business_customers', 'bulk_orders', 'bulk_order_inquiry'] (4 docs)
    [Retriever] ['ticket_015', 'ticket_023', 'ticket_039', 'policy_006']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_023', 'ticket_039', 'policy_006']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=9.398s  generation=36.82s  total=46.218s
    Words       : 157
    ----------------------------------------------------------------------
    [Retriever] Filter applied : categories=['product_questions', 'products', 'pre_sales', 'product_comparison'] (7 docs)
    [Retriever] ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'faq_019', 'faq_006']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'faq_019', 'faq_006']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.253s  generation=45.053s  total=47.306s
    Words       : 604
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.088s  generation=14.743s  total=16.831s
    Words       : 162
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : no category detected
    [Retriever] ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.085s  generation=10.31s  total=12.395s
    Words       : 142
    ----------------------------------------------------------------------
    [Retriever] Filter skipped : only 1 matches, falling back
    [Retriever] ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.064s  generation=22.374s  total=24.438s
    Words       : 306
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 85%
    Faithfulness        : {'YES': 3, 'NO': 5, 'PARTIAL': 0, 'UNKNOWN': 2}
    Avg retrieval time  : 2.621s
    Avg generation time : 39.267s
    Avg total latency   : 41.888s
    Avg response words  : 339

# Hibrid Retrieval, Top8k RFF + improved filtering before

    === Running Evaluation ===

    [Retriever] Filter: categories=['returns', 'return_request', 'shipping_info']
    [Retriever] ['ticket_018', 'ticket_028', 'faq_018', 'ticket_005', 'policy_001', 'ticket_034', 'faq_007']
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'faq_018', 'ticket_005', 'policy_001', 'ticket_034', 'faq_007']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.107s  generation=60.584s  total=62.691s
    Words       : 347
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['technical_troubleshooting', 'technical_support']
    [Retriever] ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006', 'ticket_029', 'ticket_031', 'ticket_040']
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006', 'ticket_029', 'ticket_031', 'ticket_040']
    Retrieval : 4/4 (100%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.049s  generation=70.228s  total=72.277s
    Words       : 574
    ----------------------------------------------------------------------
    [Retriever] Filter: no category detected, unfiltered
    [Retriever] ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_019', 'faq_011', 'faq_003', 'faq_005', 'faq_012', 'faq_010', 'faq_004']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.057s  generation=41.172s  total=43.229s
    Words       : 512
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ['faq_018', 'ticket_001', 'ticket_016', 'ticket_011', 'faq_007', 'ticket_027', 'ticket_004', 'policy_003']
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['faq_018', 'ticket_001', 'ticket_016', 'ticket_011', 'faq_007', 'ticket_027', 'ticket_004', 'policy_003']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.062s  generation=61.722s  total=63.784s
    Words       : 346
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'policy_002', 'ticket_010', 'ticket_021', 'ticket_030']
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'ticket_036', 'ticket_019', 'policy_002', 'ticket_010', 'ticket_021', 'ticket_030']
    Retrieval : 4/4 (100%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.042s  generation=62.17s  total=64.212s
    Words       : 333
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ['ticket_015', 'ticket_023', 'ticket_039', 'policy_006']
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_023', 'ticket_039', 'policy_006']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=49.206s  total=51.272s
    Words       : 330
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['product_questions', 'products', 'pre_sales', 'product_comparison']
    [Retriever] ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'faq_019', 'faq_006', 'faq_011']
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'faq_019', 'faq_006', 'faq_011']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.05s  generation=39.099s  total=41.149s
    Words       : 541
    ----------------------------------------------------------------------
    [Retriever] Filter: no category detected, unfiltered
    [Retriever] ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['faq_015', 'ticket_026', 'ticket_035', 'faq_006', 'faq_011', 'faq_004', 'faq_017', 'faq_012']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.063s  generation=63.592s  total=65.655s
    Words       : 851
    ----------------------------------------------------------------------
    [Retriever] Filter: no category detected, unfiltered
    [Retriever] ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_035', 'faq_012', 'faq_008', 'faq_016', 'faq_015', 'ticket_013']
    Retrieval : 1/2 (50%)
    Faithful  : YES
    Latency     : retrieval=2.054s  generation=12.136s  total=14.19s
    Words       : 171
    ----------------------------------------------------------------------
    [Retriever] Filter: categories=['environmental_sustainability']
    [Retriever] Too few filtered results, falling back to unfiltered
    [Retriever] ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007', 'faq_012', 'faq_013', 'policy_002', 'faq_009', 'faq_017', 'faq_006', 'ticket_017']
    Retrieval : 1/1 (100%)
    Faithful  : NO
    Latency     : retrieval=2.095s  generation=16.097s  total=18.192s
    Words       : 217
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 85%
    Faithfulness        : {'YES': 4, 'NO': 4, 'PARTIAL': 1, 'UNKNOWN': 1}
    Avg retrieval time  : 2.064s
    Avg generation time : 47.601s
    Avg total latency   : 49.665s
    Avg response words  : 422

# Hibrid Retrieval, Top8k + Boost strategy + filtering

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.9 (sem=1.0 kw=0.5 rec=0.1 sat=0.1 cat=0.2)
    [Retriever] ticket_005   score=1.448 (sem=0.857 kw=0.191 rec=0.1 sat=0.1 cat=0.2)
    [Retriever] ticket_028   score=1.4 (sem=0.571 kw=0.328 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] policy_001   score=1.319 (sem=0.714 kw=0.304 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_034   score=1.179 (sem=0.429 kw=0.25 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] faq_007      score=0.827 (sem=0.286 kw=0.242 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_018      score=0.766 (sem=0.143 kw=0.324 rec=0.1 sat=0.0 cat=0.2)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_005', 'ticket_028', 'policy_001', 'ticket_034', 'faq_007', 'faq_018']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.067s  generation=58.243s  total=60.31s
    Words       : 297
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.9 (sem=1.0 kw=0.5 rec=0.1 sat=0.1 cat=0.2)
    [Retriever] faq_016      score=1.582 (sem=0.917 kw=0.365 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_008      score=1.461 (sem=0.833 kw=0.328 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_006   score=1.25 (sem=0.75 kw=0.0 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] faq_020      score=1.234 (sem=0.667 kw=0.267 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_031   score=1.082 (sem=0.5 kw=0.082 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_029   score=0.883 (sem=0.583 kw=0.0 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_013   score=0.862 (sem=0.333 kw=0.028 rec=0.1 sat=0.2 cat=0.2)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'ticket_006', 'faq_020', 'ticket_031', 'ticket_029', 'ticket_013']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.057s  generation=62.056s  total=64.113s
    Words       : 393
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_006      score=1.6 (sem=1.0 kw=0.5 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_035   score=1.278 (sem=0.9 kw=0.078 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_015      score=1.212 (sem=0.95 kw=0.162 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_019      score=1.198 (sem=0.8 kw=0.298 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_005      score=1.143 (sem=0.85 kw=0.193 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_012      score=1.05 (sem=0.7 kw=0.25 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_003      score=1.043 (sem=0.65 kw=0.293 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_010      score=1.039 (sem=0.75 kw=0.189 rec=0.1 sat=0.0 cat=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'ticket_035', 'faq_015', 'faq_019', 'faq_005', 'faq_012', 'faq_003', 'faq_010']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.067s  generation=44.936s  total=47.003s
    Words       : 585
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.72 (sem=1.0 kw=0.22 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_011   score=1.453 (sem=0.75 kw=0.203 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] faq_018      score=1.416 (sem=0.875 kw=0.24 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_016   score=1.352 (sem=0.625 kw=0.227 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_027   score=1.067 (sem=0.375 kw=0.192 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] faq_007      score=0.938 (sem=0.5 kw=0.138 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_004   score=0.91 (sem=0.25 kw=0.16 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] policy_003   score=0.553 (sem=0.125 kw=0.128 rec=0.1 sat=0.0 cat=0.2)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_011', 'faq_018', 'ticket_016', 'ticket_027', 'faq_007', 'ticket_004', 'policy_003']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.062s  generation=69.906s  total=71.968s
    Words       : 421
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.8 (sem=1.0 kw=0.5 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_017      score=1.394 (sem=0.778 kw=0.316 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] policy_002   score=1.377 (sem=0.889 kw=0.188 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_010   score=1.348 (sem=0.667 kw=0.181 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_021   score=1.306 (sem=0.556 kw=0.25 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_036   score=1.172 (sem=0.444 kw=0.328 rec=0.1 sat=0.1 cat=0.2)
    [Retriever] ticket_019   score=1.011 (sem=0.222 kw=0.288 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_030   score=0.867 (sem=0.333 kw=0.234 rec=0.1 sat=0.0 cat=0.2)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002', 'ticket_010', 'ticket_021', 'ticket_036', 'ticket_019', 'ticket_030']
    Retrieval : 4/4 (100%)
    Faithful  : YES
    Latency     : retrieval=2.434s  generation=58.384s  total=60.818s
    Words       : 302
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.969 (sem=1.0 kw=0.469 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_039   score=1.614 (sem=0.75 kw=0.364 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] ticket_023   score=1.412 (sem=0.5 kw=0.412 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] policy_006   score=0.84 (sem=0.25 kw=0.29 rec=0.1 sat=0.0 cat=0.2)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.053s  generation=54.166s  total=56.219s
    Words       : 301
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'technical_support']
    [Retriever] faq_012      score=1.8 (sem=1.0 kw=0.5 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] ticket_038   score=1.608 (sem=0.7 kw=0.408 rec=0.1 sat=0.2 cat=0.2)
    [Retriever] faq_021      score=1.5 (sem=0.95 kw=0.25 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_005      score=1.466 (sem=0.85 kw=0.316 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_003      score=1.416 (sem=0.9 kw=0.216 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_010      score=1.33 (sem=0.8 kw=0.23 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_019      score=1.201 (sem=0.75 kw=0.151 rec=0.1 sat=0.0 cat=0.2)
    [Retriever] faq_006      score=1.112 (sem=0.65 kw=0.162 rec=0.1 sat=0.0 cat=0.2)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'ticket_038', 'faq_021', 'faq_005', 'faq_003', 'faq_010', 'faq_019', 'faq_006']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=44.664s  total=46.73s
    Words       : 488
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_035   score=1.705 (sem=0.95 kw=0.454 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_026   score=1.65 (sem=0.85 kw=0.5 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_015      score=1.578 (sem=1.0 kw=0.478 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_006      score=1.404 (sem=0.9 kw=0.404 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_023   score=1.241 (sem=0.75 kw=0.191 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_012      score=1.22 (sem=0.8 kw=0.32 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] faq_011      score=1.183 (sem=0.65 kw=0.433 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_020   score=1.102 (sem=0.5 kw=0.302 rec=0.1 sat=0.2 cat=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_035', 'ticket_026', 'faq_015', 'faq_006', 'ticket_023', 'faq_012', 'faq_011', 'ticket_020']
    Retrieval : 3/3 (100%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.044s  generation=65.553s  total=67.597s
    Words       : 793
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.6 (sem=1.0 kw=0.5 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_013   score=1.357 (sem=0.95 kw=0.107 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_021   score=1.355 (sem=0.85 kw=0.205 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_024   score=1.348 (sem=0.8 kw=0.248 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_032   score=1.326 (sem=0.9 kw=0.126 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] ticket_035   score=1.164 (sem=0.6 kw=0.264 rec=0.1 sat=0.2 cat=0.0)
    [Retriever] faq_008      score=1.032 (sem=0.7 kw=0.232 rec=0.1 sat=0.0 cat=0.0)
    [Retriever] ticket_010   score=1.008 (sem=0.65 kw=0.058 rec=0.1 sat=0.2 cat=0.0)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_013', 'ticket_021', 'ticket_024', 'ticket_032', 'ticket_035', 'faq_008', 'ticket_010']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.068s  generation=44.224s  total=46.292s
    Words       : 137
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.8 (sem=1.0 kw=0.5 rec=0.1 sat=0.0 cat=0.2)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.057s  generation=50.684s  total=52.741s
    Words       : 250
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 91%
    Faithfulness        : {'YES': 7, 'NO': 2, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg retrieval time  : 2.098s
    Avg generation time : 55.282s
    Avg total latency   : 57.379s
    Avg response words  : 397

# Hibrid Retrieval, Top8k + Boost strategy + filtering + kw + prod boost

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=0.89 (sem=0.143 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_007      score=0.869 (sem=0.286 kw=0.483 rec=0.1 sat=0.0 prod=0.0)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_005', 'ticket_034', 'faq_018', 'faq_007']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.033s  generation=71.339s  total=71.372s
    Words       : 370
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.897 (sem=0.917 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.739 (sem=0.833 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.301 (sem=0.667 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.1 (sem=0.75 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_031   score=0.863 (sem=0.5 kw=0.163 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_038   score=0.779 (sem=0.25 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_013   score=0.74 (sem=0.333 kw=0.057 rec=0.1 sat=0.1 prod=0.15)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006', 'ticket_031', 'ticket_038', 'ticket_013']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.072s  generation=76.253s  total=78.325s
    Words       : 525
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.429 (sem=0.733 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.357 (sem=0.933 kw=0.324 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_005      score=1.286 (sem=0.8 kw=0.386 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.223 (sem=0.867 kw=0.156 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.222 (sem=0.467 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.219 (sem=0.533 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.199 (sem=0.6 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_019', 'faq_015', 'faq_005', 'ticket_035', 'faq_011', 'faq_003', 'faq_012']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.055s  generation=45.716s  total=47.771s
    Words       : 539
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.641 (sem=1.0 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.456 (sem=0.875 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.356 (sem=0.75 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=0.959 (sem=0.375 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_007      score=0.875 (sem=0.5 kw=0.275 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_004   score=0.769 (sem=0.25 kw=0.319 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_003   score=0.481 (sem=0.125 kw=0.256 rec=0.1 sat=0.0 prod=0.0)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_011', 'ticket_016', 'ticket_027', 'faq_007', 'ticket_004', 'policy_003']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.057s  generation=58.491s  total=60.548s
    Words       : 310
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_017      score=1.511 (sem=0.778 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] policy_002   score=1.366 (sem=0.889 kw=0.377 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_021   score=1.256 (sem=0.556 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_036   score=1.249 (sem=0.444 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_010   score=1.229 (sem=0.667 kw=0.362 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_019   score=0.999 (sem=0.222 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_030   score=0.901 (sem=0.333 kw=0.468 rec=0.1 sat=0.0 prod=0.0)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002', 'ticket_021', 'ticket_036', 'ticket_010', 'ticket_019', 'ticket_030']
    Retrieval : 4/4 (100%)
    Faithful  : NO
    Latency     : retrieval=2.059s  generation=63.382s  total=65.441s
    Words       : 297
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.087s  generation=56.426s  total=58.513s
    Words       : 293
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.682 (sem=0.8 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.533 (sem=0.933 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.399 (sem=0.867 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.294 (sem=0.733 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.253 (sem=0.267 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_033   score=1.084 (sem=0.467 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_019      score=1.069 (sem=0.667 kw=0.302 rec=0.1 sat=0.0 prod=0.0)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'faq_003', 'faq_010', 'ticket_024', 'ticket_033', 'faq_019']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.369s  generation=42.943s  total=45.312s
    Words       : 517
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_035   score=2.059 (sem=0.95 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=2.057 (sem=1.0 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_026   score=2.05 (sem=0.85 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_006      score=1.809 (sem=0.9 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.616 (sem=0.65 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.539 (sem=0.8 kw=0.639 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_004      score=1.471 (sem=0.55 kw=0.821 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.433 (sem=0.6 kw=0.733 rec=0.1 sat=0.0 prod=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_035', 'faq_015', 'ticket_026', 'faq_006', 'faq_011', 'faq_012', 'faq_004', 'faq_019']
    Retrieval : 3/3 (100%)
    Faithful  : NO
    Latency     : retrieval=2.09s  generation=57.837s  total=59.927s
    Words       : 767
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.647 (sem=0.8 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.61 (sem=0.85 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_035   score=1.479 (sem=0.6 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_013   score=1.364 (sem=0.95 kw=0.214 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_032   score=1.352 (sem=0.9 kw=0.252 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_012      score=1.284 (sem=0.5 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.265 (sem=0.7 kw=0.465 rec=0.1 sat=0.0 prod=0.0)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_021', 'ticket_035', 'ticket_013', 'ticket_032', 'faq_012', 'faq_008']
    Retrieval : 2/2 (100%)
    Faithful  : NO
    Latency     : retrieval=2.059s  generation=49.364s  total=51.423s
    Words       : 262
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.059s  generation=41.376s  total=43.435s
    Words       : 215
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 4, 'NO': 6, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg retrieval time  : 1.894s
    Avg generation time : 56.313s
    Avg total latency   : 58.207s
    Avg response words  : 410

# Hibrid Retrieval, Top5k + Boost strategy + filtering + kw + prod boost

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_005', 'ticket_034']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.042s  generation=162.182s  total=162.224s
    Words       : 338
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_006']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=7.699s  generation=61.621s  total=69.32s
    Words       : 368
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.333 (sem=0.909 kw=0.324 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.332 (sem=0.636 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_005      score=1.213 (sem=0.727 kw=0.386 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.174 (sem=0.818 kw=0.156 rec=0.1 sat=0.1 prod=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_015', 'faq_019', 'faq_005', 'ticket_035']
    Retrieval : 1/3 (33%)
    Faithful  : UNKNOWN
    Latency     : retrieval=2.101s  generation=44.815s  total=46.916s
    Words       : 234
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.641 (sem=1.0 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.456 (sem=0.875 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.356 (sem=0.75 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=0.959 (sem=0.375 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_011', 'ticket_016', 'ticket_027']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.111s  generation=57.39s  total=59.501s
    Words       : 357
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_017      score=1.511 (sem=0.778 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] policy_002   score=1.366 (sem=0.889 kw=0.377 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_021   score=1.256 (sem=0.556 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_036   score=1.249 (sem=0.444 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002', 'ticket_021', 'ticket_036']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.063s  generation=64.473s  total=66.536s
    Words       : 372
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.082s  generation=60.018s  total=62.1s
    Words       : 370
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.609 (sem=0.727 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.509 (sem=0.909 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.35 (sem=0.818 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.197 (sem=0.636 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'faq_003', 'faq_010']
    Retrieval : 1/3 (33%)
    Faithful  : NO
    Latency     : retrieval=2.071s  generation=59.395s  total=61.466s
    Words       : 337
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=2.07 (sem=0.87 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_035   score=2.066 (sem=0.957 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=2.057 (sem=1.0 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.822 (sem=0.913 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.662 (sem=0.696 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'ticket_035', 'faq_015', 'faq_006', 'faq_011']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.103s  generation=68.797s  total=70.9s
    Words       : 425
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.673 (sem=0.826 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.63 (sem=0.87 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_035   score=1.531 (sem=0.652 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_013   score=1.371 (sem=0.957 kw=0.214 rec=0.1 sat=0.1 prod=0.0)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_021', 'ticket_035', 'ticket_013']
    Retrieval : 2/2 (100%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.096s  generation=43.939s  total=46.035s
    Words       : 209
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.069s  generation=55.554s  total=57.623s
    Words       : 237
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 82%
    Faithfulness        : {'YES': 6, 'NO': 2, 'PARTIAL': 1, 'UNKNOWN': 1}
    Avg retrieval time  : 2.444s
    Avg generation time : 67.818s
    Avg total latency   : 70.262s
    Avg response words  : 325