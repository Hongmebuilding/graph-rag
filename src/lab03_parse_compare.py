"""실습 03: PDF 파싱 비교 (pypdf 단순 추출 vs docling Markdown 변환).

실행 예시:
    uv run python src/lab03_parse_compare.py

corpus/raw_pdf/nb200_spec.pdf 를 두 방식으로 파싱해 data/ 아래에 저장한다.
    - data/lab03_plain.txt  : pypdf 로 페이지별 텍스트를 단순 추출
    - data/lab03_docling.md : docling 으로 변환한 Markdown
그 뒤 "셀 정격" 표가 두 결과에서 어떻게 표현됐는지 각각 앞 40줄을 출력한다.
이미 결과 파일이 있으면 덮어쓰기 전에 .bak 사본을 남긴다.

사전 준비: uv sync --group parsing
docling 모델은 처음 실행할 때 HuggingFace 에서 내려받는다(인터넷 필요).
~/.cache/huggingface 가 root 소유라 쓸 수 없는 환경을 위해, HF_HOME 이 따로 지정되지
않았다면 프로젝트의 .cache/huggingface 를 캐시로 쓴다.
"""

import os
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# huggingface_hub 는 import 시점에 캐시 경로를 읽으므로 docling import 보다 먼저 지정한다.
os.environ.setdefault("HF_HOME", str(PROJECT_ROOT / ".cache" / "huggingface"))

from docling.document_converter import DocumentConverter  # noqa: E402
from pypdf import PdfReader  # noqa: E402


PDF_PATH = PROJECT_ROOT / "corpus" / "raw_pdf" / "nb200_spec.pdf"
DATA_DIR = PROJECT_ROOT / "data"
PLAIN_PATH = DATA_DIR / "lab03_plain.txt"
DOCLING_PATH = DATA_DIR / "lab03_docling.md"

TABLE_KEYWORD = "셀 정격"
PREVIEW_LINES = 40


def backup_if_exists(path: Path) -> None:
    """덮어쓰기 전에 기존 파일을 .bak 으로 복사해 둔다."""
    if path.exists():
        backup = path.with_suffix(path.suffix + ".bak")
        shutil.copy2(path, backup)
        print(f"  (기존 파일 백업: {backup.relative_to(PROJECT_ROOT)})")


def save_text(path: Path, text: str) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    backup_if_exists(path)
    path.write_text(text, encoding="utf-8")
    print(f"저장: {path.relative_to(PROJECT_ROOT)} ({len(text):,}자)")


def extract_plain(pdf_path: Path) -> str:
    """pypdf 로 페이지별 텍스트를 이어 붙인다 (레이아웃/표 구조 고려 없음)."""
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def convert_docling(pdf_path: Path) -> str:
    """docling 으로 PDF 를 Markdown 으로 변환한다."""
    result = DocumentConverter().convert(pdf_path)
    return result.document.export_to_markdown()


def preview(title: str, text: str, keyword: str, n: int) -> None:
    """keyword 가 처음 나오는 줄부터 n 줄을 출력한다. 없으면 문서 앞부분을 보여준다."""
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if keyword in line), None)
    if start is None:
        print(f"\n===== {title}: '{keyword}' 를 찾지 못해 문서 앞 {n}줄 출력 =====")
        start = 0
    else:
        print(f"\n===== {title}: '{keyword}' 위치(줄 {start + 1})부터 {n}줄 =====")
    for line in lines[start : start + n]:
        print(line)


def main() -> int:
    if not PDF_PATH.exists():
        print(f"[FAIL] PDF 없음: {PDF_PATH}")
        return 1

    print(f"입력: {PDF_PATH.relative_to(PROJECT_ROOT)}\n")

    print("1. pypdf 단순 텍스트 추출")
    plain = extract_plain(PDF_PATH)
    save_text(PLAIN_PATH, plain)

    print("\n2. docling Markdown 변환 (첫 실행은 모델 로딩으로 오래 걸릴 수 있음)")
    markdown = convert_docling(PDF_PATH)
    save_text(DOCLING_PATH, markdown)

    print("\n3. '셀 정격' 표 표현 비교")
    preview("pypdf (lab03_plain.txt)", plain, TABLE_KEYWORD, PREVIEW_LINES)
    preview("docling (lab03_docling.md)", markdown, TABLE_KEYWORD, PREVIEW_LINES)
    return 0


if __name__ == "__main__":
    sys.exit(main())
