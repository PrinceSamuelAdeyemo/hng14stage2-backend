# Insighta Labs Demographic Intelligence Backend

## Natural Language Parsing Approach

The `/api/profiles/search` endpoint uses a rule-based parser (no AI/LLM) to convert plain English queries into filters for the database. Supported keywords and their mappings:

- **Gender**: "male", "female", or both ("male and female")
- **Age group**: "child", "teenager(s)", "adult", "senior"
- **Young**: "young" → `min_age=16`, `max_age=24`
- **Above/Over**: "above 30", "over 30" → `min_age=30`
- **Below/Under**: "below 20", "under 20" → `max_age=20`
- **Country**: "from nigeria" → `country_id=NG` (common countries mapped by name)
- **Combined**: e.g., "adult males from kenya" → `gender=male`, `age_group=adult`, `country_id=KE`
- **Edge**: "teenagers above 17" → `age_group=teenager`, `min_age=17`

### Logic
- The parser checks for keywords in the query string and applies the corresponding filters.
- If a query can't be interpreted, it returns an error.
- All filters are combinable.

## Limitations
- Only exact keywords and simple patterns are supported (see above).
- No fuzzy matching, synonyms, or advanced NLP.
- Only a few countries are mapped by name to ISO2 code (NG, AO, KE, BJ). Others use the country name as-is.
- Complex queries, ambiguous phrases, or misspellings are not handled.
- No support for ranges (e.g., "ages 20 to 30") or logical operators ("or", "not").
- Only the fields described above are parsed; other attributes are ignored.

## Edge Cases Not Handled
- Misspelled country or age group names
- Multiple age groups or overlapping filters
- Queries with conflicting or ambiguous instructions

---

See the code for exact logic and supported keywords.
