import json
from collections import defaultdict


def get_categories(path: str):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    by_type = defaultdict(set)

    for doc in data["documents"]:
        doc_type = doc.get("type", "unknown")
        category = doc.get("category", "none")
        by_type[doc_type].add(category)

    for doc_type, categories in sorted(by_type.items()):
        print(f"\n{doc_type} ({len(categories)} categories):")
        for cat in sorted(categories):
            print(f"  - {cat}")


if __name__ == "__main__":
    get_categories("./dataset/omnia_retail_knowledge_base.json")