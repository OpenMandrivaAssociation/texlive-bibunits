%global tl_name bibunits
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Multiple bibliographies in one document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibunits
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibunits.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provide a mechanism to generate separate bibliographies for
different units (chapters, sections or bibunit-environments) of a text.
The package separates the citations of each unit of text into a separate
file to be processed by BibTeX. The global bibliography section produced
by LaTeX may also appear in the document and citations can be placed in
both the local unit and the global bibliographies at the same time. The
package is compatible with koma-script and with the babel French option
frenchb.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibunits
%dir %{_datadir}/texmf-dist/source/latex/bibunits
%dir %{_datadir}/texmf-dist/tex/latex/bibunits
%doc %{_datadir}/texmf-dist/doc/latex/bibunits/README
%doc %{_datadir}/texmf-dist/doc/latex/bibunits/bibtexall
%doc %{_datadir}/texmf-dist/doc/latex/bibunits/bibunits.pdf
%doc %{_datadir}/texmf-dist/source/latex/bibunits/bibunits.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibunits/bibunits.ins
%{_datadir}/texmf-dist/tex/latex/bibunits/bibunits.sty
