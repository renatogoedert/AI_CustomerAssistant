## Gemma4:e4b + nomic

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.754 (sem=0.604 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.438 (sem=0.581 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.296 (sem=0.587 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.267 (sem=0.52 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.234 (sem=0.534 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=8
    [Compressor] sections=31
    [Compressor] sections=16
    [Compressor] sections=9
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=0.029s  compression=0.582s  generation=47.217s  total=47.828s
    Words       : 291
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.953 (sem=0.653 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.599 (sem=0.619 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.514 (sem=0.608 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.192 (sem=0.558 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.065 (sem=0.536 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=11
    [Compressor] sections=23
    [Compressor] sections=21
    [Compressor] sections=16
    [Compressor] sections=11
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.085s  compression=0.826s  generation=46.569s  total=49.48s
    Words       : 323
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.727 (sem=0.627 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.278 (sem=0.523 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.229 (sem=0.533 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.211 (sem=0.525 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.127 (sem=0.528 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=18
    [Compressor] sections=37
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.074s  compression=1.009s  generation=48.101s  total=51.184s
    Words       : 254
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.318 (sem=0.677 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.231 (sem=0.65 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.231 (sem=0.625 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=1.144 (sem=0.56 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=7
    [Compressor] sections=16
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=10
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_016', 'faq_018', 'ticket_011', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.078s  compression=0.409s  generation=49.275s  total=51.762s
    Words       : 270
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.785 (sem=0.685 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.393 (sem=0.588 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.384 (sem=0.651 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.337 (sem=0.56 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.308 (sem=0.608 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=21
    [Compressor] sections=7
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.059s  compression=0.731s  generation=63.969s  total=66.759s
    Words       : 396
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.791 (sem=0.653 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.693 (sem=0.616 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.606 (sem=0.581 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.237 (sem=0.557 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=9
    [Compressor] sections=8
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.08s  compression=0.444s  generation=42.463s  total=44.987s
    Words       : 246
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.823 (sem=0.573 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.416 (sem=0.534 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.286 (sem=0.3 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_021      score=1.142 (sem=0.542 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_033   score=1.092 (sem=0.475 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=60
    [Compressor] sections=7
    [Compressor] sections=24
    [Compressor] sections=11
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'ticket_024', 'faq_021', 'ticket_033']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.063s  compression=1.115s  generation=36.698s  total=39.876s
    Words       : 149
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.753 (sem=0.553 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.686 (sem=0.629 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.681 (sem=0.572 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.498 (sem=0.532 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.468 (sem=0.559 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=9
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.083s  compression=0.745s  generation=57.58s  total=60.408s
    Words       : 351
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.802 (sem=0.702 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.39 (sem=0.511 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.367 (sem=0.52 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.286 (sem=0.526 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.084 (sem=0.3 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Compressor] sections=16
    [Compressor] sections=11
    [Compressor] sections=7
    [Compressor] sections=7
    [Compressor] sections=25
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_035', 'ticket_024', 'ticket_021', 'faq_012']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 4, 'completeness': 5}
    Latency     : retrieval=2.06s  compression=0.759s  generation=32.757s  total=35.576s
    Words       : 63
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.06s  compression=0.218s  generation=40.489s  total=42.767s
    Words       : 226
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 5.0/5
    Avg clarity         : 4.5/5
    Avg professionalism : 4.9/5
    Avg completeness    : 5.0/5
    Avg retrieval time  : 1.867s
    Avg compression time: 0.684s
    Avg generation time : 46.512s
    Avg total latency   : 49.063s
    Avg response words  : 257

## Gemma4:e4b + qwen

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.709 (sem=0.559 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.391 (sem=0.534 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.304 (sem=0.595 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.245 (sem=0.498 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.154 (sem=0.454 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=8
    [Compressor] sections=31
    [Compressor] sections=16
    [Compressor] sections=9
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=0.24s  compression=6.823s  generation=153.557s  total=160.62s
    Words       : 327
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.753 (sem=0.453 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.501 (sem=0.521 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.38 (sem=0.474 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.037 (sem=0.403 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=0.927 (sem=0.398 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=11
    [Compressor] sections=23
    [Compressor] sections=21
    [Compressor] sections=16
    [Compressor] sections=11
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.087s  compression=7.92s  generation=158.382s  total=255.389s
    Words       : 424
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.708 (sem=0.608 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.231 (sem=0.476 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.135 (sem=0.439 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_004      score=1.074 (sem=0.447 kw=0.527 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.028 (sem=0.429 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=18
    [Compressor] sections=48
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_004', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.881s  compression=10.292s  generation=143.917s  total=244.09s
    Words       : 200
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_016   score=1.199 (sem=0.545 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_011   score=1.171 (sem=0.565 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_001   score=1.132 (sem=0.491 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.113 (sem=0.532 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_027   score=1.053 (sem=0.469 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=16
    [Compressor] sections=10
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_016', 'ticket_011', 'ticket_001', 'faq_018', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 3, 'completeness': 5}
    Latency     : retrieval=89.598s  compression=3.502s  generation=144.548s  total=237.648s
    Words       : 137
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.629 (sem=0.529 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.271 (sem=0.466 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.229 (sem=0.496 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.213 (sem=0.436 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.141 (sem=0.441 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=21
    [Compressor] sections=7
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.456s  compression=6.277s  generation=153.285s  total=249.018s
    Words       : 285
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.652 (sem=0.514 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.648 (sem=0.571 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.539 (sem=0.514 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.132 (sem=0.452 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=9
    [Compressor] sections=8
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.857s  compression=4.177s  generation=143.559s  total=237.593s
    Words       : 188
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.916 (sem=0.666 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.461 (sem=0.475 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_005      score=1.381 (sem=0.499 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.042 (sem=0.442 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=0.998 (sem=0.437 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=7
    [Compressor] sections=60
    [Compressor] sections=24
    [Compressor] sections=13
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'ticket_024', 'faq_005', 'faq_021', 'faq_010']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.786s  compression=10.476s  generation=150.033s  total=250.295s
    Words       : 266
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.621 (sem=0.421 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.604 (sem=0.547 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.53 (sem=0.421 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.413 (sem=0.447 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.347 (sem=0.438 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=9
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=88.735s  compression=6.525s  generation=163.733s  total=258.993s
    Words       : 379
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.655 (sem=0.555 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.286 (sem=0.439 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.208 (sem=0.424 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_021   score=1.188 (sem=0.428 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_035   score=1.179 (sem=0.3 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=16
    [Compressor] sections=7
    [Compressor] sections=25
    [Compressor] sections=7
    [Compressor] sections=11
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'faq_012', 'ticket_021', 'ticket_035']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=88.071s  compression=6.726s  generation=132.819s  total=227.616s
    Words       : 170
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.616 (sem=0.516 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=89.47s  compression=2.233s  generation=151.654s  total=243.357s
    Words       : 195
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 9, 'NO': 0, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg helpfulness     : 4.9/5
    Avg clarity         : 4.5/5
    Avg professionalism : 4.8/5
    Avg completeness    : 4.9/5
    Avg retrieval time  : 80.418s
    Avg compression time: 6.495s
    Avg generation time : 149.549s
    Avg total latency   : 236.462s
    Avg response words  : 257

## Qwen3.5:4b + nomic

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.754 (sem=0.604 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.438 (sem=0.581 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.296 (sem=0.587 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.267 (sem=0.52 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.234 (sem=0.534 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=8
    [Compressor] sections=31
    [Compressor] sections=16
    [Compressor] sections=9
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.102s  compression=1.079s  generation=63.886s  total=67.067s
    Words       : 195
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.953 (sem=0.653 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.599 (sem=0.619 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.514 (sem=0.608 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.192 (sem=0.558 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.065 (sem=0.536 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=11
    [Compressor] sections=23
    [Compressor] sections=21
    [Compressor] sections=16
    [Compressor] sections=11
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 3, 'clarity': 3, 'professionalism': 3, 'completeness': 3}
    Latency     : retrieval=2.744s  compression=0.707s  generation=121.774s  total=125.225s
    Words       : 188
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.727 (sem=0.627 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.278 (sem=0.523 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.229 (sem=0.533 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.211 (sem=0.525 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.127 (sem=0.528 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=18
    [Compressor] sections=37
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.765s  compression=0.894s  generation=65.072s  total=68.731s
    Words       : 139
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.318 (sem=0.677 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.231 (sem=0.65 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.231 (sem=0.625 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=1.144 (sem=0.56 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=7
    [Compressor] sections=16
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=10
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_016', 'faq_018', 'ticket_011', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 3, 'clarity': 3, 'professionalism': 3, 'completeness': 3}
    Latency     : retrieval=2.06s  compression=0.463s  generation=121.57s  total=124.093s
    Words       : 120
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.785 (sem=0.685 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.393 (sem=0.588 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.384 (sem=0.651 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.337 (sem=0.56 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.308 (sem=0.608 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=21
    [Compressor] sections=7
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.736s  compression=0.643s  generation=76.776s  total=80.155s
    Words       : 202
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.791 (sem=0.653 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.693 (sem=0.616 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.606 (sem=0.581 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.237 (sem=0.557 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=9
    [Compressor] sections=8
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.771s  compression=0.384s  generation=89.76s  total=92.915s
    Words       : 150
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.823 (sem=0.573 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.416 (sem=0.534 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.286 (sem=0.3 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_021      score=1.142 (sem=0.542 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_033   score=1.092 (sem=0.475 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=60
    [Compressor] sections=7
    [Compressor] sections=24
    [Compressor] sections=11
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'ticket_024', 'faq_021', 'ticket_033']
    Retrieval   : 2/3 (67%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 3, 'clarity': 3, 'professionalism': 3, 'completeness': 3}
    Latency     : retrieval=2.063s  compression=1.079s  generation=262.354s  total=265.496s
    Words       : 0
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.753 (sem=0.553 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.686 (sem=0.629 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.681 (sem=0.572 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.498 (sem=0.532 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.468 (sem=0.559 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=9
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 3, 'clarity': 3, 'professionalism': 3, 'completeness': 3}
    Latency     : retrieval=3.545s  compression=0.642s  generation=255.491s  total=259.678s
    Words       : 0
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.802 (sem=0.702 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.39 (sem=0.511 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.367 (sem=0.52 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.286 (sem=0.526 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.084 (sem=0.3 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Compressor] sections=16
    [Compressor] sections=11
    [Compressor] sections=7
    [Compressor] sections=7
    [Compressor] sections=25
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_035', 'ticket_024', 'ticket_021', 'faq_012']
    Retrieval   : 2/2 (100%)
    Faithful    : UNKNOWN
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=3.564s  compression=0.695s  generation=188.938s  total=193.197s
    Words       : 130
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=3.408s  compression=0.202s  generation=93.716s  total=97.326s
    Words       : 162
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 2, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 8}
    Avg helpfulness     : 4.2/5
    Avg clarity         : 4.2/5
    Avg professionalism : 4.2/5
    Avg completeness    : 4.2/5
    Avg retrieval time  : 2.776s
    Avg compression time: 0.679s
    Avg generation time : 133.934s
    Avg total latency   : 137.388s
    Avg response words  : 129

## Llama3.1:8b + nomic

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.754 (sem=0.604 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.438 (sem=0.581 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.296 (sem=0.587 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.267 (sem=0.52 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.234 (sem=0.534 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=8
    [Compressor] sections=31
    [Compressor] sections=16
    [Compressor] sections=9
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=2.105s  compression=0.917s  generation=13.195s  total=16.217s
    Words       : 146
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.953 (sem=0.653 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.599 (sem=0.619 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.514 (sem=0.608 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.192 (sem=0.558 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.065 (sem=0.536 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=11
    [Compressor] sections=23
    [Compressor] sections=21
    [Compressor] sections=16
    [Compressor] sections=11
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=3.715s  compression=0.778s  generation=11.53s  total=16.023s
    Words       : 119
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.727 (sem=0.627 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.278 (sem=0.523 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.229 (sem=0.533 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.211 (sem=0.525 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.127 (sem=0.528 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=18
    [Compressor] sections=37
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=3.671s  compression=0.81s  generation=12.331s  total=16.812s
    Words       : 128
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.318 (sem=0.677 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.231 (sem=0.65 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.231 (sem=0.625 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=1.144 (sem=0.56 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=7
    [Compressor] sections=16
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=10
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_016', 'faq_018', 'ticket_011', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 3}
    Latency     : retrieval=3.691s  compression=0.347s  generation=9.32s  total=13.358s
    Words       : 76
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.785 (sem=0.685 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.393 (sem=0.588 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.384 (sem=0.651 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.337 (sem=0.56 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.308 (sem=0.608 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=21
    [Compressor] sections=7
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.698s  compression=0.594s  generation=13.182s  total=17.474s
    Words       : 149
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.791 (sem=0.653 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.693 (sem=0.616 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.606 (sem=0.581 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.237 (sem=0.557 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=9
    [Compressor] sections=8
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.684s  compression=0.356s  generation=10.134s  total=14.174s
    Words       : 85
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.823 (sem=0.573 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.416 (sem=0.534 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.286 (sem=0.3 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_021      score=1.142 (sem=0.542 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_033   score=1.092 (sem=0.475 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=60
    [Compressor] sections=7
    [Compressor] sections=24
    [Compressor] sections=11
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'ticket_024', 'faq_021', 'ticket_033']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.674s  compression=0.9s  generation=13.978s  total=18.552s
    Words       : 166
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.753 (sem=0.553 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.686 (sem=0.629 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.681 (sem=0.572 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.498 (sem=0.532 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.468 (sem=0.559 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=9
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.676s  compression=0.586s  generation=15.879s  total=20.141s
    Words       : 186
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.802 (sem=0.702 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.39 (sem=0.511 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.367 (sem=0.52 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.286 (sem=0.526 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.084 (sem=0.3 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Compressor] sections=16
    [Compressor] sections=11
    [Compressor] sections=7
    [Compressor] sections=7
    [Compressor] sections=25
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_035', 'ticket_024', 'ticket_021', 'faq_012']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.705s  compression=0.639s  generation=13.555s  total=17.899s
    Words       : 154
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=3.716s  compression=0.188s  generation=13.108s  total=17.012s
    Words       : 153
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 4.1/5
    Avg clarity         : 4.7/5
    Avg professionalism : 5.0/5
    Avg completeness    : 4.1/5
    Avg retrieval time  : 3.534s
    Avg compression time: 0.612s
    Avg generation time : 12.621s
    Avg total latency   : 16.766s
    Avg response words  : 136

## Llama3.1:8b + qwen

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.709 (sem=0.559 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.391 (sem=0.534 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.304 (sem=0.595 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.245 (sem=0.498 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.154 (sem=0.454 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=8
    [Compressor] sections=31
    [Compressor] sections=16
    [Compressor] sections=9
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.448s  compression=6.21s  generation=45.619s  total=54.277s
    Words       : 113
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.753 (sem=0.453 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.501 (sem=0.521 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.38 (sem=0.474 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.037 (sem=0.403 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=0.927 (sem=0.398 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=11
    [Compressor] sections=23
    [Compressor] sections=21
    [Compressor] sections=16
    [Compressor] sections=11
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=87.525s  compression=7.816s  generation=51.404s  total=146.745s
    Words       : 205
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.708 (sem=0.608 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.232 (sem=0.477 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.135 (sem=0.439 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_004      score=1.074 (sem=0.447 kw=0.527 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.028 (sem=0.429 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=18
    [Compressor] sections=48
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_004', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=87.25s  compression=8.133s  generation=43.058s  total=138.441s
    Words       : 59
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_016   score=1.199 (sem=0.545 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_011   score=1.173 (sem=0.567 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_001   score=1.131 (sem=0.49 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.112 (sem=0.531 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_027   score=1.052 (sem=0.468 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=16
    [Compressor] sections=10
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_016', 'ticket_011', 'ticket_001', 'faq_018', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=86.602s  compression=2.78s  generation=42.557s  total=131.939s
    Words       : 65
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.627 (sem=0.527 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.27 (sem=0.465 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.229 (sem=0.496 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.211 (sem=0.434 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.14 (sem=0.44 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=21
    [Compressor] sections=7
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=52.933s  compression=5.187s  generation=51.255s  total=109.375s
    Words       : 197
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_039   score=1.65 (sem=0.573 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_015   score=1.65 (sem=0.512 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_023   score=1.54 (sem=0.515 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.13 (sem=0.45 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=8
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_039', 'ticket_015', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 4, 'professionalism': 5, 'completeness': 3}
    Latency     : retrieval=75.141s  compression=3.504s  generation=43.167s  total=121.812s
    Words       : 78
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.919 (sem=0.669 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.459 (sem=0.473 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_005      score=1.383 (sem=0.501 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.042 (sem=0.442 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_010      score=0.999 (sem=0.438 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=7
    [Compressor] sections=60
    [Compressor] sections=24
    [Compressor] sections=13
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'ticket_024', 'faq_005', 'faq_021', 'faq_010']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 4, 'professionalism': 5, 'completeness': 3}
    Latency     : retrieval=49.778s  compression=8.61s  generation=46.963s  total=105.351s
    Words       : 125
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.621 (sem=0.421 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.607 (sem=0.55 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.531 (sem=0.422 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.415 (sem=0.449 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.349 (sem=0.44 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=9
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=82.253s  compression=5.356s  generation=49.861s  total=137.47s
    Words       : 160
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.655 (sem=0.555 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_024   score=1.288 (sem=0.441 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.209 (sem=0.425 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_021   score=1.188 (sem=0.428 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_035   score=1.179 (sem=0.3 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Compressor] sections=16
    [Compressor] sections=7
    [Compressor] sections=25
    [Compressor] sections=7
    [Compressor] sections=11
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_024', 'faq_012', 'ticket_021', 'ticket_035']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=39.536s  compression=5.496s  generation=49.212s  total=94.244s
    Words       : 178
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.614 (sem=0.514 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 4, 'clarity': 4, 'professionalism': 5, 'completeness': 3}
    Latency     : retrieval=79.955s  compression=1.977s  generation=48.046s  total=129.978s
    Words       : 166
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 4.2/5
    Avg clarity         : 4.5/5
    Avg professionalism : 5.0/5
    Avg completeness    : 3.9/5
    Avg retrieval time  : 64.342s
    Avg compression time: 5.507s
    Avg generation time : 47.114s
    Avg total latency   : 116.963s
    Avg response words  : 135