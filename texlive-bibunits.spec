# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bibunits
# catalog-date 2009-09-27 09:44:19 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-bibunits
Version:	2.2
Release:	2
Summary:	Multiple bibliographies in one document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibunits
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 749698
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 717944
- texlive-bibunits
- texlive-bibunits
- texlive-bibunits
- texlive-bibunits
- texlive-bibunits

