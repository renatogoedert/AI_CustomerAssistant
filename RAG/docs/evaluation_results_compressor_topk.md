## Top 3 Chunks

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
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 4, 'completeness': 5}
    Latency     : retrieval=0.035s  compression=0.626s  generation=41.387s  total=42.048s
    Words       : 226
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.061s  compression=0.829s  generation=53.544s  total=56.434s
    Words       : 295
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
    Latency     : retrieval=2.054s  compression=1.119s  generation=36.961s  total=40.134s
    Words       : 196
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.066s  compression=0.397s  generation=44.901s  total=47.364s
    Words       : 257
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
    Latency     : retrieval=2.066s  compression=0.719s  generation=60.022s  total=62.807s
    Words       : 353
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
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.057s  compression=0.447s  generation=43.62s  total=46.124s
    Words       : 235
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
    Judge       : {'helpfulness': 1, 'clarity': 5, 'professionalism': 5, 'completeness': 2}
    Latency     : retrieval=2.059s  compression=1.19s  generation=30.044s  total=33.293s
    Words       : 78
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
    Judge       : {'helpfulness': 3, 'clarity': 3, 'professionalism': 4, 'completeness': 2}
    Latency     : retrieval=2.061s  compression=0.814s  generation=57.039s  total=59.914s
    Words       : 310
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.064s  compression=0.788s  generation=25.817s  total=28.669s
    Words       : 76
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.069s  compression=0.272s  generation=40.121s  total=42.462s
    Words       : 210
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 8, 'NO': 0, 'PARTIAL': 2, 'UNKNOWN': 0}
    Avg helpfulness     : 4.4/5
    Avg clarity         : 4.0/5
    Avg professionalism : 4.8/5
    Avg completeness    : 4.4/5
    Avg retrieval time  : 1.859s
    Avg compression time: 0.72s
    Avg generation time : 43.346s
    Avg total latency   : 45.925s
    Avg response words  : 224

## Top 4 Chunks

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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.12s  compression=0.829s  generation=154.173s  total=157.122s
    Words       : 278
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
    Judge       : {'helpfulness': 4, 'clarity': 2, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=7.564s  compression=0.986s  generation=42.884s  total=51.434s
    Words       : 261
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
    Latency     : retrieval=2.055s  compression=1.121s  generation=43.014s  total=46.19s
    Words       : 175
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
    Latency     : retrieval=2.067s  compression=0.44s  generation=52.535s  total=55.042s
    Words       : 320
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
    Faithful    : NO
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.067s  compression=0.77s  generation=66.849s  total=69.686s
    Words       : 363
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
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.065s  compression=0.486s  generation=46.646s  total=49.197s
    Words       : 265
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
    Judge       : {'helpfulness': 1, 'clarity': 2, 'professionalism': 5, 'completeness': 1}
    Latency     : retrieval=2.06s  compression=1.115s  generation=42.82s  total=45.995s
    Words       : 76
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
    Latency     : retrieval=2.073s  compression=0.734s  generation=49.19s  total=51.997s
    Words       : 272
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.072s  compression=0.774s  generation=30.68s  total=33.526s
    Words       : 90
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
    Latency     : retrieval=2.068s  compression=0.22s  generation=47.668s  total=49.956s
    Words       : 257
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 8, 'NO': 1, 'PARTIAL': 1, 'UNKNOWN': 0}
    Avg helpfulness     : 4.5/5
    Avg clarity         : 4.2/5
    Avg professionalism : 5.0/5
    Avg completeness    : 4.6/5
    Avg retrieval time  : 2.621s
    Avg compression time: 0.747s
    Avg generation time : 57.646s
    Avg total latency   : 61.014s
    Avg response words  : 236

