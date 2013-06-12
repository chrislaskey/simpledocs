About Simple Docs
================================================================================

**Simplifying documentation**

Version 1.0.0

Mirror plain text files effortlessly. No compilation. No caches to clear. A
real time mirror of files. Perfect for individuals or small teams who need to
share knowledge without any added complexity of a Wiki or flat-file compilers.

Instead of rebuilding new layers for the web, simple docs builds on what's
already there:

- Documentation files can be written in plain-text Markdown
- Files and directories are mirrored and displayed online
- File names are automatically cleaned up, no special meta-data required
- Safe search using `grep`, `ls` and `find` returns smart weighted results
- Control read/write access using file system permissions

Motivation
================================================================================

As a full-stack software engineer, I spend a lot of time documenting various
pieces of knowledge. A note about server configuration today, updating virtual
machine notes from months ago, or documenting a programming bug so I don't make
the same mistake again.

I noticed I was spending too much time managing the existing notes, than
writing and updating the content:

- Wiki's were a big context switch, requiring dropping out of the command line
to load a web browser. Or worse making mental notes when troubleshooting a
remote desktop and hoping I remember.
- Old XML based solutions let me return to writing notes on the command line,
but required too much boilerplate.
- VimWiki notes were great for my personal notes, but were hard to share with
colleagues.
- Compiled flat-file systems like `Jekyll` and `Pelican` were
almost perfect. But still required automated scripts to compile and buy-in from
colleagues.

Taking compiled flat-file systems as a jumping off point, my goals were to:

- Write notes in Markdown files and have the file system mirrored online
- No special overhead to managing user permissions, allowing colleagues - only the right colleagues - the ability to modify or add files.
- Searchable documentation with weighted results.
- Piggy-back on known, solid technology instead of re-inventing it all in the
browser.
- Requires no management after initial setup.

The result is Simple Docs. Built on top of Python Flask. Easy to setup, no
additional maintenance required.

Finally I'm able to stop managing documentation and get back to writing it.

License
================================================================================

All code written by me is released under MIT license. See the attached
license.txt file for more information, including commentary on license choice.
