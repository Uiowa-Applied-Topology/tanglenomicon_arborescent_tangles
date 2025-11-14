# The Tanglenomicon: A Table of Two String Arborescent Tangles Up to 16 Crossings


[![DOI - 10.5281/zenodo.17612688](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17612688-2ea44f?logo=doi)](https://doi.org/10.5281/zenodo.17612688)
[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This repository contains a list of all arborescent tangles up to 16 crossings.

# Note to Reader

If you discover an issue with this repository or have a question please feel
free to open an issue. We have included templates for the following issues:

-   🐞 Spelling and Grammar
-   🤷 Clarity
-   ❓ Question
-   🚀 Enhancement

# What's in This Repository?

The list of tangles can be found in the `data` directory. The tangles are split
into 1396 files each approximately 1 MB in size. Inside the files, the tangles
are sorted by, in order:

1. Tree Crossing Number
2. Lexicographical

> [!IMPORTANT]
> The following is an example of the order you can expect to find
> tangles in:<br/> i[0]<br/> .<br/> .<br/> .<br/> i[1]<br/> .<br/> .<br/> .<br/>
> i[2 2]<br/> i[-2 -2]<br/> i([2][2])<br/> i(([2][3]))

The tangle is not human-readable, containing no separator between tangles. The
tangles are inherently delimited by their label in $V_4$. Storing the tangles in
this way is a dramatic space savings over presenting the data in a
human-readable form. To ease the viewing, use, and analysis of the data, a basic
Python script is supplied (`read.py`). The script will read into an array each
of the tangles in the dataset.

> [!NOTE]
> The list contains 49640818 items and requires 1.5GB of memory.

# Cite Me 📃

A `CITATION` file is provided; additionally, preformatted BibTeX and APA for the
citation are
[found on the right sidebar.](https://docs.github.com/assets/cb-223034/mw-1440/images/help/repository/citation-link.webp)

# License ⚖️

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">The
        Tanglenomicon: A Table of Two String Arborescent Tangles Up to 16 Crossings </span> by <span
        property="cc:attributionName">Joseph Starr and Isabel Darcy</span> is licensed under <a
        href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank"
        rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img
            style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
            src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img
            style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
            src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img
            style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
            src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img
            style="height:22px!important;margin-left:3px;vertical-align:text-bottom;"
            src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
