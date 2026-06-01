## semantic scores
    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.754 (sem=0.604 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.438 (sem=0.581 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.296 (sem=0.587 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.267 (sem=0.52 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.234 (sem=0.534 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : PARTIAL
    Latency     : retrieval=0.031s  compression=0.657s  generation=45.223s  total=45.911s
    Words       : 262
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.953 (sem=0.653 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.599 (sem=0.619 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.514 (sem=0.608 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.192 (sem=0.558 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.065 (sem=0.536 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : NO
    Latency     : retrieval=2.073s  compression=0.869s  generation=38.37s  total=41.312s
    Words       : 226
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.727 (sem=0.627 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.278 (sem=0.523 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.229 (sem=0.533 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.211 (sem=0.525 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.127 (sem=0.528 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Latency     : retrieval=2.06s  compression=1.029s  generation=45.106s  total=48.195s
    Words       : 227
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.318 (sem=0.677 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.231 (sem=0.65 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.231 (sem=0.625 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=1.144 (sem=0.56 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_016', 'faq_018', 'ticket_011', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : PARTIAL
    Latency     : retrieval=2.074s  compression=0.372s  generation=46.701s  total=49.147s
    Words       : 274
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.785 (sem=0.685 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.393 (sem=0.588 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.384 (sem=0.651 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.337 (sem=0.56 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.308 (sem=0.608 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : NO
    Latency     : retrieval=2.053s  compression=0.734s  generation=56.668s  total=59.455s
    Words       : 380
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.791 (sem=0.653 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.693 (sem=0.616 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.606 (sem=0.581 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.237 (sem=0.557 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=2.063s  compression=0.449s  generation=43.583s  total=46.095s
    Words       : 245
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.823 (sem=0.573 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.416 (sem=0.534 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_021      score=1.142 (sem=0.542 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_033   score=1.092 (sem=0.475 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_010      score=1.08 (sem=0.519 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'faq_021', 'ticket_033', 'faq_010']
    Retrieval   : 1/3 (33%)
    Faithful    : NO
    Latency     : retrieval=2.059s  compression=1.085s  generation=27.059s  total=30.203s
    Words       : 166
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.753 (sem=0.553 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.686 (sem=0.629 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.681 (sem=0.572 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.498 (sem=0.532 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.468 (sem=0.559 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=2.069s  compression=0.647s  generation=63.077s  total=65.793s
    Words       : 385
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.802 (sem=0.702 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.39 (sem=0.511 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.367 (sem=0.52 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.286 (sem=0.526 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_008      score=1.078 (sem=0.513 kw=0.465 rec=0.1 sat=0.0 prod=0.0)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_035', 'ticket_024', 'ticket_021', 'faq_008']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Latency     : retrieval=2.052s  compression=0.678s  generation=23.644s  total=26.374s
    Words       : 90
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : PARTIAL
    Latency     : retrieval=2.053s  compression=0.268s  generation=37.749s  total=40.07s
    Words       : 224
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 84%
    Faithfulness        : {'YES': 4, 'NO': 3, 'PARTIAL': 3, 'UNKNOWN': 0}
    Avg retrieval time  : 1.859s
    Avg compression time: 0.679s
    Avg generation time : 42.718s
    Avg total latency   : 45.255s
    Avg response words  : 248

## based 0.3 semantic

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.754 (sem=0.604 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_028   score=1.438 (sem=0.581 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_001   score=1.296 (sem=0.587 kw=0.609 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_018      score=1.267 (sem=0.52 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_034   score=1.234 (sem=0.534 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'ticket_028', 'policy_001', 'faq_018', 'ticket_034']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=0.064s  compression=1.062s  generation=146.333s  total=147.459s
    Words       : 207
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.953 (sem=0.653 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.599 (sem=0.619 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.514 (sem=0.608 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.192 (sem=0.558 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.065 (sem=0.536 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
    [TQ-002] My laptop keeps shutting down unexpectedly. What should I do?
    Expected    : ['ticket_025', 'ticket_040', 'faq_008', 'faq_016']
    Retrieved   : ['ticket_025', 'faq_016', 'faq_008', 'faq_020', 'ticket_038']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Latency     : retrieval=7.576s  compression=0.994s  generation=42.025s  total=50.595s
    Words       : 216
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.727 (sem=0.627 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.278 (sem=0.523 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.229 (sem=0.533 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.211 (sem=0.525 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.127 (sem=0.528 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_019', 'faq_003', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Latency     : retrieval=2.39s  compression=1.257s  generation=36.049s  total=39.696s
    Words       : 162
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_001   score=1.318 (sem=0.677 kw=0.441 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.279 (sem=0.625 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_018      score=1.231 (sem=0.65 kw=0.481 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_011   score=1.231 (sem=0.625 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_027   score=1.144 (sem=0.56 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_001', 'ticket_016', 'faq_018', 'ticket_011', 'ticket_027']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Latency     : retrieval=2.091s  compression=0.398s  generation=36.122s  total=38.611s
    Words       : 153
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] faq_009      score=1.785 (sem=0.685 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.393 (sem=0.588 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_017      score=1.384 (sem=0.651 kw=0.633 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_019   score=1.337 (sem=0.56 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.308 (sem=0.608 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['faq_009', 'ticket_036', 'faq_017', 'ticket_019', 'ticket_021']
    Retrieval   : 4/4 (100%)
    Faithful    : YES
    Latency     : retrieval=2.079s  compression=0.817s  generation=56.826s  total=59.722s
    Words       : 289
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_015   score=1.791 (sem=0.653 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.693 (sem=0.616 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_023   score=1.606 (sem=0.581 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.237 (sem=0.557 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_015', 'ticket_039', 'ticket_023', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=2.39s  compression=0.499s  generation=57.027s  total=59.916s
    Words       : 324
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.823 (sem=0.573 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.416 (sem=0.534 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_024   score=1.286 (sem=0.3 kw=0.636 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_021      score=1.142 (sem=0.542 kw=0.5 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_033   score=1.092 (sem=0.475 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'ticket_024', 'faq_021', 'ticket_033']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Latency     : retrieval=2.374s  compression=1.322s  generation=26.573s  total=30.269s
    Words       : 48
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=1.753 (sem=0.553 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_015      score=1.686 (sem=0.629 kw=0.957 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.681 (sem=0.572 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.498 (sem=0.532 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_006      score=1.468 (sem=0.559 kw=0.809 rec=0.1 sat=0.0 prod=0.0)
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_015', 'ticket_035', 'faq_011', 'faq_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=2.416s  compression=0.803s  generation=56.95s  total=60.169s
    Words       : 306
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] faq_020      score=1.802 (sem=0.702 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.39 (sem=0.511 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.367 (sem=0.52 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.286 (sem=0.526 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_012      score=1.084 (sem=0.3 kw=0.534 rec=0.1 sat=0.0 prod=0.15)
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['faq_020', 'ticket_035', 'ticket_024', 'ticket_021', 'faq_012']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Latency     : retrieval=2.051s  compression=0.883s  generation=29.751s  total=32.685s
    Words       : 135
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.698 (sem=0.598 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : YES
    Latency     : retrieval=2.068s  compression=0.228s  generation=44.418s  total=46.714s
    Words       : 245
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 88%
    Faithfulness        : {'YES': 10, 'NO': 0, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg retrieval time  : 2.55s
    Avg compression time: 0.826s
    Avg generation time : 53.207s
    Avg total latency   : 56.584s
    Avg response words  : 208

## Simple distance semantic normalize bm25

    === Running Evaluation ===

    [Retriever] Filter: ['returns', 'return_request', 'shipping_info']
    [Retriever] ticket_018   score=1.806 (sem=0.656 kw=1.0 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] faq_018      score=1.671 (sem=0.924 kw=0.647 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_028   score=1.578 (sem=0.721 kw=0.657 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_034   score=1.572 (sem=0.872 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_007      score=1.459 (sem=0.876 kw=0.483 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=16
    [Compressor] sections=8
    [Compressor] sections=9
    [Compressor] sections=31
    [TQ-001] What is Omnia Retail's return policy for a product I changed my mind about?
    Expected    : ['policy_001', 'ticket_018', 'ticket_028']
    Retrieved   : ['ticket_018', 'faq_018', 'ticket_028', 'ticket_034', 'faq_007']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Latency     : retrieval=2.102s  compression=1.232s  generation=45.323s  total=48.657s
    Words       : 186
    ----------------------------------------------------------------------
    [Retriever] Filter: ['technical_troubleshooting', 'technical_support']
    [Retriever] ticket_025   score=1.832 (sem=0.532 kw=1.0 rec=0.1 sat=0.05 prod=0.15)
    [Retriever] faq_016      score=1.595 (sem=0.615 kw=0.73 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_008      score=1.551 (sem=0.645 kw=0.656 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_020      score=1.426 (sem=0.792 kw=0.534 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_038   score=1.395 (sem=0.866 kw=0.179 rec=0.1 sat=0.1 prod=0.15)
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
    Latency     : retrieval=2.064s  compression=0.963s  generation=49.192s  total=52.219s
    Words       : 308
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_006      score=1.695 (sem=0.595 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_011      score=1.668 (sem=0.913 kw=0.655 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_003      score=1.59 (sem=0.904 kw=0.586 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.573 (sem=0.877 kw=0.596 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_012      score=1.491 (sem=0.892 kw=0.499 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=17
    [Compressor] sections=37
    [Compressor] sections=18
    [Compressor] sections=25
    [TQ-003] How much RAM do I need for video editing?
    Expected    : ['faq_006', 'faq_010', 'ticket_020']
    Retrieved   : ['faq_006', 'faq_011', 'faq_003', 'faq_019', 'faq_012']
    Retrieval   : 1/3 (33%)
    Faithful    : YES
    Latency     : retrieval=2.049s  compression=0.982s  generation=42.414s  total=45.445s
    Words       : 173
    ----------------------------------------------------------------------
    [Retriever] Filter: ['shipping', 'shipping_info', 'delivery_issue', 'delivery_issues', 'damaged_delivery']
    [Retriever] ticket_027   score=1.369 (sem=0.785 kw=0.384 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_004   score=1.333 (sem=0.814 kw=0.319 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_016   score=1.255 (sem=0.601 kw=0.454 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_011   score=1.206 (sem=0.6 kw=0.406 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_003   score=1.194 (sem=0.838 kw=0.256 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=10
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=7
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=48
    [TQ-004] My order hasn't arrived and tracking shows it was delivered but I didn't receive it.
    Expected    : ['ticket_016', 'faq_018']
    Retrieved   : ['ticket_027', 'ticket_004', 'ticket_016', 'ticket_011', 'policy_003']
    Retrieval   : 1/2 (50%)
    Faithful    : YES
    Latency     : retrieval=2.056s  compression=0.605s  generation=49.258s  total=51.919s
    Words       : 267
    ----------------------------------------------------------------------
    [Retriever] Filter: ['warranty', 'warranty_questions', 'warranty_claim', 'warranty_claims', 'defects']
    [Retriever] ticket_019   score=1.564 (sem=0.787 kw=0.577 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_009      score=1.559 (sem=0.459 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_036   score=1.506 (sem=0.701 kw=0.655 rec=0.1 sat=0.05 prod=0.0)
    [Retriever] ticket_032   score=1.476 (sem=0.817 kw=0.459 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_021   score=1.344 (sem=0.644 kw=0.5 rec=0.1 sat=0.1 prod=0.0)
    [Compressor] sections=7
    [Compressor] sections=21
    [Compressor] sections=8
    [Compressor] sections=8
    [Compressor] sections=7
    [TQ-005] What are my warranty rights if a product develops a fault after 10 months?
    Expected    : ['faq_009', 'ticket_019', 'ticket_021', 'faq_017']
    Retrieved   : ['ticket_019', 'faq_009', 'ticket_036', 'ticket_032', 'ticket_021']
    Retrieval   : 3/4 (75%)
    Faithful    : YES
    Latency     : retrieval=2.061s  compression=0.604s  generation=50.238s  total=52.903s
    Words       : 318
    ----------------------------------------------------------------------
    [Retriever] Filter: ['business_customers', 'bulk_orders', 'bulk_order_inquiry']
    [Retriever] ticket_023   score=1.746 (sem=0.721 kw=0.825 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_039   score=1.701 (sem=0.624 kw=0.727 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_015   score=1.669 (sem=0.531 kw=0.938 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] policy_006   score=1.475 (sem=0.795 kw=0.58 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=8
    [Compressor] sections=9
    [Compressor] sections=1
    [Compressor] Single section — returning full text
    [Compressor] sections=22
    [TQ-006] I want to buy monitors in bulk for my office. Do you offer business pricing?
    Expected    : ['policy_006', 'ticket_039', 'ticket_023']
    Retrieved   : ['ticket_023', 'ticket_039', 'ticket_015', 'policy_006']
    Retrieval   : 3/3 (100%)
    Faithful    : YES
    Latency     : retrieval=2.047s  compression=0.501s  generation=42.606s  total=45.154s
    Words       : 265
    ----------------------------------------------------------------------
    [Retriever] Filter: ['product_questions', 'products', 'pre_sales', 'product_comparison', 'installation_help']
    [Retriever] faq_012      score=1.997 (sem=0.747 kw=1.0 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] faq_005      score=1.754 (sem=0.872 kw=0.632 rec=0.1 sat=0.0 prod=0.15)
    [Retriever] ticket_033   score=1.721 (sem=1.104 kw=0.417 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] ticket_026   score=1.508 (sem=1.104 kw=0.204 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_010      score=1.488 (sem=0.927 kw=0.461 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=25
    [Compressor] sections=60
    [Compressor] sections=11
    [Compressor] sections=9
    [Compressor] sections=13
    [TQ-007] What is the difference between NVMe and SATA SSD?
    Expected    : ['faq_012', 'ticket_024', 'ticket_038']
    Retrieved   : ['faq_012', 'faq_005', 'ticket_033', 'ticket_026', 'faq_010']
    Retrieval   : 1/3 (33%)
    Faithful    : NO
    Latency     : retrieval=2.054s  compression=1.069s  generation=27.15s  total=30.273s
    Words       : 53
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_026   score=2.008 (sem=0.808 kw=1.0 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_004      score=1.864 (sem=0.943 kw=0.821 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] ticket_035   score=1.858 (sem=0.749 kw=0.909 rec=0.1 sat=0.1 prod=0.0)
    [Retriever] faq_011      score=1.844 (sem=0.878 kw=0.866 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_019      score=1.715 (sem=0.882 kw=0.733 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=9
    [Compressor] sections=48
    [Compressor] sections=11
    [Compressor] sections=17
    [Compressor] sections=18
    [TQ-008] How do I set up a good home office on a budget?
    Expected    : ['faq_015', 'ticket_026', 'faq_011']
    Retrieved   : ['ticket_026', 'faq_004', 'ticket_035', 'faq_011', 'faq_019']
    Retrieval   : 2/3 (67%)
    Faithful    : YES
    Latency     : retrieval=2.06s  compression=0.981s  generation=51.778s  total=54.819s
    Words       : 287
    ----------------------------------------------------------------------
    [Retriever] Filter: none detected
    [Retriever] ticket_035   score=1.838 (sem=0.959 kw=0.529 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_024   score=1.769 (sem=0.922 kw=0.497 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] ticket_021   score=1.662 (sem=0.902 kw=0.41 rec=0.1 sat=0.1 prod=0.15)
    [Retriever] faq_020      score=1.523 (sem=0.423 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Retriever] faq_015      score=1.523 (sem=0.963 kw=0.46 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=11
    [Compressor] sections=7
    [Compressor] sections=7
    [Compressor] sections=16
    [Compressor] sections=17
    [TQ-009] My external hard drive is making a clicking noise and not showing up.
    Expected    : ['faq_020', 'ticket_021']
    Retrieved   : ['ticket_035', 'ticket_024', 'ticket_021', 'faq_020', 'faq_015']
    Retrieval   : 2/2 (100%)
    Faithful    : YES
    Latency     : retrieval=2.049s  compression=0.66s  generation=26.367s  total=29.076s
    Words       : 104
    ----------------------------------------------------------------------
    [Retriever] Filter: ['environmental_sustainability']
    [Retriever] policy_007   score=1.772 (sem=0.672 kw=1.0 rec=0.1 sat=0.0 prod=0.0)
    [Compressor] sections=21
    [TQ-010] Does Omnia Retail recycle old electronics and how does WEEE work?
    Expected    : ['policy_007']
    Retrieved   : ['policy_007']
    Retrieval   : 1/1 (100%)
    Faithful    : NO
    Latency     : retrieval=2.05s  compression=0.221s  generation=49.309s  total=51.58s
    Words       : 267
    ----------------------------------------------------------------------

    === Evaluation Summary ===
    Total queries       : 10
    Avg retrieval score : 70%
    Faithfulness        : {'YES': 8, 'NO': 2, 'PARTIAL': 0, 'UNKNOWN': 0}
    Avg retrieval time  : 2.059s
    Avg compression time: 0.782s
    Avg generation time : 43.364s
    Avg total latency   : 46.205s
    Avg response words  : 223