# Finding a name

Creative Project Plan programming exploration for IS218. The research page asks whether approximate search can improve a small student directory when a name is misspelled. It compares literal matching with ranked fuzzy suggestions and records the initial observations and the next experiment.

Open the [published research page](https://is218-directory-search-exploration.akindemuyi18.chatgpt.site) or [preview the page locally](dist/index.html). The page is static and the baseline interaction uses its embedded four-name fictional fixture. [GitHub source](https://github.com/oa356/is218-class/tree/main/creative-exploration)

## Research decision

Start with normalized substring matching. Test [Fuse.js](https://www.fusejs.io/) as a fallback for empty results before introducing suggestions. The [ECMAScript string specification](https://tc39.es/ecma262/multipage/text-processing.html#sec-string.prototype.includes) and Fuse.js documentation were checked November 11, 2026.

Five local assertions passed for exact input with spaces and uppercase, a partial name, a decomposed accent, a transposed typo, and an unrelated query. The typo and unrelated query both returned no matches. The fuzzy evaluation and partner walkthrough are pending.

The proposed later application journey is sign in → directory lookup → save a result → private saved-results dashboard → account maintenance.

[Portfolio Plan career research](https://is218-ai-career-research.akindemuyi18.chatgpt.site)
