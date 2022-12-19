import re

from PyPDF2 import PdfReader
from gooey import Gooey, GooeyParser


@Gooey(show_stop_warning=False, show_success_modal=False)
def main():
    parser = GooeyParser(description="Choose PDF file from which to extract email addresses "
                                     "and print them using the separator.")
    parser.add_argument('filename', default="data.pdf", widget="FileChooser")
    parser.add_argument('separator', default=",", action="store")
    args = parser.parse_args()
    reader = PdfReader(args.filename)
    text = "".join(page.extract_text() for page in reader.pages)
    search = re.findall(r"\S+@\S+\.\S+", text, re.IGNORECASE)
    print(args.separator.join(search))


if __name__ == '__main__':
    main()
