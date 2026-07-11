%global tl_name latex-uni8
%global tl_revision 49729

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Universal inputenc, fontenc, and babel for pdfLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-uni8
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-uni8.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-uni8.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX style file which makes it easy to use
input encoding (UTF-8 by default, can be changed), fontspec.sty
(optional), font encoding (T1 if fontspec.sty is not used), babel
(English language by default), hyphenation, underline (with soul.sty),
default text and math fonts (Computer Modern or Times), and paper sizes
correctly with both pdfLaTeX and LuaLaTeX.

