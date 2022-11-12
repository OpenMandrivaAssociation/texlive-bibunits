Name:		texlive-bibunits
Version:	15878
Release:	1
Summary:	Multiple bibliographies in one document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibunits
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provide a mechanism to generate separate
bibliographies for different units (chapters, sections or
bibunit-environments) of a text. The package separates the
citations of each unit of text into a separate file to be
processed by BibTeX. The global bibliography section produced
by LaTeX may also appear in the document and citations can be
placed in both the local unit and the global bibliographies at
the same time. The package is compatible with koma-script and
with the babel French option frenchb.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibunits/bibunits.sty
%doc %{_texmfdistdir}/doc/latex/bibunits/README
%doc %{_texmfdistdir}/doc/latex/bibunits/bibtexall
%doc %{_texmfdistdir}/doc/latex/bibunits/bibunits.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bibunits/bibunits.dtx
%doc %{_texmfdistdir}/source/latex/bibunits/bibunits.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
