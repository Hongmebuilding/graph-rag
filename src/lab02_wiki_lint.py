# 실습 02: 위키 린트 (frontmatter 필수 필드 / [[링크]] 대상 존재 / 고아 문서)
# 실행 예시: uv run python src/lab02_wiki_lint.py
#           uv run python src/lab02_wiki_lint.py --count-index-links  (index.md·log.md의 링크도 인바운드로 센다)
# 종료 코드: 위반 0건이면 0, 위반이 있으면 1
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"

# 색인·적재 대상은 이 세 폴더의 md뿐이다 (wiki/TEMPLATE.md 규칙)
DOC_DIRS = ("entities", "sources", "concepts")
# 위키 문서가 아닌 탐색용 파일: frontmatter는 검사하지 않고 링크 대상 존재만 검사한다
NAV_FILES = ("index.md", "log.md")
REQUIRED_FIELDS = (
    "id", "title", "doc_type", "source_file", "created", "updated", "tags", "status",
)

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.S)
FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
LINK_RE = re.compile(r"\[\[([^\[\]]+)\]\]")


def split_frontmatter(text):
    """(frontmatter dict 또는 None, 본문)을 돌려준다."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line[0].isspace() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, m.group(2)


def extract_links(body):
    """코드 블록·인라인 코드 안의 예시를 뺀 [[링크]] 대상 id 목록 (별칭 `|`, 앵커 `#` 제거)."""
    body = FENCE_RE.sub("", body)
    body = INLINE_CODE_RE.sub("", body)
    targets = []
    for raw in LINK_RE.findall(body):
        target = raw.split("|")[0].split("#")[0].strip()
        if target:
            targets.append(target)
    return targets


def rel(path):
    return path.relative_to(ROOT).as_posix()


def main():
    parser = argparse.ArgumentParser(description="wiki 린트")
    parser.add_argument(
        "--count-index-links",
        action="store_true",
        help="index.md·log.md에서 오는 링크도 고아 판정의 인바운드 링크로 센다",
    )
    args = parser.parse_args()

    docs = {}  # id(파일명) -> Path
    dup_ids = []
    for folder in DOC_DIRS:
        for path in sorted((WIKI_DIR / folder).glob("*.md")):
            if path.stem in docs:
                dup_ids.append(path.stem)
            docs[path.stem] = path
    nav_paths = [WIKI_DIR / name for name in NAV_FILES if (WIKI_DIR / name).is_file()]

    missing_fields = []  # (경로, 누락 필드 목록)
    broken_links = []  # (경로, 대상 id)
    inbound = {doc_id: set() for doc_id in docs}
    link_total = 0

    for doc_id, path in docs.items():
        text = path.read_text(encoding="utf-8")
        fields, body = split_frontmatter(text)
        if fields is None:
            missing_fields.append((rel(path), ["(frontmatter 없음)"]))
        else:
            absent = [f for f in REQUIRED_FIELDS if not fields.get(f)]
            if absent:
                missing_fields.append((rel(path), absent))
        for target in extract_links(body):
            link_total += 1
            if target not in docs:
                broken_links.append((rel(path), target))
            elif target != doc_id:
                inbound[target].add(doc_id)

    for path in nav_paths:
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        for target in extract_links(body):
            link_total += 1
            if target not in docs:
                broken_links.append((rel(path), target))
            elif args.count_index_links:
                inbound[target].add(path.stem)

    orphans = [doc_id for doc_id, srcs in inbound.items() if not srcs]

    # ---- 리포트 ----
    counts = {f: sum(1 for p in docs.values() if p.parent.name == f) for f in DOC_DIRS}
    print("== Wiki Lint 리포트 ==")
    print(
        f"대상 문서 {len(docs)}개 ("
        + ", ".join(f"{f} {n}" for f, n in counts.items())
        + f") / 링크 {link_total}개 검사 / 링크 검사 추가 대상: "
        + (", ".join(p.name for p in nav_paths) or "없음")
    )
    basis = "index.md·log.md 포함" if args.count_index_links else "위키 문서끼리의 링크만, index.md·log.md 제외"
    print(f"고아 판정 기준: 다른 문서에서 오는 [[링크]]가 없는 문서 ({basis})")
    if dup_ids:
        print(f"참고: 폴더 간 중복 id가 있어 링크 대상이 모호하다: {', '.join(sorted(set(dup_ids)))}")
    print()

    print(f"1) frontmatter 필수 필드 누락: {len(missing_fields)}건")
    for path, absent in missing_fields:
        print(f"   - {path}: {', '.join(absent)}")

    print(f"2) 존재하지 않는 [[링크]] 대상: {len(broken_links)}건")
    for path, target in broken_links:
        print(f"   - {path}: [[{target}]]")

    print(f"3) 고아 문서: {len(orphans)}건")
    for doc_id in orphans:
        print(f"   - {rel(docs[doc_id])}")

    violations = len(missing_fields) + len(broken_links) + len(orphans)
    print()
    print(f"결과: 위반 {violations}건" + (" -> FAIL" if violations else " -> OK"))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