## Top 5 Chunks

    `=== Running Evaluation ===

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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=0.034s  compression=0.759s  generation=49.215s  total=50.008s
    Words       : 242
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.07s  compression=0.864s  generation=63.093s  total=66.027s
    Words       : 435
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
    Latency     : retrieval=2.07s  compression=0.993s  generation=43.877s  total=46.94s
    Words       : 191
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
    Latency     : retrieval=2.064s  compression=0.421s  generation=46.408s  total=48.893s
    Words       : 233
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.069s  compression=0.716s  generation=65.692s  total=68.477s
    Words       : 359
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
    Latency     : retrieval=2.049s  compression=0.521s  generation=49.516s  total=52.086s
    Words       : 250
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
    Judge       : {'helpfulness': 2, 'clarity': 2, 'professionalism': 5, 'completeness': 1}
    Latency     : retrieval=2.065s  compression=1.143s  generation=34.02s  total=37.228s
    Words       : 102
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
    Latency     : retrieval=2.075s  compression=0.716s  generation=61.78s  total=64.571s
    Words       : 378
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
    Faithful    : NO
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.075s  compression=0.786s  generation=51.221s  total=54.082s
    Words       : 196
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
    Latency     : retrieval=2.067s  compression=0.229s  generation=44.41s  total=46.706s
    Words       : 230
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 9, 'NO': 1, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 4.7/5
    Avg clarity         : 4.4/5
    Avg professionalism : 5.0/5
    Avg completeness    : 4.6/5
    Avg retrieval time  : 1.864s
    Avg compression time: 0.715s
    Avg generation time : 50.923s
    Avg total latency   : 53.502s
    Avg response words  : 262`

## Top 6 Chunks

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

## Top 7 Chunks

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
    Latency     : retrieval=0.031s  compression=0.78s  generation=50.425s  total=51.236s
    Words       : 280
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
    Latency     : retrieval=2.066s  compression=0.846s  generation=54.237s  total=57.149s
    Words       : 371
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
    Latency     : retrieval=2.065s  compression=1.061s  generation=52.26s  total=55.386s
    Words       : 263
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
    Latency     : retrieval=2.066s  compression=0.398s  generation=53.975s  total=56.439s
    Words       : 312
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
    Latency     : retrieval=2.074s  compression=0.721s  generation=64.351s  total=67.146s
    Words       : 385
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
    Latency     : retrieval=2.08s  compression=0.504s  generation=48.565s  total=51.149s
    Words       : 239
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.07s  compression=1.106s  generation=41.012s  total=44.188s
    Words       : 168
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
    Latency     : retrieval=2.072s  compression=0.712s  generation=68.878s  total=71.662s
    Words       : 479
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 3, 'completeness': 5}
    Latency     : retrieval=2.082s  compression=0.837s  generation=28.271s  total=31.19s
    Words       : 103
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.068s  compression=0.222s  generation=49.373s  total=51.663s
    Words       : 264
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 4.9/5
    Avg clarity         : 4.4/5
    Avg professionalism : 4.8/5
    Avg completeness    : 5.0/5
    Avg retrieval time  : 1.867s
    Avg compression time: 0.719s
    Avg generation time : 51.135s
    Avg total latency   : 53.721s
    Avg response words  : 286

## Top 8 Chunks

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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=0.03s  compression=0.843s  generation=157.127s  total=158.0s
    Words       : 257
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=8.028s  compression=1.003s  generation=66.775s  total=75.806s
    Words       : 524
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
    Latency     : retrieval=2.061s  compression=1.086s  generation=52.985s  total=56.132s
    Words       : 310
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
    Latency     : retrieval=2.048s  compression=0.446s  generation=49.527s  total=52.021s
    Words       : 232
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
    Latency     : retrieval=2.085s  compression=0.762s  generation=64.461s  total=67.308s
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.061s  compression=0.52s  generation=56.801s  total=59.382s
    Words       : 280
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 4, 'completeness': 5}
    Latency     : retrieval=2.042s  compression=1.217s  generation=42.975s  total=46.234s
    Words       : 188
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 4}
    Latency     : retrieval=2.055s  compression=0.714s  generation=74.357s  total=77.126s
    Words       : 372
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.071s  compression=0.737s  generation=28.095s  total=30.903s
    Words       : 88
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
    Latency     : retrieval=2.07s  compression=0.228s  generation=47.493s  total=49.791s
    Words       : 177
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 5.0/5
    Avg clarity         : 4.6/5
    Avg professionalism : 4.9/5
    Avg completeness    : 4.9/5
    Avg retrieval time  : 2.455s
    Avg compression time: 0.756s
    Avg generation time : 64.06s
    Avg total latency   : 67.27s
    Avg response words  : 282

