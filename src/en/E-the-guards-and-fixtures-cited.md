---
id: the-guards-and-fixtures-cited
appendix: E
number: 105
title: The guards and fixtures cited, by chapter
status: draft
generated: guards
---

A guard is a file of the library's test tree that holds assertions. A chapter that says "this is proved" names the guards that prove it, in the front matter of its source, and the build reads each one: it finds the file in the library at the commit the book runs at, and counts the assertions in it. A guard that is not there fails the build.

This appendix is that reading, by chapter. No figure in it is typed. It is regenerated at every build, so the figures are always the ones the last build read.

Two things to keep in mind. A figure is the number of assertion calls the file holds, counted in its text; it is not a run. Most of these guards are not run by the book, because they write files, open ports or spawn processes. The few I ran myself are named in the chapters that rely on them, with the date. And the only fixtures the book cites are the ones the guards and the blocks read: the course folder of the library's education program, and the data folders its guards name. The blocks of the book are themselves the other fixtures: each one runs inside the library at the commit named under every chapter's title.
