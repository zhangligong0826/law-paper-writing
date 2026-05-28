# Contributing

Thanks for improving `law-paper-writing`. This project is designed for law students and researchers, especially people without a programming background. Contributions should be accurate, readable, and easy to reuse.

## What You Can Contribute

- Copyable prompts for legal academic writing tasks.
- Examples based on real workflows, with sensitive details removed.
- Updates to citation, journal, thesis, or Word-format guidance.
- Additional law subfield templates.
- Tests for `references/citation-converter.py`.

## Contribution Rules

- Do not add legal advice for individual disputes.
- Do not add fabricated statutes, cases, citations, journal requirements, or impact factors.
- For high-change information, include source and last verification date.
- Keep prompts usable by non-programmers.
- Prefer concrete examples over abstract slogans.

## Prompt Template Standard

Every new prompt should include:

- `适用场景`
- `Prompt 模板`
- `需要替换的变量`
- `示例输入`
- `预期输出`
- `注意事项`

## Example Standard

Every example should:

- Be understandable without running code.
- Use anonymized or fictionalized facts if based on real work.
- Mark statutes, cases, journal requirements, and citations as requiring final verification.

## Testing

If you change `references/citation-converter.py`, run:

```bash
python3 -m py_compile references/citation-converter.py
python3 -m unittest discover -s tests
```

If you change README links, check that every relative link points to an existing file or directory.
