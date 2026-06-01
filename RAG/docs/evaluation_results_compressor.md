## Before Compress

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

## Compress 45% Score

    `=== Running Evaluation ===

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
    Latency     : retrieval=0.035s  generation=54.83s  total=54.865s
    Words       : 289
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
    Faithful  : NO
    Latency     : retrieval=2.081s  generation=32.049s  total=34.13s
    Words       : 80
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
    Faithful  : YES
    Latency     : retrieval=2.083s  generation=36.73s  total=38.813s
    Words       : 115
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
    Latency     : retrieval=2.084s  generation=45.405s  total=47.489s
    Words       : 267
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
    Faithful  : YES
    Latency     : retrieval=2.074s  generation=56.752s  total=58.826s
    Words       : 351
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 0.962 (threshold=0.45 × top=2.138)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     : retrieval=2.064s  generation=31.935s  total=33.999s
    Words       : 158
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
    Faithful  : YES
    Latency     : retrieval=2.072s  generation=68.109s  total=70.181s
    Words       : 467
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
    Latency     : retrieval=2.077s  generation=54.961s  total=57.038s
    Words       : 308
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
    Latency     : retrieval=2.076s  generation=27.423s  total=29.499s
    Words       : 162
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.069s  generation=47.082s  total=49.151s
    Words       : 162
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 78%
    Faithfulness        : {'YES': 8, 'NO': 1, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg retrieval time  : 1.871s
    Avg generation time : 45.528s
    Avg total latency   : 47.399s
    Avg response words  : 236`

## Compress 50% Score

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
    Latency     : retrieval=0.054s  generation=48.761s  total=48.815s
    Words       : 271
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] Dropped 1 doc(s) below score 1.150 (threshold=0.5 × top=2.300)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     : retrieval=2.097s  generation=31.844s  total=33.941s
    Words       : 125
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
    Faithful  : NO
    Latency     : retrieval=2.093s  generation=31.406s  total=33.499s
    Words       : 141
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
    Faithful  : PARTIAL
    Latency     : retrieval=2.063s  generation=44.931s  total=46.994s
    Words       : 281
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
    Faithful  : PARTIAL
    Latency     : retrieval=2.062s  generation=53.037s  total=55.099s
    Words       : 347
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.069 (threshold=0.5 × top=2.138)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.06s  generation=31.058s  total=33.118s
    Words       : 140
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
    Faithful  : YES
    Latency     : retrieval=2.062s  generation=61.349s  total=63.411s
    Words       : 360
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
    Latency     : retrieval=2.102s  generation=50.26s  total=52.362s
    Words       : 340
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
    Faithful  : YES
    Latency     : retrieval=2.085s  generation=25.446s  total=27.531s
    Words       : 93
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.048s  generation=45.935s  total=47.983s
    Words       : 209
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 78%
    Faithfulness        : {'YES': 6, 'NO': 2, 'PARTIAL': 2, 'UNKNOWN': 0}
    Avg retrieval time  : 1.873s
    Avg generation time : 42.403s
    Avg total latency   : 44.275s
    Avg response words  : 231

