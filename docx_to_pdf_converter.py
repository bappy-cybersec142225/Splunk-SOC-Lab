"""
===========================================================
  DOC/DOCX → PDF Converter  |  Production-Ready Script
  Works on Windows, macOS, and Linux
===========================================================

REQUIREMENTS (install once):
  pip install python-docx docx2pdf

OPTIONAL (for advanced/batch use):
  pip install tqdm colorama

USAGE EXAMPLES:
  # Single file
  python docx_to_pdf_converter.py --input report.docx

  # Batch convert a folder
  python docx_to_pdf_converter.py --folder ./docs/

  # Auto-name output PDF from document title
  python docx_to_pdf_converter.py --input report.docx --use-title

  # Specify output folder
  python docx_to_pdf_converter.py --folder ./docs/ --output ./pdfs/
"""

import os
import sys
import argparse
import platform
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────
#  CORE CONVERSION FUNCTION
# ─────────────────────────────────────────────

def convert_to_pdf(input_path: str, output_path: str = None, use_title: bool = False) -> str:
    """
    Convert a .doc or .docx file to PDF.
    Returns the path of the generated PDF.
    """
    input_path = Path(input_path).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.suffix.lower() not in [".doc", ".docx"]:
        raise ValueError(f"Unsupported file type: {input_path.suffix}. Use .doc or .docx")

    # Determine output PDF path
    if use_title:
        title = _get_document_title(input_path)
        pdf_name = _sanitize_filename(title) + ".pdf" if title else input_path.stem + ".pdf"
    else:
        pdf_name = input_path.stem + ".pdf"

    if output_path:
        out_dir = Path(output_path)
        out_dir.mkdir(parents=True, exist_ok=True)
        pdf_path = out_dir / pdf_name
    else:
        pdf_path = input_path.parent / pdf_name

    os_name = platform.system()

    if os_name == "Windows":
        _convert_windows(input_path, pdf_path)
    elif os_name == "Darwin":
        _convert_mac(input_path, pdf_path)
    else:
        _convert_linux(input_path, pdf_path)

    if not pdf_path.exists():
        raise RuntimeError(f"Conversion failed — output PDF not found: {pdf_path}")

    print(f"  ✅  {input_path.name}  →  {pdf_path}")
    return str(pdf_path)


# ─────────────────────────────────────────────
#  PLATFORM-SPECIFIC CONVERTERS
# ─────────────────────────────────────────────

def _convert_windows(input_path: Path, pdf_path: Path):
    """
    Windows: uses Microsoft Word via COM (requires Word installed)
    or falls back to docx2pdf (which also uses Word).
    """
    try:
        from docx2pdf import convert
        convert(str(input_path), str(pdf_path))
    except ImportError:
        # Fallback: use Word COM directly (requires pywin32)
        try:
            import win32com.client
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False
            doc = word.Documents.Open(str(input_path))
            doc.SaveAs(str(pdf_path), FileFormat=17)  # 17 = wdFormatPDF
            doc.Close()
            word.Quit()
        except ImportError:
            raise RuntimeError(
                "On Windows, install either:\n"
                "  pip install docx2pdf        (requires Microsoft Word)\n"
                "  pip install pywin32          (alternative COM method)\n"
                "Or install LibreOffice from https://libreoffice.org"
            )


def _convert_mac(input_path: Path, pdf_path: Path):
    """
    macOS: uses docx2pdf (which uses Word on Mac) or LibreOffice.
    """
    try:
        from docx2pdf import convert
        convert(str(input_path), str(pdf_path))
    except (ImportError, Exception):
        _convert_libreoffice(input_path, pdf_path)


def _convert_linux(input_path: Path, pdf_path: Path):
    """
    Linux: uses LibreOffice headless (best cross-platform option).
    Install: sudo apt install libreoffice  OR  sudo dnf install libreoffice
    """
    _convert_libreoffice(input_path, pdf_path)


