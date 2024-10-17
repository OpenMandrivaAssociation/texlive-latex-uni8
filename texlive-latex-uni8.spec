Name:		texlive-latex-uni8
Version:	49729
Release:	2
Summary:	Universal inputenc, fontenc, and babel for pdfLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-uni8
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-uni8.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-uni8.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX style file which makes it easy to
use input encoding (UTF-8 by default, can be changed),
fontspec.sty (optional), font encoding (T1 if fontspec.sty is
not used), babel (English language by default), hyphenation,
underline (with soul.sty), default text and math fonts
(Computer Modern or Times), and paper sizes correctly with both
pdfLaTeX and LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/latex-uni8
%doc %{_texmfdistdir}/doc/latex/latex-uni8

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