## Top 9 Chunks

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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=0.029s  compression=0.59s  generation=58.253s  total=58.872s
    Words       : 278
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
    Latency     : retrieval=2.389s  compression=0.88s  generation=52.888s  total=56.157s
    Words       : 303
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
    Latency     : retrieval=2.076s  compression=1.015s  generation=48.835s  total=51.926s
    Words       : 272
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.071s  compression=0.387s  generation=47.137s  total=49.595s
    Words       : 280
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
    Latency     : retrieval=2.066s  compression=0.748s  generation=68.522s  total=71.336s
    Words       : 442
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.081s  compression=0.465s  generation=42.758s  total=45.304s
    Words       : 267
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
    Latency     : retrieval=2.057s  compression=1.128s  generation=51.364s  total=54.549s
    Words       : 255
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
    Latency     : retrieval=2.051s  compression=0.738s  generation=68.696s  total=71.485s
    Words       : 372
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.079s  compression=0.775s  generation=35.303s  total=38.157s
    Words       : 150
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
    Latency     : retrieval=2.064s  compression=0.279s  generation=55.489s  total=57.832s
    Words       : 276
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg helpfulness     : 4.9/5
    Avg clarity         : 4.6/5
    Avg professionalism : 5.0/5
    Avg completeness    : 5.0/5
    Avg retrieval time  : 1.896s
    Avg compression time: 0.701s
    Avg generation time : 52.925s
    Avg total latency   : 55.521s
    Avg response words  : 290

## Top 10 Chunks

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
    Judge       : {'helpfulness': 5, 'clarity': 3, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.079s  compression=0.859s  generation=55.638s  total=58.576s
    Words       : 313
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
    Judge       : {'helpfulness': 5, 'clarity': 4, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.063s  compression=0.865s  generation=67.563s  total=70.491s
    Words       : 423
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
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.053s  compression=1.058s  generation=51.577s  total=54.688s
    Words       : 284
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 3, 'completeness': 5}
    Latency     : retrieval=2.082s  compression=0.446s  generation=51.475s  total=54.003s
    Words       : 286
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
    Faithful    : PARTIAL
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.065s  compression=0.773s  generation=70.396s  total=73.234s
    Words       : 395
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
    Latency     : retrieval=2.054s  compression=0.502s  generation=50.466s  total=53.022s
    Words       : 267
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
    Latency     : retrieval=2.057s  compression=1.2s  generation=51.506s  total=54.763s
    Words       : 334
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
    Latency     : retrieval=2.071s  compression=0.739s  generation=79.732s  total=82.542s
    Words       : 445
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
    Judge       : {'helpfulness': 5, 'clarity': 5, 'professionalism': 5, 'completeness': 5}
    Latency     : retrieval=2.06s  compression=0.808s  generation=36.396s  total=39.264s
    Words       : 150
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
    Latency     : retrieval=2.063s  compression=0.249s  generation=46.289s  total=48.601s
    Words       : 237
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 8, 'NO': 0, 'PARTIAL': 2, 'UNKNOWN': 0}
    Avg helpfulness     : 5.0/5
    Avg clarity         : 4.6/5
    Avg professionalism : 4.8/5
    Avg completeness    : 5.0/5
    Avg retrieval time  : 2.065s
    Avg compression time: 0.75s
    Avg generation time : 56.104s
    Avg total latency   : 58.918s
    Avg response words  : 313