## Compress 55%

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.183 (threshold=0.55 × top=2.150)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_005']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.031s  generation=50.152s  total=50.183s
    Words       : 218
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] Dropped 2 doc(s) below score 1.265 (threshold=0.55 × top=2.300)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008']
    Retrieval : 3/4 (75%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.365s  generation=41.037s  total=43.402s
    Words       : 180
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
    Faithful  : PARTIAL
    Latency     : retrieval=2.059s  generation=35.066s  total=37.125s
    Words       : 106
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
    Faithful  : PARTIAL
    Latency     : retrieval=2.056s  generation=51.221s  total=53.277s
    Words       : 285
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
    Latency     : retrieval=2.083s  generation=62.166s  total=64.249s
    Words       : 353
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.176 (threshold=0.55 × top=2.138)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.084s  generation=39.764s  total=41.848s
    Words       : 206
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.609 (sem=0.727 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.509 (sem=0.909 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.35 (sem=0.818 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.197 (sem=0.636 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.238 (threshold=0.55 × top=2.250)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'faq_003']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.083s  generation=54.364s  total=56.447s
    Words       : 346
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
    Latency     : retrieval=2.089s  generation=54.578s  total=56.667s
    Words       : 320
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
    Faithful  : YES
    Latency     : retrieval=2.381s  generation=32.359s  total=34.74s
    Words       : 142
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.055s  generation=39.997s  total=42.052s
    Words       : 176
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 78%
    Faithfulness        : {'YES': 5, 'NO': 2, 'PARTIAL': 3, 'UNKNOWN': 0}
    Avg retrieval time  : 1.929s
    Avg generation time : 46.07s
    Avg total latency   : 47.999s
    Avg response words  : 233

## Compress 60% Score

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.290 (threshold=0.6 × top=2.150)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_005']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=2.082s  generation=43.844s  total=45.926s
    Words       : 198
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] Dropped 2 doc(s) below score 1.380 (threshold=0.6 × top=2.300)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.068s  generation=26.798s  total=28.866s
    Words       : 123
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.333 (sem=0.909 kw=0.324 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.332 (sem=0.636 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_005      score=1.213 (sem=0.727 kw=0.386 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.174 (sem=0.818 kw=0.156 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 2 doc(s) below score 1.260 (threshold=0.6 × top=2.100)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_015', 'faq_019']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=28.297s  total=30.363s
    Words       : 56
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.641 (sem=1.0 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.456 (sem=0.875 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.356 (sem=0.75 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=0.959 (sem=0.375 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 0.985 (threshold=0.6 × top=1.641)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_011', 'ticket_016']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.058s  generation=44.573s  total=46.631s
    Words       : 219
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_017      score=1.511 (sem=0.778 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] policy_002   score=1.366 (sem=0.889 kw=0.377 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_021   score=1.256 (sem=0.556 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_036   score=1.249 (sem=0.444 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Compressor] Dropped 2 doc(s) below score 1.260 (threshold=0.6 × top=2.100)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002']
    Retrieval : 2/4 (50%)
    Faithful  : YES
    Latency     : retrieval=2.066s  generation=52.356s  total=54.422s
    Words       : 370
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.283 (threshold=0.6 × top=2.138)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.058s  generation=41.315s  total=43.373s
    Words       : 169
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.609 (sem=0.727 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.509 (sem=0.909 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.35 (sem=0.818 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.197 (sem=0.636 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.350 (threshold=0.6 × top=2.250)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'faq_003']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.075s  generation=54.177s  total=56.252s
    Words       : 396
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
    Latency     : retrieval=2.057s  generation=57.964s  total=60.021s
    Words       : 359
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
    Latency     : retrieval=2.066s  generation=35.658s  total=37.724s
    Words       : 115
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.05s  generation=40.518s  total=42.568s
    Words       : 166
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 76%
    Faithfulness        : {'YES': 7, 'NO': 2, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg retrieval time  : 2.065s
    Avg generation time : 42.55s
    Avg total latency   : 44.615s
    Avg response words  : 217

## Compress 65% Score

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 2 doc(s) below score 1.397 (threshold=0.65 × top=2.150)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     : retrieval=0.03s  generation=45.744s  total=45.774s
    Words       : 249
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] Dropped 2 doc(s) below score 1.495 (threshold=0.65 × top=2.300)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     : retrieval=2.074s  generation=36.293s  total=38.367s
    Words       : 133
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.333 (sem=0.909 kw=0.324 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.332 (sem=0.636 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_005      score=1.213 (sem=0.727 kw=0.386 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.174 (sem=0.818 kw=0.156 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 4 doc(s) below score 1.365 (threshold=0.65 × top=2.100)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006']
    Retrieval : 1/3 (33%)
    Faithful  : PARTIAL
    Latency     : retrieval=2.106s  generation=18.113s  total=20.219s
    Words       : 32
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.641 (sem=1.0 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.456 (sem=0.875 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.356 (sem=0.75 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=0.959 (sem=0.375 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.067 (threshold=0.65 × top=1.641)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_011', 'ticket_016']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     : retrieval=2.07s  generation=44.228s  total=46.298s
    Words       : 228
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_017      score=1.511 (sem=0.778 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] policy_002   score=1.366 (sem=0.889 kw=0.377 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_021   score=1.256 (sem=0.556 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_036   score=1.249 (sem=0.444 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Compressor] Dropped 2 doc(s) below score 1.365 (threshold=0.65 × top=2.100)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002']
    Retrieval : 2/4 (50%)
    Faithful  : YES
    Latency     : retrieval=2.043s  generation=46.29s  total=48.333s
    Words       : 326
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.390 (threshold=0.65 × top=2.138)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : NO
    Latency     : retrieval=2.058s  generation=37.03s  total=39.088s
    Words       : 170
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.609 (sem=0.727 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.509 (sem=0.909 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.35 (sem=0.818 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.197 (sem=0.636 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 2 doc(s) below score 1.463 (threshold=0.65 × top=2.250)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     : retrieval=2.078s  generation=53.4s  total=55.478s
    Words       : 371
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
    Latency     : retrieval=2.061s  generation=52.258s  total=54.319s
    Words       : 295
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
    Latency     : retrieval=2.073s  generation=34.944s  total=37.017s
    Words       : 118
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     : retrieval=2.057s  generation=41.605s  total=43.662s
    Words       : 182
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 76%
    Faithfulness        : {'YES': 6, 'NO': 2, 'PARTIAL': 2, 'UNKNOWN': 0}
    Avg retrieval time  : 1.865s
    Avg generation time : 40.99s
    Avg total latency   : 42.855s
    Avg response words  : 210

## Compress 50% + semantic and bm25 revine

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=2.15 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.428 (sem=0.571 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.423 (sem=0.714 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_005   score=1.389 (sem=0.857 kw=0.382 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_034   score=1.129 (sem=0.429 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] lexical=0.0s  semantic=0.348s
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'ticket_005', 'ticket_034']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     :
        retrieval   = 0.05s
        lexical     = 0.0s
        semantic    = 0.348s
        generation  = 50.287s
        total       = 50.337s
    Words       : 290
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=2.3 (sem=1.0 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.88 (sem=0.9 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.706 (sem=0.8 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.234 (sem=0.6 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_006   score=1.05 (sem=0.7 kw=0.0 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] Dropped 1 doc(s) below score 1.150 (threshold=0.5 × top=2.300)
    [Compressor] lexical=0.0s  semantic=0.542s
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020']
    Retrieval : 3/4 (75%)
    Faithful  : NO
    Latency     :
        retrieval   = 2.101s
        lexical     = 0.0s
        semantic    = 0.542s
        generation  = 32.107s
        total       = 34.208s
    Words       : 110
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.333 (sem=0.909 kw=0.324 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.332 (sem=0.636 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_005      score=1.213 (sem=0.727 kw=0.386 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.174 (sem=0.818 kw=0.156 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] lexical=0.001s  semantic=0.743s
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_015', 'faq_019', 'faq_005', 'ticket_035']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.066s
        lexical     = 0.001s
        semantic    = 0.743s
        generation  = 30.097s
        total       = 32.163s
    Words       : 99
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.641 (sem=1.0 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.456 (sem=0.875 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.356 (sem=0.75 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=0.959 (sem=0.375 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] lexical=0.0s  semantic=0.306s
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'faq_018', 'ticket_011', 'ticket_016', 'ticket_027']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.06s
        lexical     = 0.0s
        semantic    = 0.306s
        generation  = 50.127s
        total       = 52.187s
    Words       : 306
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_017      score=1.511 (sem=0.778 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] policy_002   score=1.366 (sem=0.889 kw=0.377 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_021   score=1.256 (sem=0.556 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_036   score=1.249 (sem=0.444 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Compressor] lexical=0.001s  semantic=0.581s
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'faq_017', 'policy_002', 'ticket_021', 'ticket_036']
    Retrieval : 3/4 (75%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.057s
        lexical     = 0.001s
        semantic    = 0.581s
        generation  = 47.993s
        total       = 50.05s
    Words       : 339
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=2.138 (sem=1.0 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.827 (sem=0.75 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.525 (sem=0.5 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=0.93 (sem=0.25 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] Dropped 1 doc(s) below score 1.069 (threshold=0.5 × top=2.138)
    [Compressor] lexical=0.0s  semantic=0.218s
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023']
    Retrieval : 2/3 (67%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.056s
        lexical     = 0.0s
        semantic    = 0.218s
        generation  = 35.372s
        total       = 37.428s
    Words       : 126
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=2.25 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.609 (sem=0.727 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.509 (sem=0.909 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.35 (sem=0.818 kw=0.432 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=1.197 (sem=0.636 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] lexical=0.001s  semantic=0.651s
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'faq_003', 'faq_010']
    Retrieval : 1/3 (33%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.054s
        lexical     = 0.001s
        semantic    = 0.651s
        generation  = 56.273s
        total       = 58.327s
    Words       : 400
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=2.07 (sem=0.87 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_035   score=2.066 (sem=0.957 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=2.057 (sem=1.0 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.822 (sem=0.913 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.662 (sem=0.696 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] lexical=0.001s  semantic=0.566s
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'ticket_035', 'faq_015', 'faq_006', 'faq_011']
    Retrieval : 3/3 (100%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.085s
        lexical     = 0.001s
        semantic    = 0.566s
        generation  = 46.831s
        total       = 48.916s
    Words       : 287
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.673 (sem=0.826 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.63 (sem=0.87 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_035   score=1.531 (sem=0.652 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_013   score=1.371 (sem=0.957 kw=0.214 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] lexical=0.001s  semantic=0.426s
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'ticket_021', 'ticket_035', 'ticket_013']
    Retrieval : 2/2 (100%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.048s
        lexical     = 0.001s
        semantic    = 0.426s
        generation  = 35.773s
        total       = 37.821s
    Words       : 129
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=2.1 (sem=1.0 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] lexical=0.0s  semantic=0.172s
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval : 1/1 (100%)
    Faithful  : YES
    Latency     :
        retrieval   = 2.046s
        lexical     = 0.0s
        semantic    = 0.172s
        generation  = 43.896s
        total       = 45.942s
    Words       : 166
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 78%
    Faithfulness        : {'YES': 9, 'NO': 1, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg retrieval time  : 1.862s
    Avg Lexical compression time: 0.001s
    Avg Semantic compression time: 0.455s
    Avg generation time : 42.876s
    Avg total latency   : 44.738s
    Avg response words  : 225