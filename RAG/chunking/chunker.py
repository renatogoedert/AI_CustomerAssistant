from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter


class Chunker:
    """
    Chunks documents using different strategies.

    Usage:
        chunker = Chunker()
        chunker.fixed_size(content=my_text)
        chunker.fixed_size(path="documents/my_file.txt")
        chunker.recursive(content=my_text, chunk_size=400, chunk_overlap=50)
        chunker.semantic_chunk(content=my_text, separator="##")
        chunker.chunk_by_paragraph(content=my_text)
        chunker.chunk_by_sentences(content=my_text, sentences_per_chunk=3, overlap=1)
    """

    def __init__(self):
        pass
        

    def _check_content(self, content: str = None, path: str = None) -> str:

        """Helper to validate and return document content."""

        if content is None and path is None:
            raise ValueError("Provide either content or path.")
        
        if content is not None and path is not None:
            raise ValueError("Provide either content or path, not both.")
        
        if path is not None:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
            
        return content

    def fixed_size(self, content: str = None, path: str = None, chunk_size: int = 400, chunk_overlap: int = 50, separator: str = "\n") -> list:

        """Fixed-size chunking using character splitter."""

        content = self._check_content(content, path)

        char_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separator=separator
        )
        chunks = char_splitter.split_text(content)
        print(f"Created {len(chunks)} chunks using Fixed Size Chunking")
        return chunks

    def recursive(self, content: str = None, path: str = None, chunk_size: int = 400, chunk_overlap: int = 50, separators: list = None) -> list:

        """Recursive splitting — respects document structure."""

        content = self._check_content(content, path)

        if separators is None:
            separators = ["\n## ", "\n\n", "\n", " "]

        recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators
        )
        chunks = recursive_splitter.split_text(content)
        print(f"Created {len(chunks)} chunks using Recursive Chunking")
        return chunks

    def semantic_chunk(self, content: str = None, path: str = None, separator: str = "##", line_split: str = "\n") -> list:

        """Semantic chunking — splits by section headers."""

        content = self._check_content(content, path)

        sections = []
        current_section = []

        for line in content.split(line_split):
            if line.startswith(separator):
                if current_section:
                    sections.append(line_split.join(current_section))
                current_section = [line]
            else:
                current_section.append(line)

        if current_section:
            sections.append(line_split.join(current_section))

        print(f"Created {len(sections)} chunks using Semantic Chunking")
        return sections

    def chunk_by_paragraph(self, content: str = None, path: str = None, separator: str = "\n\n") -> list:

        """Split on paragraph boundaries (double newlines by default)."""

        content = self._check_content(content, path)

        chunks = [p.strip() for p in content.split(separator) if p.strip()]
        print(f"Created {len(chunks)} chunks using Paragraph Chunking")
        return chunks

    def chunk_by_sentences(self, content: str = None, path: str = None, sentences_per_chunk: int = 3, overlap: int = 1) -> list:

        """Split into sentence groups with overlap."""

        content = self._check_content(content, path)

        if overlap >= sentences_per_chunk:
            raise ValueError(f"overlap ({overlap}) must be less than sentences_per_chunk ({sentences_per_chunk})")

        sentences = [s.strip() + '.' for s in content.split('.') if s.strip()]

        chunks = []
        for i in range(0, len(sentences), sentences_per_chunk - overlap):
            chunk = ' '.join(sentences[i:i + sentences_per_chunk])
            if chunk:
                chunks.append(chunk)

        print(f"Created {len(chunks)} chunks using Sentence Chunking")
        return chunks