def _convert_libreoffice(input_path: Path, pdf_path: Path):
    """
    LibreOffice headless conversion — works on Linux/macOS/Windows.
    Preserves headings, bullet points, tables, and images faithfully.
    """
    import subprocess
    import shutil

    soffice = _find_libreoffice()
    if not soffice:
        raise RuntimeError(
            "LibreOffice not found. Install it:\n"
            "  Ubuntu/Debian : sudo apt install libreoffice\n"
            "  Fedora/RHEL   : sudo dnf install libreoffice\n"
            "  macOS         : brew install --cask libreoffice\n"
            "  Windows       : https://libreoffice.org/download"
        )

    out_dir = pdf_path.parent
    result = subprocess.run(
        [soffice, "--headless", "--convert-to", "pdf",
         "--outdir", str(out_dir), str(input_path)],
        capture_output=True, text=True, timeout=120
    )

    # LibreOffice always names the output <stem>.pdf in the outdir
    generated = out_dir / (input_path.stem + ".pdf")
    if generated.exists() and generated != pdf_path:
        generated.rename(pdf_path)

    if result.returncode != 0:
        raise RuntimeError(f"LibreOffice error:\n{result.stderr}")


def _find_libreoffice() -> str | None:
    """Find the LibreOffice executable across common install paths."""
    import shutil
    candidates = [
        "soffice",                                              # in PATH
        "/usr/bin/soffice",
        "/usr/lib/libreoffice/program/soffice",
        "/opt/libreoffice/program/soffice",
        r"C:\Program Files\LibreOffice\program\soffice.exe",
        r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    ]
    for c in candidates:
        if shutil.which(c) or Path(c).exists():
            return c
    return None


# ─────────────────────────────────────────────
#  HELPERS: TITLE EXTRACTION & SANITIZE
# ─────────────────────────────────────────────

def _get_document_title(path: Path) -> str | None:
    """Extract the title from a DOCX file's core properties."""
    if path.suffix.lower() == ".docx":
        try:
            from docx import Document
            doc = Document(str(path))
            return doc.core_properties.title or None
        except Exception:
            pass
    return None


def _sanitize_filename(name: str) -> str:
    """Remove characters that are illegal in file names."""
    import re
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    return name.strip(". ")[:200]  # Max 200 chars


# ─────────────────────────────────────────────
#  BATCH CONVERSION
# ─────────────────────────────────────────────

def batch_convert(folder: str, output_folder: str = None, use_title: bool = False) -> dict:
    """
    Convert all .doc and .docx files in a folder to PDF.
    Returns a summary dict with success/failure counts.
    """
    folder = Path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    files = list(folder.glob("*.docx")) + list(folder.glob("*.doc"))
    if not files:
        print(f"  ⚠️  No .doc or .docx files found in: {folder}")
        return {"success": 0, "failed": 0, "files": []}

    print(f"\n📂  Found {len(files)} file(s) in: {folder}")
    print("─" * 55)

    results = {"success": 0, "failed": 0, "files": []}

    for f in sorted(files):
        try:
            pdf = convert_to_pdf(str(f), output_folder, use_title)
            results["success"] += 1
            results["files"].append({"input": str(f), "output": pdf, "status": "ok"})
        except Exception as e:
            print(f"  ❌  {f.name}  →  ERROR: {e}")
            results["failed"] += 1
            results["files"].append({"input": str(f), "error": str(e), "status": "failed"})

    print("─" * 55)
    print(f"  Done: {results['success']} converted, {results['failed']} failed.\n")
    return results


# ─────────────────────────────────────────────
#  CLI ENTRY POINT
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Convert DOC/DOCX files to PDF with formatting preserved.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python docx_to_pdf_converter.py --input report.docx
  python docx_to_pdf_converter.py --input lab.doc --output ./pdfs/ --use-title
  python docx_to_pdf_converter.py --folder ./documents/ --output ./pdfs/
        """
    )
    parser.add_argument("--input",     help="Single .doc/.docx file to convert")
    parser.add_argument("--folder",    help="Folder containing .doc/.docx files (batch mode)")
    parser.add_argument("--output",    help="Output folder for PDF(s). Defaults to same folder as input.")
    parser.add_argument("--use-title", action="store_true",
                        help="Name the PDF using the document's Title property instead of filename")

    args = parser.parse_args()

    if not args.input and not args.folder:
        parser.print_help()
        sys.exit(1)

    print(f"\n{'='*55}")
    print("  DOC/DOCX → PDF Converter")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  |  {platform.system()}")
    print(f"{'='*55}\n")

    if args.folder:
        batch_convert(args.folder, args.output, args.use_title)
    elif args.input:
        convert_to_pdf(args.input, args.output, args.use_title)


if __name__ == "__main__":
    main()
